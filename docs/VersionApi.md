# swagger_client.VersionApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get_version**](VersionApi.md#version_get_version) | **GET** /version | API version


# **version_get_version**
> VersionModel version_get_version()

API version

Get the version and the date of build of the API-service. This is the only call available without Bearer token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.VersionApi(swagger_client.ApiClient(configuration))

try:
    # API version
    api_response = api_instance.version_get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->version_get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionModel**](VersionModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

