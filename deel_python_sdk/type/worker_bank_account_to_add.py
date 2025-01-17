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


class RequiredWorkerBankAccountToAdd(TypedDict):
    pass

class OptionalWorkerBankAccountToAdd(TypedDict, total=False):
    # Full name of the user.
    full_name: str

    # The user's phone number.
    phone: str

    # The primary address line.
    address_line1: str

    # The secondary address line.
    address_line2: str

    # The city of the user's address.
    city: str

    # The state or province of the user's address.
    province_state: str

    # The user's postal or ZIP code.
    postal: str

    # Name of the user's bank.
    bank_name: str

    # The country code of the user.
    country_code: str

    # The country code where the bank is located.
    bank_country_code: str

    # SWIFT/BIC code for the bank.
    swift_bic: str

    # The user's bank account number.
    account_number: str

    # The bank code.
    bank_code: str

    # The original name of the user.
    original_name: str

    # The user's tax identification number.
    tax_id: str

    # The branch code of the user's bank.
    branch_code: str

    # The currency code for transactions.
    currency_code: str

    # The name of the user's bank branch.
    bank_branch_name: str

    # The International Bank Account Number (IBAN).
    iban: str

    # The user's email address.
    email: str

    # The RIB(Relevé d'Identité Bancaire).
    rib_number: str

    # Bank account type.
    account_type: str

    # The ACH (Automated Clearing House) Routing Number.
    ach_routing_number: str

class WorkerBankAccountToAdd(RequiredWorkerBankAccountToAdd, OptionalWorkerBankAccountToAdd):
    pass
