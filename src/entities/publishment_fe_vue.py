#! /usr/bin/env python3

from .entity import Entity, Base
from .git_repo import GitRepoSchema
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class PublishmentFeVue(Base, Entity):
    __tablename__ = 'publishment_fe_vue'

    id = Column(Integer, Sequence('publishment_fe_vue_id_seq'), primary_key=True, comment='主键id')
    name = Column(String(64), nullable=False, comment='发布名称')
    description = Column(String(128), nullable=False, comment='发布描述')
    git_repo_id = Column(Integer, ForeignKey('git_repo.id'), nullable=False, comment='git仓库id')
    git_branches = Column(String(32), nullable=False, comment='发布的git分支')
    profile = Column(String(8), nullable=False, comment='发布环境')
    source_file_dir = Column(String(64), nullable=True, default='', comment='发布文件的相对目录（相对于源项目的根目录）')
    to_ip = Column(String(64), nullable=False, comment='目标服务器ip')
    to_project_home = Column(String(64), nullable=False, comment='目标服务器主目录')
    git_repo = relationship("GitRepo", uselist=False, primaryjoin='PublishmentFeVue.git_repo_id == GitRepo.id',
                            lazy=False)

    def __init__(self, name, description, git_repo_id, git_branches, profile, source_file_dir, to_ip, to_project_home,
                 created_by=None):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description
        self.git_repo_id = git_repo_id
        self.git_branches = git_branches
        self.profile = profile
        self.source_file_dir = source_file_dir
        self.to_ip = to_ip
        self.to_project_home = to_project_home


class PublishmentFeVueSchema(Schema):
    id = git_repo_id = git_delete_temp_branch = fields.Number()
    name = description = git_branches = profile = source_file_dir = to_ip = to_project_home = fields.Str(missing=None)
    git_repo = fields.Nested(GitRepoSchema, many=False)
