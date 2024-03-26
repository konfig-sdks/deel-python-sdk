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


class RequiredPensionEORContractToCreate(TypedDict):
    pass

class OptionalPensionEORContractToCreate(TypedDict, total=False):
    # Pension provider id. You can see available pension providers in the country guide endpoint.
    id: str

    # Enter the value of pension contribution. You should send this value only if the contribution object is available in the country guide endpoint and the value should be there between minimum and maximum values indicated.
    contribution: str

class PensionEORContractToCreate(RequiredPensionEORContractToCreate, OptionalPensionEORContractToCreate):
    pass
