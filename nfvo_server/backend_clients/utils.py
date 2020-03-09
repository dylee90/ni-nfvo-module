# -*- coding: utf-8 -*-
import requests

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client

from flask import abort
from flask import current_app

from nfvo_server.config import cfg


class OpenstackClient():
    def __init__(self, auth_cfg):
        self.auth_cfg = auth_cfg
        self.client = self._create_openstack_client()
        self.base_urls = self._get_base_urls()

    def _create_openstack_client(self):
        auth = v3.Password(**self.auth_cfg)
        sess = session.Session(auth=auth)
        client = keystone_client.Client(session=sess)
        client.authenticate(**self.auth_cfg)
        return client

    def _get_base_urls(self):
        base_urls = dict()
        endpoints = self.client.endpoints.list()
        for endpoint in endpoints:
            service = self.client.services.get(endpoint.service_id)
            base_urls[service.type] = endpoint.url
        return base_urls

    def rset_auth_info(self):
        # FIXME: after the token is expired(?), we should re-authenticate.
        # however, the auth_url, username and password is also lost,
        # causing error on  re-authenticate call. A dirty fix
        # is to set them every call.
        self.client.auth_url = self.auth_cfg["auth_url"]
        self.client.username = self.auth_cfg["username"]
        self.client.password = self.auth_cfg["password"]


def get_net_id_from_name(net_name):
    openstack_client.rset_auth_info()
    base_url = openstack_client.base_urls["network"]
    headers = {'X-Auth-Token': openstack_client.client.auth_token}

    req = requests.get("{}{}".format(base_url, "/v2.0/networks"),
        headers={'X-Auth-Token': openstack_client.client.auth_token})
    if req.status_code != 200:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)

    for net in req.json()["networks"]:
        if net.get("name") == net_name:
            return net["id"]

    error_msg = "there is no network with name: " + net_name
    current_app.logger.error(error_msg)
    abort(404, error_msg)


openstack_client = OpenstackClient(cfg["openstack_client"]["auth"])
