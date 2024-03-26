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


class FinalPaymentCalculated(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "calculation_type",
            "total",
            "daily_rate",
            "last_cycle",
            "workweek_end",
            "remaining_days",
            "workweek_start",
        }
        
        class properties:
            daily_rate = schemas.StrSchema
            total = schemas.StrSchema
            remaining_days = schemas.StrSchema
            
            
            class last_cycle(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        start = schemas.DateTimeSchema
                        end = schemas.DateTimeSchema
                        completion_date = schemas.DateTimeSchema
                        __annotations__ = {
                            "start": start,
                            "end": end,
                            "completion_date": completion_date,
                        }
            
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["completion_date"]) -> MetaOapg.properties.completion_date: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["start", "end", "completion_date", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["completion_date"]) -> typing.Union[MetaOapg.properties.completion_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start", "end", "completion_date", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    start: typing.Union[MetaOapg.properties.start, str, datetime, schemas.Unset] = schemas.unset,
                    end: typing.Union[MetaOapg.properties.end, str, datetime, schemas.Unset] = schemas.unset,
                    completion_date: typing.Union[MetaOapg.properties.completion_date, str, datetime, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'last_cycle':
                    return super().__new__(
                        cls,
                        *args,
                        start=start,
                        end=end,
                        completion_date=completion_date,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class calculation_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CUSTOM_AMOUNT(cls):
                    return cls("CUSTOM_AMOUNT")
                
                @schemas.classproperty
                def WORK_DAYS(cls):
                    return cls("WORK_DAYS")
                
                @schemas.classproperty
                def CALENDAR_DAYS(cls):
                    return cls("CALENDAR_DAYS")
                
                @schemas.classproperty
                def FULL_AMOUNT(cls):
                    return cls("FULL_AMOUNT")
            workweek_start = schemas.NumberSchema
            workweek_end = schemas.NumberSchema
            __annotations__ = {
                "daily_rate": daily_rate,
                "total": total,
                "remaining_days": remaining_days,
                "last_cycle": last_cycle,
                "calculation_type": calculation_type,
                "workweek_start": workweek_start,
                "workweek_end": workweek_end,
            }
    
    calculation_type: MetaOapg.properties.calculation_type
    total: MetaOapg.properties.total
    daily_rate: MetaOapg.properties.daily_rate
    last_cycle: MetaOapg.properties.last_cycle
    workweek_end: MetaOapg.properties.workweek_end
    remaining_days: MetaOapg.properties.remaining_days
    workweek_start: MetaOapg.properties.workweek_start
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daily_rate"]) -> MetaOapg.properties.daily_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remaining_days"]) -> MetaOapg.properties.remaining_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_cycle"]) -> MetaOapg.properties.last_cycle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calculation_type"]) -> MetaOapg.properties.calculation_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workweek_start"]) -> MetaOapg.properties.workweek_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workweek_end"]) -> MetaOapg.properties.workweek_end: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["daily_rate", "total", "remaining_days", "last_cycle", "calculation_type", "workweek_start", "workweek_end", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daily_rate"]) -> MetaOapg.properties.daily_rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remaining_days"]) -> MetaOapg.properties.remaining_days: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_cycle"]) -> MetaOapg.properties.last_cycle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calculation_type"]) -> MetaOapg.properties.calculation_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workweek_start"]) -> MetaOapg.properties.workweek_start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workweek_end"]) -> MetaOapg.properties.workweek_end: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["daily_rate", "total", "remaining_days", "last_cycle", "calculation_type", "workweek_start", "workweek_end", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        calculation_type: typing.Union[MetaOapg.properties.calculation_type, str, ],
        total: typing.Union[MetaOapg.properties.total, str, ],
        daily_rate: typing.Union[MetaOapg.properties.daily_rate, str, ],
        last_cycle: typing.Union[MetaOapg.properties.last_cycle, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        workweek_end: typing.Union[MetaOapg.properties.workweek_end, decimal.Decimal, int, float, ],
        remaining_days: typing.Union[MetaOapg.properties.remaining_days, str, ],
        workweek_start: typing.Union[MetaOapg.properties.workweek_start, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinalPaymentCalculated':
        return super().__new__(
            cls,
            *args,
            calculation_type=calculation_type,
            total=total,
            daily_rate=daily_rate,
            last_cycle=last_cycle,
            workweek_end=workweek_end,
            remaining_days=remaining_days,
            workweek_start=workweek_start,
            _configuration=_configuration,
            **kwargs,
        )
