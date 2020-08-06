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
* 发布系统支持不同的git平台（gitlab V3 V4、gitee、github 等）；
    > 发布系统work_home拓展支持，形如：[base_path\]/[git_platform\]/[namespace or group\]/[project_name\]
    > 随之而变的是，发布冲突的锁和队列机制，联合唯一性决定因素：git_platform_id + git_repo_id + to_ip[ + to_project_home\]
* 支持docker容器化项目的发布；
* 本地代码质量
    * http 接口、参数等的重设计；（restful）
    * 发送邮件的优化；（间歇性 bug：need connect() first）
    * 异常设计、开发debug、日志框架、权限框架；
    * 发布系统架构图、项目结构、单元测试、代码质量、性能、安全等的补充和优化；
* 高级特性
    * 可随时终止正在进行中的发布；
    * 根据历史发布数据，做出更准确的发布进度预估（百分比）；
    * 优雅停机/微服务的优雅上下线的支持；
    * 支持发布冲突时（同一 git 仓库），选择是否排队等待发布，并可随时取消发布；
    * 支持多项目排队发布，并可随时取消排队中的任务或调整排队顺序；
    * 支持对发布到的目标服务器分组，串行、并行发布；（灰度发布）
    * 支持定时发布（可结合定时调度平台，开放发布接口即可）；
    * 集成代码质量检查、单元测试等模块或插件；（CI/CD）
    * 持续拓展与优化发布系统生命周期，比如：动态构建命令、发布阶段调整顺序等（提高可扩展性）；
* 自身的高可用
    * 分布式的发布系统（主要解决单点、性能问题）；
    * 发布系统docker化；
    * 热升级/热更新
* 前端（用户体验）
    * 页面体验持续优化（CSS、异常反馈、结果状态通知）
* 远程服务端
    * 优化远程服务端获取/杀死进程的方式（pid file）；
    * scp 改为 rsync，支持断点续传；
* 快速运维
    * web ssh 功能的支持（在页面上输入常用的 shell 命令）；
* 配置集中管理
    * 远程服务端脚本一键分发（前端、后端、远程服务端集成一体式工程，配置同步）；
* 权限设置与用户体验
    * 分组与分类：用户组、项目组、服务器组等；
* 发布单
    * 发布审批流程；（工作流）
    * 发布单与发布脚本；（自动化，真正的一键发布）
        * 手动触发一键发布发布或定时全自动化发布；
        * 支持灰度发布配置；
        * 支持多种事件的嵌入（如数据库备份、sql执行、日志清理等）
* ...

---
#### 参考资料
* [Python](https://www.python.org/)
* [Python Package Index](https://pypi.org/)
* [PostgreSQL](https://www.postgresql.org/)
