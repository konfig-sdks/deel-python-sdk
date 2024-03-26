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

from deel_python_sdk.pydantic.payment_list import PaymentList

class PaymentObject(BaseModel):
    rows: typing.Optional[PaymentList] = Field(None, alias='rows')

    total: typing.Optional[typing.Union[int, float]] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
