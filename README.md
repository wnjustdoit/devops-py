## 发布系统后台（Python Web & Python Script）

#### 功能特性
* 支持发布的项目类型：
    * Java 项目的发布（支持 jar、war 格式）；
    * 静态资源的发布（文件、文件夹内容同步）；
    * 前端 vue 的发布；
    * nodejs 的发布
* 支持发布日志查看：
    * 页面近实时日志输出；
    * 发布日志写入数据库存储，随时在控制台查看历史日志（默认存储近 30 天）；
    * 日志内容作为正文图片、附件和链接形式发送至邮件、钉钉等消息通知
* 支持高效的发布：
    * 一键发布（发布按钮、浏览器地址键入/页面刷新/收藏夹等）；
    * 自动发布/无感知发布，通过 gitlab web-hook 触发发布（可根据分支、commit comment 内容等过滤[默认过滤词：devops\]）；
* 其他：
    * 支持用户及其权限管理、分组及告警管理；
    * 支持 gitlab 项目列表查看（同步到本地数据库，提高效率）、实时获取项目分支/标签/commit id；
    * 支持 gitlab web hooks 的管理（添加和删除）

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
    > - 索引等约束可能需要手动处理；
    > - 字段顺序可能需要手动调整（当继承时）

---
#### TODOs
以下不分优先级。
* 持续拓展与优化发布系统生命周期，比如：动态构建命令、发布阶段调整顺序等（提高可扩展性）；
* 集成代码质量检查、单元测试等模块或插件；（CI/CD）
* 支持发布冲突时，选择是否排队等待发布，并可随时取消发布（消息队列）；
* 支持定时发布（可结合定时调度平台，开放发布接口即可，非必须）；
* 发布系统架构图、项目结构、单元测试、代码质量、性能、安全等的补充和优化；
* 发布系统支持不同的git平台（自建 gitlab、gitee、github 等）；
    > 发布系统work_home拓展支持，形如：[base_path\]/[git_platform\]/[namespace or group\]/[project_name\]
    > 随之而变的是，发布冲突的锁和队列机制，联合唯一性决定因素：git_platform_id + git_repo_id + to_ip[ + to_project_home\]
* 可随时终止正在进行中的发布；
* 异常设计、开发debug、日志框架、权限框架；
* 支持docker容器化项目的发布；
* 支持对发布到的目标服务器分组，串行、并行发布；
* 发送邮件的优化；（间歇性 bug：need connect() first）
* websocket 的优化；（间歇性 bug：没有 connect，页面无反应）
* http 接口、参数等的重设计；（restful）
* scp 改为 rsync，支持断点续传；
* 分布式的发布系统（主要解决单点、性能问题）；
* 页面体验持续优化（CSS、异常反馈、结果状态通知）；
* 优化远程服务端获取/杀死进程的方式；
* 优化近实时输出日志的方式（tail）；
* web shell 功能的支持（在页面上输入常用的 shell 命令）；
* 远程服务端脚本一键分发（前端、后端、远程服务端集成一体式工程）；
* 热升级/热更新；
* ...

---
#### 参考资料
* [Python](https://www.python.org/)
* [Python Package Index](https://pypi.org/)
* [PostgreSQL](https://www.postgresql.org/)
