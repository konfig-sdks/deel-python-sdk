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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from deel_python_sdk.pydantic.eor_holidays_rollover_type import EorHolidaysRolloverType

class EorEntitlementListItem(BaseModel):
    year: typing.Optional[typing.Union[int, float]] = Field(None, alias='year')

    # Minimum vacation allowed.
    vacation_allowed: typing.Optional[str] = Field(None, alias='vacation_allowed')

    # Maximum sick leave allowed.
    sick_leave_allowed: typing.Optional[str] = Field(None, alias='sick_leave_allowed')

    # Vacation days requested by the employee.
    vacation_requested: typing.Optional[str] = Field(None, alias='vacation_requested')

    # Vacation days approved.
    vacation_approved: typing.Optional[str] = Field(None, alias='vacation_approved')

    # Vacation days used by the employee.
    vacation_used: typing.Optional[str] = Field(None, alias='vacation_used')

    # Total number of vacation days requested, approved and used.
    vacation_total: typing.Optional[str] = Field(None, alias='vacation_total')

    # Sick days requested by the employee.
    sick_leave_requested: typing.Optional[str] = Field(None, alias='sick_leave_requested')

    # Sick days approved.
    sick_leave_approved: typing.Optional[str] = Field(None, alias='sick_leave_approved')

    # Sick days used by the employee.
    sick_leave_used: typing.Optional[str] = Field(None, alias='sick_leave_used')

    # Total number of sick days requested, approved and used.
    sick_leave_total: typing.Optional[str] = Field(None, alias='sick_leave_total')

    # Other type of time off requested by the employee.
    other_leave_requested: typing.Optional[str] = Field(None, alias='other_leave_requested')

    # Other type of time off days approved.
    other_leave_approved: typing.Optional[str] = Field(None, alias='other_leave_approved')

    # Other type of time off days used by the employee.
    other_leave_used: typing.Optional[str] = Field(None, alias='other_leave_used')

    # Total number of other type of time off days requested, approved and used.
    other_leave_total: typing.Optional[str] = Field(None, alias='other_leave_total')

    rollover_type: typing.Optional[EorHolidaysRolloverType] = Field(None, alias='rollover_type')

    max_rollover_yearly: typing.Optional[str] = Field(None, alias='max_rollover_yearly')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
