# swagger_client.ActionsApi

All URIs are relative to *http://localhost:8181/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_vnf**](ActionsApi.md#deploy_vnf) | **POST** /deploy | Instantiate an instance of a VNF flavor on a given node.
[**set_route**](ActionsApi.md#set_route) | **POST** /setRoute | Route a request via the provided route.
[**shutdown_vnf**](ActionsApi.md#shutdown_vnf) | **POST** /shutdown | Shut down a VNF instance.


# **deploy_vnf**
> deploy_vnf(body)

Instantiate an instance of a VNF flavor on a given node.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionsApi()
body = swagger_client.Body() # Body | Flavor of VNF instance to be deployed as well as the target node.

try:
    # Instantiate an instance of a VNF flavor on a given node.
    api_instance.deploy_vnf(body)
except ApiException as e:
    print("Exception when calling ActionsApi->deploy_vnf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Flavor of VNF instance to be deployed as well as the target node. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_route**
> set_route(body)

Route a request via the provided route.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionsApi()
body = swagger_client.Route() # Route | Route information including SFCR ID and hops.

try:
    # Route a request via the provided route.
    api_instance.set_route(body)
except ApiException as e:
    print("Exception when calling ActionsApi->set_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Route**](Route.md)| Route information including SFCR ID and hops. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_vnf**
> shutdown_vnf(body)

Shut down a VNF instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionsApi()
body = 789 # int | ID of VNF instance to be shut down.

try:
    # Shut down a VNF instance.
    api_instance.shutdown_vnf(body)
except ApiException as e:
    print("Exception when calling ActionsApi->shutdown_vnf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **int**| ID of VNF instance to be shut down. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

