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


class WeekDaysEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Days of the week.
    """
    
    @schemas.classproperty
    def SUNDAY(cls):
        return cls("Sunday")
    
    @schemas.classproperty
    def MONDAY(cls):
        return cls("Monday")
    
    @schemas.classproperty
    def TUESDAY(cls):
        return cls("Tuesday")
    
    @schemas.classproperty
    def WEDNESDAY(cls):
        return cls("Wednesday")
    
    @schemas.classproperty
    def THURSDAY(cls):
        return cls("Thursday")
    
    @schemas.classproperty
    def FRIDAY(cls):
        return cls("Friday")
    
    @schemas.classproperty
    def SATURDAY(cls):
        return cls("Saturday")
