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
from deel_python_sdk.model.people_me import PeopleMe as PeopleMeSchema

from deel_python_sdk.type.api_error_container import ApiErrorContainer
from deel_python_sdk.type.people_me import PeopleMe

from ...api_client import Dictionary
from deel_python_sdk.pydantic.people_me import PeopleMe as PeopleMePydantic
from deel_python_sdk.pydantic.api_error_container import ApiErrorContainer as ApiErrorContainerPydantic

from . import path

_auth = [
    'deelToken',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = PeopleMeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PeopleMe


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PeopleMe


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '405': _response_for_405,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_current_profile_mapped_args(
        self,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        return args

    async def _aget_current_profile_oapg(
        self,
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
        Get my current profile
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/people/me',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_current_profile_oapg(
        self,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get my current profile
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/people/me',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetCurrentProfileRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_current_profile(
        self,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_current_profile_mapped_args(
        )
        return await self._aget_current_profile_oapg(
            **kwargs,
        )
    
    def get_current_profile(
        self,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_current_profile_mapped_args(
        )
        return self._get_current_profile_oapg(
        )

class GetCurrentProfile(BaseApi):

    async def aget_current_profile(
        self,
        validate: bool = False,
        **kwargs,
    ) -> PeopleMePydantic:
        raw_response = await self.raw.aget_current_profile(
            **kwargs,
        )
        if validate:
            return PeopleMePydantic(**raw_response.body)
        return api_client.construct_model_instance(PeopleMePydantic, raw_response.body)
    
    
    def get_current_profile(
        self,
        validate: bool = False,
    ) -> PeopleMePydantic:
        raw_response = self.raw.get_current_profile(
        )
        if validate:
            return PeopleMePydantic(**raw_response.body)
        return api_client.construct_model_instance(PeopleMePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_current_profile_mapped_args(
        )
        return await self._aget_current_profile_oapg(
            **kwargs,
        )
    
    def get(
        self,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_current_profile_mapped_args(
        )
        return self._get_current_profile_oapg(
        )

