# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
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


if __name__ == '__main__':
    import unittest
    unittest.main()
