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


class GPContractToCreateEmployee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "work_email",
            "address",
            "last_name",
            "first_name",
            "email",
        }
        
        class properties:
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
        
            @staticmethod
            def email() -> typing.Type['EmailTypeRequired']:
                return EmailTypeRequired
        
            @staticmethod
            def work_email() -> typing.Type['EmailTypeRequired']:
                return EmailTypeRequired
        
            @staticmethod
            def address() -> typing.Type['GPContractToCreateEmployeeAddress']:
                return GPContractToCreateEmployeeAddress
            nationality = schemas.StrSchema
            employee_number = schemas.StrSchema
            __annotations__ = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "work_email": work_email,
                "address": address,
                "nationality": nationality,
                "employee_number": employee_number,
            }
    
    work_email: 'EmailTypeRequired'
    address: 'GPContractToCreateEmployeeAddress'
    last_name: MetaOapg.properties.last_name
    first_name: MetaOapg.properties.first_name
    email: 'EmailTypeRequired'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> 'EmailTypeRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_email"]) -> 'EmailTypeRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'GPContractToCreateEmployeeAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_number"]) -> MetaOapg.properties.employee_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "email", "work_email", "address", "nationality", "employee_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> 'EmailTypeRequired': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_email"]) -> 'EmailTypeRequired': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> 'GPContractToCreateEmployeeAddress': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality"]) -> typing.Union[MetaOapg.properties.nationality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_number"]) -> typing.Union[MetaOapg.properties.employee_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "email", "work_email", "address", "nationality", "employee_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        work_email: 'EmailTypeRequired',
        address: 'GPContractToCreateEmployeeAddress',
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        email: 'EmailTypeRequired',
        nationality: typing.Union[MetaOapg.properties.nationality, str, schemas.Unset] = schemas.unset,
        employee_number: typing.Union[MetaOapg.properties.employee_number, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GPContractToCreateEmployee':
        return super().__new__(
            cls,
            *args,
            work_email=work_email,
            address=address,
            last_name=last_name,
            first_name=first_name,
            email=email,
            nationality=nationality,
            employee_number=employee_number,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.email_type_required import EmailTypeRequired
from deel_python_sdk.model.gp_contract_to_create_employee_address import GPContractToCreateEmployeeAddress
