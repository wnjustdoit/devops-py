#!/usr/bin/env python3

from .entity import Entity, EntitySchema, Base
from sqlalchemy import Column, Integer, String, Sequence
from marshmallow import Schema, fields, post_load


class GitRepo(Entity, Base):
    __tablename__ = 'git_repo'

    id = Column(Integer, Sequence('git_repo_id_seq'), primary_key=True)
    description = Column(String(128), nullable=True)
    ssh_url_to_repo = Column(String(128), nullable=False)
    http_url_to_repo = Column(String(128), nullable=False)
    web_url = Column(String(128), nullable=False)
    name = Column(String(64), nullable=False)
    name_with_namespace = Column(String(64), nullable=False)
    path = Column(String(64), nullable=False)
    path_with_namespace = Column(String(64), nullable=False)

    def __init__(self, description, ssh_url_to_repo, http_url_to_repo, web_url, name, name_with_namespace, path,
                 path_with_namespace, id=None, created_by=None):
        Entity.__init__(self, created_by)
        self.id = id
        self.description = description
        self.ssh_url_to_repo = ssh_url_to_repo
        self.http_url_to_repo = http_url_to_repo
        self.web_url = web_url
        self.name = name
        self.name_with_namespace = name_with_namespace
        self.path = path
        self.path_with_namespace = path_with_namespace


class GitRepoSchema(EntitySchema):
    id = fields.Number()
    description = ssh_url_to_repo = http_url_to_repo = web_url = name = name_with_namespace = path = path_with_namespace = fields.Str(
        missing=None)

    @post_load
    def make_git_repo(self, data, **kwargs):
        return GitRepo(**data)
