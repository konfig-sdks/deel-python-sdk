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

from deel_python_sdk.type.employment import Employment
from deel_python_sdk.type.internal_people_contract_types import InternalPeopleContractTypes
from deel_python_sdk.type.monthly_payment import MonthlyPayment
from deel_python_sdk.type.payment import Payment
from deel_python_sdk.type.people_client_legal_entity import PeopleClientLegalEntity

class RequiredInternalPeople(TypedDict):
    pass

class OptionalInternalPeople(TypedDict, total=False):
    # Unique identifier for the user
    id: str

    # First name of the user
    first_name: str

    # Last name of the user
    last_name: str

    # Full name of the user
    full_name: str

    # Email address of the user
    email: str

    # Work email address of the user
    work_email: str

    # Personal email address of the user
    personal_email: str

    # Name of the country where the user is located
    country_name: str

    # Date of birth of the user in ISO format (yyyy-mm-dd)
    birth_date: str

    # URL of the user's profile picture
    pic_url: str

    # Date when the user started their current employment in ISO format (yyyy-mm-dd)
    start_date: str

    # List of payment objects representing the user's payment history
    payments: typing.List[Payment]

    # Total amount of hours worked by the user in ISO format (hh:mm:ss)
    hourly_report_total: str

    client_legal_entity: PeopleClientLegalEntity

    # State where the user is located
    state: str

    # Seniority level of the user's role
    seniority: str

    # Date when the user's current employment is expected to end in ISO format (yyyy-mm-ddThh:mm:ss.sssZ)
    completion_date: str

    monthly_payment: MonthlyPayment

    # Name of the user's direct manager
    direct_manager: str

    # Names of the user's direct reports
    direct_reports: str

    # Number of direct reports that the user has
    direct_reports_count: int

    # List of employment objects representing the user's employment history
    employments: typing.List[Employment]

    # Hiring status of the user
    hiring_status: str

    # Type of employment contract that the user has
    hiring_type: str

    # Title of the user's role
    job_title: str

    # ISO 3166-1 alpha-2 code of the country where the user is located
    country: str

    # Unique identifier for the team that the user belongs to
    team_id: int

    # Name of the team that the user belongs to
    team: str

    # Time zone of the user's location
    timezone: str

    # Name of the department that the user belongs to
    department: str

    # Name of the user's work location
    work_location: str

    contract_types: InternalPeopleContractTypes

    # Indicates whether the user has a Deel account or not
    has_deel_user: bool

class InternalPeople(RequiredInternalPeople, OptionalInternalPeople):
    pass
