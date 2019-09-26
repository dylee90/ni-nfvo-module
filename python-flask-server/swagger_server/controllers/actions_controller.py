import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.route import Route  # noqa: E501
from swagger_server import util


def deploy_vnf(body):  # noqa: E501
    """Instantiate an instance of a VNF flavor on a given node.

     # noqa: E501

    :param body: Flavor of VNF instance to be deployed as well as the target node.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
        print("[ actions_controller ] Received deployment request: %s.\n" % str(body))
        print("[ actions_controller ] Deploying VNF %s on node id %d.\n" % (body.flavor.name, body.node))
    return 'do some magic!'


def set_route(body):  # noqa: E501
    """Route a request via the provided route.

     # noqa: E501

    :param body: Route information including SFCR ID and hops.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Route.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def shutdown_vnf(body):  # noqa: E501
    """Shut down a VNF instance.

     # noqa: E501

    :param body: ID of VNF instance to be shut down.
    :type body: int

    :rtype: None
    """
    return 'do some magic!'
