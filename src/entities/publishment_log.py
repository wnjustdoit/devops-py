#! /usr/bin/env python3

from .entity import Entity, EntitySchema, Base
from sqlalchemy import Column, Integer, String, Text, Sequence
from marshmallow import fields


class PublishmentLog(Base, Entity):
    __tablename__ = 'publishment_log'

    id = Column(Integer, Sequence('publishment_log_id_seq'), primary_key=True, comment='主键id')
    name = Column(String(256), nullable=False, comment='发布日志名称')
    publish_id = Column(Integer, nullable=False, comment='发布id')
    publish_type = Column(String(16), nullable=False, default='backend', comment='发布类型')
    content = Column(Text, nullable=False, comment='发布日志内容')
    publish_way = Column(String(16), nullable=False, default='browser', comment='发布方式')
    user_id = Column(Integer, nullable=True, comment='用户id')
    gitlab_user_id = Column(Integer, nullable=True, comment='gitlab用户id')
    gitlab_user_name = Column(String(32), nullable=True, comment='gitlab用户名')
    gitlab_user_email = Column(String(64), nullable=True, comment='gitlab用户邮箱')
    notify_email = Column(String(256), nullable=True, comment='通知邮箱')

    def __init__(self, name, publish_id, content, publish_type='backend', publish_way='browser', user_id=None,
                 gitlab_user_id=None, gitlab_user_name=None, gitlab_user_email=None, notify_email=None,
                 created_by=None):
        Entity.__init__(self, created_by)
        self.name = name
        self.publish_id = publish_id
        self.content = content
        self.publish_type = publish_type
        self.publish_way = publish_way
        self.user_id = user_id
        self.gitlab_user_id = gitlab_user_id
        self.gitlab_user_name = gitlab_user_name
        self.gitlab_user_email = gitlab_user_email
        self.notify_email = notify_email


class PublishmentLogSchema(EntitySchema):
    id = publish_id = user_id = gitlab_user_id = fields.Number()
    name = publish_type = content = publish_way = gitlab_user_name = gitlab_user_email = notify_email = fields.Str(
        missing=None)
