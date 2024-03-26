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

from deel_python_sdk.pydantic.contract_to_create_ongoing_time_based import ContractToCreateOngoingTimeBased
from deel_python_sdk.pydantic.contract_to_create_pay_as_you_go_time_based import ContractToCreatePayAsYouGoTimeBased
from deel_python_sdk.pydantic.contract_to_create_payg_milestones import ContractToCreatePaygMilestones
from deel_python_sdk.pydantic.contract_to_create_payg_tasks import ContractToCreatePaygTasks

ContractToCreate = typing.Union[ContractToCreatePayAsYouGoTimeBased,ContractToCreatePaygTasks,ContractToCreatePaygMilestones,ContractToCreateOngoingTimeBased]
