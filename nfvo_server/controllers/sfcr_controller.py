import connexion
import datetime
import six
import time
import uuid

from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server.database import db
from nfvo_server import util

from nfvo_server.backend_clients.sfc import create_flow_classifier, delete_flow_classifier

import ai_module_client as swagc_ai


time_of_last_arrival = datetime.datetime.now()

def get_time_of_last_arrival():
    global time_of_last_arrival
    return time_of_last_arrival


def notify_ai_module():
    # Small delay to highlight the order of events.
    time.sleep(1)
    try:
        cfg = swagc_ai.Configuration()
        sfcr_api_instance = swagc_ai.AiModuleApi(swagc_ai.ApiClient(cfg))
        sfcr_api_instance.sfcr_event()
    except Exception  as e:
        print("[ sfcr_controller ] Error: %s.\n" % e)


def add_sfcr(body):  # noqa: E501
    """Add new SFC request.

     # noqa: E501

    :param body: SFC request object to be added.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        global time_of_last_arrival
        time_of_last_arrival = datetime.datetime.now()
        body = SFCR.from_dict(connexion.request.get_json())  # noqa: E501
        print("[ sfcr_controller ] Received SFC request: %s.\n" % body.to_dict())
        # print("class of body: %s" % body.__class__)
        print("[ sfcr_controller ] Notifying AI module of arrival.\n")
        notify_ai_module()

        flow_classifier_id = create_flow_classifier(body)
        body.id = flow_classifier_id
        db.insert_sfcr(body)

        return flow_classifier_id

def del_sfcr(id):  # noqa: E501
    """Delete a sfcr.

     # noqa: E501

    :param id: route id
    :type id: str

    :rtype: None
    """
    delete_flow_classifier(id)
    db.del_sfcr(id)

