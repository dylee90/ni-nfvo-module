# coding: utf-8

"""
    Traffic Generator Service

    Traffic generator service for the NI project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.trafgen_api import TrafgenApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTrafgenApi(unittest.TestCase):
    """TrafgenApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.trafgen_api.TrafgenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_sfcr(self):
        """Test case for add_sfcr

        Add new SFC request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
