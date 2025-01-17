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


class BankAccountGuide(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "key",
            "required",
        }
        
        class properties:
            key = schemas.StrSchema
            required = schemas.BoolSchema
            label = schemas.StrSchema
            
            
            class values_allowed(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BankAccountValueAllowed']:
                        return BankAccountValueAllowed
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BankAccountValueAllowed'], typing.List['BankAccountValueAllowed']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'values_allowed':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BankAccountValueAllowed':
                    return super().__getitem__(i)
            
            
            class validations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ValidationType']:
                        return ValidationType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ValidationType'], typing.List['ValidationType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'validations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ValidationType':
                    return super().__getitem__(i)
            type = schemas.StrSchema
            __annotations__ = {
                "key": key,
                "required": required,
                "label": label,
                "values_allowed": values_allowed,
                "validations": validations,
                "type": type,
            }
    
    key: MetaOapg.properties.key
    required: MetaOapg.properties.required
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values_allowed"]) -> MetaOapg.properties.values_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validations"]) -> MetaOapg.properties.validations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "required", "label", "values_allowed", "validations", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values_allowed"]) -> typing.Union[MetaOapg.properties.values_allowed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validations"]) -> typing.Union[MetaOapg.properties.validations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "required", "label", "values_allowed", "validations", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        values_allowed: typing.Union[MetaOapg.properties.values_allowed, list, tuple, schemas.Unset] = schemas.unset,
        validations: typing.Union[MetaOapg.properties.validations, list, tuple, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankAccountGuide':
        return super().__new__(
            cls,
            *args,
            key=key,
            required=required,
            label=label,
            values_allowed=values_allowed,
            validations=validations,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.bank_account_value_allowed import BankAccountValueAllowed
from deel_python_sdk.model.validation_type import ValidationType
