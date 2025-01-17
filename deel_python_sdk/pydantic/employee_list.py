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


class EmployeeList(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    full_name: typing.Optional[str] = Field(None, alias='full_name')

    email: typing.Optional[str] = Field(None, alias='email')

    timezone: typing.Optional[str] = Field(None, alias='timezone')

    personal_email: typing.Optional[str] = Field(None, alias='personal_email')

    country: typing.Optional[str] = Field(None, alias='country')

    birth_date: typing.Optional[str] = Field(None, alias='birth_date')

    pic_url: typing.Optional[str] = Field(None, alias='pic_url')

    hiring_type: typing.Optional[str] = Field(None, alias='hiring_type')

    start_date: typing.Optional[str] = Field(None, alias='start_date')

    team: typing.Optional[str] = Field(None, alias='team')

    team_id: typing.Optional[typing.Union[int, float]] = Field(None, alias='team_id')

    job_title: typing.Optional[str] = Field(None, alias='job_title')

    payments: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='payments')

    hourly_report_total: typing.Optional[str] = Field(None, alias='hourly_report_total')

    client_legal_entity: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='client_legal_entity')

    state: typing.Optional[str] = Field(None, alias='state')

    seniority: typing.Optional[str] = Field(None, alias='seniority')

    completion_date: typing.Optional[str] = Field(None, alias='completion_date')

    hiring_status: typing.Optional[str] = Field(None, alias='hiring_status')

    monthly_payment: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='monthly_payment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
