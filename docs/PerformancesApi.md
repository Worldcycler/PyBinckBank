# swagger_client.PerformancesApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**performances_get_performance**](PerformancesApi.md#performances_get_performance) | **GET** /accounts/{accountNumber}/performances/{year} | Year
[**performances_get_performances**](PerformancesApi.md#performances_get_performances) | **GET** /accounts/{accountNumber}/performances | All


# **performances_get_performance**
> PerformancesResponse performances_get_performance(year, account_number, on_position=on_position)

Year

Get the financial performance information for an account, per year. Only applicable for the years the account was active.

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
api_instance = swagger_client.PerformancesApi(swagger_client.ApiClient(configuration))
year = 56 # int | The year for the performance information.
account_number = 'account_number_example' # str | The account number.
on_position = true # bool | Performances can be calculated on position level or on instrument level. When 'onPosition' set to true,  the performance of all individual instruments will be reported. If set to false, the performance of   derivative instruments is included in the performance of the underlying instrument. (optional)

try:
    # Year
    api_response = api_instance.performances_get_performance(year, account_number, on_position=on_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformancesApi->performances_get_performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| The year for the performance information. | 
 **account_number** | **str**| The account number. | 
 **on_position** | **bool**| Performances can be calculated on position level or on instrument level. When &#39;onPosition&#39; set to true,  the performance of all individual instruments will be reported. If set to false, the performance of   derivative instruments is included in the performance of the underlying instrument. | [optional] 

### Return type

[**PerformancesResponse**](PerformancesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performances_get_performances**
> PerformancesResponse performances_get_performances(account_number)

All

Get the financial performance information for an account.

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
api_instance = swagger_client.PerformancesApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number.

try:
    # All
    api_response = api_instance.performances_get_performances(account_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformancesApi->performances_get_performances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number. | 

### Return type

[**PerformancesResponse**](PerformancesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

