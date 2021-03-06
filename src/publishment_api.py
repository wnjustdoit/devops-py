#!/usr/bin/python3
import uuid

import configparser
from flask import Blueprint, request, jsonify, make_response, session as web_session
from sqlalchemy import or_

from src.entities.entity import Session
from src.entities.git_repo import GitRepo
from src.entities.publishment import Publishment, PublishmentSchema
from src.utils.sshcmd import ssh_cmd, ssh_cmd_one

publishment_api = Blueprint('publishment_api', __name__)
app = publishment_api


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
        return jsonify({'status': 'ERROR', 'message': '发布id不可为空'})
    # TODO 暂时此处处理cookie，给要发布的客户端增加标识（第一次）；后续改为：登录后使用发布系统并借助会话的cookie来操作
    # 如果队列存在当前客户端对该id的发布，那么拒绝；否者，执行或放入队列

    if web_session.get('user') is None:
        return jsonify({'status': 'FAILED', 'login': 'yes'})

    return jsonify({'status': 'OK'})


def get_publishment_detail(id):
    session = Session()
    try:
        return session.query(Publishment).select_from(
            Publishment).join(GitRepo,
                              Publishment.git_repo_id == GitRepo.id).filter(Publishment.id == id).one_or_none()
    finally:
        session.close()


def get_publishment_by_repo_id(git_repo_id):
    session = Session()
    try:
        return session.query(Publishment).select_from(Publishment).join(GitRepo,
                                                                        Publishment.git_repo_id == GitRepo.id).filter(
            Publishment.git_repo_id == git_repo_id).all()
    finally:
        session.close()


def get_parameter(key):
    if request.get_json() is not None:
        return request.get_json().get(key)
    return None


server_passport_config_location = 'src/configs/server_passport.cfg'


# 查看应用健康状态（是否停机）
@app.route("/publish/status/<int:id>")
def publish_status(id):
    publishment = get_publishment_detail(id)
    # read config.properties
    config = configparser.ConfigParser()
    config.read(server_passport_config_location)
    to_username = config.get(publishment.to_ip, 'username')
    to_password = config.get(publishment.to_ip, 'password')
    status, ssh_cmd_result_msg = ssh_cmd_one(publishment.to_ip, to_password,
                                             'ps -ef | grep -w ' + publishment.to_process_name + ' | grep -v grep | awk \'{print $2}\'',
                                             to_username)
    if status == 1:
        return jsonify({'status': 'OK', 'process_id': ssh_cmd_result_msg})
    else:
        return jsonify({'status': 'FAILED'})


# 停止应用
@app.route("/publish/shutdown/<int:id>", methods=['POST', 'GET'])
def publish_shutdown(id):
    publishment = get_publishment_detail(id)
    # read config.properties
    config = configparser.ConfigParser()
    config.read(server_passport_config_location)
    to_username = config.get(publishment.to_ip, 'username')
    to_password = config.get(publishment.to_ip, 'password')
    ssh_cmd_result = ssh_cmd(publishment.to_ip, to_password,
                             [
                                 f'cd {publishment.to_project_home};'
                                 f'find_jar_result=$(find . -maxdepth 1 -name "*.jar");'
                                 f'if [ "$find_jar_result" != "" ]; then '
                                 f'sh /home/devops/shutdown.sh {publishment.to_process_name};'
                                 f'else '
                                 f'sh /home/devops/shutdown_war.sh {publishment.to_project_home} {publishment.to_process_name};'
                                 f'fi'],
                             to_username)
    if ssh_cmd_result == 0:
        print(f'Application[publishment:{publishment.name}] shutdown SUCCESS!')
    return jsonify({'status': 'OK' if ssh_cmd_result == 0 else 'FAILED'})


# 重启应用
@app.route("/publish/reboot/<int:id>", methods=['POST', 'GET'])
def publish_reboot(id):
    publishment = get_publishment_detail(id)
    # read config.properties
    config = configparser.ConfigParser()
    config.read(server_passport_config_location)
    to_username = config.get(publishment.to_ip, 'username')
    to_password = config.get(publishment.to_ip, 'password')
    ssh_cmd_result = ssh_cmd(publishment.to_ip, to_password,
                             [
                                 f'cd {publishment.to_project_home};'
                                 f'find_jar_result=$(find . -maxdepth 1 -name "*.jar");'
                                 f'if [ "$find_jar_result" != "" ]; then '
                                 f'sh /home/devops/reboot_jar.sh {publishment.to_project_home} {publishment.to_process_name} "{publishment.to_java_opts}";'
                                 f'else '
                                 f'sh /home/devops/reboot_war.sh {publishment.to_project_home} {publishment.to_process_name};'
                                 f'fi'],
                             to_username)
    if ssh_cmd_result == 0:
        print(f'Application[publishment:{publishment.name}] reboot SUCCESS!')
    return jsonify({'status': 'OK' if ssh_cmd_result == 0 else 'FAILED'})
