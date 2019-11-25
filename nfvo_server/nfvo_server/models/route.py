# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from nfvo_server.models.base_model_ import Model
from nfvo_server import util


class Route(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sfc_name: str=None, sfcr_id: int=None, vnf_instance_ids: List[str]=None):  # noqa: E501
        """Route - a model defined in Swagger

        :param sfc_name: The sfc_name of this Route.  # noqa: E501
        :type sfc_name: str
        :param sfcr_id: The sfcr_id of this Route.  # noqa: E501
        :type sfcr_id: int
        :param vnf_instance_ids: The vnf_instance_ids of this Route.  # noqa: E501
        :type vnf_instance_ids: List[str]
        """
        self.swagger_types = {
            'sfc_name': str,
            'sfcr_id': int,
            'vnf_instance_ids': List[str]
        }

        self.attribute_map = {
            'sfc_name': 'sfc_name',
            'sfcr_id': 'sfcr_id',
            'vnf_instance_ids': 'vnf_instance_ids'
        }

        self._sfc_name = sfc_name
        self._sfcr_id = sfcr_id
        self._vnf_instance_ids = vnf_instance_ids

    @classmethod
    def from_dict(cls, dikt) -> 'Route':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Route of this Route.  # noqa: E501
        :rtype: Route
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sfc_name(self) -> str:
        """Gets the sfc_name of this Route.


        :return: The sfc_name of this Route.
        :rtype: str
        """
        return self._sfc_name

    @sfc_name.setter
    def sfc_name(self, sfc_name: str):
        """Sets the sfc_name of this Route.


        :param sfc_name: The sfc_name of this Route.
        :type sfc_name: str
        """

        self._sfc_name = sfc_name

    @property
    def sfcr_id(self) -> int:
        """Gets the sfcr_id of this Route.


        :return: The sfcr_id of this Route.
        :rtype: int
        """
        return self._sfcr_id

    @sfcr_id.setter
    def sfcr_id(self, sfcr_id: int):
        """Sets the sfcr_id of this Route.


        :param sfcr_id: The sfcr_id of this Route.
        :type sfcr_id: int
        """

        self._sfcr_id = sfcr_id

    @property
    def vnf_instance_ids(self) -> List[str]:
        """Gets the vnf_instance_ids of this Route.


        :return: The vnf_instance_ids of this Route.
        :rtype: List[str]
        """
        return self._vnf_instance_ids

    @vnf_instance_ids.setter
    def vnf_instance_ids(self, vnf_instance_ids: List[str]):
        """Sets the vnf_instance_ids of this Route.


        :param vnf_instance_ids: The vnf_instance_ids of this Route.
        :type vnf_instance_ids: List[str]
        """

        self._vnf_instance_ids = vnf_instance_ids
