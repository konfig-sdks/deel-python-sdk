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


class PageInfoWithCursorNew(BaseModel):
    total_rows: typing.Union[int, float] = Field(alias='total_rows')

    items_per_page: typing.Union[int, float] = Field(alias='items_per_page')

    offset: typing.Union[int, float] = Field(alias='offset')

    # Use for pagination to get next set of records after the given cursor.
    cursor: typing.Optional[str] = Field(None, alias='cursor')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
