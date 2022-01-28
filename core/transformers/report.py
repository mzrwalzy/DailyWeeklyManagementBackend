import typing as tp

from core.transformers._base import BaseTransformer


class Report(BaseTransformer):
    pass


class DailyPlanTransformer(BaseTransformer):
    content: str
    condition: str
    cause: str


class DailyReportTransformer(BaseTransformer):
    daily_plan: tp.List[DailyPlanTransformer] = None
    advice: str = None
    tomorrow_plan: str = None


class NearlySevenDaysEditTimeTransformer(BaseTransformer):
    day: str
    time: str


class WeeklyPlanTransformer(BaseTransformer):
    id: int
    user_id: int
    title: str
    start_time: str
    end_time: str
    create_time: str
