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


class WorkerBankAccountToAdd(BaseModel):
    # Full name of the user.
    full_name: typing.Optional[str] = Field(None, alias='full_name')

    # The user's phone number.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # The primary address line.
    address_line1: typing.Optional[str] = Field(None, alias='address_line1')

    # The secondary address line.
    address_line2: typing.Optional[str] = Field(None, alias='address_line2')

    # The city of the user's address.
    city: typing.Optional[str] = Field(None, alias='city')

    # The state or province of the user's address.
    province_state: typing.Optional[str] = Field(None, alias='province_state')

    # The user's postal or ZIP code.
    postal: typing.Optional[str] = Field(None, alias='postal')

    # Name of the user's bank.
    bank_name: typing.Optional[str] = Field(None, alias='bank_name')

    # The country code of the user.
    country_code: typing.Optional[str] = Field(None, alias='country_code')

    # The country code where the bank is located.
    bank_country_code: typing.Optional[str] = Field(None, alias='bank_country_code')

    # SWIFT/BIC code for the bank.
    swift_bic: typing.Optional[str] = Field(None, alias='swift_bic')

    # The user's bank account number.
    account_number: typing.Optional[str] = Field(None, alias='account_number')

    # The bank code.
    bank_code: typing.Optional[str] = Field(None, alias='bank_code')

    # The original name of the user.
    original_name: typing.Optional[str] = Field(None, alias='original_name')

    # The user's tax identification number.
    tax_id: typing.Optional[str] = Field(None, alias='tax_id')

    # The branch code of the user's bank.
    branch_code: typing.Optional[str] = Field(None, alias='branch_code')

    # The currency code for transactions.
    currency_code: typing.Optional[str] = Field(None, alias='currency_code')

    # The name of the user's bank branch.
    bank_branch_name: typing.Optional[str] = Field(None, alias='bank_branch_name')

    # The International Bank Account Number (IBAN).
    iban: typing.Optional[str] = Field(None, alias='iban')

    # The user's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # The RIB(Relevé d'Identité Bancaire).
    rib_number: typing.Optional[str] = Field(None, alias='rib_number')

    # Bank account type.
    account_type: typing.Optional[str] = Field(None, alias='account_type')

    # The ACH (Automated Clearing House) Routing Number.
    ach_routing_number: typing.Optional[str] = Field(None, alias='ach_routing_number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
