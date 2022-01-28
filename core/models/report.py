from sqlalchemy import Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.sql.sqltypes import JSON, DateTime

from core.models._base import BaseModel


class DailyPlan(BaseModel):
    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11), comment='用户id')
    daily_plan = Column(JSON, comment='[{"content": "", "condition": "", "cause": ""}]')
    advice = Column(String(255), comment='意见')
    tomorrow_plan = Column(String(255), comment='明天工作计划')
    create_time = Column(DateTime, comment='填写时间')


class Employee(BaseModel):
    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20), nullable=False, comment='姓名')
    position = Column(TINYINT(1), nullable=False, comment='职位')
    today_condition = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='当日日报完成情况')
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)


class WeeklyPlan(BaseModel):
    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11), nullable=False)
    title = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, nullable=False)
