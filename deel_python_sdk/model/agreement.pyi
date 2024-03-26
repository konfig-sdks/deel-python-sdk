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


class Agreement(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "agreement_title",
            "agreement_type",
            "msa",
            "id",
            "client_legal_entity",
            "provider_legal_entity",
        }
        
        class properties:
            id = schemas.StrSchema
            agreement_title = schemas.StrSchema
            agreement_type = schemas.StrSchema
        
            @staticmethod
            def msa() -> typing.Type['AgreementMsa']:
                return AgreementMsa
        
            @staticmethod
            def client_legal_entity() -> typing.Type['AgreementClientLegalEntity']:
                return AgreementClientLegalEntity
        
            @staticmethod
            def provider_legal_entity() -> typing.Type['AgreementProviderLegalEntity']:
                return AgreementProviderLegalEntity
            __annotations__ = {
                "id": id,
                "agreement_title": agreement_title,
                "agreement_type": agreement_type,
                "msa": msa,
                "client_legal_entity": client_legal_entity,
                "provider_legal_entity": provider_legal_entity,
            }
    
    agreement_title: MetaOapg.properties.agreement_title
    agreement_type: MetaOapg.properties.agreement_type
    msa: 'AgreementMsa'
    id: MetaOapg.properties.id
    client_legal_entity: 'AgreementClientLegalEntity'
    provider_legal_entity: 'AgreementProviderLegalEntity'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreement_title"]) -> MetaOapg.properties.agreement_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreement_type"]) -> MetaOapg.properties.agreement_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["msa"]) -> 'AgreementMsa': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_legal_entity"]) -> 'AgreementClientLegalEntity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_legal_entity"]) -> 'AgreementProviderLegalEntity': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "agreement_title", "agreement_type", "msa", "client_legal_entity", "provider_legal_entity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreement_title"]) -> MetaOapg.properties.agreement_title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreement_type"]) -> MetaOapg.properties.agreement_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["msa"]) -> 'AgreementMsa': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_legal_entity"]) -> 'AgreementClientLegalEntity': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_legal_entity"]) -> 'AgreementProviderLegalEntity': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "agreement_title", "agreement_type", "msa", "client_legal_entity", "provider_legal_entity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agreement_title: typing.Union[MetaOapg.properties.agreement_title, str, ],
        agreement_type: typing.Union[MetaOapg.properties.agreement_type, str, ],
        msa: 'AgreementMsa',
        id: typing.Union[MetaOapg.properties.id, str, ],
        client_legal_entity: 'AgreementClientLegalEntity',
        provider_legal_entity: 'AgreementProviderLegalEntity',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Agreement':
        return super().__new__(
            cls,
            *args,
            agreement_title=agreement_title,
            agreement_type=agreement_type,
            msa=msa,
            id=id,
            client_legal_entity=client_legal_entity,
            provider_legal_entity=provider_legal_entity,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.agreement_client_legal_entity import AgreementClientLegalEntity
from deel_python_sdk.model.agreement_msa import AgreementMsa
from deel_python_sdk.model.agreement_provider_legal_entity import AgreementProviderLegalEntity