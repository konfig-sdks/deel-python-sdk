"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from typing import Callable, Generic, TypeVar, Any

F = TypeVar("F", bound=Callable[..., Any])


class copy_signature(Generic[F]):
    def __init__(self, func: F, *args) -> None:
        self.func = func

    def __call__(self, *args, **kwargs) -> F:
        if len(args) == 1:
            return args[0]
        return self.func(*args, **kwargs)