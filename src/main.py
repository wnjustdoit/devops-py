#!/usr/bin/env python3
import time

from flask import Flask, escape, request, render_template, current_app, session as web_session
from flask_cors import CORS
from flask_socketio import SocketIO

import os
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta, datetime
from apscheduler.schedulers.background import BackgroundScheduler

# for PyCharm
if os.getenv('IDE'):
    __name__ = 'src'
from .configs.profiles import configs, DEFAULT_CONFIG_ENV
from .utils.pymail import MailAPI
from .utils.pyimage import new_image

from .user_api import user_api
from .git_repo_api import git_repo_api
from .publishment_api import publishment_api, get_publishment_detail, get_publishment_by_repo_id
from .publishment_staticfile_api import publishment_staticfile_api, get_publishment_detail_static, \
    get_publishment_static_by_repo_id
from .publishment_fe_vue_api import publishment_fe_vue_api, get_publishment_detail_fe, get_publishment_fe_by_repo_id
from .publishment_nodejs_api import publishment_nodejs_api, get_publishment_detail_nodejs, \
    get_publishment_nodejs_by_repo_id
from .publishment_log_api import publishment_log_api, add_publishment_log, PublishmentLog, clear_publishment_log

# for PyCharm
if os.getenv('IDE'):
    __name__ = '__main__'
app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')
profile = os.environ.get('PROFILE', default=DEFAULT_CONFIG_ENV)
app.config.from_object(configs[profile])
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

app.register_blueprint(user_api)
app.register_blueprint(git_repo_api)
app.register_blueprint(publishment_api)
app.register_blueprint(publishment_staticfile_api)
app.register_blueprint(publishment_fe_vue_api)
app.register_blueprint(publishment_nodejs_api)
app.register_blueprint(publishment_log_api)

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
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print('Socket error:', e)


@socketio.on('publish_event')
def publish_event(params):
    if params is None or params.get('id') is None:
        print('ERROR: The publish id cannot be empty')
        return
    id = params['id']
    type_prefix = '' if params.get('type') is None else params['type'] + '_'

    # 模拟登录
    web_session['user'] = {'created_at': '2019-12-13T15:57:25.389417', 'created_by': 'admin',
                           'email': 'devops@mamaqunaer.com',
                           'gitlab_email': 'devops@mamaqunaer.com', 'id': 2.0, 'is_deleted': 0.0,
                           'last_updated_at': '2019-12-13T15:57:25.389417', 'last_updated_by': None,
                           'login_code': 'admin',
                           'login_pwd': None, 'nick_name': '超级管理员', 'role': 'devops'}
    user_json = web_session.get('user')
    if user_json is None:
        print('WARN: You need login at first')
        return
    email = web_session['user'].get('email')

    # union unique key, mainly consists of client user session id and business id
    client_event = 'publish_response_' + type_prefix + request.cookies.get('session_id') + '_' + str(id)

    # publish process
    lock = get_my_lock(type_prefix + str(id))  # publish id lock, group by type(such as backend, fe, node, static etc..)
    try_lock_result = lock.acquire(blocking=False)  # try lock once
    if not try_lock_result:
        socketio.emit(client_event, {'message': '当前有相同发布（type + publishId）正在进行，尝试本次发布最多等待10s'})
        lock_result = lock.acquire(timeout=10)  # lock, timeout of 10 seconds
        if not lock_result:
            socketio.emit(client_event, {'message': '当前发布繁忙（等待10s超时），请稍后再试'})
            return
    try:
        publishment = get_publishment(params)
        git_repo_id = publishment.git_repo_id
        git_lock = get_my_lock(git_repo_id)  # git repo's id lock
        try_git_lock_result = git_lock.acquire(blocking=False)  # try lock once
        if not try_git_lock_result:
            socketio.emit(client_event, {'message': '当前有相同发布（gitRepoId）正在进行，尝试本次发布最多等待10s'})
            git_lock_result = git_lock.acquire(timeout=10)  # lock, timeout of 10 seconds
            if not git_lock_result:
                socketio.emit(client_event, {'message': '当前发布繁忙（等待10s超时），请稍后再试'})
                return
        try:
            publishment_log_content = execute_publishment(client_event, params, publishment)
            to_email = [email]
            do_publishment_log_async(publishment, type_prefix, publishment_log_content, to_email=to_email)
        finally:
            git_lock.release()  # release lock (if necessary/accessed)
    finally:
        lock.release()  # release lock (if necessary/accessed)


executor = ThreadPoolExecutor(max_workers=5)


def do_publishment_log_async(publishment, publish_type, publishment_log_content, to_email: list = None,
                             publish_way: str = 'browser'):
    executor.submit(do_publishment_log, publishment, publish_type, publishment_log_content, to_email, publish_way)


def do_publishment_log(publishment, publish_type, publishment_log_content, to_email: list = None,
                       publish_way: str = 'browser'):
    log_name = f'PUBLISHED_{publishment.name}_' + time.strftime("%Y%m%d%H%M%S", time.localtime())
    publishment_log = PublishmentLog(log_name, publishment.id, publishment_log_content, publish_type, publish_way)
    add_publishment_log(publishment_log)
    if to_email is None or len(to_email) == 0:
        print('WARN: to_email is empty, ignore email sending.')
        return
    link = current_app.config['SCHEMA'] + "://" + current_app.config['HOST'] + ":" + str(
        current_app.config['VIEW_PORT']) + "/#/publishedDetail?id=" + str(publishment_log.id)
    email_content = f'发布日志如下：<a href="{link}"><img src="cid:image1"></a>'
    image_base64_bytes = new_image(1000, 4000, publishment_log_content, font_size=12)
    file_path = current_app.config['WORK_HOME'] + '/logs/' + log_name + '.txt'
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(publishment_log_content)
        f.close()
    MailAPI.GenericSender(MailAPI(), subject=log_name, to=to_email).add_text(
        email_content, _type='html').add_image_base64str(image_base64_bytes, 'image1').add_file(
        file_path).send_default()


def get_publishment(params):
    id = params.get('id')
    if params.get('type') is None or params.get('type') == 'publishment':
        return get_publishment_detail(id)
    elif params.get('type') == 'static':
        return get_publishment_detail_static(id)
    elif params.get('type') == 'fe':
        return get_publishment_detail_fe(id)
    elif params.get('type') == 'nodejs':
        return get_publishment_detail_nodejs(id)


def execute_publishment(client_event, params, publishment):
    if params.get('type') is None or params.get('type') == 'publishment':
        p = execute_script(publishment)
    elif params.get('type') == 'static':
        p = execute_script_static(publishment)
    elif params.get('type') == 'fe':
        p = execute_script_fe(publishment)
    elif params.get('type') == 'nodejs':
        p = execute_script_nodejs(publishment)
    else:
        print(f'ERROR: Unsupported publish type [{params.get("type")}]')
        return
    return output_content(p, client_event)


def execute_script(publishment):
    return subprocess.Popen("""python3 src/scripts/devops.py \
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
                            stderr=subprocess.STDOUT, shell=True, bufsize=0)


def execute_script_static(publishment_static):
    return subprocess.Popen("""python3 src/scripts/devops_staticfile.py \
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


def execute_script_fe(publishment_fe):
    return subprocess.Popen("""python3 src/scripts/devops_fe_vue.py \
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
                            stderr=subprocess.STDOUT, shell=True, bufsize=0)


def execute_script_nodejs(publishment):
    # TODO
    if True:
        return
    # return subprocess.Popen("""python3 src/scripts/devops_nodejs.py \
    #         --work_home={work_home} \
    #         --git_repo={git_repo} --git_branches={git_branches} --project_name={project_name} --profile={profile} \
    #         --source_file_dir={source_file_dir} --to_ip={to_ip} --to_project_home={to_project_home}"""
    #                         .format(work_home=current_app.config.get('WORK_HOME'),
    #                                 git_repo=publishment.git_repo.ssh_url_to_repo,
    #                                 git_branches=publishment.git_branches,
    #                                 project_name=publishment.git_repo.name,
    #                                 profile=publishment.profile,
    #                                 source_file_dir=publishment.source_file_dir if publishment.source_file_dir is not None else '',
    #                                 to_ip=publishment.to_ip, to_project_home=publishment.to_project_home),
    #                         stdout=subprocess.PIPE,
    #                         stderr=subprocess.STDOUT, shell=True, bufsize=0)


def output_content(p, client_event=None):
    content = ''
    try:
        for line in iter(p.stdout.readline, b''):
            content += line.decode(encoding="utf-8")
            if client_event is not None:
                socketio.emit(client_event, {'data': line.decode(encoding="utf-8")})
        p.wait()
        if client_event is not None:
            print("--------end----------")
            socketio.emit(client_event, {'status': 'OK' if p.returncode == 0 else 'FAILED'})
        return p.returncode, content
    finally:
        p.stdout.close()


# reentrant lock
lock_for_getting_lock = threading.RLock()
lock_dict = {'DEFAULT': threading.RLock()}


def get_my_lock(obj=None):
    if obj is None:
        return lock_dict['DEFAULT']
    lock_for_getting_lock.acquire()
    try:
        if lock_dict.get(obj) is None:
            # TODO limit length of dict
            lock_dict[obj] = threading.RLock()
        return lock_dict[obj]
    finally:
        lock_for_getting_lock.release()


def get_parameter(key):
    if request.get_json() is not None:
        return request.get_json().get(key)
    return None


@app.route("/web_hook/publish", methods=['GET', 'POST'])
def web_hook():
    object_kind = get_parameter('object_kind')
    after = get_parameter('after')
    project_id = get_parameter('project_id')
    commits = get_parameter('commits')
    current_commit = None
    for commit in commits:
        if commit['id'] == after:
            current_commit = commit
            break
    keyword = 'devops'
    if current_commit is not None and current_commit['message'].index(keyword) != -1:
        do_publish_and_notify(project_id, str(get_parameter('user_email')))
    return 'FINISHED'


def do_publish_and_notify(git_repo_id, user_email):
    publishments = get_publishment_by_repo_id(git_repo_id)
    if publishments is not None and len(publishments) != 0:
        for publishment in publishments:
            (), publishment_log_content = output_content(execute_script(publishment))
            do_publishment_log_async(publishment, 'backend', publishment_log_content, [user_email], 'webhook')
        return

    publishments = get_publishment_fe_by_repo_id(git_repo_id)
    if publishments is not None and len(publishments) != 0:
        for publishment in publishments:
            (), publishment_log_content = output_content(execute_script_fe(publishment))
            do_publishment_log_async(publishment, 'fe_vue', publishment_log_content, [user_email], 'webhook')
        return

    publishments = get_publishment_static_by_repo_id(git_repo_id)
    if publishments is not None and len(publishments) != 0:
        for publishment in publishments:
            (), publishment_log_content = output_content(execute_script_static(publishment))
            do_publishment_log_async(publishment, 'staticfile', publishment_log_content, [user_email], 'webhook')
        return

    publishments = get_publishment_nodejs_by_repo_id(git_repo_id)
    if publishments is not None and len(publishments) != 0:
        for publishment in publishments:
            (), publishment_log_content = output_content(execute_script_nodejs(publishment))
            do_publishment_log_async(publishment, 'nodejs', publishment_log_content, [user_email], 'webhook')
        return

    print(f'WARN: current project [git_repo_id:{git_repo_id}] has not been configured on the DevOps stage')
    return


scheduler = BackgroundScheduler()
# 定时清理发布日志（30天前）
scheduler.add_job(clear_publishment_log, trigger='cron', day_of_week='*', hour='3', minute='12', second='23')
scheduler.start()
