#! /usr/bin/env python3

from .entity import Entity, EntitySchema, Base
from .git_repo import GitRepoSchema
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from marshmallow import fields


class Publishment(Base, Entity):
    __tablename__ = 'publishment'

    id = Column(Integer, Sequence('publishment_id_seq'), primary_key=True, comment='主键id')
    name = Column(String(64), nullable=False, comment='发布名称')
    description = Column(String(128), nullable=False, comment='发布描述')
    git_repo_id = Column(Integer, ForeignKey('git_repo.id'), nullable=False, comment='git仓库id')
    git_branches = Column(String(32), nullable=False, comment='发布的git分支')
    profile = Column(String(8), nullable=False, comment='发布环境')
    source_file_dir = Column(String(64), nullable=True, default='target', comment='发布文件的相对目录（相对于源项目的根目录）')
    to_ip = Column(String(64), nullable=False, comment='目标服务器ip，多个以半角逗号分隔')
    to_project_home = Column(String(64), nullable=False, comment='目标服务器项目主目录')
    to_process_name = Column(String(32), nullable=False, comment='目标服务器项目进程名')
    to_java_opts = Column(String(128), comment='JAVA变量')
    git_merged_branch = Column(String(16), comment='发布完毕后git合并到的分支')
    git_tag_version = Column(String(16), comment='发布完毕后git打标签名')
    git_tag_comment = Column(String(128), comment='发布完毕后git打标签备注，依赖于git_tag_version')
    git_delete_temp_branch = Column(Integer, comment='发布完毕后是否删除临时git分支，多分支发布时有效')
    git_repo = relationship("GitRepo", uselist=False, primaryjoin='Publishment.git_repo_id == GitRepo.id', lazy=False)

    def __init__(self, name, description, git_repo_id, git_branches, profile, source_file_dir, to_ip, to_project_home,
                 to_process_name, to_java_opts, git_merged_branch, git_tag_version, git_tag_comment,
                 git_delete_temp_branch,
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
        self.to_process_name = to_process_name
        self.to_java_opts = to_java_opts
        self.git_merged_branch = git_merged_branch
        self.git_tag_version = git_tag_version
        self.git_tag_comment = git_tag_comment
        self.git_delete_temp_branch = git_delete_temp_branch


class PublishmentSchema(EntitySchema):
    id = git_repo_id = git_delete_temp_branch = fields.Number()
    name = description = git_branches = profile = source_file_dir = to_ip = to_project_home = to_process_name \
        = to_java_opts = git_merged_branch = git_tag_version = git_tag_comment = fields.Str(missing=None)
    git_repo = fields.Nested(GitRepoSchema, many=False)
