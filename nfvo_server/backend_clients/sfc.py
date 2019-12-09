# -*- coding: utf-8 -*-
import requests
import uuid

from nfvo_server.config import cfg
from nfvo_server.controllers.sfcr_controller import active_requests
from nfvo_server.backend_clients.utils import openstack_client as client

from flask import abort
from flask import current_app

vnf_cfg = cfg["openstack_client"]["vnf"]

def create_sfc(fc_prefix, sfcr_id, logical_source_port, vnf_ids):
    client.rset_auth_info()

    if len(vnf_ids) == 0:
        abort(400, "vnf list is empty")

    sfcr = active_requests.get(sfcr_id)
    if sfcr is None:
        abort(400, "no sfcr for the provided sfcr_id")

    port_ids = []
    for vnf_id in vnf_ids:
        port_ids.append(_get_data_port(vnf_id))

    if fc_prefix:
        postfix_name = "{}_{}".format(fc_prefix, str(uuid.uuid4()))
    else:
        postfix_name = "{}".format(str(uuid.uuid4()))

    flow_classifier_id = _create_flow_classifier(postfix_name, sfcr, logical_source_port)
    pp_group_id = _create_port_pair_group(postfix_name, port_ids)
    p_chain_id = _create_port_chain(postfix_name, pp_group_id, flow_classifier_id)

    return p_chain_id

def _get_data_port(vnf_instance_id):
    base_url = client.base_urls["network"]
    url = "v2.0/ports?device_id={}".format(vnf_instance_id)
    headers = {'X-Auth-Token': client.client.auth_token}

    req = requests.get("{}{}".format(base_url, url),
        headers=headers)
    req = req.json()

    for port in req["ports"]:
        if port["network_id"] == vnf_cfg["data_net_id"]:
            return port["id"]

    abort(400, "no data port for vnf id: {}".format(vnf_instance_id))

def _create_flow_classifier(postfix_name, sfcr, logical_source_port):
    base_url = client.base_urls["network"]
    url = "/v2.0/sfc/flow_classifiers"
    headers = {'X-Auth-Token': client.client.auth_token}

    body = dict()
    # logical_source_port is required
    body["logical_source_port"] = logical_source_port
    body["name"] = "fc_{}".format(postfix_name)

    if sfcr.src_ip_prefix is not None:
        body["source_ip_prefix"] = sfcr.src_ip_prefix
    if sfcr.dst_ip_prefix is not None:
        body["destination_ip_prefix"] = sfcr.dst_ip_prefix
    if sfcr.src_port_min is not None:
        body["source_port_range_min"] = sfcr.src_port_min
    if sfcr.src_port_max is not None:
        body["source_port_range_max"] = sfcr.src_port_max
    if sfcr.dst_port_min is not None:
        body["destination_port_range_min"] = sfcr.dst_port_min
    if sfcr.dst_port_max is not None:
        body["destination_port_range_max"] = sfcr.dst_port_max
    if sfcr.proto is not None:
        body["protocol"] = sfcr.proto

    body = {"flow_classifier": body}

    req = requests.post("{}{}".format(base_url, url),
        json=body,
        headers=headers)

    if req.status_code == 201:
        return req.json()["flow_classifier"]["id"]
    else:
        abort(400, req.json())

def _create_port_pair_group(postfix_name, port_ids):
    base_url = client.base_urls["network"]
    headers = {'X-Auth-Token': client.client.auth_token}

    # create port_pairs from ports. Use the same port for ingress and egress
    port_pairs = []
    for i, port_id in enumerate(port_ids):
        body = {
                    "port_pair": {
                        "ingress": port_id,
                        "egress": port_id,
                        "name": "pp_{}_{}".format(i, postfix_name),
                    }
                }

        req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_pairs"),
            json=body,
            headers=headers)

        if req.status_code == 201:
            port_pairs.append(req.json()["port_pair"]["id"])
        else:
            abort(400, req.json())

    # create port pair group for each port pair
    port_pair_groups = []
    for i, port_pair in enumerate(port_pairs):
        body = {
                    "port_pair_group": {
                        "port_pairs": [port_pair],
                        "name": "ppg_{}_{}".format(i, postfix_name),
                    }
                }

        req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_pair_groups"),
            json=body,
            headers=headers)

        if req.status_code == 201:
            port_pair_groups.append(req.json()["port_pair_group"]["id"])
        else:
            abort(400, req.json())

    return port_pair_groups

def _create_port_chain(postfix_name, port_pair_groups, flow_classifiers):
    base_url = client.base_urls["network"]
    url = "/v2.0/sfc/port_chains"
    headers = {'X-Auth-Token': client.client.auth_token}

    body = {
                "port_chain": {
                    "flow_classifiers": flow_classifiers,
                    "port_pair_groups": port_pair_groups,
                    "name": "pc_{}".format(postfix_name),
                }
            }

    req = requests.post("{}{}".format(base_url, url),
        json=body,
        headers=headers)

    if req.status_code == 201:
        return req.json()["port_chain"]["id"]
    else:
        abort(400, req.json())
