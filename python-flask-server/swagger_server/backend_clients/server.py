# -*- coding: utf-8 -*-
import requests
import uuid

from swagger_server.config import cfg
from swagger_server.backend_clients.utils import create_openstack_client, get_base_urls

auth_cfg = cfg["openstack_client"]["auth"]
vnf_cfg = cfg["openstack_client"]["vnf"]

_client = create_openstack_client(**auth_cfg)
_base_urls = get_base_urls(_client)

def rset_auth_info():
    # FIXME: after the token is expired(?), we should re-authenticate.
    # however, the auth_url, username and password is also lost,
    # causing error on  re-authenticate call. A dirty fix
    # is to set them every call.
    _client.auth_url = auth_cfg["auth_url"]
    _client.username = auth_cfg["username"]
    _client.password = auth_cfg["password"]

def create_server(flavor_id, host_name):
    rset_auth_info()

    base_url = _base_urls["compute"]
    url = "/servers"
    headers = {'X-Auth-Token': _client.auth_token}

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
