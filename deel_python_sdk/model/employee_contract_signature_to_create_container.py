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


class EmployeeContractSignatureToCreateContainer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "data",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['EmployeeContractSignatureToCreate']:
                return EmployeeContractSignatureToCreate
            __annotations__ = {
                "data": data,
            }
    
    data: 'EmployeeContractSignatureToCreate'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'EmployeeContractSignatureToCreate': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'EmployeeContractSignatureToCreate': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: 'EmployeeContractSignatureToCreate',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeContractSignatureToCreateContainer':
        return super().__new__(
            cls,
            *args,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.employee_contract_signature_to_create import EmployeeContractSignatureToCreate
