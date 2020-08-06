#!/bin/bash

zip -r -b ~/workspace/github/devops-py/ ~/workspace/github/devops-py/src.zip src
cd ~/workspace/github/devops-fe/ && sh build.sh
zip -r -b ~/workspace/github/devops-fe/ ~/workspace/github/devops-fe/dist.zip dist

scp -r ~/workspace/github/devops-py/src.zip root@192.168.1.248:/home/devops/devops-py
scp -r ~/workspace/github/devops-fe/dist.zip root@192.168.1.248:/home/devops/devops-fe

ssh root@192.168.1.248 <<EOF
  unzip -o /home/devops/devops-py/src.zip -d /home/devops/devops-py/
  unzip -o /home/devops/devops-fe/dist.zip -d /home/devops/devops-fe/
  netstat -tunlp | grep -w 5000 | awk '{print \$7}' | cut -d/ -f1 | xargs -r kill -9
  rsync -av --exclude=/home/devops/devops-fe/dist/index.html /home/devops/devops-fe/dist/* /home/devops/devops-py/src/static/
  rsync -av /home/devops/devops-fe/dist/index.html /home/devops/devops-py/src/templates/index.html
  cd /home/devops/devops-py/ && sh prod_auto_startup.sh
  exit
EOF
