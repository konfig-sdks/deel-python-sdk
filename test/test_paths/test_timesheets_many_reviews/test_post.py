# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import deel_python_sdk
from deel_python_sdk.paths.timesheets_many_reviews import post
from deel_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTimesheetsManyReviews(ApiTestMixin, unittest.TestCase):
    """
    TimesheetsManyReviews unit test stubs
        Review multiple timesheets
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
