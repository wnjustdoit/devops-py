#!/usr/bin/python3

DEFAULT_CONFIG_ENV = 'development'


class BaseConfig:
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000
    WORK_HOME = '/tmp/devops'
    DATABASE_URI = 'postgresql+psycopg2://wangnan:postgres@localhost:5432/devops'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    WORK_HOME = '/Users/wangnan/workspace/github/devops-py/devopstemp'


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    HOST = '127.0.0.1'
    PORT = 5555
    WORK_HOME = '/home/devops/workhome'
    DATABASE_URI = 'postgresql+psycopg2://wangnan:postgres@192.168.1.248:5432/devops'


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
