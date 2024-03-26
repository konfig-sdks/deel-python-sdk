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
from deel_python_sdk.model.gp_employee_pto_update_data import GPEmployeePTOUpdateData as GPEmployeePTOUpdateDataSchema
from deel_python_sdk.model.generic_result_updated import GenericResultUpdated as GenericResultUpdatedSchema
from deel_python_sdk.model.gp_employee_ptoto_update_container import GPEmployeePTOToUpdateContainer as GPEmployeePTOToUpdateContainerSchema

from deel_python_sdk.type.generic_result_updated import GenericResultUpdated
from deel_python_sdk.type.api_error_container import ApiErrorContainer
from deel_python_sdk.type.gp_employee_ptoto_update_container import GPEmployeePTOToUpdateContainer
from deel_python_sdk.type.gp_employee_pto_update_data import GPEmployeePTOUpdateData

from ...api_client import Dictionary
from deel_python_sdk.pydantic.generic_result_updated import GenericResultUpdated as GenericResultUpdatedPydantic
from deel_python_sdk.pydantic.gp_employee_pto_update_data import GPEmployeePTOUpdateData as GPEmployeePTOUpdateDataPydantic
from deel_python_sdk.pydantic.gp_employee_ptoto_update_container import GPEmployeePTOToUpdateContainer as GPEmployeePTOToUpdateContainerPydantic
from deel_python_sdk.pydantic.api_error_container import ApiErrorContainer as ApiErrorContainerPydantic

from . import path

# Path params
WorkerIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'worker_id': typing.Union[WorkerIdSchema, str, ],
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


request_path_worker_id = api_client.PathParameter(
    name="worker_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WorkerIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = GPEmployeePTOToUpdateContainerSchema


request_body_gp_employee_ptoto_update_container = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'deelToken',
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = GenericResultUpdatedSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GenericResultUpdated


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GenericResultUpdated


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_pto_policy_mapped_args(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if data is not None:
            _body["data"] = data
        args.body = _body
        if worker_id is not None:
            _path_params["worker_id"] = worker_id
        args.path = _path_params
        return args

    async def _aupdate_pto_policy_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update PTO policy
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_worker_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
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
            path_template='/gp/workers/{worker_id}/pto-policy',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_gp_employee_ptoto_update_container.serialize(body, content_type)
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


    def _update_pto_policy_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update PTO policy
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_worker_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
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
            path_template='/gp/workers/{worker_id}/pto-policy',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_gp_employee_ptoto_update_container.serialize(body, content_type)
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


class UpdatePtoPolicyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_pto_policy(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_pto_policy_mapped_args(
            data=data,
            worker_id=worker_id,
        )
        return await self._aupdate_pto_policy_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_pto_policy(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_pto_policy_mapped_args(
            data=data,
            worker_id=worker_id,
        )
        return self._update_pto_policy_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdatePtoPolicy(BaseApi):

    async def aupdate_pto_policy(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
        validate: bool = False,
        **kwargs,
    ) -> GenericResultUpdatedPydantic:
        raw_response = await self.raw.aupdate_pto_policy(
            data=data,
            worker_id=worker_id,
            **kwargs,
        )
        if validate:
            return GenericResultUpdatedPydantic(**raw_response.body)
        return api_client.construct_model_instance(GenericResultUpdatedPydantic, raw_response.body)
    
    
    def update_pto_policy(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
        validate: bool = False,
    ) -> GenericResultUpdatedPydantic:
        raw_response = self.raw.update_pto_policy(
            data=data,
            worker_id=worker_id,
        )
        if validate:
            return GenericResultUpdatedPydantic(**raw_response.body)
        return api_client.construct_model_instance(GenericResultUpdatedPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_pto_policy_mapped_args(
            data=data,
            worker_id=worker_id,
        )
        return await self._aupdate_pto_policy_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        data: GPEmployeePTOUpdateData,
        worker_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_pto_policy_mapped_args(
            data=data,
            worker_id=worker_id,
        )
        return self._update_pto_policy_oapg(
            body=args.body,
            path_params=args.path,
        )
