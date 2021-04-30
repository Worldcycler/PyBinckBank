# swagger_client.SettingsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_get_settings**](SettingsApi.md#settings_get_settings) | **GET** /accounts/{accountNumber}/settings | All


# **settings_get_settings**
> SettingsResponse settings_get_settings(account_number)

All

Get the trading settings for the specified account. If the settings return an empty list, trading is not allowed. This can be the case for a savings account, or if the account is not fully activated yet.

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number.

try:
    # All
    api_response = api_instance.settings_get_settings(account_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number. | 

### Return type

[**SettingsResponse**](SettingsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

