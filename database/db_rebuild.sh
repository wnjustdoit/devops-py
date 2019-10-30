#!/bin/bash

# shellcheck disable=SC2162
read -p "确认要删除数据库？该操作不可恢复（1：删除；2：撤销）：" opt
if [ "${opt}" == 1 ]; then
  dropdb -h localhost -p 5432 -U wangnan devops
  read -p "请输入文件名（含后缀）：" filename
  createdb -h localhost -p 5432 -U wangnan -O wangnan -w devops
  psql -h localhost -p 5432 -U wangnan -w -d devops -f "$(pwd)"/"${filename}"
else
  echo "已撤销删库。"
fi
