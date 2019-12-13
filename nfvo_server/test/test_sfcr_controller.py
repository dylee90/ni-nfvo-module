# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server.test import BaseTestCase


class TestSfcrController(BaseTestCase):
    """SfcrController integration test stubs"""

    def test_add_sfcr(self):
        """Test case for add_sfcr

        Add new SFC request. id field is optional
        """
        body = SFCR()
        response = self.client.open(
            '/v2/sfcrs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_sfcr(self):
        """Test case for del_sfcr

        Delete a sfcr.
        """
        response = self.client.open(
            '/v2/sfcrs/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
