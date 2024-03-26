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

from deel_python_sdk.type.currency_code import CurrencyCode
from deel_python_sdk.type.date_time_string import DateTimeString
from deel_python_sdk.type.payment_method import PaymentMethod
from deel_python_sdk.type.payment_status_enum import PaymentStatusEnum
from deel_python_sdk.type.payment_worker_list import PaymentWorkerList

class RequiredPayment(TypedDict):
    # Unique identifier of the payment.
    id: typing.Union[int, float]

    payment_method: PaymentMethod

    status: PaymentStatusEnum

    payment_currency: CurrencyCode

    label: str

    # Timestamp when payment was paid.
    paid_at: DateTimeString

    # Timestamp when the record was created.
    created_at: DateTimeString

    # Total paid.
    total: str

    workers: PaymentWorkerList

class OptionalPayment(TypedDict, total=False):
    pass

class Payment(RequiredPayment, OptionalPayment):
    pass