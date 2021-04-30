# swagger_client.SessionsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessions_end_session**](SessionsApi.md#sessions_end_session) | **DELETE** /sessions | Sign out
[**sessions_get_sessions**](SessionsApi.md#sessions_get_sessions) | **GET** /sessions | All


# **sessions_end_session**
> LogoffResponse sessions_end_session()

Sign out

Close the active session. Sessions must be closed before starting a new one, because there is a limit on the number of active sessions.

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
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))

try:
    # Sign out
    api_response = api_instance.sessions_end_session()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_end_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogoffResponse**](LogoffResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get_sessions**
> SessionsResponse sessions_get_sessions()

All

Get the current active sessions. Only for internal use.

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
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))

try:
    # All
    api_response = api_instance.sessions_get_sessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_get_sessions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionsResponse**](SessionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

