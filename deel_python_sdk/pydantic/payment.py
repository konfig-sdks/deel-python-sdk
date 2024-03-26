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

from deel_python_sdk.pydantic.currency_code import CurrencyCode
from deel_python_sdk.pydantic.date_time_string import DateTimeString
from deel_python_sdk.pydantic.payment_method import PaymentMethod
from deel_python_sdk.pydantic.payment_status_enum import PaymentStatusEnum
from deel_python_sdk.pydantic.payment_worker_list import PaymentWorkerList

class Payment(BaseModel):
    # Unique identifier of the payment.
    id: typing.Union[int, float] = Field(alias='id')

    payment_method: PaymentMethod = Field(alias='payment_method')

    status: PaymentStatusEnum = Field(alias='status')

    payment_currency: CurrencyCode = Field(alias='payment_currency')

    label: str = Field(alias='label')

    # Timestamp when payment was paid.
    paid_at: DateTimeString = Field(alias='paid_at')

    # Timestamp when the record was created.
    created_at: DateTimeString = Field(alias='created_at')

    # Total paid.
    total: str = Field(alias='total')

    workers: PaymentWorkerList = Field(alias='workers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
