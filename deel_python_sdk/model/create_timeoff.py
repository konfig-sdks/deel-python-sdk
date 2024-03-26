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


class CreateTimeoff(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
            "with_multiple_dates",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "VACATION": "VACATION",
                        "SICK_LEAVE": "SICK_LEAVE",
                        "OTHER": "OTHER",
                    }
                
                @schemas.classproperty
                def VACATION(cls):
                    return cls("VACATION")
                
                @schemas.classproperty
                def SICK_LEAVE(cls):
                    return cls("SICK_LEAVE")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("OTHER")
            with_multiple_dates = schemas.BoolSchema
            start_date = schemas.StrSchema
            end_date = schemas.StrSchema
            reason = schemas.StrSchema
            is_start_date_half_day = schemas.BoolSchema
            is_end_date_half_day = schemas.BoolSchema
            other_timeoff_name = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "with_multiple_dates": with_multiple_dates,
                "start_date": start_date,
                "end_date": end_date,
                "reason": reason,
                "is_start_date_half_day": is_start_date_half_day,
                "is_end_date_half_day": is_end_date_half_day,
                "other_timeoff_name": other_timeoff_name,
            }
    
    type: MetaOapg.properties.type
    with_multiple_dates: MetaOapg.properties.with_multiple_dates
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["with_multiple_dates"]) -> MetaOapg.properties.with_multiple_dates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_start_date_half_day"]) -> MetaOapg.properties.is_start_date_half_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_end_date_half_day"]) -> MetaOapg.properties.is_end_date_half_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_timeoff_name"]) -> MetaOapg.properties.other_timeoff_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "with_multiple_dates", "start_date", "end_date", "reason", "is_start_date_half_day", "is_end_date_half_day", "other_timeoff_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["with_multiple_dates"]) -> MetaOapg.properties.with_multiple_dates: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_start_date_half_day"]) -> typing.Union[MetaOapg.properties.is_start_date_half_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_end_date_half_day"]) -> typing.Union[MetaOapg.properties.is_end_date_half_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_timeoff_name"]) -> typing.Union[MetaOapg.properties.other_timeoff_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "with_multiple_dates", "start_date", "end_date", "reason", "is_start_date_half_day", "is_end_date_half_day", "other_timeoff_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        with_multiple_dates: typing.Union[MetaOapg.properties.with_multiple_dates, bool, ],
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        is_start_date_half_day: typing.Union[MetaOapg.properties.is_start_date_half_day, bool, schemas.Unset] = schemas.unset,
        is_end_date_half_day: typing.Union[MetaOapg.properties.is_end_date_half_day, bool, schemas.Unset] = schemas.unset,
        other_timeoff_name: typing.Union[MetaOapg.properties.other_timeoff_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTimeoff':
        return super().__new__(
            cls,
            *args,
            type=type,
            with_multiple_dates=with_multiple_dates,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            is_start_date_half_day=is_start_date_half_day,
            is_end_date_half_day=is_end_date_half_day,
            other_timeoff_name=other_timeoff_name,
            _configuration=_configuration,
            **kwargs,
        )