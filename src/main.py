#!/usr/bin/env python3

from flask import Flask, escape, request, make_response, session, render_template, json, jsonify, current_app
from flask_cors import CORS
from flask_socketio import SocketIO

import os
import subprocess
import threading
from datetime import datetime, timedelta
import uuid

from .mymodules.pygitlab import GitlabAPI
from .entities.entity import Session, or_
from .entities.git_repo import GitRepo, GitRepoSchema
from .entities.publishment import Publishment, PublishmentSchema
from .configs.profiles import configs, DEFAULT_CONFIG_ENV

app = Flask(__name__)
profile = os.environ.get('PROFILE', default=DEFAULT_CONFIG_ENV)
app.config.from_object(configs[profile])
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
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


# login
@app.route("/user/login", methods=["POST"])
def login():
    # TODO
    session['user'] = 'mark'
    return jsonify({'status': 'OK'})


# get user info
@app.route("/user/info", methods=["GET"])
def user_info():
    # TODO 含用户角色，区分前端、后端等身份，做权限
    print('==user/info==', request.headers)
    return jsonify(session.get('user'))


# logout
@app.route("/user/logout", methods=["GET", "POST"])
def logout():
    session.pop('user')
    session.clear()
    return jsonify('status', 'OK')


# add user
@app.route("/admin/user", methods=['PUT'])
def add_user():
    # TODO
    pass


# update user
@app.route("/admin/user", methods=['POST'])
def update_user():
    # TODO
    pass


# delete user
@app.route("/admin/user", methods=['DELETE'])
def delete_user():
    # TODO
    pass


# 调用gitlab API获取最新的git仓库信息，并更新到数据库
@app.route("/git/repos/database", methods=['POST'])
def fetch_git_repos_2_db():
    project_list = GitlabAPI().get_all_projects()
    git_repos_objects = GitRepoSchema(many=True).load(project_list)

    session = Session()
    try:
        for git_repo in git_repos_objects:
            git_repo.created_at = datetime.now()
            git_repo.created_by = 'system-auto'
            git_repo.last_updated_at = git_repo.created_at
            git_repo.last_updated_by = git_repo.created_by
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
        git_repos_objects = session.query(GitRepo).filter(GitRepo.is_deleted == 0).order_by(GitRepo.id).all()
        result_list = GitRepoSchema(many=True).dump(git_repos_objects)
    finally:
        session.close()

    return jsonify(result_list)


# 删除git仓库（逻辑删除）
@app.route("/git/repos", methods=['DELETE'])
def delete_git_repos():
    id = get_parameter('id')

    params_dict = {'is_deleted': 1}

    session = Session()
    try:
        session.query(GitRepo).filter(GitRepo.id == id).update(params_dict)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 调用gitlab API实时获取指定git仓库分支列表
@app.route("/git/repo/<int:id>/branches")
def git_repo_branches(id):
    return jsonify(GitlabAPI().get_project_branches(id))


# 获取发布列表
@app.route("/publishment/list", methods=['GET'])
def publishment_list():
    page_size = 10
    keyword = request.args.get('keyword')
    current_page = request.args.get('current_page')

    session = Session()
    try:
        base_statement = session.query(Publishment).select_from(Publishment) \
            .join(GitRepo, Publishment.git_repo_id == GitRepo.id)
        if keyword:
            base_statement = base_statement.filter(or_(Publishment.name.like('%' + keyword + '%'),
                                                       Publishment.description.like('%' + keyword + '%'),
                                                       Publishment.to_project_home.like('%' + keyword + '%'),
                                                       Publishment.to_process_name.like('%' + keyword + '%'),
                                                       GitRepo.name.like('%' + keyword + '%'),
                                                       GitRepo.description.like('%' + keyword + '%'),
                                                       GitRepo.ssh_url_to_repo.like('%' + keyword + '%'),
                                                       GitRepo.http_url_to_repo.like('%' + keyword + '%'),
                                                       GitRepo.web_url.like('%' + keyword + '%'),
                                                       GitRepo.path_with_namespace.like('%' + keyword + '%')
                                                       ))
        publishment_git_repos_objects = base_statement.limit(page_size).offset(
            (int(current_page) - 1) * page_size).all()
        if len(publishment_git_repos_objects) != 0:
            publishment_git_repos_counts = base_statement.count()
        else:
            publishment_git_repos_counts = 0
    finally:
        session.close()

    result_list = PublishmentSchema(many=True).dump(publishment_git_repos_objects)
    result = {'data': result_list, 'total': publishment_git_repos_counts}

    return jsonify(result)


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
@app.route("/publish", methods=['POST', 'GET'])
def publish():
    # TODO 考虑将参数、会话、客户端标识、是否允许发布等校验前移到此处来判断
    # TODO 暂时不允许git_repo相同的发布同时进行（可考虑构建项目和远程服务端启动服务分离成两部分，互不干扰）
    # 唯一标识参考：session（user、cookie【不同客户端同时登录是否保持一致？】）、单独维护的cookie、发布id、git_repo_url（url、group、name）
    if get_parameter('id') is None:
        return json.dumps({'status': 'ERROR', 'message' : '发布id不可为空'})
    # TODO 暂时此处处理cookie，给要发布的客户端增加标识（第一次）；后续改为：登录后使用发布系统并借助会话的cookie来操作
    # 如果队列存在当前客户端对该id的发布，那么拒绝；否者，执行或放入队列
    if request.cookies.get('publish_client_id') is None:
        response = make_response(json.dumps({'status': 'OK'}))
        response.set_cookie('publish_client_id', uuid.uuid4().hex)
        return response

    return json.dumps({'status': 'OK'})


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
    try:
        for line in iter(p.stdout.readline, b''):
            socketio.emit(client_event, {'data': line.decode(encoding="utf-8")})
    finally:
        p.stdout.close()


def get_parameter(key):
    if request.get_json() is not None:
        return request.get_json().get(key)
    return None


@socketio.on('connect', namespace='publish')
def test_connect():
    print("Socket client connected")


@socketio.on('disconnect', namespace='publish')
def test_disconnect():
    print('Socket Client disconnected')


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print('Socket error:', e)


def get_publishment_detail(id):
    session = Session()
    try:
        return session.query(Publishment).select_from(
            Publishment).join(GitRepo,
                              Publishment.git_repo_id == GitRepo.id).filter(Publishment.id == id).one_or_none()
    finally:
        session.close()


@socketio.on('publish_event')
def test_event(params):
    if request.cookies.get('publish_client_id') is None:
        print('ERROR: Get client cookie[publish_client_id] failed')
        return
    if params is None or params.get('id') is None:
        print('ERROR: The publish id cannot be empty')
        return

    # union unique key, mainly consists of client user session id and business id
    client_event = 'publish_response_' + request.cookies.get('publish_client_id') + '_' + str(params['id'])

    # publish process
    lock = get_my_lock(params['id'])
    try_lock_result = lock.acquire(blocking=False)  # try lock once
    if not try_lock_result:
        socketio.emit(client_event, {'message': '当前有相同发布正在进行，尝试本次发布最多等待10s'})
        lock_result = lock.acquire(timeout=10)  # lock, timeout of 10 seconds
        if not lock_result:
            socketio.emit(client_event, {'message': '当前发布繁忙（等待10s超时），请稍后再试'})
            return
    try:
        publishment = get_publishment_detail(params['id'])
        execute_cmd(client_event, publishment)
    finally:
        lock.release()  # release lock (if necessary)

    # publish end
    socketio.emit(client_event, {'status': 'OK', 'project': publishment.name})


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
