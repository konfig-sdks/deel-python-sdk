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


class RequiredWebhookEventTypeResponse(TypedDict):
    # Describes the webhook event and other pertinent info.
    description: str

    # Event type unique identifier.
    id: typing.Union[int, float]

    # Name of the rabbit queue.
    module_name: str

    # Display name of the rabbit queue in Deel UI.
    module_label: str

    # Name of the webhook event.
    name: str

class OptionalWebhookEventTypeResponse(TypedDict, total=False):
    # JSON payload example of the specific event.
    payload_example: typing.Optional[str]

    # Time at which the event type was created.
    created_at: str

    # Time at which the event type was updated.
    updated_at: str

class WebhookEventTypeResponse(RequiredWebhookEventTypeResponse, OptionalWebhookEventTypeResponse):
    pass
