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


class ContractTypeEnumToCreate(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Type of a contract
    """
    
    @schemas.classproperty
    def PAY_AS_YOU_GO_TIME_BASED(cls):
        return cls("pay_as_you_go_time_based")
    
    @schemas.classproperty
    def PAYG_TASKS(cls):
        return cls("payg_tasks")
    
    @schemas.classproperty
    def PAYG_MILESTONES(cls):
        return cls("payg_milestones")
