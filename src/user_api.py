#!/usr/bin/python3
import uuid

from flask import Blueprint, session as web_session, request, jsonify, make_response

from .entities.entity import Session
from .entities.user import User, UserSchema

user_api = Blueprint('user_api', __name__)
app = user_api


# user login
@app.route("/user/login", methods=["POST"])
def login():
    login_code = get_parameter('login_code')
    login_pwd = get_parameter('login_pwd')
    if login_code is None or login_code == '' or login_pwd is None or login_pwd == '':
        return jsonify({'status': 'FAILED'})

    session = Session()
    try:
        user = session.query(User).filter(
            User.login_code == login_code).filter(User.login_pwd == login_pwd).filter(
            User.is_deleted == 0).one_or_none()
    finally:
        session.close()

    if user is None:
        return jsonify('status', 'FAILED')

    user_json = UserSchema().dump(user)
    web_session['user'] = user_json
    response = make_response(jsonify({'status': 'OK', 'user': user_json}))
    response.set_cookie('session_id', uuid.uuid4().hex, max_age=7 * 24 * 60 * 60)
    return response


# get user info
@app.route("/user/info", methods=["GET"])
def user_info():
    # 模拟登录
    web_session['user'] = {'created_at': '2019-12-13T15:57:25.389417', 'created_by': 'admin',
                           'email': 'devops@mamaqunaer.com',
                           'gitlab_email': 'devops@mamaqunaer.com', 'id': 2.0, 'is_deleted': 0.0,
                           'last_updated_at': '2019-12-13T15:57:25.389417', 'last_updated_by': None,
                           'login_code': 'admin',
                           'login_pwd': None, 'nick_name': '超级管理员', 'role': 'devops'}
    user = web_session.get('user')
    if user is None:
        user = {}
    else:
        user['login_pwd'] = None
    return jsonify(user)


# user logout
@app.route("/user/logout", methods=["GET", "POST"])
def logout():
    web_session.pop('user')
    web_session.clear()
    response = make_response(jsonify({'status': 'OK'}))
    response.set_cookie('session_id', '', max_age=0)
    return response


# list all users
@app.route("/admin/user/list")
def git_repos():
    session = Session()
    try:
        user_objects = session.query(User).order_by(User.id).all()
        result_list = UserSchema(many=True).dump(user_objects)
    finally:
        session.close()

    return jsonify(result_list)


# add user
@app.route("/admin/user", methods=['PUT'])
def add_user():
    params_dict = request.get_json()
    user = UserSchema().load(params_dict)
    user.created_by = "admin"

    session = Session()
    try:
        session.add(user)
        session.commit()
    finally:
        session.close()

    return jsonify('status', 'OK')


# update user
@app.route("/admin/user/<int:id>", methods=['POST'])
def update_user(id):
    params_dict = request.get_json()

    session = Session()
    try:
        session.query(User).filter(User.id == id).update(params_dict)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# delete user(actually update)
@app.route("/admin/user/<int:id>", methods=['DELETE'])
def delete_user(id):
    is_deleted = get_parameter('is_deleted')
    if is_deleted is None or is_deleted < 0:
        return jsonify('status', 'FAILED')
    params_dict = {'is_deleted': is_deleted}

    user = web_session['user']
    if user is None or user.get('login_code') is None or user.get('login_code') == 'admin':
        return jsonify('status', 'FAILED')

    session = Session()
    try:
        session.query(User).filter(User.id == id).update(params_dict)
        session.commit()
    finally:
        session.close()

    return jsonify('status', 'OK')


def get_parameter(key):
    if request.get_json() is not None:
        return request.get_json().get(key)
    return None
