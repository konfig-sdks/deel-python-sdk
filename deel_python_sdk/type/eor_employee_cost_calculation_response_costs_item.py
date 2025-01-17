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


class RequiredEorEmployeeCostCalculationResponseCostsItem(TypedDict):
    pass

class OptionalEorEmployeeCostCalculationResponseCostsItem(TypedDict, total=False):
    # The name of the cost item.
    name: str

    # The amount or price of the cost item.
    amount: str

    # The frequency that the cost item must be paid.
    frequency: str

    # The country that the cost item is associated with.
    country: str

    # The country code for the country that the cost item is associated with.
    country_code: str

class EorEmployeeCostCalculationResponseCostsItem(RequiredEorEmployeeCostCalculationResponseCostsItem, OptionalEorEmployeeCostCalculationResponseCostsItem):
    pass
