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


class GPEmployeeCompensationUpdated(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['GPEmployeeCompensationUpdatedItem']:
            return GPEmployeeCompensationUpdatedItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['GPEmployeeCompensationUpdatedItem'], typing.List['GPEmployeeCompensationUpdatedItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GPEmployeeCompensationUpdated':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'GPEmployeeCompensationUpdatedItem':
        return super().__getitem__(i)

from deel_python_sdk.model.gp_employee_compensation_updated_item import GPEmployeeCompensationUpdatedItem
