# swagger_client.InfoApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_placement**](InfoApi.md#get_placement) | **GET** /placement | Get current placement information, i.e., list of all active VNF instances including their location.
[**get_requests**](InfoApi.md#get_requests) | **GET** /requests | Get currently active SFC requests.
[**get_routes**](InfoApi.md#get_routes) | **GET** /routes | Get current route information, i.e., list of all active SFCRs including their paths.
[**get_topology**](InfoApi.md#get_topology) | **GET** /topology | Get current topology information.
[**get_vnf_flavors**](InfoApi.md#get_vnf_flavors) | **GET** /vnfflavors | Get available VNF flavors.


# **get_placement**
> list[VNFInstance] get_placement()

Get current placement information, i.e., list of all active VNF instances including their location.



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
    # Get current placement information, i.e., list of all active VNF instances including their location.
    api_response = api_instance.get_placement()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_placement: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VNFInstance]**](VNFInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requests**
> list[SFCR] get_requests()

Get currently active SFC requests.



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
    # Get currently active SFC requests.
    api_response = api_instance.get_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SFCR]**](SFCR.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes**
> list[Route] get_routes()

Get current route information, i.e., list of all active SFCRs including their paths.



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
    # Get current route information, i.e., list of all active SFCRs including their paths.
    api_response = api_instance.get_routes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_routes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Route]**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_vnf_flavors**
> list[VNFFlavor] get_vnf_flavors()

Get available VNF flavors.



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
    # Get available VNF flavors.
    api_response = api_instance.get_vnf_flavors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_vnf_flavors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VNFFlavor]**](VNFFlavor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

