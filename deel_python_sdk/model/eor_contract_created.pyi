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


class EorContractCreated(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['ContractTypeEnum']:
                return ContractTypeEnum
        
            @staticmethod
            def created_at() -> typing.Type['DateTimeString']:
                return DateTimeString
        
            @staticmethod
            def status() -> typing.Type['ContractStatusEnum']:
                return ContractStatusEnum
            job_title = schemas.StrSchema
        
            @staticmethod
            def employment() -> typing.Type['EorContractCreatedEmployment']:
                return EorContractCreatedEmployment
        
            @staticmethod
            def client() -> typing.Type['EorContractCreatedClient']:
                return EorContractCreatedClient
        
            @staticmethod
            def compensation_details() -> typing.Type['EorContractCreatedCompensationDetails']:
                return EorContractCreatedCompensationDetails
        
            @staticmethod
            def employee() -> typing.Type['EorContractCreatedEmployee']:
                return EorContractCreatedEmployee
        
            @staticmethod
            def health_plan() -> typing.Type['EorContractCreatedHealthPlan']:
                return EorContractCreatedHealthPlan
        
            @staticmethod
            def seniority() -> typing.Type['Seniority']:
                return Seniority
            __annotations__ = {
                "id": id,
                "type": type,
                "created_at": created_at,
                "status": status,
                "job_title": job_title,
                "employment": employment,
                "client": client,
                "compensation_details": compensation_details,
                "employee": employee,
                "health_plan": health_plan,
                "seniority": seniority,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ContractTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ContractStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment"]) -> 'EorContractCreatedEmployment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'EorContractCreatedClient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensation_details"]) -> 'EorContractCreatedCompensationDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'EorContractCreatedEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["health_plan"]) -> 'EorContractCreatedHealthPlan': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seniority"]) -> 'Seniority': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "created_at", "status", "job_title", "employment", "client", "compensation_details", "employee", "health_plan", "seniority", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['ContractTypeEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union['DateTimeString', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['ContractStatusEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title"]) -> typing.Union[MetaOapg.properties.job_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment"]) -> typing.Union['EorContractCreatedEmployment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> typing.Union['EorContractCreatedClient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensation_details"]) -> typing.Union['EorContractCreatedCompensationDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['EorContractCreatedEmployee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["health_plan"]) -> typing.Union['EorContractCreatedHealthPlan', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seniority"]) -> typing.Union['Seniority', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "created_at", "status", "job_title", "employment", "client", "compensation_details", "employee", "health_plan", "seniority", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union['ContractTypeEnum', schemas.Unset] = schemas.unset,
        created_at: typing.Union['DateTimeString', schemas.Unset] = schemas.unset,
        status: typing.Union['ContractStatusEnum', schemas.Unset] = schemas.unset,
        job_title: typing.Union[MetaOapg.properties.job_title, str, schemas.Unset] = schemas.unset,
        employment: typing.Union['EorContractCreatedEmployment', schemas.Unset] = schemas.unset,
        client: typing.Union['EorContractCreatedClient', schemas.Unset] = schemas.unset,
        compensation_details: typing.Union['EorContractCreatedCompensationDetails', schemas.Unset] = schemas.unset,
        employee: typing.Union['EorContractCreatedEmployee', schemas.Unset] = schemas.unset,
        health_plan: typing.Union['EorContractCreatedHealthPlan', schemas.Unset] = schemas.unset,
        seniority: typing.Union['Seniority', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorContractCreated':
        return super().__new__(
            cls,
            *args,
            id=id,
            type=type,
            created_at=created_at,
            status=status,
            job_title=job_title,
            employment=employment,
            client=client,
            compensation_details=compensation_details,
            employee=employee,
            health_plan=health_plan,
            seniority=seniority,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.contract_status_enum import ContractStatusEnum
from deel_python_sdk.model.contract_type_enum import ContractTypeEnum
from deel_python_sdk.model.date_time_string import DateTimeString
from deel_python_sdk.model.eor_contract_created_client import EorContractCreatedClient
from deel_python_sdk.model.eor_contract_created_compensation_details import EorContractCreatedCompensationDetails
from deel_python_sdk.model.eor_contract_created_employee import EorContractCreatedEmployee
from deel_python_sdk.model.eor_contract_created_employment import EorContractCreatedEmployment
from deel_python_sdk.model.eor_contract_created_health_plan import EorContractCreatedHealthPlan
from deel_python_sdk.model.seniority import Seniority
