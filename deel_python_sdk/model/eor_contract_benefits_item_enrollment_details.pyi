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


class EORContractBenefitsItemEnrollmentDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            status = schemas.StrSchema
        
            @staticmethod
            def plan() -> typing.Type['EORContractBenefitsItemEnrollmentDetailsPlan']:
                return EORContractBenefitsItemEnrollmentDetailsPlan
        
            @staticmethod
            def standard() -> typing.Type['EORContractBenefitsItemEnrollmentDetailsStandard']:
                return EORContractBenefitsItemEnrollmentDetailsStandard
        
            @staticmethod
            def current() -> typing.Type['EORContractBenefitsItemEnrollmentDetailsCurrent']:
                return EORContractBenefitsItemEnrollmentDetailsCurrent
            __annotations__ = {
                "status": status,
                "plan": plan,
                "standard": standard,
                "current": current,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan"]) -> 'EORContractBenefitsItemEnrollmentDetailsPlan': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standard"]) -> 'EORContractBenefitsItemEnrollmentDetailsStandard': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> 'EORContractBenefitsItemEnrollmentDetailsCurrent': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "plan", "standard", "current", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> typing.Union['EORContractBenefitsItemEnrollmentDetailsPlan', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standard"]) -> typing.Union['EORContractBenefitsItemEnrollmentDetailsStandard', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> typing.Union['EORContractBenefitsItemEnrollmentDetailsCurrent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "plan", "standard", "current", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        plan: typing.Union['EORContractBenefitsItemEnrollmentDetailsPlan', schemas.Unset] = schemas.unset,
        standard: typing.Union['EORContractBenefitsItemEnrollmentDetailsStandard', schemas.Unset] = schemas.unset,
        current: typing.Union['EORContractBenefitsItemEnrollmentDetailsCurrent', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EORContractBenefitsItemEnrollmentDetails':
        return super().__new__(
            cls,
            *args,
            status=status,
            plan=plan,
            standard=standard,
            current=current,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.eor_contract_benefits_item_enrollment_details_current import EORContractBenefitsItemEnrollmentDetailsCurrent
from deel_python_sdk.model.eor_contract_benefits_item_enrollment_details_plan import EORContractBenefitsItemEnrollmentDetailsPlan
from deel_python_sdk.model.eor_contract_benefits_item_enrollment_details_standard import EORContractBenefitsItemEnrollmentDetailsStandard
