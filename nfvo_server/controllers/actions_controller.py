import connexion
import datetime
import six
from threading import Timer

from nfvo_server.models.body import Body  # noqa: E501
from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.route_id import RouteID  # noqa: E501
from nfvo_server.models.shutdown import Shutdown  # noqa: E501
from nfvo_server import util

from nfvo_server.backend_clients.server import create_server, stop_server
from nfvo_server.backend_clients.sfc import create_sfc, delete_sfc

from nfvo_server.controllers.info_controller import routes

import trafgen_module_client as swagc_trafgen

def notify_trafgen(sfcr):
    print("[ actions_controller ] Finished infrastructure setup, notifying trafgen.\n")
    try:
        cfg = swagc_trafgen.Configuration()
        trafgen_api_instance = swagc_trafgen.TrafgenApi(swagc_trafgen.ApiClient(cfg))
        trafgen_api_instance.add_sfcr(sfcr)
    except Exception  as e:
        print("[ actions_controller ] Error: %s.\n" % e)

def deploy_vnf(body):  # noqa: E501
    """Instantiate an instance of a VNF flavor on a given node.

     # noqa: E501

    :param body: Flavor of VNF instance to be deployed as well as the target node.
    :type body: dict | bytes

    :rtype: str
    """

    return create_server(body.vnf_name, body.flavor_id, body.node_name, body.user_data)

def del_route(route_id):  # noqa: E501
    """Delete a Route.

     # noqa: E501

    :param route_id:
    :type route_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        route_id = RouteID.from_dict(connexion.request.get_json())  # noqa: E501
    delete_sfc(route_id.id)
    # del routes[route_id]


def set_route(body):  # noqa: E501
    """Route a request via the provided route. Return route id if success (which also means input route id is ommitted).

     # noqa: E501

    :param body: Route information including SFCR ID and vnf instance ids.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Route.from_dict(connexion.request.get_json())  # noqa: E501
    route_id = create_sfc(body.sfc_name, body.sfcr_id, body.openstack_source_port, body.vnf_instance_ids)
    body.id = route_id
    routes[route_id] = body

    return route_id


def shutdown_vnf(body):  # noqa: E501
    """Shut down a VNF instance.

     # noqa: E501

    :param body: ID of VNF instance to be shut down.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Shutdown.from_dict(connexion.request.get_json())  # noqa: E501
    return stop_server(body.vnf_instance_id)
