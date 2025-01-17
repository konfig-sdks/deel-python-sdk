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


class PageInfoWithoutCursorNew(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "items_per_page",
            "offset",
            "total_rows",
        }
        
        class properties:
            total_rows = schemas.NumberSchema
            
            
            class items_per_page(
                schemas.NumberSchema
            ):
                pass
            
            
            class offset(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "total_rows": total_rows,
                "items_per_page": items_per_page,
                "offset": offset,
            }
    
    items_per_page: MetaOapg.properties.items_per_page
    offset: MetaOapg.properties.offset
    total_rows: MetaOapg.properties.total_rows
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_rows"]) -> MetaOapg.properties.total_rows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items_per_page"]) -> MetaOapg.properties.items_per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_rows", "items_per_page", "offset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_rows"]) -> MetaOapg.properties.total_rows: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items_per_page"]) -> MetaOapg.properties.items_per_page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_rows", "items_per_page", "offset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        items_per_page: typing.Union[MetaOapg.properties.items_per_page, decimal.Decimal, int, float, ],
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, float, ],
        total_rows: typing.Union[MetaOapg.properties.total_rows, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageInfoWithoutCursorNew':
        return super().__new__(
            cls,
            *args,
            items_per_page=items_per_page,
            offset=offset,
            total_rows=total_rows,
            _configuration=_configuration,
            **kwargs,
        )
