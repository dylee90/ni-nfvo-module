# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from nfvo_server.models.body import Body  # noqa: E501
from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.route_id import RouteID  # noqa: E501
from nfvo_server.models.route_update import RouteUpdate  # noqa: E501
from nfvo_server.models.vnfid import VNFID  # noqa: E501
from nfvo_server.test import BaseTestCase


class TestActionsController(BaseTestCase):
    """ActionsController integration test stubs"""

    def test_del_route(self):
        """Test case for del_route

        Delete a Route.
        """
        route_id = RouteID()
        response = self.client.open(
            '/v2/del_route',
            method='POST',
            data=json.dumps(route_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deploy_vnf(self):
        """Test case for deploy_vnf

        Instantiate an instance of a VNF flavor on a given node.
        """
        body = Body()
        response = self.client.open(
            '/v2/deploy_vnf',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_destroy_vnf(self):
        """Test case for destroy_vnf

        Destroy a VNF instance.
        """
        body = VNFID()
        response = self.client.open(
            '/v2/destroy_vnf',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_route(self):
        """Test case for set_route

        Route a request via the provided route. Return route id if success (which also means input route id is ommitted).
        """
        body = Route()
        response = self.client.open(
            '/v2/set_route',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shutdown_vnf(self):
        """Test case for shutdown_vnf

        Shut down a VNF instance.
        """
        body = VNFID()
        response = self.client.open(
            '/v2/shutdown_vnf',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_route(self):
        """Test case for update_route

        Update a route path.
        """
        body = RouteUpdate()
        response = self.client.open(
            '/v2/update_route',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
