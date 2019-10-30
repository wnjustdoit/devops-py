#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime, or_, and_, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'devops'
db_user = 'wangnan'
db_password = 'postgres'
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{db_name}', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity:
    # 或需要指定Sequence
    # id = Column(Integer, primary_key=True)

    # created_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime)
    # created_by = Column(DateTime, nullable=False)
    # last_updated_by = Column(String(32))

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
