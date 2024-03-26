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

from deel_python_sdk.pydantic.agreement_client_legal_entity import AgreementClientLegalEntity
from deel_python_sdk.pydantic.agreement_msa import AgreementMsa
from deel_python_sdk.pydantic.agreement_provider_legal_entity import AgreementProviderLegalEntity

class Agreement(BaseModel):
    # Unique identifier of this resource.
    id: str = Field(alias='id')

    agreement_title: str = Field(alias='agreement_title')

    agreement_type: str = Field(alias='agreement_type')

    msa: AgreementMsa = Field(alias='msa')

    client_legal_entity: AgreementClientLegalEntity = Field(alias='client_legal_entity')

    provider_legal_entity: AgreementProviderLegalEntity = Field(alias='provider_legal_entity')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
