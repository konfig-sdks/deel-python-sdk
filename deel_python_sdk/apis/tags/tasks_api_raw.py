# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.contracts_contract_id_tasks.post import CreateNewTaskRaw
from deel_python_sdk.paths.contracts_contract_id_tasks_task_id.delete import DeleteFromContractRaw
from deel_python_sdk.paths.contracts_contract_id_tasks.get import GetContractTasksRaw
from deel_python_sdk.paths.contracts_contract_id_tasks_many_reviews.post import ReviewManyTasksRaw
from deel_python_sdk.paths.contracts_contract_id_tasks_task_id_reviews.post import SubmitTaskReviewRaw


class TasksApiRaw(
    CreateNewTaskRaw,
    DeleteFromContractRaw,
    GetContractTasksRaw,
    ReviewManyTasksRaw,
    SubmitTaskReviewRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass