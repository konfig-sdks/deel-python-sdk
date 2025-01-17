# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from deel_python_sdk.type.basic_timesheet_contract import BasicTimesheetContract
from deel_python_sdk.type.basic_timesheet_payment_cycle import BasicTimesheetPaymentCycle
from deel_python_sdk.type.basic_timesheet_reported_by import BasicTimesheetReportedBy
from deel_python_sdk.type.basic_timesheet_reviewed_by import BasicTimesheetReviewedBy
from deel_python_sdk.type.basic_timesheet_worksheet import BasicTimesheetWorksheet
from deel_python_sdk.type.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.type.file_attachment_info import FileAttachmentInfo
from deel_python_sdk.type.timesheet_status_enum import TimesheetStatusEnum

class RequiredBasicTimesheet(TypedDict):
    description: str

    # Unique identifier of this resource.
    id: str

    # Deprecated - it is always \"work\"
    type: str

    status: typing.Optional[TimesheetStatusEnum]

    # Long date-time format following ISO-8601
    date_submitted: datetime

    currency_code: CurrencyCodeRequired

    # is equal to quantity times rate of active work statement + bonus in this record
    total_amount: str

    quantity: typing.Optional[typing.Union[int, float]]

    created_at: str

    attachment: typing.Optional[FileAttachmentInfo]

    worksheet: typing.Optional[BasicTimesheetWorksheet]

    reviewed_by: typing.Optional[BasicTimesheetReviewedBy]

    contract: BasicTimesheetContract

    reported_by: BasicTimesheetReportedBy

class OptionalBasicTimesheet(TypedDict, total=False):
    scale: typing.Optional[str]

    custom_scale: typing.Optional[str]

    payment_cycle: BasicTimesheetPaymentCycle

class BasicTimesheet(RequiredBasicTimesheet, OptionalBasicTimesheet):
    pass
