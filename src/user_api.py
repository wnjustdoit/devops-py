#!/usr/bin/python3

from flask import Blueprint, session, request, jsonify

user_api = Blueprint('user_api', __name__)
app = user_api


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
