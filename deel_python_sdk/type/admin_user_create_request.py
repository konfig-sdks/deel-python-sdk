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


class RequiredAdminUserCreateRequest(TypedDict):
    # User's first name
    first_name: str

    # User's last name
    last_name: str

    # User's email
    email: str

class OptionalAdminUserCreateRequest(TypedDict, total=False):
    pass

class AdminUserCreateRequest(RequiredAdminUserCreateRequest, OptionalAdminUserCreateRequest):
    pass
