#! /usr/bin/env python3

from .entity import Entity, Base
from .git_repo import GitRepoSchema
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class Publishment(Base, Entity):
    __tablename__ = 'publishment'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    git_repo_id = Column(Integer, ForeignKey('git_repo.id'))
    git_delete_temp_branch = Column(Integer)
    git_branches = Column(String)
    profile = Column(String)
    to_username = Column(String)
    to_ip = Column(String)
    to_project_home = Column(String)
    to_process_name = Column(String)
    to_java_opts = Column(String)
    git_merged_branch = Column(String)
    git_tag_version = Column(String)
    git_tag_comment = Column(String)
    git_repo = relationship("GitRepo", uselist=False, primaryjoin='Publishment.git_repo_id == GitRepo.id', lazy=False)

    def __init__(self, git_repo_id, git_branches, profile, to_username, to_ip, to_project_home, to_process_name,
                 to_java_opts,
                 git_merged_branch, git_tag_version, git_tag_comment, git_delete_temp_branch, name, description,
                 created_by=None):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description
        self.git_repo_id = git_repo_id
        self.git_branches = git_branches
        self.profile = profile
        self.to_username = to_username
        self.to_ip = to_ip
        self.to_project_home = to_project_home
        self.to_process_name = to_process_name
        self.to_java_opts = to_java_opts
        self.git_merged_branch = git_merged_branch
        self.git_tag_version = git_tag_version
        self.git_tag_comment = git_tag_comment
        self.git_delete_temp_branch = git_delete_temp_branch


class PublishmentSchema(Schema):
    id = git_repo_id = git_delete_temp_branch = fields.Number()
    git_branches = profile = to_username = to_ip = to_project_home = to_process_name = to_java_opts = git_merged_branch = \
        git_tag_version = git_tag_comment = name = description = fields.Str()
    git_repo = fields.Nested(GitRepoSchema, many=False)
