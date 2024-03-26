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


class ContractToTerminate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def completion_date() -> typing.Type['DateString']:
                return DateString
            terminate_now = schemas.BoolSchema
            message = schemas.StrSchema
            __annotations__ = {
                "completion_date": completion_date,
                "terminate_now": terminate_now,
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completion_date"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminate_now"]) -> MetaOapg.properties.terminate_now: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["completion_date", "terminate_now", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completion_date"]) -> typing.Union['DateString', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminate_now"]) -> typing.Union[MetaOapg.properties.terminate_now, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["completion_date", "terminate_now", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        completion_date: typing.Union['DateString', schemas.Unset] = schemas.unset,
        terminate_now: typing.Union[MetaOapg.properties.terminate_now, bool, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractToTerminate':
        return super().__new__(
            cls,
            *args,
            completion_date=completion_date,
            terminate_now=terminate_now,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.date_string import DateString
