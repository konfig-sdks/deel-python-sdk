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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from deel_python_sdk.pydantic.worker_bank_account_to_add import WorkerBankAccountToAdd

WorkerBankAccountInfo = typing.Union[WorkerBankAccountToAdd,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
WorkerBankAccountInfo = object
