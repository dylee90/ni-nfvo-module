# NFVO Module

Provides interfaces to the main functionalities and data of the Tacker NFVO.

### Main Responsibilities

#### Managing new requests (triggered by SFCR arrivals)

- Operator (or in our case, traffic generator / SFCR orchestrator) sends information of newly arrived SFCR to NFVO module.
- NVFO module propagates this information to the AI module which then takes care of finding the optimal placement for the new configuration. 

#### Providing information (triggered by requests from AI module)

- Topology.
- Placement.
- Routes.
- Requests.

#### Performing basic VNF / VM / SFC actions (triggered by requests from AI module)

- Deploy / shut down VNF / VM.
- Set / modify path through VNFs for a given SFCR.

### Usage Instructions

- TODO

### Modifying the API

- TODO

