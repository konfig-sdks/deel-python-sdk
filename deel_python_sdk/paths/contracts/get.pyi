# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from deel_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from deel_python_sdk.api_response import AsyncGeneratorResponse
from deel_python_sdk import api_client, exceptions
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

from deel_python_sdk.model.api_error_container import ApiErrorContainer as ApiErrorContainerSchema
from deel_python_sdk.model.currency_code_required import CurrencyCodeRequired as CurrencyCodeRequiredSchema
from deel_python_sdk.model.sort_dir_enum import SortDirEnum as SortDirEnumSchema
from deel_python_sdk.model.contract_list_container import ContractListContainer as ContractListContainerSchema
from deel_python_sdk.model.contract_status_enum_list import ContractStatusEnumList as ContractStatusEnumListSchema
from deel_python_sdk.model.contracts_sort_by_enum import ContractsSortByEnum as ContractsSortByEnumSchema
from deel_python_sdk.model.country_code_list import CountryCodeList as CountryCodeListSchema
from deel_python_sdk.model.currency_code_list import CurrencyCodeList as CurrencyCodeListSchema
from deel_python_sdk.model.contract_type_enum_list import ContractTypeEnumList as ContractTypeEnumListSchema

from deel_python_sdk.type.contracts_sort_by_enum import ContractsSortByEnum
from deel_python_sdk.type.currency_code_required import CurrencyCodeRequired
from deel_python_sdk.type.sort_dir_enum import SortDirEnum
from deel_python_sdk.type.currency_code_list import CurrencyCodeList
from deel_python_sdk.type.api_error_container import ApiErrorContainer
from deel_python_sdk.type.contract_type_enum_list import ContractTypeEnumList
from deel_python_sdk.type.country_code_list import CountryCodeList
from deel_python_sdk.type.contract_list_container import ContractListContainer
from deel_python_sdk.type.contract_status_enum_list import ContractStatusEnumList

from ...api_client import Dictionary
from deel_python_sdk.pydantic.country_code_list import CountryCodeList as CountryCodeListPydantic
from deel_python_sdk.pydantic.contracts_sort_by_enum import ContractsSortByEnum as ContractsSortByEnumPydantic
from deel_python_sdk.pydantic.contract_list_container import ContractListContainer as ContractListContainerPydantic
from deel_python_sdk.pydantic.contract_status_enum_list import ContractStatusEnumList as ContractStatusEnumListPydantic
from deel_python_sdk.pydantic.contract_type_enum_list import ContractTypeEnumList as ContractTypeEnumListPydantic
from deel_python_sdk.pydantic.sort_dir_enum import SortDirEnum as SortDirEnumPydantic
from deel_python_sdk.pydantic.currency_code_list import CurrencyCodeList as CurrencyCodeListPydantic
from deel_python_sdk.pydantic.currency_code_required import CurrencyCodeRequired as CurrencyCodeRequiredPydantic
from deel_python_sdk.pydantic.api_error_container import ApiErrorContainer as ApiErrorContainerPydantic

# Query params
AfterCursorSchema = schemas.StrSchema


class LimitSchema(
    schemas.NumberSchema
):
    pass
OrderDirectionSchema = SortDirEnumSchema
TypesSchema = ContractTypeEnumListSchema
StatusesSchema = ContractStatusEnumListSchema
TeamIdSchema = schemas.StrSchema
ExternalIdSchema = schemas.StrSchema
CountriesSchema = CountryCodeListSchema


class CurrenciesSchema(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                CurrencyCodeListSchema,
                ,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CurrenciesSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
SearchSchema = schemas.StrSchema
SortBySchema = ContractsSortByEnumSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'after_cursor': typing.Union[AfterCursorSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, float, ],
        'order_direction': typing.Union[OrderDirectionSchema, ],
        'types': typing.Union[TypesSchema, ],
        'statuses': typing.Union[StatusesSchema, ],
        'team_id': typing.Union[TeamIdSchema, str, ],
        'external_id': typing.Union[ExternalIdSchema, str, ],
        'countries': typing.Union[CountriesSchema, ],
        'currencies': typing.Union[CurrenciesSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'search': typing.Union[SearchSchema, str, ],
        'sort_by': typing.Union[SortBySchema, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_after_cursor = api_client.QueryParameter(
    name="after_cursor",
    style=api_client.ParameterStyle.FORM,
    schema=AfterCursorSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_order_direction = api_client.QueryParameter(
    name="order_direction",
    style=api_client.ParameterStyle.FORM,
    schema=SortDirEnumSchema,
    explode=True,
)
request_query_types = api_client.QueryParameter(
    name="types",
    style=api_client.ParameterStyle.FORM,
    schema=ContractTypeEnumListSchema,
    explode=True,
)
request_query_statuses = api_client.QueryParameter(
    name="statuses",
    style=api_client.ParameterStyle.FORM,
    schema=ContractStatusEnumListSchema,
    explode=True,
)
request_query_team_id = api_client.QueryParameter(
    name="team_id",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIdSchema,
    explode=True,
)
request_query_external_id = api_client.QueryParameter(
    name="external_id",
    style=api_client.ParameterStyle.FORM,
    schema=ExternalIdSchema,
    explode=True,
)
request_query_countries = api_client.QueryParameter(
    name="countries",
    style=api_client.ParameterStyle.FORM,
    schema=CountryCodeListSchema,
    explode=True,
)
request_query_currencies = api_client.QueryParameter(
    name="currencies",
    style=api_client.ParameterStyle.FORM,
    schema=CurrenciesSchema,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=ContractsSortByEnumSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ContractListContainerSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ContractListContainer


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ContractListContainer


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor405ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor405ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ApiErrorContainerSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ApiErrorContainer


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ApiErrorContainer


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_list_mapped_args(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if after_cursor is not None:
            _query_params["after_cursor"] = after_cursor
        if limit is not None:
            _query_params["limit"] = limit
        if order_direction is not None:
            _query_params["order_direction"] = order_direction
        if types is not None:
            _query_params["types"] = types
        if statuses is not None:
            _query_params["statuses"] = statuses
        if team_id is not None:
            _query_params["team_id"] = team_id
        if external_id is not None:
            _query_params["external_id"] = external_id
        if countries is not None:
            _query_params["countries"] = countries
        if currencies is not None:
            _query_params["currencies"] = currencies
        if search is not None:
            _query_params["search"] = search
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        args.query = _query_params
        return args

    async def _aget_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List of contracts
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_after_cursor,
            request_query_limit,
            request_query_order_direction,
            request_query_types,
            request_query_statuses,
            request_query_team_id,
            request_query_external_id,
            request_query_countries,
            request_query_currencies,
            request_query_search,
            request_query_sort_by,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contracts',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List of contracts
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_after_cursor,
            request_query_limit,
            request_query_order_direction,
            request_query_types,
            request_query_statuses,
            request_query_team_id,
            request_query_external_id,
            request_query_countries,
            request_query_currencies,
            request_query_search,
            request_query_sort_by,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contracts',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_list(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            after_cursor=after_cursor,
            limit=limit,
            order_direction=order_direction,
            types=types,
            statuses=statuses,
            team_id=team_id,
            external_id=external_id,
            countries=countries,
            currencies=currencies,
            search=search,
            sort_by=sort_by,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_list(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            after_cursor=after_cursor,
            limit=limit,
            order_direction=order_direction,
            types=types,
            statuses=statuses,
            team_id=team_id,
            external_id=external_id,
            countries=countries,
            currencies=currencies,
            search=search,
            sort_by=sort_by,
        )
        return self._get_list_oapg(
            query_params=args.query,
        )

class GetList(BaseApi):

    async def aget_list(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
        validate: bool = False,
        **kwargs,
    ) -> ContractListContainerPydantic:
        raw_response = await self.raw.aget_list(
            after_cursor=after_cursor,
            limit=limit,
            order_direction=order_direction,
            types=types,
            statuses=statuses,
            team_id=team_id,
            external_id=external_id,
            countries=countries,
            currencies=currencies,
            search=search,
            sort_by=sort_by,
            **kwargs,
        )
        if validate:
            return ContractListContainerPydantic(**raw_response.body)
        return api_client.construct_model_instance(ContractListContainerPydantic, raw_response.body)
    
    
    def get_list(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
        validate: bool = False,
    ) -> ContractListContainerPydantic:
        raw_response = self.raw.get_list(
            after_cursor=after_cursor,
            limit=limit,
            order_direction=order_direction,
            types=types,
            statuses=statuses,
            team_id=team_id,
            external_id=external_id,
            countries=countries,
            currencies=currencies,
            search=search,
            sort_by=sort_by,
        )
        if validate:
            return ContractListContainerPydantic(**raw_response.body)
        return api_client.construct_model_instance(ContractListContainerPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            after_cursor=after_cursor,
            limit=limit,
            order_direction=order_direction,
            types=types,
            statuses=statuses,
            team_id=team_id,
            external_id=external_id,
            countries=countries,
            currencies=currencies,
            search=search,
            sort_by=sort_by,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        after_cursor: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        order_direction: typing.Optional[SortDirEnum] = None,
        types: typing.Optional[ContractTypeEnumList] = None,
        statuses: typing.Optional[ContractStatusEnumList] = None,
        team_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        countries: typing.Optional[CountryCodeList] = None,
        currencies: typing.Optional[typing.Union[CurrencyCodeList, CurrencyCodeRequired]] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ContractsSortByEnum] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            after_cursor=after_cursor,
            limit=limit,
            order_direction=order_direction,
            types=types,
            statuses=statuses,
            team_id=team_id,
            external_id=external_id,
            countries=countries,
            currencies=currencies,
            search=search,
            sort_by=sort_by,
        )
        return self._get_list_oapg(
            query_params=args.query,
        )

