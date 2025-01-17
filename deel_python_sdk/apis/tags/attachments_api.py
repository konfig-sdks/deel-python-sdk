# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.attachments.post import UploadDeelFile
from deel_python_sdk.apis.tags.attachments_api_raw import AttachmentsApiRaw


class AttachmentsApi(
    UploadDeelFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AttachmentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AttachmentsApiRaw(api_client)
