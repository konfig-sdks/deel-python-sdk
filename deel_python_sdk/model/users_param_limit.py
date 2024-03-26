# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from deel_python_sdk import schemas  # noqa: F401


class UsersParamLimit(
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Maximum number of records to return. This is supposed to be an integer but query parameters are string. 1 to 100.
    """


    class MetaOapg:
        regex=[{
            'pattern': r'^[0-9][0-9]?$|^100$',
        }]
