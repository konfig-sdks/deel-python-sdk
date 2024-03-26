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

from deel_python_sdk.type.bank_account_value_allowed import BankAccountValueAllowed
from deel_python_sdk.type.validation_type import ValidationType

class RequiredBankAccountGuide(TypedDict):
    # The key of the field.
    key: str

    # Whether the field is required or not.
    required: bool

class OptionalBankAccountGuide(TypedDict, total=False):
    # Label for this field.
    label: str

    values_allowed: typing.List[BankAccountValueAllowed]

    validations: typing.List[ValidationType]

    # Type of the field
    type: str

class BankAccountGuide(RequiredBankAccountGuide, OptionalBankAccountGuide):
    pass
