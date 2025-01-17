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

from deel_python_sdk.pydantic.contract_type_enum import ContractTypeEnum
from deel_python_sdk.pydantic.contract_type_enum_list import ContractTypeEnumList
from deel_python_sdk.pydantic.date_string import DateString
from deel_python_sdk.pydantic.invoice_adjustment_status_enum import InvoiceAdjustmentStatusEnum
from deel_python_sdk.pydantic.invoice_adjustment_status_enum_list import InvoiceAdjustmentStatusEnumList
from deel_python_sdk.pydantic.invoice_adjustment_type_enum import InvoiceAdjustmentTypeEnum
from deel_python_sdk.pydantic.invoice_adjustment_type_enum_list import InvoiceAdjustmentTypeEnumList
from deel_python_sdk.pydantic.sort_dir_enum import SortDirEnum

class InvoiceAdjustmentSearchContainer(BaseModel):
    # Return a page of results with given number of records.
    limit: typing.Optional[str] = Field(None, alias='limit')

    offset: typing.Optional[str] = Field(None, alias='offset')

    order_direction: typing.Optional[SortDirEnum] = Field(None, alias='order_direction')

    contract_id: typing.Optional[str] = Field(None, alias='contract_id')

    invoice_id: typing.Optional[str] = Field(None, alias='invoice_id')

    reporter_id: typing.Optional[str] = Field(None, alias='reporter_id')

    contract_types: typing.Optional[typing.Union[ContractTypeEnumList, ContractTypeEnum]] = Field(None, alias='contract_types')

    types: typing.Optional[typing.Union[InvoiceAdjustmentTypeEnumList, InvoiceAdjustmentTypeEnum]] = Field(None, alias='types')

    statuses: typing.Optional[typing.Union[InvoiceAdjustmentStatusEnumList, InvoiceAdjustmentStatusEnum]] = Field(None, alias='statuses')

    date_from: typing.Optional[DateString] = Field(None, alias='date_from')

    date_to: typing.Optional[DateString] = Field(None, alias='date_to')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
