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


class RequiredEmployeeTimeoffsPoliciesItemEntitlement(TypedDict):
    pass

class OptionalEmployeeTimeoffsPoliciesItemEntitlement(TypedDict, total=False):
    # Accrual amount of the time off policy.
    accrual_amount: typing.Optional[str]

    # Accrual unit of the time off policy.
    accrual_unit: typing.Optional[str]

    # Total time off policy.
    total: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Unit amount of the time off policy.
    unit_amount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Unit of the time off policy.
    unit: typing.Optional[str]

    # Accrued time off policy.
    accrued: typing.Optional[str]

class EmployeeTimeoffsPoliciesItemEntitlement(RequiredEmployeeTimeoffsPoliciesItemEntitlement, OptionalEmployeeTimeoffsPoliciesItemEntitlement):
    pass
