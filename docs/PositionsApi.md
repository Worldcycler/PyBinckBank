# swagger_client.PositionsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positions_get_position**](PositionsApi.md#positions_get_position) | **GET** /accounts/{accountNumber}/positions/{instrumentId} | Position info
[**positions_get_positions**](PositionsApi.md#positions_get_positions) | **GET** /accounts/{accountNumber}/positions | All


# **positions_get_position**
> PositionResponse positions_get_position(account_number, instrument_id)

Position info

Get a specific position. Positions are identified by the instrument.

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
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | An account number.
instrument_id = 'instrument_id_example' # str | The id of the requested instrument.

try:
    # Position info
    api_response = api_instance.positions_get_position(account_number, instrument_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_get_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| An account number. | 
 **instrument_id** | **str**| The id of the requested instrument. | 

### Return type

[**PositionResponse**](PositionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_get_positions**
> PositionsResponse positions_get_positions(account_number, range=range)

All

Get the instrument positions of an account (portfolio). If there is no position, the collection will be empty.

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
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | An account number.
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # All
    api_response = api_instance.positions_get_positions(account_number, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_get_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| An account number. | 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**PositionsResponse**](PositionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

