#!/usr/bin/python3
import uuid

from flask import Blueprint, request, jsonify, make_response
from sqlalchemy import or_

from src.entities.git_repo import GitRepo
from .entities.publishment_nodejs import PublishmentNodejs, PublishmentNodejsSchema
from .entities.entity import Session

publishment_nodejs_api = Blueprint('publishment_nodejs_api', __name__)
app = publishment_nodejs_api


# 获取发布列表
@app.route("/publishmentNodejs/list", methods=['GET'])
def publishment_list():
    page_size = 10
    keyword = request.args.get('keyword')
    current_page = request.args.get('current_page')

    session = Session()
    try:
        base_statement = session.query(PublishmentNodejs).select_from(PublishmentNodejs) \
            .join(GitRepo, PublishmentNodejs.git_repo_id == GitRepo.id)
        if keyword:
            base_statement = base_statement.filter(or_(PublishmentNodejs.name.like('%' + keyword + '%'),
                                                       PublishmentNodejs.description.like('%' + keyword + '%'),
                                                       PublishmentNodejs.to_project_home.like('%' + keyword + '%'),
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

    result_list = PublishmentNodejsSchema(many=True).dump(publishment_git_repos_objects)
    result = {'data': result_list, 'total': publishment_git_repos_counts}

    return jsonify(result)


# 获取发布详情
@app.route("/publishmentNodejs/<int:id>")
def publishment_detail(id):
    session = Session()
    try:
        result_object = session.query(PublishmentNodejs).filter(PublishmentNodejs.id == id).one_or_none()
    finally:
        session.close()

    result = PublishmentNodejsSchema().dump(result_object)
    if result_object:
        result['git_branches'] = result.get('git_branches').split(',')
        result['to_ip'] = result.get('to_ip').split(',')

    return jsonify(result)


# 添加发布信息
@app.route("/publishmentNodejs", methods=['PUT'])
def add_publishment():
    params_dict = request.get_json()
    params_dict['git_branches'] = ','.join(params_dict.get('git_branches'))
    params_dict['to_ip'] = ','.join(params_dict.get('to_ip'))
    posted_publishment = PublishmentNodejsSchema().load(params_dict)
    publishment = PublishmentNodejs(**posted_publishment, created_by="HTTP post request")

    session = Session()
    try:
        session.add(publishment)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 更新发布信息
@app.route("/publishmentNodejs", methods=['POST'])
def update_publishment():
    params_dict = request.get_json()
    id = params_dict['id']
    params_dict['git_branches'] = ','.join(params_dict.get('git_branches'))
    params_dict['to_ip'] = ','.join(params_dict.get('to_ip'))
    params_dict.pop('id')
    params_dict.pop('git_repo')

    session = Session()
    try:
        session.query(PublishmentNodejs).filter(PublishmentNodejs.id == id).update(params_dict)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 删除发布信息
@app.route("/publishmentNodejs/<int:id>", methods=['DELETE'])
def delete_publishment(id):
    session = Session()
    try:
        session.query(PublishmentNodejs).filter(PublishmentNodejs.id == id).delete()
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 发布应用
@app.route("/publishNodejs", methods=['POST', 'GET'])
def publish():
    # TODO 考虑将参数、会话、客户端标识、是否允许发布等校验前移到此处来判断
    # TODO 暂时不允许git_repo相同的发布同时进行（可考虑构建项目和远程服务端启动服务分离成两部分，互不干扰）
    # 唯一标识参考：session（user、cookie【不同客户端同时登录是否保持一致？】）、单独维护的cookie、发布id、git_repo_url（url、group、name）
    if get_parameter('id') is None:
        return jsonify({'status': 'ERROR', 'message': '发布id不可为空'})
    # TODO 暂时此处处理cookie，给要发布的客户端增加标识（第一次）；后续改为：登录后使用发布系统并借助会话的cookie来操作
    # 如果队列存在当前客户端对该id的发布，那么拒绝；否者，执行或放入队列
    if request.cookies.get('publish_client_id') is None:
        response = make_response(jsonify({'status': 'OK'}))
        response.set_cookie('publish_client_id', uuid.uuid4().hex)
        return response

    return jsonify({'status': 'OK'})


def get_publishment_detail_nodejs(id):
    session = Session()
    try:
        return session.query(PublishmentNodejs).select_from(
            PublishmentNodejs).join(GitRepo,
                                    PublishmentNodejs.git_repo_id == GitRepo.id).filter(
            PublishmentNodejs.id == id).one_or_none()
    finally:
        session.close()


def get_publishment_nodejs_by_repo_id(git_repo_id):
    session = Session()
    try:
        return session.query(PublishmentNodejs).select_from(
            PublishmentNodejs).join(GitRepo,
                                    PublishmentNodejs.git_repo_id == GitRepo.id).filter(
            PublishmentNodejs.id == git_repo_id).all()
    finally:
        session.close()


def get_parameter(key):
    if request.get_json() is not None:
        return request.get_json().get(key)
    return None
