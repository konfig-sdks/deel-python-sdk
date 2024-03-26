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


class BasicTimesheet(
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
            type = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['TimesheetStatusEnum']:
                return TimesheetStatusEnum
            date_submitted = schemas.DateTimeSchema
        
            @staticmethod
            def currency_code() -> typing.Type['CurrencyCodeRequired']:
                return CurrencyCodeRequired
            total_amount = schemas.StrSchema
            
            
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
            created_at = schemas.StrSchema
        
            @staticmethod
            def attachment() -> typing.Type['FileAttachmentInfo']:
                return FileAttachmentInfo
        
            @staticmethod
            def worksheet() -> typing.Type['BasicTimesheetWorksheet']:
                return BasicTimesheetWorksheet
        
            @staticmethod
            def reviewed_by() -> typing.Type['BasicTimesheetReviewedBy']:
                return BasicTimesheetReviewedBy
        
            @staticmethod
            def contract() -> typing.Type['BasicTimesheetContract']:
                return BasicTimesheetContract
        
            @staticmethod
            def reported_by() -> typing.Type['BasicTimesheetReportedBy']:
                return BasicTimesheetReportedBy
            
            
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
        
            @staticmethod
            def payment_cycle() -> typing.Type['BasicTimesheetPaymentCycle']:
                return BasicTimesheetPaymentCycle
            __annotations__ = {
                "description": description,
                "id": id,
                "type": type,
                "status": status,
                "date_submitted": date_submitted,
                "currency_code": currency_code,
                "total_amount": total_amount,
                "quantity": quantity,
                "created_at": created_at,
                "attachment": attachment,
                "worksheet": worksheet,
                "reviewed_by": reviewed_by,
                "contract": contract,
                "reported_by": reported_by,
                "scale": scale,
                "custom_scale": custom_scale,
                "payment_cycle": payment_cycle,
            }
    
    date_submitted: MetaOapg.properties.date_submitted
    quantity: MetaOapg.properties.quantity
    reviewed_by: 'BasicTimesheetReviewedBy'
    contract: 'BasicTimesheetContract'
    created_at: MetaOapg.properties.created_at
    description: MetaOapg.properties.description
    type: MetaOapg.properties.type
    currency_code: 'CurrencyCodeRequired'
    attachment: 'FileAttachmentInfo'
    total_amount: MetaOapg.properties.total_amount
    reported_by: 'BasicTimesheetReportedBy'
    worksheet: 'BasicTimesheetWorksheet'
    id: MetaOapg.properties.id
    status: 'TimesheetStatusEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'TimesheetStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_submitted"]) -> MetaOapg.properties.date_submitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCodeRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment"]) -> 'FileAttachmentInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worksheet"]) -> 'BasicTimesheetWorksheet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewed_by"]) -> 'BasicTimesheetReviewedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract"]) -> 'BasicTimesheetContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reported_by"]) -> 'BasicTimesheetReportedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> MetaOapg.properties.scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_scale"]) -> MetaOapg.properties.custom_scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_cycle"]) -> 'BasicTimesheetPaymentCycle': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "type", "status", "date_submitted", "currency_code", "total_amount", "quantity", "created_at", "attachment", "worksheet", "reviewed_by", "contract", "reported_by", "scale", "custom_scale", "payment_cycle", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'TimesheetStatusEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_submitted"]) -> MetaOapg.properties.date_submitted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCodeRequired': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment"]) -> 'FileAttachmentInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worksheet"]) -> 'BasicTimesheetWorksheet': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewed_by"]) -> 'BasicTimesheetReviewedBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract"]) -> 'BasicTimesheetContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reported_by"]) -> 'BasicTimesheetReportedBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union[MetaOapg.properties.scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_scale"]) -> typing.Union[MetaOapg.properties.custom_scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_cycle"]) -> typing.Union['BasicTimesheetPaymentCycle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "type", "status", "date_submitted", "currency_code", "total_amount", "quantity", "created_at", "attachment", "worksheet", "reviewed_by", "contract", "reported_by", "scale", "custom_scale", "payment_cycle", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_submitted: typing.Union[MetaOapg.properties.date_submitted, str, datetime, ],
        quantity: typing.Union[MetaOapg.properties.quantity, None, decimal.Decimal, int, float, ],
        reviewed_by: 'BasicTimesheetReviewedBy',
        contract: 'BasicTimesheetContract',
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        currency_code: 'CurrencyCodeRequired',
        attachment: 'FileAttachmentInfo',
        total_amount: typing.Union[MetaOapg.properties.total_amount, str, ],
        reported_by: 'BasicTimesheetReportedBy',
        worksheet: 'BasicTimesheetWorksheet',
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: 'TimesheetStatusEnum',
        scale: typing.Union[MetaOapg.properties.scale, None, str, schemas.Unset] = schemas.unset,
        custom_scale: typing.Union[MetaOapg.properties.custom_scale, None, str, schemas.Unset] = schemas.unset,
        payment_cycle: typing.Union['BasicTimesheetPaymentCycle', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BasicTimesheet':
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
            attachment=attachment,
            total_amount=total_amount,
            reported_by=reported_by,
            worksheet=worksheet,
            id=id,
            status=status,
            scale=scale,
            custom_scale=custom_scale,
            payment_cycle=payment_cycle,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.basic_timesheet_contract import BasicTimesheetContract
from deel_python_sdk.model.basic_timesheet_payment_cycle import BasicTimesheetPaymentCycle
from deel_python_sdk.model.basic_timesheet_reported_by import BasicTimesheetReportedBy
from deel_python_sdk.model.basic_timesheet_reviewed_by import BasicTimesheetReviewedBy
from deel_python_sdk.model.basic_timesheet_worksheet import BasicTimesheetWorksheet
from deel_python_sdk.model.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.model.file_attachment_info import FileAttachmentInfo
from deel_python_sdk.model.timesheet_status_enum import TimesheetStatusEnum