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


ContractStatusEnum = Literal["new", "under_review", "waiting_for_employee_contract", "waiting_for_client_sign", "processing_payment", "waiting_for_contractor_sign", "waiting_for_eor_sign", "waiting_for_employee_sign", "awaiting_deposit_payment", "in_progress", "completed", "cancelled", "user_cancelled", "rejected", "waiting_for_client_payment"]