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


class GPEmployeeCompensationUpdatedItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['GPContractSalaryStatusEnum']:
                return GPContractSalaryStatusEnum
        
            @staticmethod
            def scale() -> typing.Type['GPContractSalaryScaleEnum']:
                return GPContractSalaryScaleEnum
            salary = schemas.NumberSchema
        
            @staticmethod
            def effective_date() -> typing.Type['DateStringRequired']:
                return DateStringRequired
            __annotations__ = {
                "status": status,
                "scale": scale,
                "salary": salary,
                "effective_date": effective_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'GPContractSalaryStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> 'GPContractSalaryScaleEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary"]) -> MetaOapg.properties.salary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "scale", "salary", "effective_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['GPContractSalaryStatusEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union['GPContractSalaryScaleEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary"]) -> typing.Union[MetaOapg.properties.salary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> typing.Union['DateStringRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "scale", "salary", "effective_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union['GPContractSalaryStatusEnum', schemas.Unset] = schemas.unset,
        scale: typing.Union['GPContractSalaryScaleEnum', schemas.Unset] = schemas.unset,
        salary: typing.Union[MetaOapg.properties.salary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        effective_date: typing.Union['DateStringRequired', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GPEmployeeCompensationUpdatedItem':
        return super().__new__(
            cls,
            *args,
            status=status,
            scale=scale,
            salary=salary,
            effective_date=effective_date,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.date_string_required import DateStringRequired
from deel_python_sdk.model.gp_contract_salary_scale_enum import GPContractSalaryScaleEnum
from deel_python_sdk.model.gp_contract_salary_status_enum import GPContractSalaryStatusEnum