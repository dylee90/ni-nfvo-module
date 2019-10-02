# -*- coding: utf-8 -*-
import requests
import uuid

from nfvo_server.config import cfg
from nfvo_server.backend_clients.utils import openstack_client as client


def create_sfc(vnf_ids):
    client.rset_auth_info()
    for vnf_id in vnf_ids:
        print(get_port_of_server(vnf_id))

    base_url = client.base_urls["compute"]
    url = "/servers"
    headers = {'X-Auth-Token': client.client.auth_token}

    data = {
                "server": {
                    "name" : "vnf_{}".format(str(uuid.uuid4())),
                    "imageRef" : vnf_cfg["base_image_id"],
                    "flavorRef" : flavor_id,
                    "availability_zone": "nova:{}".format(host_name),
                    "networks": [{"uuid": vnf_cfg["network_uuid"]},],
                }
            }

    req = requests.post("{}{}".format(base_url, url),
        json=data,
        headers=headers)
    # if req is accepted (202), then return ID of server with success code (200)
    if req.status_code == 202:
        return req.json()["server"]["id"], 200
    else:
        return req.json(), req.status_code

def get_port_of_server(vnf_instance_id):
    client.rset_auth_info()

    # FIXME: why networking API missing v2.0 text???
    base_url = "{}v2.0".format(client.base_urls["network"])
    url = "/networks?device_id={}".format(vnf_instance_id)
    headers = {'X-Auth-Token': _client.auth_token}
    req = requests.get("{}{}".format(base_url, url),
        headers=headers)
    return req.json()
