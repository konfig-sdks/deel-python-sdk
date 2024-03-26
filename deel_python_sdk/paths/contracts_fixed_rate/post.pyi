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
from deel_python_sdk.model.contract_container_ongoing_time_based import ContractContainerOngoingTimeBased as ContractContainerOngoingTimeBasedSchema
from deel_python_sdk.model.contract_to_create_container_ongoing_time_based import ContractToCreateContainerOngoingTimeBased as ContractToCreateContainerOngoingTimeBasedSchema
from deel_python_sdk.model.contract_to_create_ongoing_time_based import ContractToCreateOngoingTimeBased as ContractToCreateOngoingTimeBasedSchema

from deel_python_sdk.type.contract_to_create_container_ongoing_time_based import ContractToCreateContainerOngoingTimeBased
from deel_python_sdk.type.contract_to_create_ongoing_time_based import ContractToCreateOngoingTimeBased
from deel_python_sdk.type.api_error_container import ApiErrorContainer
from deel_python_sdk.type.contract_container_ongoing_time_based import ContractContainerOngoingTimeBased

from ...api_client import Dictionary
from deel_python_sdk.pydantic.contract_to_create_ongoing_time_based import ContractToCreateOngoingTimeBased as ContractToCreateOngoingTimeBasedPydantic
from deel_python_sdk.pydantic.contract_to_create_container_ongoing_time_based import ContractToCreateContainerOngoingTimeBased as ContractToCreateContainerOngoingTimeBasedPydantic
from deel_python_sdk.pydantic.contract_container_ongoing_time_based import ContractContainerOngoingTimeBased as ContractContainerOngoingTimeBasedPydantic
from deel_python_sdk.pydantic.api_error_container import ApiErrorContainer as ApiErrorContainerPydantic

# body param
SchemaForRequestBodyApplicationJson = ContractToCreateContainerOngoingTimeBasedSchema


request_body_contract_to_create_container_ongoing_time_based = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = ContractContainerOngoingTimeBasedSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ContractContainerOngoingTimeBased


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ContractContainerOngoingTimeBased


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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

    def _create_new_fixed_rate_contract_mapped_args(
        self,
        data: ContractToCreateOngoingTimeBased,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if data is not None:
            _body["data"] = data
        args.body = _body
        return args

    async def _acreate_new_fixed_rate_contract_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new contract (fixed-rate)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contracts/fixed-rate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_contract_to_create_container_ongoing_time_based.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _create_new_fixed_rate_contract_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new contract (fixed-rate)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contracts/fixed-rate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_contract_to_create_container_ongoing_time_based.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class CreateNewFixedRateContractRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_fixed_rate_contract(
        self,
        data: ContractToCreateOngoingTimeBased,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_fixed_rate_contract_mapped_args(
            data=data,
        )
        return await self._acreate_new_fixed_rate_contract_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_fixed_rate_contract(
        self,
        data: ContractToCreateOngoingTimeBased,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_fixed_rate_contract_mapped_args(
            data=data,
        )
        return self._create_new_fixed_rate_contract_oapg(
            body=args.body,
        )

class CreateNewFixedRateContract(BaseApi):

    async def acreate_new_fixed_rate_contract(
        self,
        data: ContractToCreateOngoingTimeBased,
        validate: bool = False,
        **kwargs,
    ) -> ContractContainerOngoingTimeBasedPydantic:
        raw_response = await self.raw.acreate_new_fixed_rate_contract(
            data=data,
            **kwargs,
        )
        if validate:
            return ContractContainerOngoingTimeBasedPydantic(**raw_response.body)
        return api_client.construct_model_instance(ContractContainerOngoingTimeBasedPydantic, raw_response.body)
    
    
    def create_new_fixed_rate_contract(
        self,
        data: ContractToCreateOngoingTimeBased,
        validate: bool = False,
    ) -> ContractContainerOngoingTimeBasedPydantic:
        raw_response = self.raw.create_new_fixed_rate_contract(
            data=data,
        )
        if validate:
            return ContractContainerOngoingTimeBasedPydantic(**raw_response.body)
        return api_client.construct_model_instance(ContractContainerOngoingTimeBasedPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        data: ContractToCreateOngoingTimeBased,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_fixed_rate_contract_mapped_args(
            data=data,
        )
        return await self._acreate_new_fixed_rate_contract_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        data: ContractToCreateOngoingTimeBased,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_fixed_rate_contract_mapped_args(
            data=data,
        )
        return self._create_new_fixed_rate_contract_oapg(
            body=args.body,
        )

