# -*- coding: utf-8 -*-
import requests
import uuid
import base64

from nfvo_server.config import cfg
from nfvo_server.backend_clients.utils import openstack_client as client

vnf_cfg = cfg["openstack_client"]["vnf"]


def create_server(server_prefix, flavor_id, host_name, custom_user_data):
    client.rset_auth_info()

    # extra specs API link: https://github.com/openstack/nova/blob/master/api-ref/source/os-flavor-extra-specs.inc
    base_url = client.base_urls["compute"]
    headers = {'X-Auth-Token': client.client.auth_token}

    url = "/flavors/{flavors_id}/os-extra_specs".format(flavors_id=flavor_id)
    req = requests.get("{}{}".format(base_url, url),
        headers=headers)
    if req.status_code != 200:
        abort(req.status_code, req.text)

    extra_specs = req.json()
    try:
        os_image_id = extra_specs["extra_specs"]["os_image_id"]
        default_user_data = extra_specs["extra_specs"].get("default_user_data")
    except Exception as e:
        return "Cannot find os_image_id in flavor extra specs", 404

    if custom_user_data is not None:
        user_data = base64.b64encode(custom_user_data.encode('ascii'))
    else:
        # store user_data in extra_specs convert \n to \\n. need to restore
        default_user_data = default_user_data.replace('\\n', '\n')
        user_data = base64.b64encode(default_user_data.encode('ascii'))

    if server_prefix:
        server_name = "{}_{}".format(server_prefix, str(uuid.uuid4()))
    else:
        server_name = "vnf_{}".format(str(uuid.uuid4()))

    data = {
                "server": {
                    "name" : server_name,
                    "imageRef" : os_image_id,
                    "flavorRef" : flavor_id,
                    "availability_zone": "nova:{}".format(host_name),
                    "user_data" : user_data,
                    "networks": [
                        {"uuid": vnf_cfg["mgmt_net_id"]},
                        {"uuid": vnf_cfg["data_net_id"]},
                    ],
                }
            }

    url = "/servers"
    req = requests.post("{}{}".format(base_url, url),
        json=data,
        headers=headers)
    # if req is accepted (202), then return ID of server with success code (200)
    if req.status_code == 202:
        return req.json()["server"]["id"], 200
    else:
        abort(req.status_code, req.text)

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

    if req.status_code != 202:
        abort(req.status_code, req.text)

def destroy_server(server_id):
    client.rset_auth_info()

    base_url = client.base_urls["compute"]
    url = "/servers/{}".format(server_id)
    headers = {'X-Auth-Token': client.client.auth_token}

    req = requests.delete("{}{}".format(base_url, url),
        headers=headers)

    if req.status_code != 204:
        abort(req.status_code, req.text)
