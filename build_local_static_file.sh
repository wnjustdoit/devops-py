#!/bin/bash

cd ../devops-fe && npm run buildx
cp -rf dist/* ../devops-py/src/static/
cp -rf ../devops-py/src/static/index.html ../devops-py/src/templates/
rm -rf ../devops-py/src/static/index.html