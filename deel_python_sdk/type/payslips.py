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


RequiredPayslips = TypedDict("RequiredPayslips", {
    # Unique identifier for the payslip.
    "id": str,

    # Start date of the payslip.
    "from": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    # End date of the payslip.
    "to": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    # Status of the payslip.
    "status": str,
    })

OptionalPayslips = TypedDict("OptionalPayslips", {
    }, total=False)

class Payslips(RequiredPayslips, OptionalPayslips):
    pass