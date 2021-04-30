# swagger_client.QuotesApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotes_get_historical_quotes**](QuotesApi.md#quotes_get_historical_quotes) | **GET** /quotes/{instrumentId}/history | History
[**quotes_get_quotes**](QuotesApi.md#quotes_get_quotes) | **GET** /quotes | Latest


# **quotes_get_historical_quotes**
> HistoricalQuotesResponseModel quotes_get_historical_quotes(instrument_id, account_number, from_date_time, interval, to_date_time=to_date_time)

History

Get historical quotes for an instrument over a period. The different intervals each have different maximum period lengths, ranging from five days for one minute, to 10 years for one week.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
instrument_id = 'instrument_id_example' # str | The Id of the instrument for which the historical quotes will be retrieved
account_number = 'account_number_example' # str | Mandatory account number
from_date_time = '2013-10-20T19:20:30+01:00' # datetime | The start moment of historical quotes
interval = 'interval_example' # str | Interval for historical quotes  Depending on the interval, the historical quotes collection returned will be limited to a certain period:  Max. number of days for one minute interval is 5.  Max. number of days for five minute interval is 20.  Max. number of days for ten minute interval is 20.  Max. number of days for fifteen minute interval is 60.  Max. number of days for one hour interval is 120.  Max. number of years for one day interval is 10.  Max. number of years for one week interval is 10.
to_date_time = '2013-10-20T19:20:30+01:00' # datetime | The end moment of historical quotes, defaulting to the Current date and time according to UTC time standard (optional)

try:
    # History
    api_response = api_instance.quotes_get_historical_quotes(instrument_id, account_number, from_date_time, interval, to_date_time=to_date_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_get_historical_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **str**| The Id of the instrument for which the historical quotes will be retrieved | 
 **account_number** | **str**| Mandatory account number | 
 **from_date_time** | **datetime**| The start moment of historical quotes | 
 **interval** | **str**| Interval for historical quotes  Depending on the interval, the historical quotes collection returned will be limited to a certain period:  Max. number of days for one minute interval is 5.  Max. number of days for five minute interval is 20.  Max. number of days for ten minute interval is 20.  Max. number of days for fifteen minute interval is 60.  Max. number of days for one hour interval is 120.  Max. number of years for one day interval is 10.  Max. number of years for one week interval is 10. | 
 **to_date_time** | **datetime**| The end moment of historical quotes, defaulting to the Current date and time according to UTC time standard | [optional] 

### Return type

[**HistoricalQuotesResponseModel**](HistoricalQuotesResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotes_get_quotes**
> QuotesResponseModel quotes_get_quotes(account_number, instrument_ids, level=level, range=range)

Latest

Get current quotes and quote subscription (realtime/delayed) for one or more instruments.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
instrument_ids = 'instrument_ids_example' # str | Ids of the instruments to retrieve. If there are multiple ids, separate them by commas.
level = 'level_example' # str | The maximal quote level returned (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Latest
    api_response = api_instance.quotes_get_quotes(account_number, instrument_ids, level=level, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_get_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **instrument_ids** | **str**| Ids of the instruments to retrieve. If there are multiple ids, separate them by commas. | 
 **level** | **str**| The maximal quote level returned | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**QuotesResponseModel**](QuotesResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

