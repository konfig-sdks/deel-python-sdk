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


class RequiredEmployeeList(TypedDict):
    pass

class OptionalEmployeeList(TypedDict, total=False):
    id: str

    first_name: str

    last_name: str

    full_name: str

    email: str

    timezone: str

    personal_email: str

    country: str

    birth_date: str

    pic_url: str

    hiring_type: str

    start_date: str

    team: str

    team_id: typing.Union[int, float]

    job_title: str

    payments: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    hourly_report_total: str

    client_legal_entity: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    state: str

    seniority: str

    completion_date: str

    hiring_status: str

    monthly_payment: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class EmployeeList(RequiredEmployeeList, OptionalEmployeeList):
    pass
