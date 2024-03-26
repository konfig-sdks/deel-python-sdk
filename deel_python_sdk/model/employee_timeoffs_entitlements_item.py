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


class EmployeeTimeoffsEntitlementsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "vacation_requested",
            "sick_leave_allowed",
            "other_leave_approved",
            "year",
            "vacation_approved",
            "vacation_rollover",
            "sick_leave_total",
            "sick_leave_used",
            "vacation_used",
            "other_leave_total",
            "other_leave_requested",
            "sick_leave_approved",
            "vacation_allowed",
            "vacation_total",
            "sick_leave_requested",
            "tracking_period",
            "vacation_payout",
            "other_leave_used",
            "vacation_expired",
        }
        
        class properties:
            year = schemas.NumberSchema
            tracking_period = schemas.StrSchema
            vacation_allowed = schemas.StrSchema
            vacation_rollover = schemas.StrSchema
            vacation_expired = schemas.StrSchema
            vacation_payout = schemas.StrSchema
            vacation_requested = schemas.StrSchema
            vacation_approved = schemas.StrSchema
            vacation_used = schemas.StrSchema
            vacation_total = schemas.StrSchema
            sick_leave_requested = schemas.StrSchema
            sick_leave_approved = schemas.StrSchema
            sick_leave_used = schemas.StrSchema
            sick_leave_total = schemas.StrSchema
            sick_leave_allowed = schemas.StrSchema
            other_leave_requested = schemas.StrSchema
            other_leave_approved = schemas.StrSchema
            other_leave_used = schemas.StrSchema
            other_leave_total = schemas.StrSchema
            __annotations__ = {
                "year": year,
                "tracking_period": tracking_period,
                "vacation_allowed": vacation_allowed,
                "vacation_rollover": vacation_rollover,
                "vacation_expired": vacation_expired,
                "vacation_payout": vacation_payout,
                "vacation_requested": vacation_requested,
                "vacation_approved": vacation_approved,
                "vacation_used": vacation_used,
                "vacation_total": vacation_total,
                "sick_leave_requested": sick_leave_requested,
                "sick_leave_approved": sick_leave_approved,
                "sick_leave_used": sick_leave_used,
                "sick_leave_total": sick_leave_total,
                "sick_leave_allowed": sick_leave_allowed,
                "other_leave_requested": other_leave_requested,
                "other_leave_approved": other_leave_approved,
                "other_leave_used": other_leave_used,
                "other_leave_total": other_leave_total,
            }
    
    vacation_requested: MetaOapg.properties.vacation_requested
    sick_leave_allowed: MetaOapg.properties.sick_leave_allowed
    other_leave_approved: MetaOapg.properties.other_leave_approved
    year: MetaOapg.properties.year
    vacation_approved: MetaOapg.properties.vacation_approved
    vacation_rollover: MetaOapg.properties.vacation_rollover
    sick_leave_total: MetaOapg.properties.sick_leave_total
    sick_leave_used: MetaOapg.properties.sick_leave_used
    vacation_used: MetaOapg.properties.vacation_used
    other_leave_total: MetaOapg.properties.other_leave_total
    other_leave_requested: MetaOapg.properties.other_leave_requested
    sick_leave_approved: MetaOapg.properties.sick_leave_approved
    vacation_allowed: MetaOapg.properties.vacation_allowed
    vacation_total: MetaOapg.properties.vacation_total
    sick_leave_requested: MetaOapg.properties.sick_leave_requested
    tracking_period: MetaOapg.properties.tracking_period
    vacation_payout: MetaOapg.properties.vacation_payout
    other_leave_used: MetaOapg.properties.other_leave_used
    vacation_expired: MetaOapg.properties.vacation_expired
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tracking_period"]) -> MetaOapg.properties.tracking_period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_allowed"]) -> MetaOapg.properties.vacation_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_rollover"]) -> MetaOapg.properties.vacation_rollover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_expired"]) -> MetaOapg.properties.vacation_expired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_payout"]) -> MetaOapg.properties.vacation_payout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_requested"]) -> MetaOapg.properties.vacation_requested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_approved"]) -> MetaOapg.properties.vacation_approved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_used"]) -> MetaOapg.properties.vacation_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacation_total"]) -> MetaOapg.properties.vacation_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sick_leave_requested"]) -> MetaOapg.properties.sick_leave_requested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sick_leave_approved"]) -> MetaOapg.properties.sick_leave_approved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sick_leave_used"]) -> MetaOapg.properties.sick_leave_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sick_leave_total"]) -> MetaOapg.properties.sick_leave_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sick_leave_allowed"]) -> MetaOapg.properties.sick_leave_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_leave_requested"]) -> MetaOapg.properties.other_leave_requested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_leave_approved"]) -> MetaOapg.properties.other_leave_approved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_leave_used"]) -> MetaOapg.properties.other_leave_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_leave_total"]) -> MetaOapg.properties.other_leave_total: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["year", "tracking_period", "vacation_allowed", "vacation_rollover", "vacation_expired", "vacation_payout", "vacation_requested", "vacation_approved", "vacation_used", "vacation_total", "sick_leave_requested", "sick_leave_approved", "sick_leave_used", "sick_leave_total", "sick_leave_allowed", "other_leave_requested", "other_leave_approved", "other_leave_used", "other_leave_total", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tracking_period"]) -> MetaOapg.properties.tracking_period: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_allowed"]) -> MetaOapg.properties.vacation_allowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_rollover"]) -> MetaOapg.properties.vacation_rollover: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_expired"]) -> MetaOapg.properties.vacation_expired: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_payout"]) -> MetaOapg.properties.vacation_payout: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_requested"]) -> MetaOapg.properties.vacation_requested: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_approved"]) -> MetaOapg.properties.vacation_approved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_used"]) -> MetaOapg.properties.vacation_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacation_total"]) -> MetaOapg.properties.vacation_total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sick_leave_requested"]) -> MetaOapg.properties.sick_leave_requested: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sick_leave_approved"]) -> MetaOapg.properties.sick_leave_approved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sick_leave_used"]) -> MetaOapg.properties.sick_leave_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sick_leave_total"]) -> MetaOapg.properties.sick_leave_total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sick_leave_allowed"]) -> MetaOapg.properties.sick_leave_allowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_leave_requested"]) -> MetaOapg.properties.other_leave_requested: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_leave_approved"]) -> MetaOapg.properties.other_leave_approved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_leave_used"]) -> MetaOapg.properties.other_leave_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_leave_total"]) -> MetaOapg.properties.other_leave_total: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["year", "tracking_period", "vacation_allowed", "vacation_rollover", "vacation_expired", "vacation_payout", "vacation_requested", "vacation_approved", "vacation_used", "vacation_total", "sick_leave_requested", "sick_leave_approved", "sick_leave_used", "sick_leave_total", "sick_leave_allowed", "other_leave_requested", "other_leave_approved", "other_leave_used", "other_leave_total", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vacation_requested: typing.Union[MetaOapg.properties.vacation_requested, str, ],
        sick_leave_allowed: typing.Union[MetaOapg.properties.sick_leave_allowed, str, ],
        other_leave_approved: typing.Union[MetaOapg.properties.other_leave_approved, str, ],
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, float, ],
        vacation_approved: typing.Union[MetaOapg.properties.vacation_approved, str, ],
        vacation_rollover: typing.Union[MetaOapg.properties.vacation_rollover, str, ],
        sick_leave_total: typing.Union[MetaOapg.properties.sick_leave_total, str, ],
        sick_leave_used: typing.Union[MetaOapg.properties.sick_leave_used, str, ],
        vacation_used: typing.Union[MetaOapg.properties.vacation_used, str, ],
        other_leave_total: typing.Union[MetaOapg.properties.other_leave_total, str, ],
        other_leave_requested: typing.Union[MetaOapg.properties.other_leave_requested, str, ],
        sick_leave_approved: typing.Union[MetaOapg.properties.sick_leave_approved, str, ],
        vacation_allowed: typing.Union[MetaOapg.properties.vacation_allowed, str, ],
        vacation_total: typing.Union[MetaOapg.properties.vacation_total, str, ],
        sick_leave_requested: typing.Union[MetaOapg.properties.sick_leave_requested, str, ],
        tracking_period: typing.Union[MetaOapg.properties.tracking_period, str, ],
        vacation_payout: typing.Union[MetaOapg.properties.vacation_payout, str, ],
        other_leave_used: typing.Union[MetaOapg.properties.other_leave_used, str, ],
        vacation_expired: typing.Union[MetaOapg.properties.vacation_expired, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeTimeoffsEntitlementsItem':
        return super().__new__(
            cls,
            *args,
            vacation_requested=vacation_requested,
            sick_leave_allowed=sick_leave_allowed,
            other_leave_approved=other_leave_approved,
            year=year,
            vacation_approved=vacation_approved,
            vacation_rollover=vacation_rollover,
            sick_leave_total=sick_leave_total,
            sick_leave_used=sick_leave_used,
            vacation_used=vacation_used,
            other_leave_total=other_leave_total,
            other_leave_requested=other_leave_requested,
            sick_leave_approved=sick_leave_approved,
            vacation_allowed=vacation_allowed,
            vacation_total=vacation_total,
            sick_leave_requested=sick_leave_requested,
            tracking_period=tracking_period,
            vacation_payout=vacation_payout,
            other_leave_used=other_leave_used,
            vacation_expired=vacation_expired,
            _configuration=_configuration,
            **kwargs,
        )