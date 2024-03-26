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

from deel_python_sdk.type.country_code import CountryCode
from deel_python_sdk.type.date_string import DateString
from deel_python_sdk.type.date_string_required import DateStringRequired

class RequiredEorContractToCreateEmployment(TypedDict):
    country: CountryCode

    # Do you require Deel to apply for work visa for this person?
    work_visa_required: bool

    start_date: DateStringRequired

class OptionalEorContractToCreateEmployment(TypedDict, total=False):
    # State code of the state/province where the this person will be employed.
    state: typing.Optional[str]

    # Is it a full-time contract or a part-time contract?
    type: str

    end_date: DateString

    # Number of probation days.
    probation_period: typing.Optional[typing.Union[int, float]]

    # Scope of work description.
    scope_of_work: str

    # If you want to use standard number of holidays for this employee, choose \"STANDARD\". If you want to enter a specific number of holidays, choose \"SPECIFIC\" and enter the number of days in the holidays field.
    time_off_type: str

    # Enter the number of holidays. Leave this field blank if you are chooseing \"STANDARD\" time_off_type.
    holidays: typing.Optional[typing.Union[int, float]]

class EorContractToCreateEmployment(RequiredEorContractToCreateEmployment, OptionalEorContractToCreateEmployment):
    pass
