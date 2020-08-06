#!/bin/bash
# 如果是IDE启动加入环境变量：PYTHONUNBUFFERED=1;FLASK_ENV=development;FLASK_APP=./src/main.py;IDE=true
ENV_PARAM=$1
if [ "$1" == "" ] || [ "$1" == "development" ] || [ "$1" == "dev" ]; then
  ENV_PARAM=development
elif [ "$1" == "production" ] || [ "$1" == "prod" ]; then
  ENV_PARAM=production
else
  ENV_PARAM=development
fi

export FLASK_APP=./src/main.py
# alternative options: ['development', 'production']
export FLASK_ENV=$ENV_PARAM
# alternative options: ['development', 'testing', 'production']
export PROFILE=$ENV_PARAM
flask app_run
