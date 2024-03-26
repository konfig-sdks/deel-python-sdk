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


class RequiredAdjustmentToUpdate(TypedDict):
    pass

class OptionalAdjustmentToUpdate(TypedDict, total=False):
    # Title of adjustment.
    title: str

    # Description of adjustment.
    description: str

    # Amount of adjustment.
    amount: typing.Union[str, typing.Union[int, float]]

    # File of adjustment.
    file: typing.IO

class AdjustmentToUpdate(RequiredAdjustmentToUpdate, OptionalAdjustmentToUpdate):
    pass
