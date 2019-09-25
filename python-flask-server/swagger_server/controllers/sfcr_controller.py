import connexion
import six

from swagger_server.models.sfcr import SFCR  # noqa: E501
from swagger_server import util


def add_sfcr(body):  # noqa: E501
    """Add new SFC request.

     # noqa: E501

    :param body: SFC request object to be added.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SFCR.from_dict(connexion.request.get_json())  # noqa: E501
        print("[ sfcr_controller ] Received SFC request: %s." % body.to_dict())
    return 'do some magic!'
