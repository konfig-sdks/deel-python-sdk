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


class EorEmployeeCostCalculationResponseAdditionalData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Textual notes describing important additional data regarding the employement process or costs.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def additional_notes() -> typing.Type['EorEmployeeCostCalculationResponseAdditionalDataAdditionalNotes']:
                return EorEmployeeCostCalculationResponseAdditionalDataAdditionalNotes
            __annotations__ = {
                "additional_notes": additional_notes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_notes"]) -> 'EorEmployeeCostCalculationResponseAdditionalDataAdditionalNotes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["additional_notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_notes"]) -> typing.Union['EorEmployeeCostCalculationResponseAdditionalDataAdditionalNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["additional_notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        additional_notes: typing.Union['EorEmployeeCostCalculationResponseAdditionalDataAdditionalNotes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EorEmployeeCostCalculationResponseAdditionalData':
        return super().__new__(
            cls,
            *args,
            additional_notes=additional_notes,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.eor_employee_cost_calculation_response_additional_data_additional_notes import EorEmployeeCostCalculationResponseAdditionalDataAdditionalNotes