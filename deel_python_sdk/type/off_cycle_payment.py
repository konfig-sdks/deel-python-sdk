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
from deel_python_sdk.type.invoice_adjustment_status_enum import InvoiceAdjustmentStatusEnum
from deel_python_sdk.type.off_cycle_payment_reported_by import OffCyclePaymentReportedBy

class RequiredOffCyclePayment(TypedDict):
    # Description of the off-cycle payment entry.
    description: str

    # Unique identifier of this resource.
    id: str

    status: typing.Optional[InvoiceAdjustmentStatusEnum]

    # Long date-time format following ISO-8601
    date_submitted: datetime

    currency_code: CurrencyCodeRequired

    # Amount of off-cycle payment.
    amount: str

    # Long date-time format following ISO-8601
    created_at: datetime

    reported_by: OffCyclePaymentReportedBy

class OptionalOffCyclePayment(TypedDict, total=False):
    pass

class OffCyclePayment(RequiredOffCyclePayment, OptionalOffCyclePayment):
    pass
