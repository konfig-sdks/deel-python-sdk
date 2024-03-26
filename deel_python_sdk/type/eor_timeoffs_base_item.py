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

from deel_python_sdk.type.date_time_string import DateTimeString
from deel_python_sdk.type.date_time_string_nullable import DateTimeStringNullable
from deel_python_sdk.type.timeoffs_attachments_nullable import TimeoffsAttachmentsNullable
from deel_python_sdk.type.timeoffs_profile import TimeoffsProfile
from deel_python_sdk.type.timeoffs_profile_nullable import TimeoffsProfileNullable
from deel_python_sdk.type.timeoffs_status_enum import TimeoffsStatusEnum
from deel_python_sdk.type.timeoffs_type_enum import TimeoffsTypeEnum

class RequiredEorTimeoffsBaseItem(TypedDict):
    # The type of time off.
    type: TimeoffsTypeEnum

    # Timestamp when time off was requested.
    requested_at: DateTimeString

    # Status of the time off request.
    status: TimeoffsStatusEnum

class OptionalEorTimeoffsBaseItem(TypedDict, total=False):
    # Reason for requesting time off.
    reason: typing.Optional[str]

    # Timestamp when time off was reviewed.
    reviewed_at: DateTimeStringNullable

    # Reason why time off was denied.
    denial_reason: typing.Optional[str]

    # Indicates if multiple time off days are requested.
    has_multiple_dates: typing.Optional[bool]

    # Custom title for the time off. Only specify if type is \"OTHER\".
    other_timeoff_name: typing.Optional[str]

    # Employee who requested the time off.
    requester: typing.Optional[TimeoffsProfileNullable]

    # User who reviewed the time off.
    reviewer: TimeoffsProfile

    # Days used at the start year.
    days_used_start_year: str

    # Days used at the end year.
    days_used_end_year: str

    # Total number of time off days used.
    total_days_used: str

    # Indicates if the first day of time off is a half day.
    start_date_is_half_day: bool

    # Indicates if the last day of time off is a half day.
    end_date_is_half_day: bool

    single_date: DateTimeString

    # If true, only a single date was specified.
    date_is_half_day: typing.Optional[bool]

    attachments: typing.Optional[TimeoffsAttachmentsNullable]

class EorTimeoffsBaseItem(RequiredEorTimeoffsBaseItem, OptionalEorTimeoffsBaseItem):
    pass
