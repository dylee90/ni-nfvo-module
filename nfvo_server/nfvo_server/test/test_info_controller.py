# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server.models.topology import Topology  # noqa: E501
from nfvo_server.models.vnf_flavor import VNFFlavor  # noqa: E501
from nfvo_server.models.vnf_instance import VNFInstance  # noqa: E501
from nfvo_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_placement(self):
        """Test case for get_placement

        Get current placement information, i.e., list of all active VNF instances including their location.
        """
        response = self.client.open(
            '/v2/placement',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_get_topology(self):
        """Test case for get_topology

        Get current topology information.
        """
        response = self.client.open(
            '/v2/topology',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vnf_flavors(self):
        """Test case for get_vnf_flavors

        Get available VNF flavors.
        """
        response = self.client.open(
            '/v2/vnfflavors',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
