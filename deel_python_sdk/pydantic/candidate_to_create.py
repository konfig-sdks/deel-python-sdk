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

from deel_python_sdk.pydantic.candidate_status_enum import CandidateStatusEnum
from deel_python_sdk.pydantic.country_code import CountryCode
from deel_python_sdk.pydantic.date_string_required import DateStringRequired
from deel_python_sdk.pydantic.email_type_required import EmailTypeRequired
from deel_python_sdk.pydantic.nationality_type import NationalityType

class CandidateToCreate(BaseModel):
    # Unique identifier of candidate in your ATS.
    id: str = Field(alias='id')

    # Candidate's first name.
    first_name: str = Field(alias='first_name')

    # Candidate's last name.
    last_name: str = Field(alias='last_name')

    status: CandidateStatusEnum = Field(alias='status')

    start_date: DateStringRequired = Field(alias='start_date')

    # Link to candidate's profile in ATS.
    link: str = Field(alias='link')

    # Job Title.
    job_title: typing.Optional[str] = Field(None, alias='job_title')

    email: typing.Optional[EmailTypeRequired] = Field(None, alias='email')

    nationality: typing.Optional[NationalityType] = Field(None, alias='nationality')

    country: typing.Optional[CountryCode] = Field(None, alias='country')

    # Job location state.
    state: typing.Optional[str] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )