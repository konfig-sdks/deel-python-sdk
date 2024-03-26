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


class ContractDetailsToAmend(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    You can specify any combination of data points that need changing.
    """


    class MetaOapg:
        
        class properties:
            
            
            class amount(
                schemas.NumberSchema
            ):
                pass
        
            @staticmethod
            def currency_code() -> typing.Type['CurrencyCodeRequired']:
                return CurrencyCodeRequired
        
            @staticmethod
            def scale() -> typing.Type['WorkStatementScaleEnum']:
                return WorkStatementScaleEnum
        
            @staticmethod
            def effective_date() -> typing.Type['DateStringRequired']:
                return DateStringRequired
        
            @staticmethod
            def first_payment_date() -> typing.Type['DateStringRequired']:
                return DateStringRequired
            
            
            class first_payment(
                schemas.NumberSchema
            ):
                pass
        
            @staticmethod
            def frequency() -> typing.Type['WorkStatementCycleScaleEnum']:
                return WorkStatementCycleScaleEnum
            
            
            class cycle_end(
                schemas.NumberSchema
            ):
                pass
        
            @staticmethod
            def cycle_end_type() -> typing.Type['WorkStatementCycleEndTypeEnum']:
                return WorkStatementCycleEndTypeEnum
        
            @staticmethod
            def payment_due_type() -> typing.Type['WorkStatementPaymentDueTypeEnum']:
                return WorkStatementPaymentDueTypeEnum
            
            
            class payment_due_days(
                schemas.NumberSchema
            ):
                pass
            pay_before_weekends = schemas.BoolSchema
            job_title_name = schemas.StrSchema
            job_title_id = schemas.StrSchema
            seniority_id = schemas.StrSchema
            special_clause = schemas.StrSchema
            scope_of_work = schemas.StrSchema
            __annotations__ = {
                "amount": amount,
                "currency_code": currency_code,
                "scale": scale,
                "effective_date": effective_date,
                "first_payment_date": first_payment_date,
                "first_payment": first_payment,
                "frequency": frequency,
                "cycle_end": cycle_end,
                "cycle_end_type": cycle_end_type,
                "payment_due_type": payment_due_type,
                "payment_due_days": payment_due_days,
                "pay_before_weekends": pay_before_weekends,
                "job_title_name": job_title_name,
                "job_title_id": job_title_id,
                "seniority_id": seniority_id,
                "special_clause": special_clause,
                "scope_of_work": scope_of_work,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCodeRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> 'WorkStatementScaleEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_payment_date"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_payment"]) -> MetaOapg.properties.first_payment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> 'WorkStatementCycleScaleEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cycle_end"]) -> MetaOapg.properties.cycle_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cycle_end_type"]) -> 'WorkStatementCycleEndTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_due_type"]) -> 'WorkStatementPaymentDueTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_due_days"]) -> MetaOapg.properties.payment_due_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_before_weekends"]) -> MetaOapg.properties.pay_before_weekends: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title_name"]) -> MetaOapg.properties.job_title_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title_id"]) -> MetaOapg.properties.job_title_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seniority_id"]) -> MetaOapg.properties.seniority_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["special_clause"]) -> MetaOapg.properties.special_clause: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope_of_work"]) -> MetaOapg.properties.scope_of_work: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "currency_code", "scale", "effective_date", "first_payment_date", "first_payment", "frequency", "cycle_end", "cycle_end_type", "payment_due_type", "payment_due_days", "pay_before_weekends", "job_title_name", "job_title_id", "seniority_id", "special_clause", "scope_of_work", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union['CurrencyCodeRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union['WorkStatementScaleEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> typing.Union['DateStringRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_payment_date"]) -> typing.Union['DateStringRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_payment"]) -> typing.Union[MetaOapg.properties.first_payment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union['WorkStatementCycleScaleEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cycle_end"]) -> typing.Union[MetaOapg.properties.cycle_end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cycle_end_type"]) -> typing.Union['WorkStatementCycleEndTypeEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_due_type"]) -> typing.Union['WorkStatementPaymentDueTypeEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_due_days"]) -> typing.Union[MetaOapg.properties.payment_due_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_before_weekends"]) -> typing.Union[MetaOapg.properties.pay_before_weekends, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title_name"]) -> typing.Union[MetaOapg.properties.job_title_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title_id"]) -> typing.Union[MetaOapg.properties.job_title_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seniority_id"]) -> typing.Union[MetaOapg.properties.seniority_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["special_clause"]) -> typing.Union[MetaOapg.properties.special_clause, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope_of_work"]) -> typing.Union[MetaOapg.properties.scope_of_work, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "currency_code", "scale", "effective_date", "first_payment_date", "first_payment", "frequency", "cycle_end", "cycle_end_type", "payment_due_type", "payment_due_days", "pay_before_weekends", "job_title_name", "job_title_id", "seniority_id", "special_clause", "scope_of_work", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currency_code: typing.Union['CurrencyCodeRequired', schemas.Unset] = schemas.unset,
        scale: typing.Union['WorkStatementScaleEnum', schemas.Unset] = schemas.unset,
        effective_date: typing.Union['DateStringRequired', schemas.Unset] = schemas.unset,
        first_payment_date: typing.Union['DateStringRequired', schemas.Unset] = schemas.unset,
        first_payment: typing.Union[MetaOapg.properties.first_payment, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        frequency: typing.Union['WorkStatementCycleScaleEnum', schemas.Unset] = schemas.unset,
        cycle_end: typing.Union[MetaOapg.properties.cycle_end, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cycle_end_type: typing.Union['WorkStatementCycleEndTypeEnum', schemas.Unset] = schemas.unset,
        payment_due_type: typing.Union['WorkStatementPaymentDueTypeEnum', schemas.Unset] = schemas.unset,
        payment_due_days: typing.Union[MetaOapg.properties.payment_due_days, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pay_before_weekends: typing.Union[MetaOapg.properties.pay_before_weekends, bool, schemas.Unset] = schemas.unset,
        job_title_name: typing.Union[MetaOapg.properties.job_title_name, str, schemas.Unset] = schemas.unset,
        job_title_id: typing.Union[MetaOapg.properties.job_title_id, str, schemas.Unset] = schemas.unset,
        seniority_id: typing.Union[MetaOapg.properties.seniority_id, str, schemas.Unset] = schemas.unset,
        special_clause: typing.Union[MetaOapg.properties.special_clause, str, schemas.Unset] = schemas.unset,
        scope_of_work: typing.Union[MetaOapg.properties.scope_of_work, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractDetailsToAmend':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            currency_code=currency_code,
            scale=scale,
            effective_date=effective_date,
            first_payment_date=first_payment_date,
            first_payment=first_payment,
            frequency=frequency,
            cycle_end=cycle_end,
            cycle_end_type=cycle_end_type,
            payment_due_type=payment_due_type,
            payment_due_days=payment_due_days,
            pay_before_weekends=pay_before_weekends,
            job_title_name=job_title_name,
            job_title_id=job_title_id,
            seniority_id=seniority_id,
            special_clause=special_clause,
            scope_of_work=scope_of_work,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.model.date_string_required import DateStringRequired
from deel_python_sdk.model.work_statement_cycle_end_type_enum import WorkStatementCycleEndTypeEnum
from deel_python_sdk.model.work_statement_cycle_scale_enum import WorkStatementCycleScaleEnum
from deel_python_sdk.model.work_statement_payment_due_type_enum import WorkStatementPaymentDueTypeEnum
from deel_python_sdk.model.work_statement_scale_enum import WorkStatementScaleEnum
