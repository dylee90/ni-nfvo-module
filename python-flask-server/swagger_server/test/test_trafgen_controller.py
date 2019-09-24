# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.sfcr import SFCR  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrafgenController(BaseTestCase):
    """TrafgenController integration test stubs"""

    def test_add_sfcr(self):
        """Test case for add_sfcr

        Add new SFC request.
        """
        body = SFCR()
        response = self.client.open(
            '/v2/sfcr',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
