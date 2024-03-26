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

from deel_python_sdk.pydantic.adjustment_status_enum import AdjustmentStatusEnum
from deel_python_sdk.pydantic.payroll_adjustment_file import PayrollAdjustmentFile

class PayrollAdjustment(BaseModel):
    # The title of the adjustment
    title: typing.Optional[str] = Field(None, alias='title')

    # The description of the adjustment
    description: typing.Optional[str] = Field(None, alias='description')

    # The unique identifier of the adjustment
    id: typing.Optional[str] = Field(None, alias='id')

    # The identifier of the contract associated with the adjustment
    contract_id: typing.Optional[str] = Field(None, alias='contract_id')

    # The amount of the adjustment
    amount: typing.Optional[str] = Field(None, alias='amount')

    # The date of the adjustment
    date_of_adjustment: typing.Optional[date] = Field(None, alias='date_of_adjustment')

    # The reference to the cycle associated with the adjustment
    cycle_reference: typing.Optional[typing.Optional[str]] = Field(None, alias='cycle_reference')

    status: typing.Optional[AdjustmentStatusEnum] = Field(None, alias='status')

    # The identifier of the adjustment category associated with the adjustment
    adjustment_category_id: typing.Optional[str] = Field(None, alias='adjustment_category_id')

    # The date of the actual start cycle date
    actual_start_cycle_date: typing.Optional[str] = Field(None, alias='actual_start_cycle_date')

    # The date of the actual end cycle date
    actual_end_cycle_date: typing.Optional[str] = Field(None, alias='actual_end_cycle_date')

    # If an adjustments can belong to another payroll cycle
    move_next_cycle: typing.Optional[bool] = Field(None, alias='move_next_cycle')

    file: typing.Optional[PayrollAdjustmentFile] = Field(None, alias='file')

    # The date and time when the adjustment was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The date and time when the adjustment was last updated
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )