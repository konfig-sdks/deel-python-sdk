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


class UserSearchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class Resources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserResponse']:
                        return UserResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserResponse'], typing.List['UserResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Resources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserResponse':
                    return super().__getitem__(i)
            itemsPerPage = schemas.Int64Schema
        
            @staticmethod
            def schemas() -> typing.Type['UserSearchResponseSchemas']:
                return UserSearchResponseSchemas
            startIndex = schemas.Int64Schema
            totalResults = schemas.Int64Schema
            __annotations__ = {
                "Resources": Resources,
                "itemsPerPage": itemsPerPage,
                "schemas": schemas,
                "startIndex": startIndex,
                "totalResults": totalResults,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Resources"]) -> MetaOapg.properties.Resources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemsPerPage"]) -> MetaOapg.properties.itemsPerPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemas"]) -> 'UserSearchResponseSchemas': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startIndex"]) -> MetaOapg.properties.startIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalResults"]) -> MetaOapg.properties.totalResults: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Resources", "itemsPerPage", "schemas", "startIndex", "totalResults", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Resources"]) -> typing.Union[MetaOapg.properties.Resources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemsPerPage"]) -> typing.Union[MetaOapg.properties.itemsPerPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemas"]) -> typing.Union['UserSearchResponseSchemas', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startIndex"]) -> typing.Union[MetaOapg.properties.startIndex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalResults"]) -> typing.Union[MetaOapg.properties.totalResults, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Resources", "itemsPerPage", "schemas", "startIndex", "totalResults", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Resources: typing.Union[MetaOapg.properties.Resources, list, tuple, schemas.Unset] = schemas.unset,
        itemsPerPage: typing.Union[MetaOapg.properties.itemsPerPage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        schemas: typing.Union['UserSearchResponseSchemas', schemas.Unset] = schemas.unset,
        startIndex: typing.Union[MetaOapg.properties.startIndex, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalResults: typing.Union[MetaOapg.properties.totalResults, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserSearchResponse':
        return super().__new__(
            cls,
            *args,
            Resources=Resources,
            itemsPerPage=itemsPerPage,
            schemas=schemas,
            startIndex=startIndex,
            totalResults=totalResults,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.user_response import UserResponse
from deel_python_sdk.model.user_search_response_schemas import UserSearchResponseSchemas
