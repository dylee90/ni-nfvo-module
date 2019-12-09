import connexion
import datetime
import six
from threading import Timer

from nfvo_server.models.body import Body  # noqa: E501
from nfvo_server.models.route import Route  # noqa: E501
from nfvo_server.models.shutdown import Shutdown  # noqa: E501
from nfvo_server import util

from nfvo_server.controllers.sfcr_controller import get_active_requests, get_time_of_last_arrival
from nfvo_server.backend_clients.server import create_server, stop_server
from nfvo_server.backend_clients.sfc import create_sfc

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
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
        print("[ actions_controller ] Received deployment request: %s.\n" % str(body))
        print("[ actions_controller ] Deploying VNF %s on node id %s.\n" % (body.flavor_id, body.node_name))
        try:
            current_sfcr = get_active_requests()[-1]
            timediff = (datetime.datetime.now() - get_time_of_last_arrival()).total_seconds()
            print("[ actions_contoller ] Time between arrival and deployment action: %f" % timediff)
            t = Timer(3, notify_trafgen, [current_sfcr])
            t.start()
        except Exception as e:
            print("[ actions_controller ] Error: %s.\n" % e)

    return create_server(body.vnf_name, body.flavor_id, body.node_name, body.user_data)


def set_route(body):  # noqa: E501
    """Route a request via the provided route.

     # noqa: E501

    :param body: Route information including SFCR ID and hops.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Route.from_dict(connexion.request.get_json())  # noqa: E501
    ret = create_sfc(body.sfc_name, body.sfcr_id, body.openstack_source_port, body.vnf_instance_ids)

    routes.append(body)

    return ret


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