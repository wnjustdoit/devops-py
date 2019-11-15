# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class GitRepo(Base):
    __tablename__ = 'git_repo'

    id = Column(Integer, primary_key=True, server_default=text("nextval('git_repo_id_seq'::regclass)"))
    description = Column(String(128))
    ssh_url_to_repo = Column(String(128), nullable=False)
    http_url_to_repo = Column(String(128), nullable=False)
    web_url = Column(String(128), nullable=False)
    name = Column(String(64), nullable=False)
    name_with_namespace = Column(String(64), nullable=False)
    path = Column(String(64), nullable=False)
    path_with_namespace = Column(String(64), nullable=False)
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by = Column(String(32), nullable=False, comment='创建人')
    last_updated_at = Column(DateTime, nullable=False, comment='最后更新时间')
    last_updated_by = Column(String(32), nullable=False, comment='最后更新人')
    is_deleted = Column(Integer, nullable=False, comment='是否删除：0表示正常，1表示已删除')


class Publishment(Base):
    __tablename__ = 'publishment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('publishment_id_seq'::regclass)"), comment='主键id')
    name = Column(String, nullable=False, comment='发布名称')
    description = Column(String, nullable=False, comment='发布描述')
    git_repo_id = Column(ForeignKey('git_repo.id'), nullable=False, comment='git仓库id')
    git_branches = Column(String(32), nullable=False, comment='发布的git分支')
    profile = Column(String(8), nullable=False, comment='发布环境')
    to_ip = Column(String(64), nullable=False, comment='目标服务器ip，多个以半角逗号分隔')
    to_project_home = Column(String(64), nullable=False, comment='目标服务器项目主目录')
    to_process_name = Column(String(32), nullable=False, comment='目标服务器项目进程名')
    to_java_opts = Column(String(128), comment='JAVA变量')
    git_merged_branch = Column(String(16), comment='发布完毕后git合并到的分支')
    git_tag_version = Column(String(16), comment='发布完毕后git打标签名')
    git_tag_comment = Column(String(128), comment='发布完毕后git打标签备注，依赖于git_tag_version')
    git_delete_temp_branch = Column(Integer, comment='发布完毕后是否删除临时git分支，多分支发布时有效')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by = Column(String(32), nullable=False, comment='创建人')
    last_updated_at = Column(DateTime, nullable=False, comment='最后更新时间')
    last_updated_by = Column(String(32), nullable=False, comment='最后更新人')
    is_deleted = Column(Integer, nullable=False, comment='是否删除：0表示正常，1表示已删除')

    git_repo = relationship('GitRepo')


class PublishmentFeVue(Base):
    __tablename__ = 'publishment_fe_vue'

    id = Column(Integer, primary_key=True, server_default=text("nextval('publishment_fe_vue_id_seq'::regclass)"), comment='主键id')
    name = Column(String, nullable=False, comment='发布名称')
    description = Column(String, nullable=False, comment='发布描述')
    git_repo_id = Column(ForeignKey('git_repo.id'), nullable=False, comment='git仓库id')
    git_branches = Column(String(32), nullable=False, comment='发布的git分支')
    profile = Column(String(8), nullable=False, comment='发布环境')
    to_ip = Column(String(64), nullable=False, comment='目标服务器ip')
    to_project_home = Column(String(64), nullable=False, comment='目标服务器主目录')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by = Column(String(32), nullable=False, comment='创建人')
    last_updated_at = Column(DateTime, nullable=False, comment='最后更新时间')
    last_updated_by = Column(String(32), nullable=False, comment='最后更新人')
    is_deleted = Column(Integer, nullable=False, comment='是否删除：0表示正常，1表示已删除')

    git_repo = relationship('GitRepo')


class PublishmentStaticfile(Base):
    __tablename__ = 'publishment_staticfile'

    id = Column(Integer, primary_key=True, server_default=text("nextval('publishment_staticfile_id_seq'::regclass)"), comment='主键id')
    name = Column(String, nullable=False, comment='发布名称')
    description = Column(String, nullable=False, comment='发布描述')
    git_repo_id = Column(ForeignKey('git_repo.id'), nullable=False, comment='git仓库id')
    git_branches = Column(String(32), nullable=False, comment='发布的git分支')
    to_ip = Column(String(64), nullable=False, comment='目标服务器ip')
    to_project_home = Column(String(64), nullable=False, comment='目标服务器主目录')

    git_repo = relationship('GitRepo')
