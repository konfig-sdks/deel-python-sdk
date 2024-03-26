# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from deel_python_sdk import schemas  # noqa: F401


class GPContractToCreateEmployment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "holidays",
            "type",
            "start_date",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['GPContractStatusTypeEnum']:
                return GPContractStatusTypeEnum
        
            @staticmethod
            def start_date() -> typing.Type['DateStringRequired']:
                return DateStringRequired
        
            @staticmethod
            def holidays() -> typing.Type['GPContractToCreateEmploymentHolidays']:
                return GPContractToCreateEmploymentHolidays
            __annotations__ = {
                "type": type,
                "start_date": start_date,
                "holidays": holidays,
            }
    
    holidays: 'GPContractToCreateEmploymentHolidays'
    type: 'GPContractStatusTypeEnum'
    start_date: 'DateStringRequired'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'GPContractStatusTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holidays"]) -> 'GPContractToCreateEmploymentHolidays': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "start_date", "holidays", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'GPContractStatusTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holidays"]) -> 'GPContractToCreateEmploymentHolidays': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "start_date", "holidays", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        holidays: 'GPContractToCreateEmploymentHolidays',
        type: 'GPContractStatusTypeEnum',
        start_date: 'DateStringRequired',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GPContractToCreateEmployment':
        return super().__new__(
            cls,
            *args,
            holidays=holidays,
            type=type,
            start_date=start_date,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.date_string_required import DateStringRequired
from deel_python_sdk.model.gp_contract_status_type_enum import GPContractStatusTypeEnum
from deel_python_sdk.model.gp_contract_to_create_employment_holidays import GPContractToCreateEmploymentHolidays
