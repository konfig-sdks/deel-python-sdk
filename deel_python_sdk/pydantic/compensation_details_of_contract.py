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

from deel_python_sdk.pydantic.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.pydantic.date_time_string import DateTimeString

class CompensationDetailsOfContract(BaseModel):
    currency_code: CurrencyCodeRequired = Field(alias='currency_code')

    amount: str = Field(alias='amount')

    scale: str = Field(alias='scale')

    frequency: str = Field(alias='frequency')

    first_payment: str = Field(alias='first_payment')

    first_payment_date: DateTimeString = Field(alias='first_payment_date')

    gross_annual_salary: str = Field(alias='gross_annual_salary')

    gross_signing_bonus: str = Field(alias='gross_signing_bonus')

    gross_variable_bonus: str = Field(alias='gross_variable_bonus')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
