# swagger_client.AccountsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get_account**](AccountsApi.md#accounts_get_account) | **GET** /accounts/{accountNumber} | Account info
[**accounts_get_accounts**](AccountsApi.md#accounts_get_accounts) | **GET** /accounts | All


# **accounts_get_account**
> AccountsResponse accounts_get_account(account_number)

Account info

Get the specific account details. Only active accounts are returned.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number.

try:
    # Account info
    api_response = api_instance.accounts_get_account(account_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number. | 

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_accounts**
> AccountsResponse accounts_get_accounts()

All

Get all the active accounts of the customer. If there is no account, the collection will be empty.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))

try:
    # All
    api_response = api_instance.accounts_get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

