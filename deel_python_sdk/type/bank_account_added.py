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

from deel_python_sdk.type.bank_account_status import BankAccountStatus
from deel_python_sdk.type.date_time_string import DateTimeString

class RequiredBankAccountAdded(TypedDict):
    pass

class OptionalBankAccountAdded(TypedDict, total=False):
    # ID of Bank Account.
    id: str

    status: BankAccountStatus

    created_at: DateTimeString

    updated_at: DateTimeString

class BankAccountAdded(RequiredBankAccountAdded, OptionalBankAccountAdded):
    pass
