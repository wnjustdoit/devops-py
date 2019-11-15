#!/bin/bash
export FLASK_APP=./src/main.py
export FLASK_ENV=development
export FLASK_DEBUG=1
#flask run --host=0.0.0.0 --port=5000
flask app_run
