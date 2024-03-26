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


class CreateWebhookRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "signing_key",
            "name",
            "description",
            "api_version",
            "events",
            "url",
            "status",
        }
        
        class properties:
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ENABLED(cls):
                    return cls("enabled")
                
                @schemas.classproperty
                def DISABLED(cls):
                    return cls("disabled")
            url = schemas.StrSchema
            
            
            class signing_key(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'signing_key':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            api_version = schemas.StrSchema
        
            @staticmethod
            def events() -> typing.Type['CreateWebhookRequestEvents']:
                return CreateWebhookRequestEvents
            __annotations__ = {
                "description": description,
                "name": name,
                "status": status,
                "url": url,
                "signing_key": signing_key,
                "api_version": api_version,
                "events": events,
            }
    
    signing_key: MetaOapg.properties.signing_key
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    api_version: MetaOapg.properties.api_version
    events: 'CreateWebhookRequestEvents'
    url: MetaOapg.properties.url
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signing_key"]) -> MetaOapg.properties.signing_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_version"]) -> MetaOapg.properties.api_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'CreateWebhookRequestEvents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "status", "url", "signing_key", "api_version", "events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signing_key"]) -> MetaOapg.properties.signing_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_version"]) -> MetaOapg.properties.api_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> 'CreateWebhookRequestEvents': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "status", "url", "signing_key", "api_version", "events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        signing_key: typing.Union[MetaOapg.properties.signing_key, None, str, ],
        name: typing.Union[MetaOapg.properties.name, None, str, ],
        description: typing.Union[MetaOapg.properties.description, None, str, ],
        api_version: typing.Union[MetaOapg.properties.api_version, str, ],
        events: 'CreateWebhookRequestEvents',
        url: typing.Union[MetaOapg.properties.url, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateWebhookRequest':
        return super().__new__(
            cls,
            *args,
            signing_key=signing_key,
            name=name,
            description=description,
            api_version=api_version,
            events=events,
            url=url,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.create_webhook_request_events import CreateWebhookRequestEvents
