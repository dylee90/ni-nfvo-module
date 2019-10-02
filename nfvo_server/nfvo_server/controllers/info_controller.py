import connexion
import six

from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server.models.topology import Topology  # noqa: E501
from nfvo_server.models.vnf_flavor import VNFFlavor  # noqa: E501
from nfvo_server.models.vnf_instance import VNFInstance  # noqa: E501
from nfvo_server import util

from nfvo_server.controllers.sfcr_controller import get_active_requests

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
    return get_active_requests()


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
    topology = Topology(edge_list=[1, 4, 7], node_list=[i for i in range(1, 11)])
    return topology


def get_vnf_flavors():  # noqa: E501
    """Get available VNF flavors.

     # noqa: E501


    :rtype: List[VNFFlavor]
    """
    print("[ info_controller ] Returning available VNF flavors.")

    flavors = [
        VNFFlavor(name="firewall", capacity_mbps=900, delay_us=45, n_cores=4, ram_mb=1024),
        VNFFlavor(name="ids", capacity_mbps=400, delay_us=95, n_cores=8, ram_mb=4096)]

    return flavors
