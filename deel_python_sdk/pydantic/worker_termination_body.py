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

from deel_python_sdk.pydantic.worker_termination_body_severance import WorkerTerminationBodySeverance

class WorkerTerminationBody(BaseModel):
    # The preferred end date for terminating the worker's engagement.
    desired_end_date: date = Field(alias='desired_end_date')

    # The effective termination date of the worker's employment.
    last_date_of_work: date = Field(alias='last_date_of_work')

    # The reason for terminating the worker's engagement.
    message: str = Field(alias='message')

    # Indicates whether the worker termination is voluntary (true) or involuntary (false).
    is_voluntary: bool = Field(alias='is_voluntary')

    severance: WorkerTerminationBodySeverance = Field(alias='severance')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
