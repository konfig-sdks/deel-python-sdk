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


class Meta(BaseModel):
    created: typing.Optional[datetime] = Field(None, alias='created')

    last_modified: typing.Optional[datetime] = Field(None, alias='lastModified')

    # resource location URI
    location: typing.Optional[str] = Field(None, alias='location')

    resource_type: typing.Optional[Literal["User", "Group"]] = Field(None, alias='resourceType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
