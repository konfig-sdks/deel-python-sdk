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

from deel_python_sdk.type.alternate_email_list import AlternateEmailList
from deel_python_sdk.type.email_type import EmailType
from deel_python_sdk.type.url_type import UrlType

class RequiredWorkerOfBasicContract(TypedDict):
    # Unique identifier of this resource.
    id: str

    full_name: str

    email: EmailType

class OptionalWorkerOfBasicContract(TypedDict, total=False):
    alternate_email: AlternateEmailList

    image: UrlType

class WorkerOfBasicContract(RequiredWorkerOfBasicContract, OptionalWorkerOfBasicContract):
    pass
