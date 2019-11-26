#!/usr/bin/python3
from datetime import datetime

from flask import Blueprint, jsonify

from src.entities.entity import Session
from src.mymodules.pygitlab import GitlabAPI
from src.entities.git_repo import GitRepo, GitRepoSchema

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


# 调用gitlab API实时获取指定git仓库分支列表
@app.route("/git/repo/<int:id>/branches")
def git_repo_branches(id):
    return jsonify(GitlabAPI().get_project_branches(id))
