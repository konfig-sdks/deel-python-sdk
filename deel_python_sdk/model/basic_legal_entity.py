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


class BasicLegalEntity(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entity_type",
            "entity_subtype",
            "name",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def entity_type() -> typing.Type['LegalEntityType']:
                return LegalEntityType
            entity_subtype = schemas.StrSchema
            country = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "entity_type": entity_type,
                "entity_subtype": entity_subtype,
                "country": country,
            }
    
    entity_type: 'LegalEntityType'
    entity_subtype: MetaOapg.properties.entity_subtype
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_type"]) -> 'LegalEntityType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_subtype"]) -> MetaOapg.properties.entity_subtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "entity_type", "entity_subtype", "country", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_type"]) -> 'LegalEntityType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_subtype"]) -> MetaOapg.properties.entity_subtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "entity_type", "entity_subtype", "country", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entity_type: 'LegalEntityType',
        entity_subtype: typing.Union[MetaOapg.properties.entity_subtype, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BasicLegalEntity':
        return super().__new__(
            cls,
            *args,
            entity_type=entity_type,
            entity_subtype=entity_subtype,
            name=name,
            id=id,
            country=country,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.legal_entity_type import LegalEntityType
