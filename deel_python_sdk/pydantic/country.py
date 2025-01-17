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

from deel_python_sdk.pydantic.country_code import CountryCode
from deel_python_sdk.pydantic.state_of_country import StateOfCountry

class Country(BaseModel):
    code: CountryCode = Field(alias='code')

    # Country name.
    name: str = Field(alias='name')

    # Identifies if Deel provides visa support for employees being hired in this country.
    visa_support: bool = Field(alias='visa_support')

    # Identifies if Deel support EoR in this country.
    eor_support: bool = Field(alias='eor_support')

    # Identifies the type of sub-territory within a country where local laws may apply. Some countries may have states, provinces, prefectures or regions.
    state_type: typing.Optional[str] = Field(alias='state_type')

    states: typing.List[StateOfCountry] = Field(alias='states')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
