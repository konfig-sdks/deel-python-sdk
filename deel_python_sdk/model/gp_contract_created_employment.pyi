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


class GPContractCreatedEmployment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def start_date() -> typing.Type['DateString']:
                return DateString
        
            @staticmethod
            def end_date() -> typing.Type['DateString']:
                return DateString
            country = schemas.StrSchema
            
            
            class state(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'state':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            type = schemas.StrSchema
            work_visa_required = schemas.BoolSchema
        
            @staticmethod
            def holidays() -> typing.Type['GPContractCreatedEmploymentHolidays']:
                return GPContractCreatedEmploymentHolidays
            __annotations__ = {
                "start_date": start_date,
                "end_date": end_date,
                "country": country,
                "state": state,
                "type": type,
                "work_visa_required": work_visa_required,
                "holidays": holidays,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_visa_required"]) -> MetaOapg.properties.work_visa_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holidays"]) -> 'GPContractCreatedEmploymentHolidays': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["start_date", "end_date", "country", "state", "type", "work_visa_required", "holidays", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union['DateString', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union['DateString', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_visa_required"]) -> typing.Union[MetaOapg.properties.work_visa_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holidays"]) -> typing.Union['GPContractCreatedEmploymentHolidays', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start_date", "end_date", "country", "state", "type", "work_visa_required", "holidays", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        start_date: typing.Union['DateString', schemas.Unset] = schemas.unset,
        end_date: typing.Union['DateString', schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, None, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        work_visa_required: typing.Union[MetaOapg.properties.work_visa_required, bool, schemas.Unset] = schemas.unset,
        holidays: typing.Union['GPContractCreatedEmploymentHolidays', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GPContractCreatedEmployment':
        return super().__new__(
            cls,
            *args,
            start_date=start_date,
            end_date=end_date,
            country=country,
            state=state,
            type=type,
            work_visa_required=work_visa_required,
            holidays=holidays,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.date_string import DateString
from deel_python_sdk.model.gp_contract_created_employment_holidays import GPContractCreatedEmploymentHolidays
