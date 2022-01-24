from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT

from core.models._base import BaseModel
from core.models.report import Employee, DailyPlan

UserEmployee = Employee
UserDailyPlan = DailyPlan


class Position(BaseModel):
    id = Column(INTEGER(11), primary_key=True)
    position = Column(String(255), nullable=False)


class Condition(BaseModel):
    id = Column(TINYINT(1), primary_key=True)
    condition = Column(String(255), nullable=False)
