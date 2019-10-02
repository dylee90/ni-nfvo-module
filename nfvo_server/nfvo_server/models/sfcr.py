# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from nfvo_server.models.base_model_ import Model
from nfvo_server import util


class SFCR(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, arrivaltime: datetime=None, src_ip: str=None, dst_ip: str=None, src_port: int=None, dst_port: int=None, bw: int=None, delay: int=None, duration: int=None, proto: str=None, nf_chain: List[str]=None):  # noqa: E501
        """SFCR - a model defined in Swagger

        :param id: The id of this SFCR.  # noqa: E501
        :type id: int
        :param arrivaltime: The arrivaltime of this SFCR.  # noqa: E501
        :type arrivaltime: datetime
        :param src_ip: The src_ip of this SFCR.  # noqa: E501
        :type src_ip: str
        :param dst_ip: The dst_ip of this SFCR.  # noqa: E501
        :type dst_ip: str
        :param src_port: The src_port of this SFCR.  # noqa: E501
        :type src_port: int
        :param dst_port: The dst_port of this SFCR.  # noqa: E501
        :type dst_port: int
        :param bw: The bw of this SFCR.  # noqa: E501
        :type bw: int
        :param delay: The delay of this SFCR.  # noqa: E501
        :type delay: int
        :param duration: The duration of this SFCR.  # noqa: E501
        :type duration: int
        :param proto: The proto of this SFCR.  # noqa: E501
        :type proto: str
        :param nf_chain: The nf_chain of this SFCR.  # noqa: E501
        :type nf_chain: List[str]
        """
        self.swagger_types = {
            'id': int,
            'arrivaltime': datetime,
            'src_ip': str,
            'dst_ip': str,
            'src_port': int,
            'dst_port': int,
            'bw': int,
            'delay': int,
            'duration': int,
            'proto': str,
            'nf_chain': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'arrivaltime': 'arrivaltime',
            'src_ip': 'src_ip',
            'dst_ip': 'dst_ip',
            'src_port': 'src_port',
            'dst_port': 'dst_port',
            'bw': 'bw',
            'delay': 'delay',
            'duration': 'duration',
            'proto': 'proto',
            'nf_chain': 'nf_chain'
        }

        self._id = id
        self._arrivaltime = arrivaltime
        self._src_ip = src_ip
        self._dst_ip = dst_ip
        self._src_port = src_port
        self._dst_port = dst_port
        self._bw = bw
        self._delay = delay
        self._duration = duration
        self._proto = proto
        self._nf_chain = nf_chain

    @classmethod
    def from_dict(cls, dikt) -> 'SFCR':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SFCR of this SFCR.  # noqa: E501
        :rtype: SFCR
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SFCR.


        :return: The id of this SFCR.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SFCR.


        :param id: The id of this SFCR.
        :type id: int
        """

        self._id = id

    @property
    def arrivaltime(self) -> datetime:
        """Gets the arrivaltime of this SFCR.


        :return: The arrivaltime of this SFCR.
        :rtype: datetime
        """
        return self._arrivaltime

    @arrivaltime.setter
    def arrivaltime(self, arrivaltime: datetime):
        """Sets the arrivaltime of this SFCR.


        :param arrivaltime: The arrivaltime of this SFCR.
        :type arrivaltime: datetime
        """

        self._arrivaltime = arrivaltime

    @property
    def src_ip(self) -> str:
        """Gets the src_ip of this SFCR.


        :return: The src_ip of this SFCR.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip: str):
        """Sets the src_ip of this SFCR.


        :param src_ip: The src_ip of this SFCR.
        :type src_ip: str
        """

        self._src_ip = src_ip

    @property
    def dst_ip(self) -> str:
        """Gets the dst_ip of this SFCR.


        :return: The dst_ip of this SFCR.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip: str):
        """Sets the dst_ip of this SFCR.


        :param dst_ip: The dst_ip of this SFCR.
        :type dst_ip: str
        """

        self._dst_ip = dst_ip

    @property
    def src_port(self) -> int:
        """Gets the src_port of this SFCR.


        :return: The src_port of this SFCR.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port: int):
        """Sets the src_port of this SFCR.


        :param src_port: The src_port of this SFCR.
        :type src_port: int
        """

        self._src_port = src_port

    @property
    def dst_port(self) -> int:
        """Gets the dst_port of this SFCR.


        :return: The dst_port of this SFCR.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port: int):
        """Sets the dst_port of this SFCR.


        :param dst_port: The dst_port of this SFCR.
        :type dst_port: int
        """

        self._dst_port = dst_port

    @property
    def bw(self) -> int:
        """Gets the bw of this SFCR.


        :return: The bw of this SFCR.
        :rtype: int
        """
        return self._bw

    @bw.setter
    def bw(self, bw: int):
        """Sets the bw of this SFCR.


        :param bw: The bw of this SFCR.
        :type bw: int
        """

        self._bw = bw

    @property
    def delay(self) -> int:
        """Gets the delay of this SFCR.


        :return: The delay of this SFCR.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay: int):
        """Sets the delay of this SFCR.


        :param delay: The delay of this SFCR.
        :type delay: int
        """

        self._delay = delay

    @property
    def duration(self) -> int:
        """Gets the duration of this SFCR.


        :return: The duration of this SFCR.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this SFCR.


        :param duration: The duration of this SFCR.
        :type duration: int
        """

        self._duration = duration

    @property
    def proto(self) -> str:
        """Gets the proto of this SFCR.


        :return: The proto of this SFCR.
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto: str):
        """Sets the proto of this SFCR.


        :param proto: The proto of this SFCR.
        :type proto: str
        """

        self._proto = proto

    @property
    def nf_chain(self) -> List[str]:
        """Gets the nf_chain of this SFCR.


        :return: The nf_chain of this SFCR.
        :rtype: List[str]
        """
        return self._nf_chain

    @nf_chain.setter
    def nf_chain(self, nf_chain: List[str]):
        """Sets the nf_chain of this SFCR.


        :param nf_chain: The nf_chain of this SFCR.
        :type nf_chain: List[str]
        """

        self._nf_chain = nf_chain
