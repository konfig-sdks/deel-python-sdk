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

from deel_python_sdk.type.eor_holidays_rollover_type import EorHolidaysRolloverType

class RequiredEorEntitlementListItem(TypedDict):
    pass

class OptionalEorEntitlementListItem(TypedDict, total=False):
    year: typing.Union[int, float]

    # Minimum vacation allowed.
    vacation_allowed: str

    # Maximum sick leave allowed.
    sick_leave_allowed: str

    # Vacation days requested by the employee.
    vacation_requested: str

    # Vacation days approved.
    vacation_approved: str

    # Vacation days used by the employee.
    vacation_used: str

    # Total number of vacation days requested, approved and used.
    vacation_total: str

    # Sick days requested by the employee.
    sick_leave_requested: str

    # Sick days approved.
    sick_leave_approved: str

    # Sick days used by the employee.
    sick_leave_used: str

    # Total number of sick days requested, approved and used.
    sick_leave_total: str

    # Other type of time off requested by the employee.
    other_leave_requested: str

    # Other type of time off days approved.
    other_leave_approved: str

    # Other type of time off days used by the employee.
    other_leave_used: str

    # Total number of other type of time off days requested, approved and used.
    other_leave_total: str

    rollover_type: EorHolidaysRolloverType

    max_rollover_yearly: str

class EorEntitlementListItem(RequiredEorEntitlementListItem, OptionalEorEntitlementListItem):
    pass
