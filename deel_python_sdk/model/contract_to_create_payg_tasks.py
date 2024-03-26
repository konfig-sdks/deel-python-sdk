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


class ContractToCreatePaygTasks(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "type",
                    "start_date",
                }
                
                class properties:
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "payg_tasks": "PAYG_TASKS",
                            }
                        
                        @schemas.classproperty
                        def PAYG_TASKS(cls):
                            return cls("payg_tasks")
                
                    @staticmethod
                    def start_date() -> typing.Type['DateStringRequired']:
                        return DateStringRequired
                    __annotations__ = {
                        "type": type,
                        "start_date": start_date,
                    }
            
            type: MetaOapg.properties.type
            start_date: 'DateStringRequired'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> 'DateStringRequired': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "start_date", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> 'DateStringRequired': ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "start_date", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                type: typing.Union[MetaOapg.properties.type, str, ],
                start_date: 'DateStringRequired',
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    type=type,
                    start_date=start_date,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class all_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "compensation_details",
                }
                
                class properties:
                
                    @staticmethod
                    def compensation_details() -> typing.Type['CompensationDetailsOfContractToCreateShared']:
                        return CompensationDetailsOfContractToCreateShared
                    __annotations__ = {
                        "compensation_details": compensation_details,
                    }
            
            compensation_details: 'CompensationDetailsOfContractToCreateShared'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["compensation_details"]) -> 'CompensationDetailsOfContractToCreateShared': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["compensation_details", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["compensation_details"]) -> 'CompensationDetailsOfContractToCreateShared': ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["compensation_details", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                compensation_details: 'CompensationDetailsOfContractToCreateShared',
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_2':
                return super().__new__(
                    cls,
                    *args,
                    compensation_details=compensation_details,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                ContractToCreateShared,
                cls.all_of_1,
                cls.all_of_2,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractToCreatePaygTasks':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.compensation_details_of_contract_to_create_shared import CompensationDetailsOfContractToCreateShared
from deel_python_sdk.model.contract_to_create_shared import ContractToCreateShared
from deel_python_sdk.model.date_string_required import DateStringRequired
