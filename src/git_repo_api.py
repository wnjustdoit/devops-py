#!/usr/bin/python3
from datetime import datetime

from flask import Blueprint, jsonify, current_app

from .entities.entity import Session
from .utils.pygitlab import GitlabAPI
from .entities.git_repo import GitRepo, GitRepoSchema

git_repo_api = Blueprint('git_repo_api', __name__)
app = git_repo_api


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
            # 特殊处理
            git_repo.ssh_url_to_repo = git_repo.ssh_url_to_repo.replace('192.168.1.248', 'git.mamaqunaer.cc')
            git_repo.http_url_to_repo = git_repo.http_url_to_repo.replace('192.168.1.248:8080', 'git.mamaqunaer.cc')
            git_repo.web_url = git_repo.web_url.replace('192.168.1.248:8080', 'git.mamaqunaer.cc')
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
@app.route("/git/repos/<int:id>", methods=['DELETE'])
def delete_git_repos(id):
    params_dict = {'is_deleted': 1}

    session = Session()
    try:
        session.query(GitRepo).filter(GitRepo.id == id).update(params_dict)
        session.commit()
    finally:
        session.close()

    return jsonify({'status': 'OK'})


# 根据repo id查询所有gitlab web hooks
@app.route("/git/repo/<int:id>/web_hooks")
def list_all_gitlab_web_hooks(id):
    result_list = []
    for hook in GitlabAPI().gl.projects.get(id).hooks.list():
        result_list.append({"id": hook.id, "url": hook.url, "project_id": hook.project_id})
    return jsonify(result_list)


# 添加gitlab project web hook
@app.route("/git/repo/<int:id>/web_hook", methods=['PUT'])
def add_gitlab_web_hook(id):
    GitlabAPI().gl.projects.get(id).hooks.create(current_app.config['GITLAB_WEB_HOOK_CONFIG'])
    return jsonify({'status': 'OK'})


# 根据repo id删除gitlab project web hook（全部）
@app.route("/git/repo/<int:id>/web_hook", methods=['DELETE'])
def delete_gitlab_web_hook(id):
    for hook in GitlabAPI().gl.projects.get(id).hooks.list():
        hook.delete()
    return jsonify({'status': 'OK'})


# 调用gitlab API实时获取指定git仓库的分支列表
@app.route("/git/repo/<int:id>/branches")
def git_repo_branches(id):
    return jsonify(GitlabAPI().get_project_branches(id))


# 调用gitlab API实时获取指定git仓库的标签列表
@app.route("/git/repo/<int:id>/tags")
def git_repo_tags(id):
    return jsonify(GitlabAPI().get_project_tags(id))


# 调用gitlab API实时获取指定git仓库的标签列表
@app.route("/git/repo/<int:id>/commits")
def git_repo_commits(id):
    return jsonify(GitlabAPI().get_project_commits(id))
