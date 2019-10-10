import connexion
import six
import time

from nfvo_server.models.sfcr import SFCR  # noqa: E501
from nfvo_server import util

import ai_module_client as swagc_ai

active_requests = dict()


def get_active_requests():
    global active_requests
    return list(active_requests.values())


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

    :rtype: None
    """
    if connexion.request.is_json:
        body = SFCR.from_dict(connexion.request.get_json())  # noqa: E501
        print("[ sfcr_controller ] Received SFC request: %s.\n" % body.to_dict())
        # print("class of body: %s" % body.__class__)
        print("[ sfcr_controller ] Notifying AI module of arrival.\n")
        notify_ai_module()
        active_requests[body.id] = body
    return 'do some magic!'
