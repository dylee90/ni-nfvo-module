# swagger_client.InfoApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_topology**](InfoApi.md#get_topology) | **GET** /topology | Get current topology information.


# **get_topology**
> Topology get_topology()

Get current topology information.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Get current topology information.
    api_response = api_instance.get_topology()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_topology: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

