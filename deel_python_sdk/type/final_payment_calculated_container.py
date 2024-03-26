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

from deel_python_sdk.type.final_payment_calculated import FinalPaymentCalculated

class RequiredFinalPaymentCalculatedContainer(TypedDict):
    data: FinalPaymentCalculated

class OptionalFinalPaymentCalculatedContainer(TypedDict, total=False):
    pass

class FinalPaymentCalculatedContainer(RequiredFinalPaymentCalculatedContainer, OptionalFinalPaymentCalculatedContainer):
    pass
