# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.contracts_contract_id_time_offs.post import AddRequestObsoleteRaw
from deel_python_sdk.paths.contracts_contract_id_time_offs_timeoff_id.delete import CancelRequestObsoleteRaw
from deel_python_sdk.paths.contracts_contract_id_time_offs_timeoff_id.put import EditRequestObsoleteRaw
from deel_python_sdk.paths.time_offs.get import GetAllObsoleteRaw
from deel_python_sdk.paths.lookups_time_off_types.get import GetTimeOffTypesRaw
from deel_python_sdk.paths.contracts_contract_id_time_offs.get import ListByContractRaw
from deel_python_sdk.paths.contracts_contract_id_entitlements.get import ListEntitlementsRaw
from deel_python_sdk.paths.time_offs_timeoff_id_review.patch import ManageRequestRaw


class TimeOffApiRaw(
    AddRequestObsoleteRaw,
    CancelRequestObsoleteRaw,
    EditRequestObsoleteRaw,
    GetAllObsoleteRaw,
    GetTimeOffTypesRaw,
    ListByContractRaw,
    ListEntitlementsRaw,
    ManageRequestRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
