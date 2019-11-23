#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime, or_, and_, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields, post_load
import os, sys

sys.path.append(os.path.realpath('.'))
from src.configs.profiles import configs


def get_profile_obj():
    return configs[os.environ.get('PROFILE', default='development')]


engine = create_engine(get_profile_obj().DATABASE_URI, echo=get_profile_obj().DEBUG)

Session = sessionmaker(bind=engine)

Base = declarative_base()


# 自动生成数据库表时，需要手动调整列名顺序
class Entity:
    # 或需要指定Sequence
    # id = Column(Integer, primary_key=True, comment='主键ID')

    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by = Column(String(32), nullable=False, comment='创建人')
    last_updated_at = Column(DateTime, nullable=False, comment='最后更新时间')
    last_updated_by = Column(String(32), nullable=False, comment='最后更新人')
    is_deleted = Column(Integer, nullable=False, default=0, comment='是否删除：0表示正常，1表示已删除')

    def __init__(self, created_by='system-auto'):
        self.created_at = datetime.now()
        self.created_by = created_by
        self.last_updated_at = self.created_at
        self.last_updated_by = self.created_by
        self.is_deleted = 0

    def init(self):
        self.__init__()


class EntitySchema(Schema):
    created_at = last_updated_at = fields.DateTime()
    created_by = last_updated_by = fields.Str()
