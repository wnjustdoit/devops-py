## 发布系统后台（Python Web & Python Script）

---
#### 技术选型
- web框架：Flask
- orm框架：SQLAlchemy
- 序列化框架：marshmallow、Flask.json
- 数据库：PostgreSQL

---
#### 数据库版本控制
alembic revision --autogenerate -m "your comment"
alembic upgrade head
    
    注意要点：
    1、数据库表关系不加约束；
    2、字段顺序可能需要手动调整（当继承时）

---
#### 参考资料
* [Python](https://www.python.org/)
* [Python Package Index](https://pypi.org/)
* [PostgreSQL](https://www.postgresql.org/)

