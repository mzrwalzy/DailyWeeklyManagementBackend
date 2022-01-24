from core.transformers._base import OrmTransformer, BaseTransformer
import typing as tp


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
