#!/usr/bin/env python3

from flask import Flask, escape, request, render_template
from .mymodules import pygitlab as gl, devops as do, postgresql as pg
import json
import subprocess
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)


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
        idx = 0
        for field in fields_list:
            params.append(str(project[field]))
            idx = idx + 1
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
        idx = 0
        dict_result = {}
        for val in result:
            dict_result[fields_list[idx]] = val
            idx = idx + 1
        return_list.append(dict_result)
    return json.dumps(return_list)


# 调用gitlab API实时获取指定git仓库分支列表
@app.route("/git/repo/<int:repoId>/branches")
def git_repo_branches(repoId):
    return json.dumps(gl.GitlabAPI().get_project_branches(repoId))


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
        idx = 0
        dict_result = {}
        for val in result:
            dict_result[fields_list[idx]] = val
            idx = idx + 1
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
        idx = 0
        dict_result = {}
        for val in result:
            if fields_list[idx] == 'git_branches':
                val = val.split(',')
            elif fields_list[idx] == 'to_ip':
                val = val.split(',')
            dict_result[fields_list[idx]] = val
            idx = idx + 1
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
    pid = json.loads(request._get_data_for_json(False).decode('utf8'))['id']
    pg.write_db("""delete from publishment where id = %s""", (str(pid)),
                'wangnan', 'postgres', 'devops')
    return json.dumps({'status': 'OK'})


# 发布应用
@app.route("/publish", methods=['POST'])
def publish():
    # 根据应用id查询应用发布信息
    # id = pg.select_all("""select """,
    #                    (get_parameter('id')),
    #                    'wangnan', 'postgres', 'devops')
    # return do.publish(gl.GitlabAPI().get_project_repo(int(get_parameter('git_repo_id'))), get_parameter('git_branches'),
    #                   gl.GitlabAPI().get_project_name(int(get_parameter('git_repo_id'))),
    #                   get_parameter('profile'),
    #                   get_parameter('to_username'), get_parameter('to_ip')[0], get_parameter('to_project_home'),
    #                   get_parameter('to_process_name'),
    #                   get_parameter('to_java_opts'),
    #                   get_parameter('git_merged_branch'), get_parameter('git_tag_version'),
    #                   get_parameter('git_tag_comment'),
    #                   get_parameter('git_delete_temp_branch'))
    p = subprocess.Popen('python3 -m /Users/wangnan/workspace/newlanguage/python/python3/flask/mymodules/devops.py',
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        print(line, )
    p.stdout.close()
    p.wait()
    return json.dumps({'status': 'OK'})


def get_parameter(key):
    return request.get_json()[key]
