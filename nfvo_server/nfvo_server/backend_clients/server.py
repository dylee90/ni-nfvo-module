# -*- coding: utf-8 -*-
import requests
import uuid

from nfvo_server.config import cfg
from nfvo_server.backend_clients.utils import openstack_client as client

vnf_cfg = cfg["openstack_client"]["vnf"]


def create_server(flavor_id, host_name):
    client.rset_auth_info()

    base_url = client.base_urls["compute"]
    url = "/servers"
    headers = {'X-Auth-Token': client.client.auth_token}

    data = {
                "server": {
                    "name" : "vnf_{}".format(str(uuid.uuid4())),
                    "imageRef" : vnf_cfg["base_image_id"],
                    "flavorRef" : flavor_id,
                    "availability_zone": "nova:{}".format(host_name),
                    "networks": [
                        {"uuid": vnf_cfg["data_net_id"]},
                        {"uuid": vnf_cfg["mgmt_net_id"]},
                    ],
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

def stop_server(server_id):
    client.rset_auth_info()

    base_url = client.base_urls["compute"]
    url = "/servers/{}/action".format(server_id)
    headers = {'X-Auth-Token': client.client.auth_token}

    data = {
                "os-stop" : "dummy"
            }

    req = requests.post("{}{}".format(base_url, url),
        json=data,
        headers=headers)

    if req.status_code == 202:
        return "Success", 200
    else:
        return req.json(), req.status_code
