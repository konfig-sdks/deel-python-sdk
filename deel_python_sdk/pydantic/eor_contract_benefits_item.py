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

from deel_python_sdk.pydantic.eor_contract_benefits_item_enrollment_details import EORContractBenefitsItemEnrollmentDetails
from deel_python_sdk.pydantic.eor_contract_benefits_item_plan import EORContractBenefitsItemPlan
from deel_python_sdk.pydantic.eor_contract_benefits_item_provider import EORContractBenefitsItemProvider

class EORContractBenefitsItem(BaseModel):
    # Unique identifier of the benefit.
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the benefit.
    name: typing.Optional[str] = Field(None, alias='name')

    provider: typing.Optional[EORContractBenefitsItemProvider] = Field(None, alias='provider')

    # Status of the offer.
    offer_status: typing.Optional[Literal["Offered", "Not offered"]] = Field(None, alias='offer_status')

    plan: typing.Optional[EORContractBenefitsItemPlan] = Field(None, alias='plan')

    enrollment_details: typing.Optional[EORContractBenefitsItemEnrollmentDetails] = Field(None, alias='enrollment_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
