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
from deel_python_sdk.model.generic_result_deleted import GenericResultDeleted as GenericResultDeletedSchema

from deel_python_sdk.type.api_error_container import ApiErrorContainer
from deel_python_sdk.type.generic_result_deleted import GenericResultDeleted

from ...api_client import Dictionary
from deel_python_sdk.pydantic.generic_result_deleted import GenericResultDeleted as GenericResultDeletedPydantic
from deel_python_sdk.pydantic.api_error_container import ApiErrorContainer as ApiErrorContainerPydantic

from . import path

# Query params
ReasonSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'reason': typing.Union[ReasonSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_reason = api_client.QueryParameter(
    name="reason",
    style=api_client.ParameterStyle.FORM,
    schema=ReasonSchema,
    explode=True,
)
# Path params
InvoiceAdjustmentIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'invoice_adjustment_id': typing.Union[InvoiceAdjustmentIdSchema, decimal.Decimal, int, float, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_invoice_adjustment_id = api_client.PathParameter(
    name="invoice_adjustment_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=InvoiceAdjustmentIdSchema,
    required=True,
)
_auth = [
    'deelToken',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = GenericResultDeletedSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GenericResultDeleted


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GenericResultDeleted


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

    def _delete_adjustment_mapped_args(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if reason is not None:
            _query_params["reason"] = reason
        if invoice_adjustment_id is not None:
            _path_params["invoice_adjustment_id"] = invoice_adjustment_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _adelete_adjustment_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Delete an invoice adjustment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_invoice_adjustment_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_reason,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/invoice-adjustments/{invoice_adjustment_id}',
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


    def _delete_adjustment_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Delete an invoice adjustment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_invoice_adjustment_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_reason,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/invoice-adjustments/{invoice_adjustment_id}',
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


class DeleteAdjustmentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adelete_adjustment(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._delete_adjustment_mapped_args(
            invoice_adjustment_id=invoice_adjustment_id,
            reason=reason,
        )
        return await self._adelete_adjustment_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def delete_adjustment(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._delete_adjustment_mapped_args(
            invoice_adjustment_id=invoice_adjustment_id,
            reason=reason,
        )
        return self._delete_adjustment_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class DeleteAdjustment(BaseApi):

    async def adelete_adjustment(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> GenericResultDeletedPydantic:
        raw_response = await self.raw.adelete_adjustment(
            invoice_adjustment_id=invoice_adjustment_id,
            reason=reason,
            **kwargs,
        )
        if validate:
            return GenericResultDeletedPydantic(**raw_response.body)
        return api_client.construct_model_instance(GenericResultDeletedPydantic, raw_response.body)
    
    
    def delete_adjustment(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
        validate: bool = False,
    ) -> GenericResultDeletedPydantic:
        raw_response = self.raw.delete_adjustment(
            invoice_adjustment_id=invoice_adjustment_id,
            reason=reason,
        )
        if validate:
            return GenericResultDeletedPydantic(**raw_response.body)
        return api_client.construct_model_instance(GenericResultDeletedPydantic, raw_response.body)


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._delete_adjustment_mapped_args(
            invoice_adjustment_id=invoice_adjustment_id,
            reason=reason,
        )
        return await self._adelete_adjustment_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        invoice_adjustment_id: typing.Union[int, float],
        reason: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._delete_adjustment_mapped_args(
            invoice_adjustment_id=invoice_adjustment_id,
            reason=reason,
        )
        return self._delete_adjustment_oapg(
            query_params=args.query,
            path_params=args.path,
        )

