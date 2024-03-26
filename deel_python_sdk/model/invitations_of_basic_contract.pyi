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


class InvitationsOfBasicContract(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def client_email() -> typing.Type['EmailType']:
                return EmailType
        
            @staticmethod
            def worker_email() -> typing.Type['EmailType']:
                return EmailType
            __annotations__ = {
                "client_email": client_email,
                "worker_email": worker_email,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_email"]) -> 'EmailType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worker_email"]) -> 'EmailType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_email", "worker_email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_email"]) -> typing.Union['EmailType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worker_email"]) -> typing.Union['EmailType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_email", "worker_email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        client_email: typing.Union['EmailType', schemas.Unset] = schemas.unset,
        worker_email: typing.Union['EmailType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvitationsOfBasicContract':
        return super().__new__(
            cls,
            *args,
            client_email=client_email,
            worker_email=worker_email,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.email_type import EmailType