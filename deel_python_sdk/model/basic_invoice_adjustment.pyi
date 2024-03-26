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


class BasicInvoiceAdjustment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date_submitted",
            "quantity",
            "reviewed_by",
            "contract",
            "created_at",
            "description",
            "type",
            "currency_code",
            "payment_cycle",
            "attachment",
            "total_amount",
            "reported_by",
            "worksheet",
            "id",
            "status",
        }
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['InvoiceAdjustmentTypeEnum']:
                return InvoiceAdjustmentTypeEnum
        
            @staticmethod
            def status() -> typing.Type['InvoiceAdjustmentStatusEnum']:
                return InvoiceAdjustmentStatusEnum
            date_submitted = schemas.DateTimeSchema
        
            @staticmethod
            def currency_code() -> typing.Type['CurrencyCodeRequired']:
                return CurrencyCodeRequired
            
            
            class quantity(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'quantity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            total_amount = schemas.StrSchema
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def attachment() -> typing.Type['FileAttachmentInfo']:
                return FileAttachmentInfo
        
            @staticmethod
            def worksheet() -> typing.Type['BasicInvoiceAdjustmentWorksheet']:
                return BasicInvoiceAdjustmentWorksheet
        
            @staticmethod
            def reviewed_by() -> typing.Type['BasicInvoiceAdjustmentReviewedBy']:
                return BasicInvoiceAdjustmentReviewedBy
        
            @staticmethod
            def contract() -> typing.Type['BasicInvoiceAdjustmentContract']:
                return BasicInvoiceAdjustmentContract
        
            @staticmethod
            def payment_cycle() -> typing.Type['BasicInvoiceAdjustmentPaymentCycle']:
                return BasicInvoiceAdjustmentPaymentCycle
        
            @staticmethod
            def reported_by() -> typing.Type['BasicInvoiceAdjustmentReportedBy']:
                return BasicInvoiceAdjustmentReportedBy
            
            
            class invoice_id(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'invoice_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class scale(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scale':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class custom_scale(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_scale':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "description": description,
                "id": id,
                "type": type,
                "status": status,
                "date_submitted": date_submitted,
                "currency_code": currency_code,
                "quantity": quantity,
                "total_amount": total_amount,
                "created_at": created_at,
                "attachment": attachment,
                "worksheet": worksheet,
                "reviewed_by": reviewed_by,
                "contract": contract,
                "payment_cycle": payment_cycle,
                "reported_by": reported_by,
                "invoice_id": invoice_id,
                "scale": scale,
                "custom_scale": custom_scale,
            }
    
    date_submitted: MetaOapg.properties.date_submitted
    quantity: MetaOapg.properties.quantity
    reviewed_by: 'BasicInvoiceAdjustmentReviewedBy'
    contract: 'BasicInvoiceAdjustmentContract'
    created_at: MetaOapg.properties.created_at
    description: MetaOapg.properties.description
    type: 'InvoiceAdjustmentTypeEnum'
    currency_code: 'CurrencyCodeRequired'
    payment_cycle: 'BasicInvoiceAdjustmentPaymentCycle'
    attachment: 'FileAttachmentInfo'
    total_amount: MetaOapg.properties.total_amount
    reported_by: 'BasicInvoiceAdjustmentReportedBy'
    worksheet: 'BasicInvoiceAdjustmentWorksheet'
    id: MetaOapg.properties.id
    status: 'InvoiceAdjustmentStatusEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'InvoiceAdjustmentTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'InvoiceAdjustmentStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_submitted"]) -> MetaOapg.properties.date_submitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCodeRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment"]) -> 'FileAttachmentInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worksheet"]) -> 'BasicInvoiceAdjustmentWorksheet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewed_by"]) -> 'BasicInvoiceAdjustmentReviewedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract"]) -> 'BasicInvoiceAdjustmentContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_cycle"]) -> 'BasicInvoiceAdjustmentPaymentCycle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reported_by"]) -> 'BasicInvoiceAdjustmentReportedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoice_id"]) -> MetaOapg.properties.invoice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> MetaOapg.properties.scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_scale"]) -> MetaOapg.properties.custom_scale: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "type", "status", "date_submitted", "currency_code", "quantity", "total_amount", "created_at", "attachment", "worksheet", "reviewed_by", "contract", "payment_cycle", "reported_by", "invoice_id", "scale", "custom_scale", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'InvoiceAdjustmentTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'InvoiceAdjustmentStatusEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_submitted"]) -> MetaOapg.properties.date_submitted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCodeRequired': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment"]) -> 'FileAttachmentInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worksheet"]) -> 'BasicInvoiceAdjustmentWorksheet': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewed_by"]) -> 'BasicInvoiceAdjustmentReviewedBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract"]) -> 'BasicInvoiceAdjustmentContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_cycle"]) -> 'BasicInvoiceAdjustmentPaymentCycle': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reported_by"]) -> 'BasicInvoiceAdjustmentReportedBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoice_id"]) -> typing.Union[MetaOapg.properties.invoice_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union[MetaOapg.properties.scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_scale"]) -> typing.Union[MetaOapg.properties.custom_scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "type", "status", "date_submitted", "currency_code", "quantity", "total_amount", "created_at", "attachment", "worksheet", "reviewed_by", "contract", "payment_cycle", "reported_by", "invoice_id", "scale", "custom_scale", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_submitted: typing.Union[MetaOapg.properties.date_submitted, str, datetime, ],
        quantity: typing.Union[MetaOapg.properties.quantity, None, decimal.Decimal, int, float, ],
        reviewed_by: 'BasicInvoiceAdjustmentReviewedBy',
        contract: 'BasicInvoiceAdjustmentContract',
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        type: 'InvoiceAdjustmentTypeEnum',
        currency_code: 'CurrencyCodeRequired',
        payment_cycle: 'BasicInvoiceAdjustmentPaymentCycle',
        attachment: 'FileAttachmentInfo',
        total_amount: typing.Union[MetaOapg.properties.total_amount, str, ],
        reported_by: 'BasicInvoiceAdjustmentReportedBy',
        worksheet: 'BasicInvoiceAdjustmentWorksheet',
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: 'InvoiceAdjustmentStatusEnum',
        invoice_id: typing.Union[MetaOapg.properties.invoice_id, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scale: typing.Union[MetaOapg.properties.scale, None, str, schemas.Unset] = schemas.unset,
        custom_scale: typing.Union[MetaOapg.properties.custom_scale, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BasicInvoiceAdjustment':
        return super().__new__(
            cls,
            *args,
            date_submitted=date_submitted,
            quantity=quantity,
            reviewed_by=reviewed_by,
            contract=contract,
            created_at=created_at,
            description=description,
            type=type,
            currency_code=currency_code,
            payment_cycle=payment_cycle,
            attachment=attachment,
            total_amount=total_amount,
            reported_by=reported_by,
            worksheet=worksheet,
            id=id,
            status=status,
            invoice_id=invoice_id,
            scale=scale,
            custom_scale=custom_scale,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.basic_invoice_adjustment_contract import BasicInvoiceAdjustmentContract
from deel_python_sdk.model.basic_invoice_adjustment_payment_cycle import BasicInvoiceAdjustmentPaymentCycle
from deel_python_sdk.model.basic_invoice_adjustment_reported_by import BasicInvoiceAdjustmentReportedBy
from deel_python_sdk.model.basic_invoice_adjustment_reviewed_by import BasicInvoiceAdjustmentReviewedBy
from deel_python_sdk.model.basic_invoice_adjustment_worksheet import BasicInvoiceAdjustmentWorksheet
from deel_python_sdk.model.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.model.file_attachment_info import FileAttachmentInfo
from deel_python_sdk.model.invoice_adjustment_status_enum import InvoiceAdjustmentStatusEnum
from deel_python_sdk.model.invoice_adjustment_type_enum import InvoiceAdjustmentTypeEnum