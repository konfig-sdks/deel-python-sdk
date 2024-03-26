# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.people_worker_id_time_offs.post import AddTimeOffRequestRaw
from deel_python_sdk.paths.hris_direct_employees.post import CreateDirectEmployeeRaw
from deel_python_sdk.paths.people_worker_id_time_offs_timeoff_id.delete import DeleteTimeOffRequestRaw
from deel_python_sdk.paths.people_worker_id_time_offs_timeoff_id.patch import EditTimeOffRequestRaw
from deel_python_sdk.paths.people_me.get import GetCurrentProfileRaw
from deel_python_sdk.paths.internal_people.get import GetListRaw
from deel_python_sdk.paths.people.get import GetList0Raw
from deel_python_sdk.paths.people_worker_id.get import GetPersonRaw
from deel_python_sdk.paths.people_worker_id_time_offs_entitlements.get import ListTimeOffEntitlementsRaw
from deel_python_sdk.paths.people_worker_id_time_offs_policies.get import ListTimeOffPoliciesRaw
from deel_python_sdk.paths.people_worker_id_time_offs.get import ListTimeOffsByWorkerIdRaw
from deel_python_sdk.paths.people_worker_id_time_offs_timeoff_id_review.patch import ReviewTimeOffRaw
from deel_python_sdk.paths.people_worker_id_department.put import UpdateDepartmentRaw
from deel_python_sdk.paths.people_worker_id_working_location.put import UpdateWorkingLocationRaw


class PeopleApiRaw(
    AddTimeOffRequestRaw,
    CreateDirectEmployeeRaw,
    DeleteTimeOffRequestRaw,
    EditTimeOffRequestRaw,
    GetCurrentProfileRaw,
    GetListRaw,
    GetList0Raw,
    GetPersonRaw,
    ListTimeOffEntitlementsRaw,
    ListTimeOffPoliciesRaw,
    ListTimeOffsByWorkerIdRaw,
    ReviewTimeOffRaw,
    UpdateDepartmentRaw,
    UpdateWorkingLocationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
