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


class EorContractCreatedCompensationDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            salary = schemas.NumberSchema
            currency = schemas.StrSchema
            variable_compensation = schemas.StrSchema
            
            
            class variable_compensation_type(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'variable_compensation_type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "salary": salary,
                "currency": currency,
                "variable_compensation": variable_compensation,
                "variable_compensation_type": variable_compensation_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary"]) -> MetaOapg.properties.salary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_compensation"]) -> MetaOapg.properties.variable_compensation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_compensation_type"]) -> MetaOapg.properties.variable_compensation_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["salary", "currency", "variable_compensation", "variable_compensation_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary"]) -> typing.Union[MetaOapg.properties.salary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_compensation"]) -> typing.Union[MetaOapg.properties.variable_compensation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_compensation_type"]) -> typing.Union[MetaOapg.properties.variable_compensation_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["salary", "currency", "variable_compensation", "variable_compensation_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        salary: typing.Union[MetaOapg.properties.salary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        variable_compensation: typing.Union[MetaOapg.properties.variable_compensation, str, schemas.Unset] = schemas.unset,
        variable_compensation_type: typing.Union[MetaOapg.properties.variable_compensation_type, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorContractCreatedCompensationDetails':
        return super().__new__(
            cls,
            *args,
            salary=salary,
            currency=currency,
            variable_compensation=variable_compensation,
            variable_compensation_type=variable_compensation_type,
            _configuration=_configuration,
            **kwargs,
        )
