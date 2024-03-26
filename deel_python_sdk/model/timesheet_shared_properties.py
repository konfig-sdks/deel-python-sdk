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


class TimesheetSharedProperties(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the timesheet to create. Both a client or a contractor may create a timesheet.
    """


    class MetaOapg:
        required = {
            "date_submitted",
            "quantity",
            "contract_id",
            "description",
        }
        
        class properties:
            description = schemas.StrSchema
            contract_id = schemas.StrSchema
        
            @staticmethod
            def date_submitted() -> typing.Type['DateStringRequired']:
                return DateStringRequired
            
            
            class quantity(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.01
            __annotations__ = {
                "description": description,
                "contract_id": contract_id,
                "date_submitted": date_submitted,
                "quantity": quantity,
            }
    
    date_submitted: 'DateStringRequired'
    quantity: MetaOapg.properties.quantity
    contract_id: MetaOapg.properties.contract_id
    description: MetaOapg.properties.description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_id"]) -> MetaOapg.properties.contract_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_submitted"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "contract_id", "date_submitted", "quantity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_id"]) -> MetaOapg.properties.contract_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_submitted"]) -> 'DateStringRequired': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "contract_id", "date_submitted", "quantity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_submitted: 'DateStringRequired',
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, float, ],
        contract_id: typing.Union[MetaOapg.properties.contract_id, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimesheetSharedProperties':
        return super().__new__(
            cls,
            *args,
            date_submitted=date_submitted,
            quantity=quantity,
            contract_id=contract_id,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.date_string_required import DateStringRequired
