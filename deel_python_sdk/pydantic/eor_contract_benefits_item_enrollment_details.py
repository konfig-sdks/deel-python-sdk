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

from deel_python_sdk.pydantic.eor_contract_benefits_item_enrollment_details_current import EORContractBenefitsItemEnrollmentDetailsCurrent
from deel_python_sdk.pydantic.eor_contract_benefits_item_enrollment_details_plan import EORContractBenefitsItemEnrollmentDetailsPlan
from deel_python_sdk.pydantic.eor_contract_benefits_item_enrollment_details_standard import EORContractBenefitsItemEnrollmentDetailsStandard

class EORContractBenefitsItemEnrollmentDetails(BaseModel):
    # Status of the enrollment.
    status: typing.Optional[str] = Field(None, alias='status')

    plan: typing.Optional[EORContractBenefitsItemEnrollmentDetailsPlan] = Field(None, alias='plan')

    standard: typing.Optional[EORContractBenefitsItemEnrollmentDetailsStandard] = Field(None, alias='standard')

    current: typing.Optional[EORContractBenefitsItemEnrollmentDetailsCurrent] = Field(None, alias='current')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
