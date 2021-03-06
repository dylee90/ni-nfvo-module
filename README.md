# NFVO Module

Provides interfaces to the main functionalities and data of the Tacker NFVO.

This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.
## Main Responsibilities

### Managing new requests (triggered by SFCR arrivals)

- Operator (or in our case, traffic generator / SFCR orchestrator) sends information of newly arrived SFCR to NFVO module.
- NVFO module propagates this information to the AI module which then takes care of finding the optimal placement for the new configuration.

### Providing information (triggered by requests from AI module)

- Topology - also covered by monitoring module (`/nodes`, `/nodes/{id}`, `/links`, and `/link/{id}`).
- Placement - also covered by monitoring module (`/vnfinstances`, `/vnfinstances/{id}`).
- Routes.
- Requests.
- Available VNF flavors - also covered by monitoring module (`/vnfflavors` and `/vnfflavors/{id}`).

### Performing basic VNF / VM / SFC actions (triggered by requests from AI module)

- Deploy / shut down VNF / VM.
- Set / modify path through VNFs for a given SFCR.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m nfvo_server
```

and open your browser to here:

```
http://localhost:8181/v2/ui/
```

Your Swagger definition lives here:

```
http://localhost:8181/v2/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t nfvo_server .

# starting up a container
docker run -p 8181:8181 nfvo_server
```

## Modifying the API

- Import `swagger.yaml` into swagger editor [1].
- Perform desired changes.
- Use swagger editor to export an updated YAML file (`File -> Save as YAML`) and generate both server and client code (`Generate Server -> python-flask`, `Generate Client -> python`).
- Copy the three files into this directory and run `refresh.sh`.

## Create vnfflavor
Currently, creating vnfflavor is the same as openstack flavor, with:
- vnfflavor name should start with `vnf.`.
- Metadata should contains two custom fields: `os_image_id` - the openstack image id of the vnf, and `default_user_data` - the default user data to configure the vnf at the start (e.g., cloud config, commands to run at start).


[1] https://editor.swagger.io/


