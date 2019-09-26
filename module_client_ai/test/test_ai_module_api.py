# coding: utf-8

"""
    AI Module Service

    AI module service for the NI project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ai_module_api import AiModuleApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAiModuleApi(unittest.TestCase):
    """AiModuleApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ai_module_api.AiModuleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sfcr_event(self):
        """Test case for sfcr_event

        Notify AI module of SFC request arrival / departure event.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()