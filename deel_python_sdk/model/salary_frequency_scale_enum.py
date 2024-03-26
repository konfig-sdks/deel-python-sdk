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


class SalaryFrequencyScaleEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Scale of the salary frequency.
    """


    class MetaOapg:
        enum_value_to_name = {
            "monthly": "MONTHLY",
            "quarterly": "QUARTERLY",
            "annually": "ANNUALLY",
            "specific_month": "SPECIFIC_MONTH",
            "specific_date": "SPECIFIC_DATE",
        }
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("monthly")
    
    @schemas.classproperty
    def QUARTERLY(cls):
        return cls("quarterly")
    
    @schemas.classproperty
    def ANNUALLY(cls):
        return cls("annually")
    
    @schemas.classproperty
    def SPECIFIC_MONTH(cls):
        return cls("specific_month")
    
    @schemas.classproperty
    def SPECIFIC_DATE(cls):
        return cls("specific_date")
