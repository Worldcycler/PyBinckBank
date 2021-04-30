# swagger_client.BalancesApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balances_get_account_balances**](BalancesApi.md#balances_get_account_balances) | **GET** /accounts/{accountNumber}/balances | Balance info


# **balances_get_account_balances**
> BalancesResponse balances_get_account_balances(account_number)

Balance info

Get the balance for a specific account. This call can be used to get the spending limit and total asset value.

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
api_instance = swagger_client.BalancesApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number.

try:
    # Balance info
    api_response = api_instance.balances_get_account_balances(account_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancesApi->balances_get_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number. | 

### Return type

[**BalancesResponse**](BalancesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

