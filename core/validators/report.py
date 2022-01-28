import typing as tp
from core.validators._base import BaseValidator


class DailyPlanValidator(BaseValidator):
    content: str
    condition: str
    cause: str


class ReportValidator(BaseValidator):
    user_id: int
    daily_plan: tp.List[DailyPlanValidator]
    advice: str
    tomorrow_plan: str


class WeeklyPlanValidator(BaseValidator):
    id: int = None
    user_id: int
    title: str
    start_time: str
    end_time: str
    update: bool = False
