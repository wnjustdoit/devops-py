#!/usr/bin/env python3

from flask import Flask, escape, request, render_template, current_app
from flask_cors import CORS
from flask_socketio import SocketIO

import os
import subprocess
import threading
from datetime import timedelta

from .entities.git_repo import GitRepo
from .configs.profiles import configs, DEFAULT_CONFIG_ENV

from .user_api import user_api
from .git_repo_api import git_repo_api
from .publishment_api import publishment_api, get_publishment_detail
from .publishment_staticfile_api import publishment_staticfile_api, get_publishment_detail_static
from .publishment_fe_vue_api import publishment_fe_vue_api, get_publishment_detail_fe

app = Flask(__name__)
profile = os.environ.get('PROFILE', default=DEFAULT_CONFIG_ENV)
app.config.from_object(configs[profile])
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

app.register_blueprint(user_api)
app.register_blueprint(git_repo_api)
app.register_blueprint(publishment_api)
app.register_blueprint(publishment_staticfile_api)
app.register_blueprint(publishment_fe_vue_api)

cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')


@app.cli.command("app_run")
def app_run():
    socketio.run(app, host=current_app.config['HOST'], port=current_app.config['PORT'])


if __name__ == '__main__':
    app_run()


# index
@app.route("/")
def index():
    return render_template('index.html')


# hello
@app.route("/hello")
def hello():
    git_repo = GitRepo
    git_repo.id = 112
    print('--', git_repo)
    # pprint('-=-', git_repo)
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print('Socket error:', e)


@socketio.on('publish_event')
def test_event(params):
    if request.cookies.get('publish_client_id') is None:
        print('ERROR: Get client cookie[publish_client_id] failed')
        return
    if params is None or params.get('id') is None:
        print('ERROR: The publish id cannot be empty')
        return
    id = params['id']
    type_prefix = '' if params.get('type') is None else params['type'] + '_'

    # union unique key, mainly consists of client user session id and business id
    client_event = 'publish_response_' + type_prefix + request.cookies.get('publish_client_id') + '_' + str(id)

    # publish process
    lock = get_my_lock(type_prefix + str(id))
    try_lock_result = lock.acquire(blocking=False)  # try lock once
    if not try_lock_result:
        socketio.emit(client_event, {'message': '当前有相同发布正在进行，尝试本次发布最多等待10s'})
        lock_result = lock.acquire(timeout=10)  # lock, timeout of 10 seconds
        if not lock_result:
            socketio.emit(client_event, {'message': '当前发布繁忙（等待10s超时），请稍后再试'})
            return
    project_name = None
    try:
        if params.get('type') is None or params['type'] == 'publishment':
            publishment = get_publishment_detail(id)
            execute_cmd(client_event, publishment)
            project_name = publishment.name
        elif params['type'] == 'static':
            publishment_static = get_publishment_detail_static(id)
            execute_cmd_static(client_event, publishment_static)
            project_name = publishment_static.name
        elif params['type'] == 'fe':
            publishment_fe = get_publishment_detail_fe(id)
            execute_cmd_fe(client_event, publishment_fe)
            project_name = publishment_fe.name
    finally:
        lock.release()  # release lock (if necessary)

    # publish end
    socketio.emit(client_event, {'status': 'OK', 'project': project_name})


def execute_cmd(client_event, publishment):
    p = subprocess.Popen("""python3 src/mymodules/devops.py \
            --work_home={work_home} --source_file_dir={source_file_dir} \
            --git_repo={git_repo} --git_branches={git_branches} --project_name={project_name} --profile={profile} --to_ip={to_ip} --to_project_home={to_project_home} \
            --to_process_name={to_process_name} --to_java_opts="{to_java_opts}" --git_merged_branch={git_merged_branch} --git_tag_version={git_tag_version} --git_tag_comment={git_tag_comment} --git_delete_temp_branch={git_delete_temp_branch}"""
                         .format(work_home=current_app.config.get('WORK_HOME'),
                                 git_repo=publishment.git_repo.ssh_url_to_repo,
                                 git_branches=publishment.git_branches,
                                 project_name=publishment.git_repo.name,
                                 profile=publishment.profile,
                                 source_file_dir=publishment.source_file_dir if publishment.source_file_dir is not None else '',
                                 to_ip=publishment.to_ip, to_project_home=publishment.to_project_home,
                                 to_process_name=publishment.to_process_name if publishment.to_process_name is not None else '',
                                 to_java_opts=publishment.to_java_opts if publishment.to_java_opts is not None else '',
                                 git_merged_branch=publishment.git_merged_branch if publishment.git_merged_branch is not None else '',
                                 git_tag_version=publishment.git_tag_version if publishment.git_tag_version is not None else '',
                                 git_tag_comment=publishment.git_tag_comment if publishment.git_tag_comment is not None else '',
                                 git_delete_temp_branch=int(publishment.git_delete_temp_branch)),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True, bufsize=1)
    process_output(p, client_event)


def execute_cmd_static(client_event, publishment_static):
    p = subprocess.Popen("""python3 src/mymodules/devops_staticfile.py \
            --work_home={work_home} \
            --git_repo={git_repo} --git_branches={git_branches} --project_name={project_name} \
            --source_file_dir={source_file_dir} --to_ip={to_ip} --to_project_home={to_project_home}"""
                         .format(work_home=current_app.config.get('WORK_HOME'),
                                 git_repo=publishment_static.git_repo.ssh_url_to_repo,
                                 git_branches=publishment_static.git_branches,
                                 project_name=publishment_static.git_repo.name,
                                 source_file_dir=publishment_static.source_file_dir if publishment_static.source_file_dir is not None else '',
                                 to_ip=publishment_static.to_ip, to_project_home=publishment_static.to_project_home),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True, bufsize=1)
    process_output(p, client_event)


def execute_cmd_fe(client_event, publishment_fe):
    p = subprocess.Popen("""python3 src/mymodules/devops_fe_vue.py \
            --work_home={work_home} \
            --git_repo={git_repo} --git_branches={git_branches} --project_name={project_name} --profile={profile} \
            --source_file_dir={source_file_dir} --to_ip={to_ip} --to_project_home={to_project_home}"""
                         .format(work_home=current_app.config.get('WORK_HOME'),
                                 git_repo=publishment_fe.git_repo.ssh_url_to_repo,
                                 git_branches=publishment_fe.git_branches,
                                 project_name=publishment_fe.git_repo.name,
                                 profile=publishment_fe.profile,
                                 source_file_dir=publishment_fe.source_file_dir if publishment_fe.source_file_dir is not None else '',
                                 to_ip=publishment_fe.to_ip, to_project_home=publishment_fe.to_project_home),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True, bufsize=1)
    process_output(p, client_event)


def process_output(p, client_event):
    try:
        for line in iter(p.stdout.readline, b''):
            socketio.emit(client_event, {'data': line.decode(encoding="utf-8")})
    finally:
        p.stdout.close()


global_lock_tool = threading.RLock()
lock_dict = {'DEFAULT': threading.RLock()}


def get_my_lock(obj=None):
    if obj is None:
        return lock_dict['DEFAULT']
    global_lock_tool.acquire()
    try:
        if lock_dict.get(obj) is None:
            # TODO limit length of dict
            lock_dict[obj] = threading.RLock()
        return lock_dict[obj]
    finally:
        global_lock_tool.release()
