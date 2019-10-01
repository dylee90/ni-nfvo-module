# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.route import Route  # noqa: E501
from swagger_server.models.shutdown import Shutdown  # noqa: E501
from swagger_server.test import BaseTestCase


class TestActionsController(BaseTestCase):
    """ActionsController integration test stubs"""

    def test_deploy_vnf(self):
        """Test case for deploy_vnf

        Instantiate an instance of a VNF flavor on a given node.
        """
        body = Body()
        response = self.client.open(
            '/v2/deploy',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_route(self):
        """Test case for set_route

        Route a request via the provided route.
        """
        body = Route()
        response = self.client.open(
            '/v2/setRoute',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shutdown_vnf(self):
        """Test case for shutdown_vnf

        Shut down a VNF instance.
        """
        body = Shutdown()
        response = self.client.open(
            '/v2/shutdown',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
