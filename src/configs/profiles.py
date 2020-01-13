#!/usr/bin/python3

DEFAULT_CONFIG_ENV = 'development'


class BaseConfig:
    DEBUG = False
    TESTING = False
    SCHEMA = 'http'
    HOST = '0.0.0.0'
    PORT = 5000
    VIEW_PORT = PORT
    WORK_HOME = '/tmp/devops'
    DATABASE_URI = 'postgresql+psycopg2://wangnan:postgres@localhost:5432/devops'
    GITLAB_WEB_HOOK_CONFIG = {'url': 'http://192.168.1.248:5000/web_hook/publish', 'push_events': True,
                             'tag_push_events': True, 'note_events': True}


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # HOST = "localhost"
    VIEW_PORT = 9999
    WORK_HOME = '/Users/wangnan/workspace/github/devops-py/devopstemp'


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    HOST = '192.168.1.248'
    WORK_HOME = '/home/devops/workhome'
    DATABASE_URI = 'postgresql+psycopg2://wangnan:postgres@192.168.1.248:5432/devops'


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
