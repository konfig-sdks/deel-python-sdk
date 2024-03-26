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


class RequiredPeoplePayment(TypedDict):
    pass

class OptionalPeoplePayment(TypedDict, total=False):
    # The payment rate
    rate: typing.Union[int, float]

    # The payment scale (e.g., hourly, weekly, monthly, etc.)
    scale: str

    # The currency code (ISO 4217) for the payment
    currency: str

    # The name of the contract associated with the payment
    contract_name: str

class PeoplePayment(RequiredPeoplePayment, OptionalPeoplePayment):
    pass
