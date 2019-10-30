#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://wangnan:postgres@localhost/devops', echo=True)
Session = sessionmaker(bind=engine)
