# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredApiErrorRequest(TypedDict):
    pass

class OptionalApiErrorRequest(TypedDict, total=False):
    # The HTTP method of the failed request
    method: str

    # The relative URL of the failed request
    url: str

    # The status code of the response
    status: typing.Union[int, float]

    # The request ID of the failed request
    api_req_id: str

    # A link to the official documentation for the requested endpoint resource
    docs: str

    # The source handler which produced the returned error
    source: str

    # The code of the source handler which produced the returned error
    code: typing.Union[int, float]

class ApiErrorRequest(RequiredApiErrorRequest, OptionalApiErrorRequest):
    pass