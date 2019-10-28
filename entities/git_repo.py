#!/usr/bin/env python3

from .entity import Entity, Base
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields, post_load


class GitRepo(Entity, Base):
    __tablename__ = 'git_repo'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    ssh_url_to_repo = Column(String)
    http_url_to_repo = Column(String)
    web_url = Column(String)
    name = Column(String)
    name_with_namespace = Column(String)
    path = Column(String)
    path_with_namespace = Column(String)

    def __init__(self, description, ssh_url_to_repo, http_url_to_repo, web_url, name, name_with_namespace, path,
                 path_with_namespace, id = None, created_by=None):
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

    # TODO
    # def __repr__(self):
    #     print(GitRepoSchema.dump(self))
    #     return "<GitRepo(id={self.id})>".format(self=self)


class GitRepoSchema(Schema):
    id = fields.Number()
    description = ssh_url_to_repo = http_url_to_repo = web_url = name = name_with_namespace = path = path_with_namespace = fields.Str()

    @post_load
    def make_git_repo(self, data, **kwargs):
        return GitRepo(**data)
