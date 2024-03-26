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


class MetaDataOfContractToCreate(BaseModel):
    # Require the contractor to upload necessary compliance documents as per their country’s labor laws.
    documents_required: bool = Field(alias='documents_required')

    is_main_income: typing.Optional[bool] = Field(None, alias='is_main_income')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
