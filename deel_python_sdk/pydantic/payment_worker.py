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


class PaymentWorker(BaseModel):
    # Worker's full name.
    name: str = Field(alias='name')

    # URL to worker's Deel avatar.
    pic_url: typing.Optional[str] = Field(alias='picUrl')

    # Worker's unique id.
    id: typing.Optional[typing.Union[int, float]] = Field(None, alias='id')

    # The worker's Deel contract Id.
    contract_id: typing.Optional[typing.Optional[str]] = Field(None, alias='contract_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
