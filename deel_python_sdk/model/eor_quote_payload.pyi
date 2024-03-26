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


class EorQuotePayload(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    EOR quote approved by Deel
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    contract_id = schemas.StrSchema
                    contract_name = schemas.StrSchema
                
                    @staticmethod
                    def country_code() -> typing.Type['CountryCode']:
                        return CountryCode
                    country_name = schemas.StrSchema
                    __annotations__ = {
                        "contract_id": contract_id,
                        "contract_name": contract_name,
                        "country_code": country_code,
                        "country_name": country_name,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contract_id"]) -> MetaOapg.properties.contract_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contract_name"]) -> MetaOapg.properties.contract_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> 'CountryCode': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country_name"]) -> MetaOapg.properties.country_name: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["contract_id", "contract_name", "country_code", "country_name", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contract_id"]) -> typing.Union[MetaOapg.properties.contract_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contract_name"]) -> typing.Union[MetaOapg.properties.contract_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> typing.Union['CountryCode', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country_name"]) -> typing.Union[MetaOapg.properties.country_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contract_id", "contract_name", "country_code", "country_name", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                contract_id: typing.Union[MetaOapg.properties.contract_id, str, schemas.Unset] = schemas.unset,
                contract_name: typing.Union[MetaOapg.properties.contract_name, str, schemas.Unset] = schemas.unset,
                country_code: typing.Union['CountryCode', schemas.Unset] = schemas.unset,
                country_name: typing.Union[MetaOapg.properties.country_name, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    contract_id=contract_id,
                    contract_name=contract_name,
                    country_code=country_code,
                    country_name=country_name,
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
                EorQuoteBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorQuotePayload':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.country_code import CountryCode
from deel_python_sdk.model.eor_quote_base import EorQuoteBase
