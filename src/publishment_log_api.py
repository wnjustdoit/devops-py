#!/usr/bin/python3

from flask import Blueprint, request, jsonify, make_response
from sqlalchemy import or_
import demjson
from datetime import timedelta, datetime

from .entities.publishment_log import PublishmentLog, PublishmentLogSchema
from .entities.entity import Session

publishment_log_api = Blueprint('publishment_log_api', __name__)
app = publishment_log_api


# 查询发布日志列表
@app.route("/publishmentLog/list")
def publishment_list():
    publish_log_str = request.args.get('publishLog')
    current_page = request.args.get('current_page')
    page_size = int(request.args.get('page_size'))

    session = Session()
    try:
        base_statement = session.query(PublishmentLog).select_from(PublishmentLog)
        if publish_log_str is not None and publish_log_str != '':
            publish_log = demjson.decode(publish_log_str)
            name = publish_log.get('name')
            content = publish_log.get('content')
            publish_id = publish_log.get('publish_id')
            publish_type = publish_log.get('publish_type')
            publish_way = publish_log.get('publish_way')
            user_id = publish_log.get('user_id')
            if name is not None:
                base_statement = base_statement.filter(PublishmentLog.name.like('%' + name + '%'))
            if content is not None:
                base_statement = base_statement.filter(PublishmentLog.content.like('%' + content + '%'))
            if publish_id is not None and publish_id != '':
                base_statement = base_statement.filter(PublishmentLog.publish_id == int(publish_id))
            if user_id is not None and user_id != '':
                base_statement = base_statement.filter(PublishmentLog.user_id == int(user_id))
            if publish_type is not None:
                base_statement = base_statement.filter(PublishmentLog.publish_type == publish_type)
            if publish_way is not None:
                base_statement = base_statement.filter(PublishmentLog.publish_way == publish_way)
        base_statement = base_statement.order_by(PublishmentLog.created_at.desc())
        publishment_objects = base_statement.limit(page_size).offset(
            (int(current_page) - 1) * page_size).all()
        if len(publishment_objects) != 0:
            publishment_counts = base_statement.count()
        else:
            publishment_counts = 0
    finally:
        session.close()

    result_list = PublishmentLogSchema(many=True).dump(publishment_objects)
    result = {'data': result_list, 'total': publishment_counts}

    return jsonify(result)


# 获取发布日志详情
@app.route("/publishmentLog/<int:id>")
def publishment_detail(id):
    session = Session()
    try:
        result_object = session.query(PublishmentLog).filter(PublishmentLog.id == id).one_or_none()
    finally:
        session.close()

    result = PublishmentLogSchema().dump(result_object)

    return jsonify(result)


def add_publishment_log(publishment_log):
    publishment_log.created_by = "Method invocation"

    session = Session()
    try:
        session.add(publishment_log)
        session.commit()
        session.refresh(publishment_log)
        session.expunge(publishment_log)
    finally:
        session.close()


def clear_publishment_log():
    delta = timedelta(days=-30)
    thirty_days_ago = datetime.now() + delta

    session = Session()
    try:
        session.query(PublishmentLog).filter(PublishmentLog.created_at <= thirty_days_ago).delete()
        session.commit()
    finally:
        session.close()


def get_parameter(key):
    if request.get_json() is not None:
        return request.get_json().get(key)
    return None
