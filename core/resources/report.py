
from core.actions.report import DownloadDailyReportAction, DownloadDailyReportAllAction, AddDailyReport, \
    GetDailyReportByTime
# from core.models.report import Report as Model
from core.repositories._base import CRUDRepository
from core.repositories.report import ReportRepository
from core.resources._base import BaseResource
from core.transformers.report import Report as Transformer


class ReportResource(BaseResource):
    name = 'report'
    name_doc = ''
    path = '/reports'

    Actions = [DownloadDailyReportAction, DownloadDailyReportAllAction, AddDailyReport, GetDailyReportByTime]

    repository = ReportRepository()
    Transformer = Transformer

    # create_Validator = Validator1
    # partial_update_Validator = Validator2


resource = ReportResource().register_resource()
