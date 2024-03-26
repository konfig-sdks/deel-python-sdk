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


class EorCountryValidationsHealthInsurance(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['BenefitStatusEnum']:
                return BenefitStatusEnum
            
            
            class providers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['HealthInsuranceProvider']:
                        return HealthInsuranceProvider
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['HealthInsuranceProvider'], typing.List['HealthInsuranceProvider']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'providers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'HealthInsuranceProvider':
                    return super().__getitem__(i)
            __annotations__ = {
                "status": status,
                "providers": providers,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'BenefitStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providers"]) -> MetaOapg.properties.providers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "providers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['BenefitStatusEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providers"]) -> typing.Union[MetaOapg.properties.providers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "providers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        status: typing.Union['BenefitStatusEnum', schemas.Unset] = schemas.unset,
        providers: typing.Union[MetaOapg.properties.providers, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorCountryValidationsHealthInsurance':
        return super().__new__(
            cls,
            *args,
            status=status,
            providers=providers,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.benefit_status_enum import BenefitStatusEnum
from deel_python_sdk.model.health_insurance_provider import HealthInsuranceProvider
