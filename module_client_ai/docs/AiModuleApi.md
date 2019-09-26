# swagger_client.AiModuleApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sfcr_event**](AiModuleApi.md#sfcr_event) | **POST** /sfcr_event | Notify AI module of SFC request arrival / departure event.


# **sfcr_event**
> sfcr_event()

Notify AI module of SFC request arrival / departure event.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AiModuleApi()

try:
    # Notify AI module of SFC request arrival / departure event.
    api_instance.sfcr_event()
except ApiException as e:
    print("Exception when calling AiModuleApi->sfcr_event: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

