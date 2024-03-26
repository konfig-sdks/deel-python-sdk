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

from deel_python_sdk.type.eor_employee_cost_calculation_request_body_benefits import EorEmployeeCostCalculationRequestBodyBenefits

class RequiredEorEmployeeCostCalculationRequestBody(TypedDict):
    # The gross annual salary of the employee.
    salary: typing.Union[int, float]

    # The country of employment.
    country: str

    # The currency that the salary is paid in.
    currency: str

class OptionalEorEmployeeCostCalculationRequestBody(TypedDict, total=False):
    benefits: typing.Optional[EorEmployeeCostCalculationRequestBodyBenefits]

class EorEmployeeCostCalculationRequestBody(RequiredEorEmployeeCostCalculationRequestBody, OptionalEorEmployeeCostCalculationRequestBody):
    pass