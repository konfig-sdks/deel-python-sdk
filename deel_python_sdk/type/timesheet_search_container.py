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

from deel_python_sdk.type.contract_type_enum import ContractTypeEnum
from deel_python_sdk.type.contract_type_enum_list import ContractTypeEnumList
from deel_python_sdk.type.date_string import DateString
from deel_python_sdk.type.sort_dir_enum import SortDirEnum
from deel_python_sdk.type.timesheet_status_enum import TimesheetStatusEnum
from deel_python_sdk.type.timesheet_status_enum_list import TimesheetStatusEnumList
from deel_python_sdk.type.timesheet_type_enum import TimesheetTypeEnum
from deel_python_sdk.type.timesheet_type_enum_list import TimesheetTypeEnumList

class RequiredTimesheetSearchContainer(TypedDict):
    pass

class OptionalTimesheetSearchContainer(TypedDict, total=False):
    # Return a page of results with given number of records.
    limit: str

    offset: str

    order_direction: SortDirEnum

    contract_id: str

    invoice_id: str

    reporter_id: str

    contract_types: typing.Union[ContractTypeEnumList, ContractTypeEnum]

    types: typing.Union[TimesheetTypeEnumList, TimesheetTypeEnum]

    statuses: typing.Union[TimesheetStatusEnumList, TimesheetStatusEnum]

    date_from: DateString

    date_to: DateString

class TimesheetSearchContainer(RequiredTimesheetSearchContainer, OptionalTimesheetSearchContainer):
    pass
