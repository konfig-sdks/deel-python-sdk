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


class RequiredEorCountryValidationsSickDays(TypedDict):
    pass

class OptionalEorCountryValidationsSickDays(TypedDict, total=False):
    # Minimum number of sick days required for a legally compliant contract.
    min: str

    # Maximum number of sick days allowed for a legally compliant contract.
    max: str

class EorCountryValidationsSickDays(RequiredEorCountryValidationsSickDays, OptionalEorCountryValidationsSickDays):
    pass
