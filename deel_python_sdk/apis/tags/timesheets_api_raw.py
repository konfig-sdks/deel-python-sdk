# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.timesheets_timesheet_id.delete import DeleteEntryRaw
from deel_python_sdk.paths.timesheets.get import GetListRaw
from deel_python_sdk.paths.timesheets_timesheet_id.get import GetSingleEntryRaw
from deel_python_sdk.paths.contracts_contract_id_timesheets.get import ListByContractRaw
from deel_python_sdk.paths.timesheets_many_reviews.post import ReviewMultipleRaw
from deel_python_sdk.paths.timesheets_timesheet_id_reviews.post import ReviewSingleTimesheetRaw
from deel_python_sdk.paths.timesheets.post import SubmitWorkForContractorRaw
from deel_python_sdk.paths.timesheets_timesheet_id.patch import UpdateEntryRaw


class TimesheetsApiRaw(
    DeleteEntryRaw,
    GetListRaw,
    GetSingleEntryRaw,
    ListByContractRaw,
    ReviewMultipleRaw,
    ReviewSingleTimesheetRaw,
    SubmitWorkForContractorRaw,
    UpdateEntryRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass