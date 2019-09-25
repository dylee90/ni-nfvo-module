# NFVO Module

Provides interfaces to the main functionalities and data of the Tacker NFVO.

### Main Responsibilities

#### Managing new requests (triggered by SFCR arrivals)

- Operator (or in our case, traffic generator / SFCR orchestrator) sends information of newly arrived SFCR to NFVO module.
- NVFO module propagates this information to the AI module which then takes care of finding the optimal placement for the new configuration.

#### Providing information (triggered by requests from AI module)

- Topology - also covered by monitoring module (`/nodes`, `/nodes/{id}`, `/links`, and `/link/{id}`).
- Placement - also covered by monitoring module (`/vnfinstances`, `/vnfinstances/{id}`).
- Routes.
- Requests.
- Available VNF flavors - also covered by monitoring module (`/vnfflavors` and `/vnfflavors/{id}`).

#### Performing basic VNF / VM / SFC actions (triggered by requests from AI module)

- Deploy / shut down VNF / VM.
- Set / modify path through VNFs for a given SFCR.

### Usage Instructions

- Start server locally by calling `python3 -m swagger_server` in `python-flask-server`.
- For the exemplary `minimal_client.py`, either copy and run the file in the `python-client` folder or add said folder to your `PYTHONPATH` environment variable prior to running it (e.g., `export PYTHONPATH=/mnt/e/git/nfvo-module/python-client`, `python3 minimal_client.py`).

### Modifying the API

- Import `swagger.yaml` into swagger editor [1].
- Perform desired changes.
- Use swagger editor to export an updated YAML file (`File -> Save as YAML`) and generate both server and client code (`Generate Server -> python-flask`, `Generate Client -> python`).
- Copy the three files into this directory and run `refresh.sh`.

[1] https://editor.swagger.io/


