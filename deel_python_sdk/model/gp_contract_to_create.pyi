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


class GPContractToCreate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "client",
            "compensation_details",
            "employment",
            "employee",
            "job_title",
        }
        
        class properties:
        
            @staticmethod
            def employee() -> typing.Type['GPContractToCreateEmployee']:
                return GPContractToCreateEmployee
        
            @staticmethod
            def employment() -> typing.Type['GPContractToCreateEmployment']:
                return GPContractToCreateEmployment
            job_title = schemas.StrSchema
        
            @staticmethod
            def client() -> typing.Type['GPClient']:
                return GPClient
        
            @staticmethod
            def compensation_details() -> typing.Type['GPContractToCreateCompensationDetails']:
                return GPContractToCreateCompensationDetails
            __annotations__ = {
                "employee": employee,
                "employment": employment,
                "job_title": job_title,
                "client": client,
                "compensation_details": compensation_details,
            }
    
    client: 'GPClient'
    compensation_details: 'GPContractToCreateCompensationDetails'
    employment: 'GPContractToCreateEmployment'
    employee: 'GPContractToCreateEmployee'
    job_title: MetaOapg.properties.job_title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'GPContractToCreateEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment"]) -> 'GPContractToCreateEmployment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'GPClient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensation_details"]) -> 'GPContractToCreateCompensationDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employee", "employment", "job_title", "client", "compensation_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> 'GPContractToCreateEmployee': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment"]) -> 'GPContractToCreateEmployment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> 'GPClient': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensation_details"]) -> 'GPContractToCreateCompensationDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employee", "employment", "job_title", "client", "compensation_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        client: 'GPClient',
        compensation_details: 'GPContractToCreateCompensationDetails',
        employment: 'GPContractToCreateEmployment',
        employee: 'GPContractToCreateEmployee',
        job_title: typing.Union[MetaOapg.properties.job_title, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GPContractToCreate':
        return super().__new__(
            cls,
            *args,
            client=client,
            compensation_details=compensation_details,
            employment=employment,
            employee=employee,
            job_title=job_title,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.gp_client import GPClient
from deel_python_sdk.model.gp_contract_to_create_compensation_details import GPContractToCreateCompensationDetails
from deel_python_sdk.model.gp_contract_to_create_employee import GPContractToCreateEmployee
from deel_python_sdk.model.gp_contract_to_create_employment import GPContractToCreateEmployment
