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


class WorkStatementScaleEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Defines the scale at which the amount is paid. For example, enter 'hourly' to define the amount per hour. This field can be excluded when creating a Pay-as-you-go task-based or Milestone contracts.
    """
    
    @schemas.classproperty
    def HOURLY(cls):
        return cls("hourly")
    
    @schemas.classproperty
    def DAILY(cls):
        return cls("daily")
    
    @schemas.classproperty
    def WEEKLY(cls):
        return cls("weekly")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("monthly")
    
    @schemas.classproperty
    def BIWEEKLY(cls):
        return cls("biweekly")
    
    @schemas.classproperty
    def SEMIMONTHLY(cls):
        return cls("semimonthly")
    
    @schemas.classproperty
    def CUSTOM(cls):
        return cls("custom")