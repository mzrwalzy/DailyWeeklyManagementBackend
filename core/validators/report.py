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
