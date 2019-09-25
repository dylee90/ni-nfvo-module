import connexion
import six

from swagger_server.models.route import Route  # noqa: E501
from swagger_server.models.sfcr import SFCR  # noqa: E501
from swagger_server.models.topology import Topology  # noqa: E501
from swagger_server.models.vnf_flavor import VNFFlavor  # noqa: E501
from swagger_server.models.vnf_instance import VNFInstance  # noqa: E501
from swagger_server import util


def get_placement():  # noqa: E501
    """Get current placement information, i.e., list of all active VNF instances including their location.

     # noqa: E501


    :rtype: List[VNFInstance]
    """
    return 'do some magic!'


def get_requests():  # noqa: E501
    """Get currently active SFC requests.

     # noqa: E501


    :rtype: List[SFCR]
    """
    return 'do some magic!'


def get_routes():  # noqa: E501
    """Get current route information, i.e., list of all active SFCRs including their paths.

     # noqa: E501


    :rtype: List[Route]
    """
    return 'do some magic!'


def get_topology():  # noqa: E501
    """Get current topology information.

     # noqa: E501


    :rtype: Topology
    """
    print("[ info_controller ] Returning topology info.")
    topology = Topology(edge_list = [1, 4, 7], node_list = [i for i in range(1, 11)])
    return topology


def get_vnf_flavors():  # noqa: E501
    """Get available VNF flavors.

     # noqa: E501


    :rtype: List[VNFFlavor]
    """
    return 'do some magic!'
