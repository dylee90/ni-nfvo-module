import connexion
import six

from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server import util

from nfvo_server.controllers.sfcr_controller import get_active_requests


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
