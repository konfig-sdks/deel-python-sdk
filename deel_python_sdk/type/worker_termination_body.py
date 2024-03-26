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

from deel_python_sdk.type.worker_termination_body_severance import WorkerTerminationBodySeverance

class RequiredWorkerTerminationBody(TypedDict):
    # The preferred end date for terminating the worker's engagement.
    desired_end_date: date

    # The effective termination date of the worker's employment.
    last_date_of_work: date

    # The reason for terminating the worker's engagement.
    message: str

    # Indicates whether the worker termination is voluntary (true) or involuntary (false).
    is_voluntary: bool

    severance: WorkerTerminationBodySeverance

class OptionalWorkerTerminationBody(TypedDict, total=False):
    pass

class WorkerTerminationBody(RequiredWorkerTerminationBody, OptionalWorkerTerminationBody):
    pass