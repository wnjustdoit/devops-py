## 发布系统后台（Python Web & Python Script）

---
#### 技术选型
> - web框架：Flask
> - orm框架：SQLAlchemy
> - 序列化框架：marshmallow、Flask.json
> - 其他：websocket
> - 数据库：PostgreSQL

---
#### Python环境
###### 安装虚拟环境
```
virtualenv -p /usr/bin/python3 py3flask
# 或者 python3 -m pip install virtualenvwrapper
pip3 install flask
```

###### 将本地依赖写入文件
```
pip3 freeze > requirements.txt
```

###### 从文件安装依赖
```
pip3 install -r requirements.txt
```

---
#### 数据库备份与版本管理
###### 数据库备份与恢复
* 定期备份
```
./database/db_backup.sh
```
* 从备份中的sql脚本恢复
```
./database/db_rebuild.sh
```

###### 数据库版本管理
* 自动生成升级脚本
```
alembic revision --autogenerate -m "your comment"
```
* 执行升级命令
```
alembic upgrade head
```
* 如需降级等其他操作，请查阅官网文档

###### 自动代码生成工具
* 功能：从数据库自动生成model代码
* 执行脚本：
```
./database/db_2_model.sh
```
* 注意要点：
    > - 数据库表关系不加约束；
    > - 主键如果需要sequence，那么设置各自的sequence；
    > - 字段顺序可能需要手动调整（当继承时）

---
#### TODOs
* 支持nodejs的发布；
* 支持gitlab hook发布（可过滤分支、提交关键词、用户等）；
* 支持发送邮件/钉钉通知发布日志；
* 支持查看最近发布记录和日志；
* 支持用户管理、登录注册等；
* redis的接入（缓存与消息队列）；
* websocket多线程优化；
* flask web框架持续优化；
* 发布系统架构图；
* ...

---
#### 参考资料
* [Python](https://www.python.org/)
* [Python Package Index](https://pypi.org/)
* [PostgreSQL](https://www.postgresql.org/)
