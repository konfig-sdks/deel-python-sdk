# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.timesheets_timesheet_id.delete import DeleteEntry
from deel_python_sdk.paths.timesheets.get import GetList
from deel_python_sdk.paths.timesheets_timesheet_id.get import GetSingleEntry
from deel_python_sdk.paths.contracts_contract_id_timesheets.get import ListByContract
from deel_python_sdk.paths.timesheets_many_reviews.post import ReviewMultiple
from deel_python_sdk.paths.timesheets_timesheet_id_reviews.post import ReviewSingleTimesheet
from deel_python_sdk.paths.timesheets.post import SubmitWorkForContractor
from deel_python_sdk.paths.timesheets_timesheet_id.patch import UpdateEntry
from deel_python_sdk.apis.tags.timesheets_api_raw import TimesheetsApiRaw


class TimesheetsApi(
    DeleteEntry,
    GetList,
    GetSingleEntry,
    ListByContract,
    ReviewMultiple,
    ReviewSingleTimesheet,
    SubmitWorkForContractor,
    UpdateEntry,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TimesheetsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TimesheetsApiRaw(api_client)
