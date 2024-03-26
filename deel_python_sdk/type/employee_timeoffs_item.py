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

from deel_python_sdk.type.employee_timeoffs_item_attachments import EmployeeTimeoffsItemAttachments
from deel_python_sdk.type.employee_timeoffs_item_requester import EmployeeTimeoffsItemRequester
from deel_python_sdk.type.employee_timeoffs_item_reviewer import EmployeeTimeoffsItemReviewer

class RequiredEmployeeTimeoffsItem(TypedDict):
    # Unique identifier of this resource.
    time_off_id: str

    reason: str

    # Time off type.
    type: str

    requested_at: str

    reviewed_at: str

    with_multiple_dates: bool

    created_at: str

    updated_at: str

    denial_reason: typing.Optional[str]

    requester: EmployeeTimeoffsItemRequester

    reviewer: EmployeeTimeoffsItemReviewer

    days_used_start_year: str

    days_used_end_year: str

    days_used: str

    start_date: str

    end_date: str

    is_start_date_half_day: bool

    is_end_date_half_day: bool

    attachments: EmployeeTimeoffsItemAttachments

    change_request: typing.Optional[str]

class OptionalEmployeeTimeoffsItem(TypedDict, total=False):
    pass

class EmployeeTimeoffsItem(RequiredEmployeeTimeoffsItem, OptionalEmployeeTimeoffsItem):
    pass
