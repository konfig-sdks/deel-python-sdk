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


class EorEmployeeCostCalculationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            salary = schemas.StrSchema
            currency = schemas.StrSchema
            country = schemas.StrSchema
            country_code = schemas.StrSchema
            frequency = schemas.StrSchema
            deel_fee = schemas.StrSchema
            severance_accrual = schemas.StrSchema
            total_costs = schemas.StrSchema
            employer_costs = schemas.StrSchema
        
            @staticmethod
            def costs() -> typing.Type['EorEmployeeCostCalculationResponseCosts']:
                return EorEmployeeCostCalculationResponseCosts
        
            @staticmethod
            def additional_data() -> typing.Type['EorEmployeeCostCalculationResponseAdditionalData']:
                return EorEmployeeCostCalculationResponseAdditionalData
        
            @staticmethod
            def benefits_data() -> typing.Type['EorEmployeeCostCalculationResponseBenefitsData']:
                return EorEmployeeCostCalculationResponseBenefitsData
            __annotations__ = {
                "salary": salary,
                "currency": currency,
                "country": country,
                "country_code": country_code,
                "frequency": frequency,
                "deel_fee": deel_fee,
                "severance_accrual": severance_accrual,
                "total_costs": total_costs,
                "employer_costs": employer_costs,
                "costs": costs,
                "additional_data": additional_data,
                "benefits_data": benefits_data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary"]) -> MetaOapg.properties.salary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deel_fee"]) -> MetaOapg.properties.deel_fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severance_accrual"]) -> MetaOapg.properties.severance_accrual: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_costs"]) -> MetaOapg.properties.total_costs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer_costs"]) -> MetaOapg.properties.employer_costs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costs"]) -> 'EorEmployeeCostCalculationResponseCosts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_data"]) -> 'EorEmployeeCostCalculationResponseAdditionalData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefits_data"]) -> 'EorEmployeeCostCalculationResponseBenefitsData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["salary", "currency", "country", "country_code", "frequency", "deel_fee", "severance_accrual", "total_costs", "employer_costs", "costs", "additional_data", "benefits_data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary"]) -> typing.Union[MetaOapg.properties.salary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> typing.Union[MetaOapg.properties.country_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deel_fee"]) -> typing.Union[MetaOapg.properties.deel_fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severance_accrual"]) -> typing.Union[MetaOapg.properties.severance_accrual, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_costs"]) -> typing.Union[MetaOapg.properties.total_costs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer_costs"]) -> typing.Union[MetaOapg.properties.employer_costs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costs"]) -> typing.Union['EorEmployeeCostCalculationResponseCosts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_data"]) -> typing.Union['EorEmployeeCostCalculationResponseAdditionalData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefits_data"]) -> typing.Union['EorEmployeeCostCalculationResponseBenefitsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["salary", "currency", "country", "country_code", "frequency", "deel_fee", "severance_accrual", "total_costs", "employer_costs", "costs", "additional_data", "benefits_data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        salary: typing.Union[MetaOapg.properties.salary, str, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        country_code: typing.Union[MetaOapg.properties.country_code, str, schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, str, schemas.Unset] = schemas.unset,
        deel_fee: typing.Union[MetaOapg.properties.deel_fee, str, schemas.Unset] = schemas.unset,
        severance_accrual: typing.Union[MetaOapg.properties.severance_accrual, str, schemas.Unset] = schemas.unset,
        total_costs: typing.Union[MetaOapg.properties.total_costs, str, schemas.Unset] = schemas.unset,
        employer_costs: typing.Union[MetaOapg.properties.employer_costs, str, schemas.Unset] = schemas.unset,
        costs: typing.Union['EorEmployeeCostCalculationResponseCosts', schemas.Unset] = schemas.unset,
        additional_data: typing.Union['EorEmployeeCostCalculationResponseAdditionalData', schemas.Unset] = schemas.unset,
        benefits_data: typing.Union['EorEmployeeCostCalculationResponseBenefitsData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorEmployeeCostCalculationResponse':
        return super().__new__(
            cls,
            *args,
            salary=salary,
            currency=currency,
            country=country,
            country_code=country_code,
            frequency=frequency,
            deel_fee=deel_fee,
            severance_accrual=severance_accrual,
            total_costs=total_costs,
            employer_costs=employer_costs,
            costs=costs,
            additional_data=additional_data,
            benefits_data=benefits_data,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.eor_employee_cost_calculation_response_additional_data import EorEmployeeCostCalculationResponseAdditionalData
from deel_python_sdk.model.eor_employee_cost_calculation_response_benefits_data import EorEmployeeCostCalculationResponseBenefitsData
from deel_python_sdk.model.eor_employee_cost_calculation_response_costs import EorEmployeeCostCalculationResponseCosts