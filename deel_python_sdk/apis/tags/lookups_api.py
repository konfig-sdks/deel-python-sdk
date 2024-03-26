# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.lookups_countries.get import GetCountryList
from deel_python_sdk.paths.lookups_currencies.get import GetCurrenciesList
from deel_python_sdk.paths.lookups_job_titles.get import GetJobTitlesList
from deel_python_sdk.paths.lookups_seniorities.get import GetSeniorityLevels
from deel_python_sdk.paths.lookups_time_off_types.get import GetTimeOffTypes
from deel_python_sdk.apis.tags.lookups_api_raw import LookupsApiRaw


class LookupsApi(
    GetCountryList,
    GetCurrenciesList,
    GetJobTitlesList,
    GetSeniorityLevels,
    GetTimeOffTypes,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LookupsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LookupsApiRaw(api_client)
