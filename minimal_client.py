from __future__ import print_function
import datetime
import time
import swagger_client as swagc
from swagger_client.rest import ApiException
from pprint import pprint

# Create instances of the three API classes.
cfg = swagc.Configuration()
sfcr_api_instance = swagc.SfcrApi(swagc.ApiClient(cfg))
info_api_instance = swagc.InfoApi(swagc.ApiClient(cfg))
actions_api_instance = swagc.ActionsApi(swagc.ApiClient(cfg))

# SFC request to be added.
sfcr = swagc.SFCR(
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
    # Get current topology information.
    topology = info_api_instance.get_topology()
    print("[ minimal_client ] Received topology: %s." % str(topology))
except ApiException as e:
    print("Exception when calling InfoApi->get_topology: %s\n" % e)


## actions

# Body of deployment request.
body = swagc.Body(
        flavor = swagc.VNFFlavor(
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

