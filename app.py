#!/usr/bin/env python3

from flask import Flask, escape, request, render_template, json, jsonify
from flask_cors import CORS

from .mymodules.pygitlab import GitlabAPI
from .entities.entity import Session
from .entities.git_repo import GitRepo, GitRepoSchema
from .entities.publishment import Publishment, PublishmentSchema
import subprocess
from flask_socketio import SocketIO, send, emit
import click
import threading
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')


@app.cli.command("app_run")
def app_run():
    # app.run()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)


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


# 调用gitlab API获取最新的git仓库信息，并更新到数据库
@app.route("/git/repos/database", methods=['POST'])
def fetch_git_repos_2_db():
    project_list = GitlabAPI().get_all_projects()
    git_repos_objects = GitRepoSchema(many=True).load(project_list)
    session = Session()
    try:
        for git_repo in git_repos_objects:
            session.merge(git_repo)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 查询git仓库列表
@app.route("/git/repos")
def git_repos():
    session = Session()
    try:
        git_repos_objects = session.query(GitRepo).order_by(GitRepo.id).all()
        result_list = GitRepoSchema(many=True).dump(git_repos_objects)
    finally:
        session.close()
    return jsonify(result_list)


# 调用gitlab API实时获取指定git仓库分支列表
@app.route("/git/repo/<int:id>/branches")
def git_repo_branches(id):
    return jsonify(GitlabAPI().get_project_branches(id))


# 获取发布列表
@app.route("/publishment/list")
def publishment_list():
    session = Session()
    try:
        publishment_git_repos_objects = session.query(Publishment).select_from(
            Publishment).join(GitRepo,
                              Publishment.git_repo_id == GitRepo.id).all()
    finally:
        session.close()

    result_list = PublishmentSchema(many=True).dump(publishment_git_repos_objects)

    return jsonify(result_list)


# 获取发布详情
@app.route("/publishment/<int:id>")
def publishment_detail(id):
    session = Session()
    try:
        result_object = session.query(Publishment).filter(Publishment.id == id).one_or_none()
    finally:
        session.close()

    result = PublishmentSchema().dump(result_object)
    if result_object:
        result['git_branches'] = result.get('git_branches').split(',')
        result['to_ip'] = result.get('to_ip').split(',')
        result['git_delete_temp_branch'] = True if result.get('git_delete_temp_branch') == 1 else False

    return jsonify(result)


# 添加发布信息
@app.route("/publishment", methods=['PUT'])
def add_publishment():
    params_dict = request.get_json()
    params_dict['git_branches'] = ','.join(params_dict.get('git_branches'))
    params_dict['to_ip'] = ','.join(params_dict.get('to_ip'))
    params_dict['git_delete_temp_branch'] = 1 if params_dict.get('git_delete_temp_branch') else 0
    posted_publishment = PublishmentSchema().load(params_dict)
    publishment = Publishment(**posted_publishment, created_by="HTTP post request")

    session = Session()
    try:
        session.add(publishment)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 更新发布信息
@app.route("/publishment", methods=['POST'])
def update_publishment():
    params_dict = request.get_json()
    id = params_dict['id']
    params_dict['git_branches'] = ','.join(params_dict.get('git_branches'))
    params_dict['to_ip'] = ','.join(params_dict.get('to_ip'))
    params_dict['git_delete_temp_branch'] = 1 if params_dict.get('git_delete_temp_branch') else 0
    params_dict.pop('id')
    params_dict.pop('git_repo')

    session = Session()
    try:
        session.query(Publishment).filter(Publishment.id == id).update(params_dict)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 删除发布信息
@app.route("/publishment", methods=['DELETE'])
def delete_publishment():
    id = get_parameter('id')

    session = Session()
    try:
        session.query(Publishment).filter(Publishment.id == id).delete()
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 发布应用
@app.route("/publish", methods=['POST'])
def publish():
    id = get_parameter('id')

    session = Session()
    try:
        result_object = session.query(Publishment).select_from(
            Publishment).join(GitRepo,
                              Publishment.git_repo_id == GitRepo.id).filter(Publishment.id == id).one_or_none()
    finally:
        session.close()

    params_json = PublishmentSchema().dump(result_object)

    threading.Thread(target=execute_cmd, kwargs=params_json).start()

    return json.dumps({'status': 'OK'})


def execute_cmd(**kwargs):
    params_json = kwargs
    p = subprocess.Popen("""python3 mymodules/devops.py \
            --git_repo={git_repo} --git_branches={git_branches} --project_name={project_name} --profile={profile} --to_username={to_username} --to_ip={to_ip} --to_project_home={to_project_home} \
            --to_process_name={to_process_name} --to_java_opts="{to_java_opts}" --git_merged_branch={git_merged_branch} --git_tag_version={git_tag_version} --git_tag_comment={git_tag_comment} --git_delete_temp_branch={git_delete_temp_branch}"""
                         .format(git_repo=params_json.get('git_repo').get('ssh_url_to_repo'),
                                 git_branches=params_json.get('git_branches'),
                                 project_name=params_json.get('git_repo').get('name'),
                                 profile=params_json.get('profile'), to_username=params_json.get('to_username'),
                                 to_ip=params_json.get('to_ip'), to_project_home=params_json.get('to_project_home'),
                                 to_process_name=params_json.get('to_process_name'),
                                 to_java_opts=params_json.get('to_java_opts'),
                                 git_merged_branch=params_json.get('git_merged_branch'),
                                 git_tag_version=params_json.get('git_tag_version'),
                                 git_tag_comment=params_json.get('git_tag_comment'),
                                 git_delete_temp_branch=params_json.get('git_delete_temp_branch')),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True, bufsize=1)

    # for info in p.communicate():
    #     print(info, )

    for line in iter(p.stdout.readline, b''):
        print(line.decode(encoding="utf-8"), )
        lock.acquire()
        try:
            list.append(line.decode(encoding="utf-8"))
        finally:
            lock.release()
    p.stdout.close()


list = []
lock = threading.Lock()


def get_parameter(key):
    return request.get_json().get(key)


@socketio.on('connect')
def test_connect():
    print("Socket client connected")


@socketio.on('disconnect')
def test_disconnect():
    print('Socket Client disconnected')


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print('Socket error:', e)


@socketio.on('my_event')
def test_event(params):
    print('my event', params)
    while True:
        lock.acquire()
        try:
            for line in list:
                socketio.emit('my_response', {'data': line})
                # socketio.sleep(1)
            list.clear()
        finally:
            lock.release()
