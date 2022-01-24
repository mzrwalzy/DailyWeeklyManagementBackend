# -*- coding:utf-8 -*-
# @Time     : 2022/1/24 14:54
# @Author   : Charon.
from core.models.report import Employee
from core.services import get_db


def change_daily_condition_at_time():
    db_client = get_db()
    db = next(db_client)
    db.query(Employee).update({'today_condition': 0})
    db.flush()
    return
