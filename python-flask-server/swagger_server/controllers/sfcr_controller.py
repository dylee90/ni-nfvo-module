import connexion
import six
import time

from swagger_server.models.sfcr import SFCR  # noqa: E501
import module_client_ai.swagger_client_ai as swagc_ai
from swagger_server import util

active_requests = []

def get_active_requests():
    global active_requests
    return active_requests

def notify_ai_module():
    # Small delay to highlight the order of events.
    time.sleep(1)
    cfg = swagc_ai.Configuration()
    sfcr_api_instance = swagc_ai.AiModuleApi(swagc_ai.ApiClient(cfg))
    sfcr_api_instance.sfcr_event()


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
        active_requests.append(body)
    return 'do some magic!'
