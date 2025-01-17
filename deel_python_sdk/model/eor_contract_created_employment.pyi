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


class EorContractCreatedEmployment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            scope_of_work = schemas.StrSchema
        
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
            work_visa_required = schemas.BoolSchema
            time_off_type = schemas.StrSchema
            
            
            class probation_period(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'probation_period':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            calculated_holidays = schemas.StrSchema
            __annotations__ = {
                "scope_of_work": scope_of_work,
                "start_date": start_date,
                "end_date": end_date,
                "country": country,
                "state": state,
                "work_visa_required": work_visa_required,
                "time_off_type": time_off_type,
                "probation_period": probation_period,
                "calculated_holidays": calculated_holidays,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope_of_work"]) -> MetaOapg.properties.scope_of_work: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_visa_required"]) -> MetaOapg.properties.work_visa_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_off_type"]) -> MetaOapg.properties.time_off_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probation_period"]) -> MetaOapg.properties.probation_period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calculated_holidays"]) -> MetaOapg.properties.calculated_holidays: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scope_of_work", "start_date", "end_date", "country", "state", "work_visa_required", "time_off_type", "probation_period", "calculated_holidays", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope_of_work"]) -> typing.Union[MetaOapg.properties.scope_of_work, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union['DateString', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union['DateString', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_visa_required"]) -> typing.Union[MetaOapg.properties.work_visa_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_off_type"]) -> typing.Union[MetaOapg.properties.time_off_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probation_period"]) -> typing.Union[MetaOapg.properties.probation_period, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calculated_holidays"]) -> typing.Union[MetaOapg.properties.calculated_holidays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scope_of_work", "start_date", "end_date", "country", "state", "work_visa_required", "time_off_type", "probation_period", "calculated_holidays", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scope_of_work: typing.Union[MetaOapg.properties.scope_of_work, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union['DateString', schemas.Unset] = schemas.unset,
        end_date: typing.Union['DateString', schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, None, str, schemas.Unset] = schemas.unset,
        work_visa_required: typing.Union[MetaOapg.properties.work_visa_required, bool, schemas.Unset] = schemas.unset,
        time_off_type: typing.Union[MetaOapg.properties.time_off_type, str, schemas.Unset] = schemas.unset,
        probation_period: typing.Union[MetaOapg.properties.probation_period, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        calculated_holidays: typing.Union[MetaOapg.properties.calculated_holidays, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorContractCreatedEmployment':
        return super().__new__(
            cls,
            *args,
            scope_of_work=scope_of_work,
            start_date=start_date,
            end_date=end_date,
            country=country,
            state=state,
            work_visa_required=work_visa_required,
            time_off_type=time_off_type,
            probation_period=probation_period,
            calculated_holidays=calculated_holidays,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.date_string import DateString
