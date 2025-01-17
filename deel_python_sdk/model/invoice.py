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


class Invoice(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "contract_id",
            "due_date",
            "created_at",
            "is_overdue",
            "label",
            "issued_at",
            "vat_total",
            "paid_at",
            "total",
            "vat_id",
            "currency",
            "id",
            "vat_percentage",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['InvoiceStatusEnum']:
                return InvoiceStatusEnum
        
            @staticmethod
            def currency() -> typing.Type['CurrencyCode']:
                return CurrencyCode
        
            @staticmethod
            def created_at() -> typing.Type['DateTimeString']:
                return DateTimeString
            total = schemas.StrSchema
            label = schemas.StrSchema
        
            @staticmethod
            def paid_at() -> typing.Type['DateTimeString']:
                return DateTimeString
            
            
            class vat_total(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vat_total':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class vat_percentage(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vat_percentage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class is_overdue(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_overdue':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def issued_at() -> typing.Type['DateString']:
                return DateString
            
            
            class vat_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vat_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def due_date() -> typing.Type['DateString']:
                return DateString
        
            @staticmethod
            def contract_id() -> typing.Type['DateString']:
                return DateString
            __annotations__ = {
                "id": id,
                "status": status,
                "currency": currency,
                "created_at": created_at,
                "total": total,
                "label": label,
                "paid_at": paid_at,
                "vat_total": vat_total,
                "vat_percentage": vat_percentage,
                "is_overdue": is_overdue,
                "issued_at": issued_at,
                "vat_id": vat_id,
                "due_date": due_date,
                "contract_id": contract_id,
            }
    
    contract_id: 'DateString'
    due_date: 'DateString'
    created_at: 'DateTimeString'
    is_overdue: MetaOapg.properties.is_overdue
    label: MetaOapg.properties.label
    issued_at: 'DateString'
    vat_total: MetaOapg.properties.vat_total
    paid_at: 'DateTimeString'
    total: MetaOapg.properties.total
    vat_id: MetaOapg.properties.vat_id
    currency: 'CurrencyCode'
    id: MetaOapg.properties.id
    vat_percentage: MetaOapg.properties.vat_percentage
    status: 'InvoiceStatusEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'InvoiceStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'CurrencyCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paid_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vat_total"]) -> MetaOapg.properties.vat_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vat_percentage"]) -> MetaOapg.properties.vat_percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_overdue"]) -> MetaOapg.properties.is_overdue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issued_at"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vat_id"]) -> MetaOapg.properties.vat_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_id"]) -> 'DateString': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "status", "currency", "created_at", "total", "label", "paid_at", "vat_total", "vat_percentage", "is_overdue", "issued_at", "vat_id", "due_date", "contract_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'InvoiceStatusEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> 'CurrencyCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paid_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vat_total"]) -> MetaOapg.properties.vat_total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vat_percentage"]) -> MetaOapg.properties.vat_percentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_overdue"]) -> MetaOapg.properties.is_overdue: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issued_at"]) -> 'DateString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vat_id"]) -> MetaOapg.properties.vat_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> 'DateString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_id"]) -> 'DateString': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "status", "currency", "created_at", "total", "label", "paid_at", "vat_total", "vat_percentage", "is_overdue", "issued_at", "vat_id", "due_date", "contract_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        contract_id: 'DateString',
        due_date: 'DateString',
        created_at: 'DateTimeString',
        is_overdue: typing.Union[MetaOapg.properties.is_overdue, None, bool, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        issued_at: 'DateString',
        vat_total: typing.Union[MetaOapg.properties.vat_total, None, str, ],
        paid_at: 'DateTimeString',
        total: typing.Union[MetaOapg.properties.total, str, ],
        vat_id: typing.Union[MetaOapg.properties.vat_id, None, str, ],
        currency: 'CurrencyCode',
        id: typing.Union[MetaOapg.properties.id, str, ],
        vat_percentage: typing.Union[MetaOapg.properties.vat_percentage, None, str, ],
        status: 'InvoiceStatusEnum',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Invoice':
        return super().__new__(
            cls,
            *args,
            contract_id=contract_id,
            due_date=due_date,
            created_at=created_at,
            is_overdue=is_overdue,
            label=label,
            issued_at=issued_at,
            vat_total=vat_total,
            paid_at=paid_at,
            total=total,
            vat_id=vat_id,
            currency=currency,
            id=id,
            vat_percentage=vat_percentage,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.currency_code import CurrencyCode
from deel_python_sdk.model.date_string import DateString
from deel_python_sdk.model.date_time_string import DateTimeString
from deel_python_sdk.model.invoice_status_enum import InvoiceStatusEnum
