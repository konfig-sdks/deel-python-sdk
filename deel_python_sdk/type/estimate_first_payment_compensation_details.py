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
from deel_python_sdk.type.week_days_enum import WeekDaysEnum
from deel_python_sdk.type.work_statement_cycle_end_type_enum import WorkStatementCycleEndTypeEnum
from deel_python_sdk.type.work_statement_cycle_scale_enum import WorkStatementCycleScaleEnum
from deel_python_sdk.type.work_statement_payment_due_type_enum import WorkStatementPaymentDueTypeEnum

class RequiredEstimateFirstPaymentCompensationDetails(TypedDict):
    pass

class OptionalEstimateFirstPaymentCompensationDetails(TypedDict, total=False):
    # Amount to be paid. Must be a positive number.
    amount: typing.Union[int, float]

    currency_code: CurrencyCodeRequired

    scale: WorkStatementCycleScaleEnum

    # Date invoice cycle ends.
    cycle_end: typing.Union[int, float]

    cycle_end_type: WorkStatementCycleEndTypeEnum

    payment_due_type: WorkStatementPaymentDueTypeEnum

    payment_due_days: typing.Union[int, float]

    # Either works days or calendar days
    calculation_type: str

    work_week_start: WeekDaysEnum

    work_week_end: WeekDaysEnum

class EstimateFirstPaymentCompensationDetails(RequiredEstimateFirstPaymentCompensationDetails, OptionalEstimateFirstPaymentCompensationDetails):
    pass