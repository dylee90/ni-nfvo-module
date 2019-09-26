from __future__ import print_function
import datetime

from pprint import pprint

import module_client_nfvo.swagger_client_nfvo as swagc_nfvo
import module_client_ai.swagger_client_ai as swagc_ai

from module_client_nfvo.swagger_client_nfvo.rest import ApiException

pprint(swagc_nfvo.Topology())
pprint(swagc_ai.Topology())

# Create instances of the three API classes.
cfg = swagc_nfvo.Configuration()
sfcr_api_instance = swagc_nfvo.SfcrApi(swagc_nfvo.ApiClient(cfg))
info_api_instance = swagc_nfvo.InfoApi(swagc_nfvo.ApiClient(cfg))
actions_api_instance = swagc_nfvo.ActionsApi(swagc_nfvo.ApiClient(cfg))

# SFC request to be added.
sfcr = swagc_nfvo.SFCR(
    arrivaltime = datetime.datetime.now().isoformat("T") + "Z",
    src_ip = "10.0.0.1",
    dst_ip = "10.0.0.2",
    src_port = 1234,
    dst_port = 6633,
    bw = 250,
    delay = 100,
    duration = 120,
    proto = "UDP",
    nf_chain = ["nat", "firewall", "ids"])

## sfcr

try:
    # Notify NFVO module of SFC request arrival.
    sfcr_api_instance.add_sfcr(sfcr)
except ApiException as e:
    print("Exception when calling SfcrApi->add_sfcr: %s\n" % e)

## info

try:
    # Get current topology and VNF flavor information.

    topology = info_api_instance.get_topology()
    print("[ minimal_client ] Received topology: %s." % str(topology))
    print("[ minimal_client ] Class of received topology: %s." % str(topology.__class__))

    flavors = info_api_instance.get_vnf_flavors()
    print("[ minimal_client ] Received VNF flavors: %s." % str(flavors))
    print("[ minimal_client ] Class of received items: %s." % str(flavors[0].__class__))

except ApiException as e:
    print("Exception when calling InfoApi->get_topology: %s\n" % e)


## actions

# Body of deployment request.
body = swagc_nfvo.Body(
        flavor = swagc_nfvo.VNFFlavor(
            name = "firewall",
            capacity_mbps = 900,
            delay_us = 45,
            n_cores = 4,
            ram_mb = 1024),
        node = 7)

try:
    # Instantiate an instance of a VNF flavor on a given node.
    actions_api_instance.deploy_vnf(body)
except ApiException as e:
    print("Exception when calling ActionsApi->deploy_vnf: %s\n" % e)
