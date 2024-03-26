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


class PaymentBreakDown(BaseModel):
    date: typing.Optional[str] = Field(None, alias='date')

    general_ledger_account: typing.Optional[str] = Field(None, alias='general_ledger_account')

    team: typing.Optional[str] = Field(None, alias='team')

    # Worker's unique identifier.
    contractor_unique_identifier: typing.Optional[str] = Field(None, alias='contractor_unique_identifier')

    # Worker's name.
    contractor_employee_name: typing.Optional[str] = Field(None, alias='contractor_employee_name')

    # Worker's email.
    contractor_email: typing.Optional[str] = Field(None, alias='contractor_email')

    # Invoice number.
    invoice_number: typing.Optional[str] = Field(None, alias='invoice_number')

    # Currency code.
    currency: typing.Optional[str] = Field(None, alias='currency')

    payment_currency: typing.Optional[str] = Field(None, alias='payment_currency')

    receipt_number: typing.Optional[str] = Field(None, alias='receipt_number')

    work: typing.Optional[str] = Field(None, alias='work')

    bonus: typing.Optional[str] = Field(None, alias='bonus')

    expenses: typing.Optional[str] = Field(None, alias='expenses')

    commissions: typing.Optional[str] = Field(None, alias='commissions')

    deductions: typing.Optional[str] = Field(None, alias='deductions')

    overtime: typing.Optional[str] = Field(None, alias='overtime')

    pro_rata: typing.Optional[str] = Field(None, alias='pro_rata')

    others: typing.Optional[str] = Field(None, alias='others')

    processing_fee: typing.Optional[str] = Field(None, alias='processing_fee')

    adjustment: typing.Optional[str] = Field(None, alias='adjustment')

    # Total due.
    total: typing.Optional[str] = Field(None, alias='total')

    # Total in payment currency.
    total_payment_currency: typing.Optional[str] = Field(None, alias='total_payment_currency')

    # Date of payment.
    payment_date: typing.Optional[str] = Field(None, alias='payment_date')

    frequency: typing.Optional[str] = Field(None, alias='frequency')

    # Country of the contract.
    contract_country: typing.Optional[str] = Field(None, alias='contract_country')

    # Contract start date.
    contract_start_date: typing.Optional[str] = Field(None, alias='contract_start_date')

    approvers: typing.Optional[str] = Field(None, alias='approvers')

    approve_date: typing.Optional[str] = Field(None, alias='approve_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )