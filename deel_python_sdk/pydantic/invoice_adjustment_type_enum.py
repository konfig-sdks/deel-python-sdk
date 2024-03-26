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


InvoiceAdjustmentTypeEnum = Literal["accrued_holiday", "additional_fee", "allowance", "bonus", "commission", "deduction", "deposit", "deposit_refund", "employer_cost", "expense", "health_allowance", "health_benefit", "health_insurance_fee", "legal_fee", "management_fee", "milestone", "offcycle", "other", "overtime", "pension", "pro_rata", "setup_fee", "severance", "shield_service", "signing_bonus", "signing_bonus_employer_cost", "refund", "task", "time_off", "vat", "withholding_tax", "work"]
