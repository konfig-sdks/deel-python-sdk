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

from deel_python_sdk.pydantic.salary_frequency_scale_enum import SalaryFrequencyScaleEnum

class EorCountryValidationsSalary(BaseModel):
    # Minimum wage for a legally compliant contract.
    min: typing.Optional[str] = Field(None, alias='min')

    # Maximum wage allowed for a legally compliant contract.
    max: typing.Optional[str] = Field(None, alias='max')

    frequency: typing.Optional[SalaryFrequencyScaleEnum] = Field(None, alias='frequency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
