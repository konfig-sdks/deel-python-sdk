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

from deel_python_sdk.type.agreement_client_legal_entity import AgreementClientLegalEntity
from deel_python_sdk.type.agreement_msa import AgreementMsa
from deel_python_sdk.type.agreement_provider_legal_entity import AgreementProviderLegalEntity

class RequiredAgreement(TypedDict):
    # Unique identifier of this resource.
    id: str

    agreement_title: str

    agreement_type: str

    msa: AgreementMsa

    client_legal_entity: AgreementClientLegalEntity

    provider_legal_entity: AgreementProviderLegalEntity

class OptionalAgreement(TypedDict, total=False):
    pass

class Agreement(RequiredAgreement, OptionalAgreement):
    pass