#!/usr/bin/python3

from flask import Blueprint, request, jsonify, make_response
from sqlalchemy import or_

from .entities.publishment_log import PublishmentLog, PublishmentLogSchema
from .entities.entity import Session

publishment_log_api = Blueprint('publishment_log_api', __name__)
app = publishment_log_api


# 查询发布日志列表
@app.route("/publishmentLog/list")
def publishment_list():
    page_size = 10
    keyword = request.args.get('keyword')
    current_page = request.args.get('current_page')

    session = Session()
    try:
        base_statement = session.query(PublishmentLog).select_from(PublishmentLog)
        if keyword:
            base_statement = base_statement.filter(or_(PublishmentLog.name.like('%' + keyword + '%'),
                                                       PublishmentLog.publish_id.like('%' + keyword + '%'),
                                                       PublishmentLog.publish_type.like('%' + keyword + '%')
                                                       ))
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
