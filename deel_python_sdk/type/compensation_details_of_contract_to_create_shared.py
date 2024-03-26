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

from deel_python_sdk.type.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.type.date_string import DateString
from deel_python_sdk.type.notice_period import NoticePeriod
from deel_python_sdk.type.work_statement_cycle_end_type_enum import WorkStatementCycleEndTypeEnum
from deel_python_sdk.type.work_statement_cycle_scale_enum import WorkStatementCycleScaleEnum
from deel_python_sdk.type.work_statement_payment_due_type_enum import WorkStatementPaymentDueTypeEnum

class RequiredCompensationDetailsOfContractToCreateShared(TypedDict):
    currency_code: CurrencyCodeRequired

    frequency: WorkStatementCycleScaleEnum

    # Date invoice cycle ends.
    cycle_end: typing.Union[int, float]

    cycle_end_type: WorkStatementCycleEndTypeEnum

    payment_due_type: WorkStatementPaymentDueTypeEnum

    payment_due_days: typing.Union[int, float]

class OptionalCompensationDetailsOfContractToCreateShared(TypedDict, total=False):
    # Amount to be paid. This field can be excluded when creating a Pay-as-you-go task-based or Milestone contracts.
    amount: typing.Union[int, float]

    # If the payment due is on a weekend, pay on Friday.
    pay_before_weekends: bool

    first_payment_date: DateString

    # First payment amount.
    first_payment: typing.Union[int, float]

    notice_period: NoticePeriod

class CompensationDetailsOfContractToCreateShared(RequiredCompensationDetailsOfContractToCreateShared, OptionalCompensationDetailsOfContractToCreateShared):
    pass