from core.actions._base import SingleAction, CreateAction, DetailAction, ListAction, PartialUpdateAction
from core.transformers.report import DailyReportTransformer, NearlySevenDaysEditTimeTransformer, WeeklyPlanTransformer
from core.types_ import Transformer


class DownloadDailyReportAction(SingleAction):
    path = '/download/{id}'
    method = 'GET'

    def init_handle(self):
        # self.handle = self.repository.download_daily_report
        self.handle = self.repository.download_daily_report


class DownloadDailyReportAllAction(SingleAction):
    path = '/download'
    method = 'GET'

    def init_handle(self):
        # self.handle = self.repository.download_daily_report
        self.handle = self.repository.download_daily_report_all


class AddDailyReport(CreateAction):
    Transformer = None

    def init_handle(self):
        self.handle = self.repository.add_daily_report


class GetDailyReportByTime(DetailAction):
    path = '/show'
    Transformer = DailyReportTransformer

    def init_handle(self):
        self.handle = self.repository.get_daily_report_by_time


class GetReportTimeInSevenDaysAction(ListAction):
    path = '/time/{id}'
    Transformer = NearlySevenDaysEditTimeTransformer

    def init_handle(self):
        self.handle = self.repository.get_nearly_seven_days_daily_report_edit_time


class AddOrUpdateWeeklyPlan(CreateAction):
    path = '/weekly'
    Transformer = WeeklyPlanTransformer

    def init_handle(self):
        self.handle = self.repository.add_or_update_weekly_plan


class GetWeeklyPlan(ListAction):
    path = '/weekly/{id}'
    Transformer = WeeklyPlanTransformer

    def init_handle(self):
        self.handle = self.repository.get_weekly_plan
