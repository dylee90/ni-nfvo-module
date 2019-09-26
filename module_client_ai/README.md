# swagger-client
AI module service for the NI project.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AiModuleApi(swagger_client.ApiClient(configuration))

try:
    # Notify AI module of SFC request arrival / departure event.
    api_instance.sfcr_event()
except ApiException as e:
    print("Exception when calling AiModuleApi->sfcr_event: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8282/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AiModuleApi* | [**sfcr_event**](docs/AiModuleApi.md#sfcr_event) | **POST** /sfcr_event | Notify AI module of SFC request arrival / departure event.


## Documentation For Models

 - [Assignment](docs/Assignment.md)
 - [Link](docs/Link.md)
 - [MonitoringEntry](docs/MonitoringEntry.md)
 - [Node](docs/Node.md)
 - [Route](docs/Route.md)
 - [RouteHops](docs/RouteHops.md)
 - [SFCR](docs/SFCR.md)
 - [Topology](docs/Topology.md)
 - [VNFInstance](docs/VNFInstance.md)
 - [VNFType](docs/VNFType.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


