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

from deel_python_sdk.type.employee_timeoffs_policies_item_entitlement import EmployeeTimeoffsPoliciesItemEntitlement

class RequiredEmployeeTimeoffsPoliciesItem(TypedDict):
    # Description of the time off policy.
    description: str

    # Unique identifier for the time off policy.
    id: str

    # Type of time off policy.
    type: str

    # Name of the time off policy.
    name: str

    # Unit amount of the time off policy.
    unit_amount: typing.Union[int, float]

    # Used time off policy.
    used: typing.Optional[typing.Union[int, float]]

    # Start date of the time off policy.
    tracking_start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # End date of the time off policy.
    tracking_end_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    entitlement: EmployeeTimeoffsPoliciesItemEntitlement

class OptionalEmployeeTimeoffsPoliciesItem(TypedDict, total=False):
    pass

class EmployeeTimeoffsPoliciesItem(RequiredEmployeeTimeoffsPoliciesItem, OptionalEmployeeTimeoffsPoliciesItem):
    pass
