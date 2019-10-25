#!/usr/bin/env python3

from flask import Flask, escape, request, render_template, json, jsonify
from flask_cors import CORS

from .mymodules import pygitlab as gl, postgresql as pg
import subprocess
from flask_socketio import SocketIO, send, emit
import click
import threading

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
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


# 调用gitlab API获取最新的git仓库信息，并更新到数据库
@app.route("/git/repos/database", methods=['POST'])
def fetch_git_repos_2_db():
    fields_list = ['id', 'description', 'ssh_url_to_repo', 'http_url_to_repo', 'web_url', 'name', 'name_with_namespace',
                   'path', 'path_with_namespace']
    project_list = gl.GitlabAPI().get_all_projects()
    # 先删除所有
    pg.write_db("""delete from git_repo""",
                (),
                'wangnan', 'postgres', 'devops')
    for project in project_list:
        params = []
        for idx, field in enumerate(fields_list):
            params.append(str(project[field]))
        # 循环插入
        pg.write_db(
            """insert into git_repo(""" + ','.join(fields_list) + """) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET """ + ','.join([seg_up + ' = EXCLUDED.' + seg_up for seg_up in fields_list]),
            params,
            'wangnan', 'postgres', 'devops')
    return json.dumps({'status': 'OK'})


# 查询git仓库列表
@app.route("/git/repos")
def git_repos():
    fields_list = ['id', 'description', 'ssh_url_to_repo', 'http_url_to_repo', 'web_url', 'name', 'name_with_namespace',
                   'path', 'path_with_namespace']
    result_list = pg.select_all("""select """ + ','.join(fields_list) + """ from git_repo""", (),
                                'wangnan', 'postgres', 'devops')
    return_list = []
    for result in result_list:
        dict_result = {}
        for idx, val in enumerate(result):
            dict_result[fields_list[idx]] = val
        return_list.append(dict_result)
    return json.dumps(return_list)


# 调用gitlab API实时获取指定git仓库分支列表
@app.route("/git/repo/<int:id>/branches")
def git_repo_branches(id):
    return json.dumps(gl.GitlabAPI().get_project_branches(id))


# 获取发布列表
@app.route("/publishment/list")
def publishment_list():
    fields_list = ['id', 'name', 'description', 'git_repo_id', 'git_branches', 'profile', 'to_username', 'to_ip',
                   'to_project_home', 'to_process_name', 'to_java_opts', 'git_merged_branch', 'git_tag_version',
                   'git_tag_comment', 'git_delete_temp_branch']
    result_list = pg.select_all("""select """ + ','.join(fields_list) + """ from publishment""", (),
                                'wangnan', 'postgres', 'devops')
    return_list = []
    for result in result_list:
        dict_result = {}
        for idx, val in enumerate(result):
            dict_result[fields_list[idx]] = val
        return_list.append(dict_result)
    return json.dumps(return_list)


# 获取发布详情
@app.route("/publishment/<int:id>")
def publishment_detail(id):
    fields_list = ['id', 'name', 'description', 'git_repo_id', 'git_branches', 'profile', 'to_username', 'to_ip',
                   'to_project_home', 'to_process_name', 'to_java_opts', 'git_merged_branch', 'git_tag_version',
                   'git_tag_comment', 'git_delete_temp_branch']
    result_list = pg.select_all("""select """ + ','.join(fields_list) + """ from publishment where id = %s""",
                                (str(id)),
                                'wangnan', 'postgres', 'devops')
    return_list = []
    for result in result_list:
        dict_result = {}
        for idx, val in enumerate(result):
            if fields_list[idx] == 'git_branches':
                val = val.split(',')
            elif fields_list[idx] == 'to_ip':
                val = val.split(',')
            dict_result[fields_list[idx]] = val
        return_list.append(dict_result)
    return json.dumps(return_list)


# 添加发布信息
@app.route("/publishment", methods=['PUT'])
def add_publishment():
    pg.write_db(
        """insert into publishment
        (name, description, git_repo_id, git_branches, profile, to_username, to_ip, to_project_home, to_process_name, 
        to_java_opts, git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch) 
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (get_parameter('name'), get_parameter('description'), get_parameter('git_repo_id'),
         ','.join(get_parameter('git_branches')),
         get_parameter('profile'),
         get_parameter('to_username'), get_parameter('to_ip')[0], get_parameter('to_project_home'),
         get_parameter('to_process_name'),
         get_parameter('to_java_opts'),
         get_parameter('git_merged_branch'), get_parameter('git_tag_version'),
         get_parameter('git_tag_comment'),
         1 if get_parameter('git_delete_temp_branch') == 'true' else 0),
        'wangnan', 'postgres', 'devops')
    return json.dumps({'status': 'OK'})


# 更新发布信息
@app.route("/publishment", methods=['POST'])
def update_publishment():
    pg.write_db("""update publishment set name = %s, description = %s, git_repo_id = %s, git_branches = %s,
     profile = %s, to_username = %s, to_ip = %s, to_project_home = %s, to_process_name = %s, 
        to_java_opts = %s, git_merged_branch = %s, git_tag_version = %s, git_tag_comment = %s, git_delete_temp_branch = %s where id = %s""",
                (get_parameter('name'), get_parameter('description'), get_parameter('git_repo_id'),
                 ','.join(get_parameter('git_branches')),
                 get_parameter('profile'),
                 get_parameter('to_username'), get_parameter('to_ip')[0], get_parameter('to_project_home'),
                 get_parameter('to_process_name'),
                 get_parameter('to_java_opts'),
                 get_parameter('git_merged_branch'), get_parameter('git_tag_version'),
                 get_parameter('git_tag_comment'),
                 1 if get_parameter('git_delete_temp_branch') == 'true' else 0,
                 get_parameter('id')),
                'wangnan', 'postgres', 'devops')
    return json.dumps({'status': 'OK'})


# 删除发布信息
@app.route("/publishment", methods=['DELETE'])
def delete_publishment():
    id = json.loads(request._get_data_for_json(False).decode('utf8'))['id']
    pg.write_db("""delete from publishment where id = %s""", (str(id)),
                'wangnan', 'postgres', 'devops')
    return json.dumps({'status': 'OK'})


# 发布应用
@app.route("/publish", methods=['POST'])
def publish():
    fields_list = ['id', 'name', 'description', 'git_repo_id', 'git_branches', 'profile', 'to_username', 'to_ip',
                   'to_project_home', 'to_process_name', 'to_java_opts', 'git_merged_branch', 'git_tag_version',
                   'git_tag_comment', 'git_delete_temp_branch']
    # 根据应用id查询应用发布信息
    result_list = pg.select_all("""select * from table where id = %s""",
                                (get_parameter('id')),
                                'wangnan', 'postgres', 'devops')
    params_json = {}
    for idx, val in enumerate(result_list[0]):
        params_json[fields_list[idx]] = val

    threading.Thread(target=execute_cmd, args=(params_json)).start()
    return json.dumps({'status': 'OK'})


def execute_cmd(params_json):
    p = subprocess.Popen("""python3 mymodules/devops.py \
            --git_repo={git_repo} --git_branches={git_branches} --project_name={project_name} --profile={profile} --to_username={to_username} --to_ip={to_ip} --to_project_home={to_project_home} \
            --to_process_name={to_process_name} --to_java_opts={to_java_opts}, --git_merged_branch={git_merged_branch}, --git_tag_version={git_tag_version}, --git_tag_comment={git_tag_comment}, --git_delete_temp_branch={git_delete_temp_branch}"""
                         .format(git_repo=params_json['git_repo'], git_branches=params_json['git_branches'],
                                 project_name=params_json['project_name']
                                 , profile=params_json['profile'], to_username=params_json['to_username'],
                                 to_ip=params_json['to_ip'], to_project_home=params_json['to_project_home']
                                 , to_process_name=params_json['to_process_name'], to_java_opts=['to_java_opts'],
                                 git_merged_branch=params_json['git_merged_branch'],
                                 git_tag_version=params_json['git_tag_version'],
                                 git_tag_comment=params_json['git_tag_comment'],
                                 git_delete_temp_branch=params_json['git_delete_temp_branch']),
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
    return request.get_json()[key]


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
