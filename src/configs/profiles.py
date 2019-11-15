#!/usr/bin/python3

CONFIG_ENV = 'development'


class BaseConfig:
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000
    WORK_HOME = '/tmp/devops'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    WORK_HOME = '/Users/wangnan/workspace/github/devops-py/devopstemp'


class ProductionConfig(BaseConfig):
    HOST = '127.0.0.1'
    PORT = 5555
    WORK_HOME = '/home/devops/workhome'


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

CURRENT_CONFIG_OBJECT = configs[CONFIG_ENV]
