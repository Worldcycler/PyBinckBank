# swagger_client.NewsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**news_get_news**](NewsApi.md#news_get_news) | **GET** /news | All


# **news_get_news**
> NewsResponseModel news_get_news(account_number, from_date=from_date, to_date=to_date, instrument_ids=instrument_ids, range=range)

All

Get news for the specified selection. The first 250 news messages for the selection in the news history are available.

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
api_instance = swagger_client.NewsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
from_date = '2013-10-20T19:20:30+01:00' # datetime | Optional start date, if left out, fromDate will be today. If no instrument ids are supplied, only dates from the  last month are accepted, otherwise only dates from the last week are accepted. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Optional end date, do not combine with instruments. (optional)
instrument_ids = 'instrument_ids_example' # str | Optional ids of the instruments to retrieve.  If there are multiple ids, separate them by commas. (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # All
    api_response = api_instance.news_get_news(account_number, from_date=from_date, to_date=to_date, instrument_ids=instrument_ids, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->news_get_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **from_date** | **datetime**| Optional start date, if left out, fromDate will be today. If no instrument ids are supplied, only dates from the  last month are accepted, otherwise only dates from the last week are accepted. | [optional] 
 **to_date** | **datetime**| Optional end date, do not combine with instruments. | [optional] 
 **instrument_ids** | **str**| Optional ids of the instruments to retrieve.  If there are multiple ids, separate them by commas. | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**NewsResponseModel**](NewsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

