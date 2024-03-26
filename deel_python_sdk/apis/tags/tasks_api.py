# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.contracts_contract_id_tasks.post import CreateNewTask
from deel_python_sdk.paths.contracts_contract_id_tasks_task_id.delete import DeleteFromContract
from deel_python_sdk.paths.contracts_contract_id_tasks.get import GetContractTasks
from deel_python_sdk.paths.contracts_contract_id_tasks_many_reviews.post import ReviewManyTasks
from deel_python_sdk.paths.contracts_contract_id_tasks_task_id_reviews.post import SubmitTaskReview
from deel_python_sdk.apis.tags.tasks_api_raw import TasksApiRaw


class TasksApi(
    CreateNewTask,
    DeleteFromContract,
    GetContractTasks,
    ReviewManyTasks,
    SubmitTaskReview,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TasksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TasksApiRaw(api_client)