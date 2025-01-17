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

from deel_python_sdk.pydantic.country_code import CountryCode

class EmploymentDetailsOfContract(BaseModel):
    type: str = Field(alias='type')

    days_per_week: typing.Union[int, float] = Field(alias='days_per_week')

    hours_per_day: typing.Union[int, float] = Field(alias='hours_per_day')

    probation_period: typing.Optional[typing.Union[int, float]] = Field(alias='probation_period')

    paid_vacation_days: typing.Union[int, float] = Field(alias='paid_vacation_days')

    country: typing.Optional[CountryCode] = Field(None, alias='country')

    # State code.
    state: typing.Optional[typing.Optional[str]] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
