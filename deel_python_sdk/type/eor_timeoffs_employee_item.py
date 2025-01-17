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

from deel_python_sdk.type.eor_client_timeoff_requests import EorClientTimeoffRequests

class RequiredEorTimeoffsEmployeeItem(TypedDict):
    # Unique identifier of this resource.
    id: str

    name: str

    eor_contract_id: typing.Union[int, float]

    contract_id: str

    # List of employee vacation time offs.
    vacations: typing.List[EorClientTimeoffRequests]

    # List of employee sick leave time offs.
    sick_leaves: typing.List[EorClientTimeoffRequests]

    # List of all other employee time offs.
    others: typing.List[EorClientTimeoffRequests]

    time_zones: str

class OptionalEorTimeoffsEmployeeItem(TypedDict, total=False):
    pass

class EorTimeoffsEmployeeItem(RequiredEorTimeoffsEmployeeItem, OptionalEorTimeoffsEmployeeItem):
    pass
