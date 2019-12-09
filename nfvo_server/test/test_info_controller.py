# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_requests(self):
        """Test case for get_requests

        Get currently active SFC requests.
        """
        response = self.client.open(
            '/v2/requests',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_routes(self):
        """Test case for get_routes

        Get current route information, i.e., list of all active SFCRs including their paths.
        """
        response = self.client.open(
            '/v2/routes',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
