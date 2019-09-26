# swagger_client.TrafgenApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sfcr**](TrafgenApi.md#add_sfcr) | **POST** /sfcr | Add new SFC request.


# **add_sfcr**
> add_sfcr(body)

Add new SFC request.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TrafgenApi()
body = swagger_client.SFCR() # SFCR | SFC request object to be added.

try:
    # Add new SFC request.
    api_instance.add_sfcr(body)
except ApiException as e:
    print("Exception when calling TrafgenApi->add_sfcr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SFCR**](SFCR.md)| SFC request object to be added. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

