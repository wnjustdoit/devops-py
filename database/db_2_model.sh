#!/bin/bash

here=$(cd $(dirname $0); pwd -P)
sqlacodegen postgresql+psycopg2://wangnan:postgres@localhost:5432/devops --outfile "${here}/model.py"
