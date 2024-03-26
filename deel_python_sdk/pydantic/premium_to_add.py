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


class PremiumToAdd(BaseModel):
    # Is the Contractor Agreement selected on the Deel Platform perfectly reflecting your organizations relation and actual working practices with the contractor?
    agreement_reflects_relation: Literal[True, False] = Field(alias='agreement_reflects_relation')

    # Workers doing certain jobs may be considered to be employees by law, even if they would otherwise be considered independent contractors under common law. Is the work of this worker characterized as: Apprentice, Trainee, Labourer, Driver, Medical worker, Legal worker, Construction worker or someone working in the fields of Finance/Investment?
    contractor_characteristics: Literal[True, False] = Field(alias='contractor_characteristics')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )