#!/bin/bash
export FLASK_APP=./src/main.py
# alternative options: ['development', 'production']
export FLASK_ENV=development
# alternative options: ['development', 'testing', 'production']
export PROFILE=development
flask app_run
