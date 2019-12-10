# -*- coding: utf-8 -*-
import requests
import uuid

from nfvo_server.config import cfg
from nfvo_server.backend_clients.utils import openstack_client as client
from nfvo_server.database import db

from flask import abort
from flask import current_app

vnf_cfg = cfg["openstack_client"]["vnf"]
base_url = client.base_urls["network"]
headers = {'X-Auth-Token': client.client.auth_token}


def create_sfc(fc_prefix, sfcr_id, logical_source_port, vnf_ids_list):
    client.rset_auth_info()
    headers = {'X-Auth-Token': client.client.auth_token}

    if len(vnf_ids_list) == 0:
        abort(req.status_code, "vnf list is empty")

    sfcr = db.get_active_request(sfcr_id)
    if sfcr is None:
        abort(req.status_code, "no sfcr for the provided sfcr_id")

    port_ids_list = []
    for vnf_ids in vnf_ids_list:
        port_ids = [_get_data_port(vnf_id) for vnf_id in vnf_ids]
        port_ids_list.append(port_ids)

    if fc_prefix:
        postfix_name = "{}_{}".format(fc_prefix, str(uuid.uuid4()))
    else:
        postfix_name = "{}".format(str(uuid.uuid4()))

    flow_classifier_id = _create_flow_classifier(postfix_name, sfcr, logical_source_port)
    port_pairs_ids_list = _create_port_pairs(postfix_name, port_ids_list)
    pp_group_ids = _create_port_pair_groups(postfix_name, port_pairs_ids_list)
    p_chain_id = _create_port_chain(postfix_name, pp_group_ids, flow_classifier_id)

    return p_chain_id

def _get_data_port(vnf_instance_id):
    url = "v2.0/ports?device_id={}".format(vnf_instance_id)
    req = requests.get("{}{}".format(base_url, url),
        headers=headers)
    req = req.json()

    for port in req["ports"]:
        if port["network_id"] == vnf_cfg["data_net_id"]:
            return port["id"]

    abort(req.status_code, "no data port for vnf id: {}".format(vnf_instance_id))

def _create_flow_classifier(postfix_name, sfcr, logical_source_port):
    url = "/v2.0/sfc/flow_classifiers"
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
        abort(req.status_code, req.text)

def _create_port_pairs(postfix_name, port_ids_list):
    # create port_pairs from ports. Use the same port for ingress and egress
    port_pairs_list = []
    for i, port_ids in enumerate(port_ids_list):
        port_pairs = []
        for j, port_id in enumerate(port_ids):
            body = {
                        "port_pair": {
                            "ingress": port_id,
                            "egress": port_id,
                            "name": "pp_{}{}_{}".format(i, j, postfix_name),
                        }
                    }

            req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_pairs"),
                json=body,
                headers=headers)

            if req.status_code == 201:
                port_pairs.append(req.json()["port_pair"]["id"])
            else:
                abort(req.status_code, req.text)

        port_pairs_list.append(port_pairs)

    return port_pairs_list

def _create_port_pair_groups(postfix_name, port_pairs_list):
    # create port pair group for each port_pairs
    port_pair_groups = []
    for i, port_pairs in enumerate(port_pairs_list):
        body = {
                    "port_pair_group": {
                        "port_pairs": port_pairs,
                        "name": "ppg_{}_{}".format(i, postfix_name),
                    }
                }

        req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_pair_groups"),
            json=body,
            headers=headers)

        if req.status_code == 201:
            port_pair_groups.append(req.json()["port_pair_group"]["id"])
        else:
            abort(req.status_code, req.text)

    return port_pair_groups

def _create_port_chain(postfix_name, port_pair_groups, flow_classifiers):
    body = {
                "port_chain": {
                    "flow_classifiers": flow_classifiers,
                    "port_pair_groups": port_pair_groups,
                    "name": "pc_{}".format(postfix_name),
                }
            }

    req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_chains"),
        json=body,
        headers=headers)

    if req.status_code == 201:
        return req.json()["port_chain"]["id"]
    else:
        abort(req.status_code, req.text)


def delete_sfc(port_chain_id):
    client.rset_auth_info()
    headers = {'X-Auth-Token': client.client.auth_token}
    _delete_port_chain_recursive(port_chain_id)

def _delete_port_chain_recursive(port_chain_id):
    url = "/v2.0/sfc/port_chains"
    req = requests.get("{}{}/{}".format(base_url, url, port_chain_id),
        headers=headers)
    if req.status_code != 200:
        abort(req.status_code, req.text)
    req = req.json()
    port_pair_groups = req["port_chain"]["port_pair_groups"]
    flow_classifiers = req["port_chain"]["flow_classifiers"]

    _delete_port_chain(port_chain_id)

    for port_pair_group in port_pair_groups:
        _delete_port_pair_group_recursive(port_pair_group)

    for flow_classifier in flow_classifiers:
        _delete_flow_classifier(flow_classifier)

def _delete_port_chain(port_chain_id):
    url = "/v2.0/sfc/port_chains"
    req = requests.delete("{}{}/{}".format(base_url, url, port_chain_id),
        headers=headers)
    if req.status_code != 204:
        abort(req.status_code, req.text)

def _delete_port_pair(port_pair_id):
    url = "/v2.0/sfc/port-pairs"
    req = requests.delete("{}{}/{}".format(base_url, url, port_pair_id),
        headers=headers)
    if req.status_code != 204:
        abort(req.status_code, req.text)

def _delete_port_pair_group_recursive(port_pair_group_id):
    url = "/v2.0/sfc/port_pair_groups"
    req = requests.get("{}{}/{}".format(base_url, url, port_pair_group_id),
        headers=headers)
    if req.status_code != 200:
        abort(req.status_code, req.text)
    req = req.json()
    port_pairs = req["port_pair_group"]["port_pairs"]

    _delete_port_pair_group(port_pair_group_id)

    for port_pair in port_pairs:
        _delete_port_pair(port_pair)

def _delete_port_pair_group(port_pair_group_id):
    url = "/v2.0/sfc/port_pair_groups"
    req = requests.delete("{}{}/{}".format(base_url, url, port_pair_group_id),
        headers=headers)
    if req.status_code != 204:
        abort(req.status_code, req.text)

def _delete_flow_classifier(flow_classifier_id):
    url = "/v2.0/sfc/flow_classifiers"
    req = requests.delete("{}{}/{}".format(base_url, url, flow_classifier_id),
        headers=headers)
    if req.status_code != 204:
        abort(req.status_code, req.text)
