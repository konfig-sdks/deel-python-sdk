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

from deel_python_sdk.pydantic.contract_status_enum import ContractStatusEnum
from deel_python_sdk.pydantic.contract_type_enum import ContractTypeEnum
from deel_python_sdk.pydantic.date_time_string import DateTimeString
from deel_python_sdk.pydantic.eor_contract_created_client import EorContractCreatedClient
from deel_python_sdk.pydantic.eor_contract_created_compensation_details import EorContractCreatedCompensationDetails
from deel_python_sdk.pydantic.eor_contract_created_employee import EorContractCreatedEmployee
from deel_python_sdk.pydantic.eor_contract_created_employment import EorContractCreatedEmployment
from deel_python_sdk.pydantic.eor_contract_created_health_plan import EorContractCreatedHealthPlan
from deel_python_sdk.pydantic.seniority import Seniority

class EorContractCreated(BaseModel):
    # Id of the contract quote created
    id: typing.Optional[str] = Field(None, alias='id')

    type: typing.Optional[ContractTypeEnum] = Field(None, alias='type')

    created_at: typing.Optional[DateTimeString] = Field(None, alias='created_at')

    status: typing.Optional[ContractStatusEnum] = Field(None, alias='status')

    # Employee's job title.
    job_title: typing.Optional[str] = Field(None, alias='job_title')

    employment: typing.Optional[EorContractCreatedEmployment] = Field(None, alias='employment')

    client: typing.Optional[EorContractCreatedClient] = Field(None, alias='client')

    compensation_details: typing.Optional[EorContractCreatedCompensationDetails] = Field(None, alias='compensation_details')

    employee: typing.Optional[EorContractCreatedEmployee] = Field(None, alias='employee')

    health_plan: typing.Optional[EorContractCreatedHealthPlan] = Field(None, alias='health_plan')

    seniority: typing.Optional[Seniority] = Field(None, alias='seniority')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )