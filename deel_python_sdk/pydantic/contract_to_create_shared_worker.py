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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from deel_python_sdk.pydantic.worker_email_type import WorkerEmailType

class ContractToCreateSharedWorker(BaseModel):
    expected_email: WorkerEmailType = Field(alias='expected_email')

    # Worker's first name
    first_name: typing.Optional[str] = Field(alias='first_name')

    # Worker's last name
    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='last_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
