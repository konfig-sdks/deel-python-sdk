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


class PremiumToAdd(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "contractor_characteristics",
            "agreement_reflects_relation",
        }
        
        class properties:
            
            
            class agreement_reflects_relation(
                schemas.EnumBase,
                schemas.BoolSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        True: "TRUE",
                        False: "FALSE",
                    }
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls(True)
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls(False)
            
            
            class contractor_characteristics(
                schemas.EnumBase,
                schemas.BoolSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        True: "TRUE",
                        False: "FALSE",
                    }
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls(True)
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls(False)
            __annotations__ = {
                "agreement_reflects_relation": agreement_reflects_relation,
                "contractor_characteristics": contractor_characteristics,
            }
    
    contractor_characteristics: MetaOapg.properties.contractor_characteristics
    agreement_reflects_relation: MetaOapg.properties.agreement_reflects_relation
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreement_reflects_relation"]) -> MetaOapg.properties.agreement_reflects_relation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_characteristics"]) -> MetaOapg.properties.contractor_characteristics: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agreement_reflects_relation", "contractor_characteristics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreement_reflects_relation"]) -> MetaOapg.properties.agreement_reflects_relation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_characteristics"]) -> MetaOapg.properties.contractor_characteristics: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agreement_reflects_relation", "contractor_characteristics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        contractor_characteristics: typing.Union[MetaOapg.properties.contractor_characteristics, bool, ],
        agreement_reflects_relation: typing.Union[MetaOapg.properties.agreement_reflects_relation, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PremiumToAdd':
        return super().__new__(
            cls,
            *args,
            contractor_characteristics=contractor_characteristics,
            agreement_reflects_relation=agreement_reflects_relation,
            _configuration=_configuration,
            **kwargs,
        )
