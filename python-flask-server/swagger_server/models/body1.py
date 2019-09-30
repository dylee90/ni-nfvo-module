# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vnf_instance_id: str=None):  # noqa: E501
        """Body1 - a model defined in Swagger

        :param vnf_instance_id: The vnf_instance_id of this Body1.  # noqa: E501
        :type vnf_instance_id: str
        """
        self.swagger_types = {
            'vnf_instance_id': str
        }

        self.attribute_map = {
            'vnf_instance_id': 'vnf_instance_id'
        }

        self._vnf_instance_id = vnf_instance_id

    @classmethod
    def from_dict(cls, dikt) -> 'Body1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_1 of this Body1.  # noqa: E501
        :rtype: Body1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vnf_instance_id(self) -> str:
        """Gets the vnf_instance_id of this Body1.


        :return: The vnf_instance_id of this Body1.
        :rtype: str
        """
        return self._vnf_instance_id

    @vnf_instance_id.setter
    def vnf_instance_id(self, vnf_instance_id: str):
        """Sets the vnf_instance_id of this Body1.


        :param vnf_instance_id: The vnf_instance_id of this Body1.
        :type vnf_instance_id: str
        """

        self._vnf_instance_id = vnf_instance_id
