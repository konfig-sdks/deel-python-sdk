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


class EorCountryValidationsDefiniteContract(BaseModel):
    type: typing.Optional[Literal["ALLOWED_WITHOUT_LIMITATION", "ALLOWED_WITH_MAXIMUM_LIMITATION", "NOT_ALLOWED"]] = Field(None, alias='type')

    maximum_limitation: typing.Optional[typing.Union[int, float]] = Field(None, alias='maximum_limitation')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
