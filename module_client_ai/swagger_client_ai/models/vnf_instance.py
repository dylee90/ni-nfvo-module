# coding: utf-8

"""
    AI Module Service

    AI module service for the NI project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client_ai.models.vnf_type import VNFType  # noqa: F401,E501


class VNFInstance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'type': 'VNFType',
        'node_id': 'int',
        'ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'node_id': 'node_id',
        'ip': 'ip'
    }

    def __init__(self, id=None, type=None, node_id=None, ip=None):  # noqa: E501
        """VNFInstance - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._node_id = None
        self._ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if node_id is not None:
            self.node_id = node_id
        if ip is not None:
            self.ip = ip

    @property
    def id(self):
        """Gets the id of this VNFInstance.  # noqa: E501


        :return: The id of this VNFInstance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VNFInstance.


        :param id: The id of this VNFInstance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this VNFInstance.  # noqa: E501


        :return: The type of this VNFInstance.  # noqa: E501
        :rtype: VNFType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VNFInstance.


        :param type: The type of this VNFInstance.  # noqa: E501
        :type: VNFType
        """

        self._type = type

    @property
    def node_id(self):
        """Gets the node_id of this VNFInstance.  # noqa: E501


        :return: The node_id of this VNFInstance.  # noqa: E501
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this VNFInstance.


        :param node_id: The node_id of this VNFInstance.  # noqa: E501
        :type: int
        """

        self._node_id = node_id

    @property
    def ip(self):
        """Gets the ip of this VNFInstance.  # noqa: E501


        :return: The ip of this VNFInstance.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this VNFInstance.


        :param ip: The ip of this VNFInstance.  # noqa: E501
        :type: str
        """

        self._ip = ip

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VNFInstance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VNFInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
