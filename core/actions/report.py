from core.actions._base import SingleAction, CreateAction, DetailAction, ListAction
from core.transformers.report import DailyReportTransformer, NearlySevenDaysEditTimeTransformer
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
