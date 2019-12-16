#!/usr/bin/env python3

from .entity import Entity, EntitySchema, Base
from sqlalchemy import Column, Integer, String, Sequence
from marshmallow import Schema, fields, post_load


class User(Entity, Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, comment='用户id')
    login_code = Column(String(32), nullable=False, comment='登录名')
    login_pwd = Column(String(32), nullable=False, comment='密码')
    nick_name = Column(String(32), nullable=False, comment='昵称')
    email = Column(String(64), nullable=False, comment='邮箱（告警用）')
    gitlab_email = Column(String(64), nullable=False, comment='gitlab邮箱')
    role = Column(String(16), nullable=False, comment='角色')

    def __init__(self, login_code, login_pwd, nick_name, email, gitlab_email, role, created_by=None):
        Entity.__init__(self, created_by)
        self.login_code = login_code
        self.login_pwd = login_pwd
        self.nick_name = nick_name
        self.email = email
        self.gitlab_email = gitlab_email
        self.role = role


class UserSchema(EntitySchema):
    id = fields.Number()
    login_code = login_pwd = nick_name = email = gitlab_email = role = fields.Str(missing=None)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
