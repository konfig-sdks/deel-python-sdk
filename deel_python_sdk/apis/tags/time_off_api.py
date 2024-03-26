# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.contracts_contract_id_time_offs.post import AddRequestObsolete
from deel_python_sdk.paths.contracts_contract_id_time_offs_timeoff_id.delete import CancelRequestObsolete
from deel_python_sdk.paths.contracts_contract_id_time_offs_timeoff_id.put import EditRequestObsolete
from deel_python_sdk.paths.time_offs.get import GetAllObsolete
from deel_python_sdk.paths.lookups_time_off_types.get import GetTimeOffTypes
from deel_python_sdk.paths.contracts_contract_id_time_offs.get import ListByContract
from deel_python_sdk.paths.contracts_contract_id_entitlements.get import ListEntitlements
from deel_python_sdk.paths.time_offs_timeoff_id_review.patch import ManageRequest
from deel_python_sdk.apis.tags.time_off_api_raw import TimeOffApiRaw


class TimeOffApi(
    AddRequestObsolete,
    CancelRequestObsolete,
    EditRequestObsolete,
    GetAllObsolete,
    GetTimeOffTypes,
    ListByContract,
    ListEntitlements,
    ManageRequest,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TimeOffApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TimeOffApiRaw(api_client)