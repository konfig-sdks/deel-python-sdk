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

from deel_python_sdk.pydantic.alternate_email_list import AlternateEmailList
from deel_python_sdk.pydantic.date_time_string import DateTimeString
from deel_python_sdk.pydantic.email_type import EmailType
from deel_python_sdk.pydantic.worker_email_type import WorkerEmailType
from deel_python_sdk.pydantic.worker_legal_entity import WorkerLegalEntity

class WorkerOfContract(BaseModel):
    # Unique identifier of this resource.
    id: typing.Optional[str] = Field(None, alias='id')

    # Worker's full name.
    full_name: typing.Optional[str] = Field(None, alias='full_name')

    email: typing.Optional[EmailType] = Field(None, alias='email')

    alternate_email: typing.Optional[AlternateEmailList] = Field(None, alias='alternate_email')

    # Worker's nationality.
    nationality: typing.Optional[typing.Optional[str]] = Field(None, alias='nationality')

    image: typing.Optional[str] = Field(None, alias='image')

    legal_entity: typing.Optional[WorkerLegalEntity] = Field(None, alias='legal_entity')

    date_of_birth: typing.Optional[DateTimeString] = Field(None, alias='date_of_birth')

    expected_email: typing.Optional[WorkerEmailType] = Field(None, alias='expected_email')

    # Worker's first name
    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='first_name')

    # Worker's last name
    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='last_name')

    # Worker's country (location not nationality)
    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )