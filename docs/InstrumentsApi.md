# swagger_client.InstrumentsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_get_bonds**](InstrumentsApi.md#instruments_get_bonds) | **GET** /instruments/bonds | Bonds
[**instruments_get_certificates**](InstrumentsApi.md#instruments_get_certificates) | **GET** /instruments/certificates | Certificates
[**instruments_get_derivatives**](InstrumentsApi.md#instruments_get_derivatives) | **GET** /instruments/derivatives | Derivatives
[**instruments_get_instrument**](InstrumentsApi.md#instruments_get_instrument) | **GET** /instruments/{id} | Instrument info
[**instruments_get_instruments**](InstrumentsApi.md#instruments_get_instruments) | **GET** /instruments | Find instrument
[**instruments_get_leveraged_products**](InstrumentsApi.md#instruments_get_leveraged_products) | **GET** /instruments/leveragedproducts | Leveraged products
[**instruments_get_list_contents**](InstrumentsApi.md#instruments_get_list_contents) | **GET** /instruments/lists/{id} | Instrument list
[**instruments_read_kid_document**](InstrumentsApi.md#instruments_read_kid_document) | **GET** /instruments/{id}/kid/{kidId} | KID document
[**instruments_search_kid_document**](InstrumentsApi.md#instruments_search_kid_document) | **GET** /instruments/{id}/kid | KID availability


# **instruments_get_bonds**
> InstrumentsResponseModel instruments_get_bonds(account_number, type, include_tick_sizes=include_tick_sizes, range=range)

Bonds

Get Bonds information. Provide a name for the Type

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
type = 'type_example' # str | Name of the Bonds type
include_tick_sizes = true # bool | When set to true, the response will include a table with the TickSizes for the instrument, default = false (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Bonds
    api_response = api_instance.instruments_get_bonds(account_number, type, include_tick_sizes=include_tick_sizes, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_bonds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **type** | **str**| Name of the Bonds type | 
 **include_tick_sizes** | **bool**| When set to true, the response will include a table with the TickSizes for the instrument, default &#x3D; false | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**InstrumentsResponseModel**](InstrumentsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_certificates**
> InstrumentsResponseModel instruments_get_certificates(account_number, include_tick_sizes=include_tick_sizes, exchange=exchange, range=range)

Certificates

Get certificate information. Provide a name for the Exchange, when no name is specified, the default (SeDeX) will be used

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
include_tick_sizes = true # bool | When set to true, the response will include a table with the TickSizes for the instrument, default = false (optional)
exchange = 'exchange_example' # str | Name of the Exchange, default is 'certificatesSeDeX' (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Certificates
    api_response = api_instance.instruments_get_certificates(account_number, include_tick_sizes=include_tick_sizes, exchange=exchange, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **include_tick_sizes** | **bool**| When set to true, the response will include a table with the TickSizes for the instrument, default &#x3D; false | [optional] 
 **exchange** | **str**| Name of the Exchange, default is &#39;certificatesSeDeX&#39; | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**InstrumentsResponseModel**](InstrumentsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_derivatives**
> DerivativesResponseModel instruments_get_derivatives(account_number, symbol=symbol, underlying_instrument_id=underlying_instrument_id, market_identification_code=market_identification_code, currency=currency, range=range)

Derivatives

Get the series for a derivatives class (options/futures). This endpoint can be used to get an option or future sheet.  If there are two classes with the same symbol, mic and currency but different contract size (due to a corporate action), there are two sheets in the response.

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
symbol = 'symbol_example' # str | Selection on symbol.  Cannot be used in combination with 'UnderlyingInstrumentId'. (optional)
underlying_instrument_id = 'underlying_instrument_id_example' # str | Selection on the ID of the underlying equity.  Cannot be used in combination with 'symbol'. (optional)
market_identification_code = 'market_identification_code_example' # str | Can be used in combination with symbol to specify the market. (optional)
currency = 'currency_example' # str | Can be used in combination with symbol to specify the currency. (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Derivatives
    api_response = api_instance.instruments_get_derivatives(account_number, symbol=symbol, underlying_instrument_id=underlying_instrument_id, market_identification_code=market_identification_code, currency=currency, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_derivatives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **symbol** | **str**| Selection on symbol.  Cannot be used in combination with &#39;UnderlyingInstrumentId&#39;. | [optional] 
 **underlying_instrument_id** | **str**| Selection on the ID of the underlying equity.  Cannot be used in combination with &#39;symbol&#39;. | [optional] 
 **market_identification_code** | **str**| Can be used in combination with symbol to specify the market. | [optional] 
 **currency** | **str**| Can be used in combination with symbol to specify the currency. | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**DerivativesResponseModel**](DerivativesResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instrument**
> InstrumentsResponseModel instruments_get_instrument(id, account_number, include_tick_sizes=include_tick_sizes)

Instrument info

Get instrument information for a specific instrument. Multiple instruments can be retrieved if separated by comma, for example to get the instrument data from the positions (GET /instruments/{id1,id2}).

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Ids of the equity to retrieve. If there are multiple ids, separate them by commas.
account_number = 'account_number_example' # str | Mandatory account number
include_tick_sizes = true # bool | When set to true, the response will include a table with the TickSizes for the instrument, default = false (optional)

try:
    # Instrument info
    api_response = api_instance.instruments_get_instrument(id, account_number, include_tick_sizes=include_tick_sizes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Ids of the equity to retrieve. If there are multiple ids, separate them by commas. | 
 **account_number** | **str**| Mandatory account number | 
 **include_tick_sizes** | **bool**| When set to true, the response will include a table with the TickSizes for the instrument, default &#x3D; false | [optional] 

### Return type

[**InstrumentsResponseModel**](InstrumentsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instruments**
> InstrumentsResponseModel instruments_get_instruments(account_number, include_tick_sizes=include_tick_sizes, instrument_type=instrument_type, search_text=search_text, isin=isin, mic=mic, range=range)

Find instrument

Get instrument information. Parameter 'SearchText', or 'Isin' is required. 'Type' is optional, 'Mic' can only be used together with 'Isin'.

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
include_tick_sizes = true # bool | When set to true, the response will include a table with the TickSizes for the instrument, default = false (optional)
instrument_type = 'instrument_type_example' # str | Additional optional filter on instrument type. Cannot be used alone. (optional)
search_text = 'search_text_example' # str | Case insensitive search text, minimum length 2. Cannot be used in combination with 'Isin'. (optional)
isin = 'isin_example' # str | Selection on isinCode. Cannot be used in combination with 'SearchText'. (optional)
mic = 'mic_example' # str | Additional optional selection on Market Identification Code, to be used only in combination with 'Isin' (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Find instrument
    api_response = api_instance.instruments_get_instruments(account_number, include_tick_sizes=include_tick_sizes, instrument_type=instrument_type, search_text=search_text, isin=isin, mic=mic, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **include_tick_sizes** | **bool**| When set to true, the response will include a table with the TickSizes for the instrument, default &#x3D; false | [optional] 
 **instrument_type** | **str**| Additional optional filter on instrument type. Cannot be used alone. | [optional] 
 **search_text** | **str**| Case insensitive search text, minimum length 2. Cannot be used in combination with &#39;Isin&#39;. | [optional] 
 **isin** | **str**| Selection on isinCode. Cannot be used in combination with &#39;SearchText&#39;. | [optional] 
 **mic** | **str**| Additional optional selection on Market Identification Code, to be used only in combination with &#39;Isin&#39; | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**InstrumentsResponseModel**](InstrumentsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_leveraged_products**
> InstrumentsResponseModel instruments_get_leveraged_products(account_number, include_tick_sizes=include_tick_sizes, publisher=publisher, long_short=long_short, category=category, type=type, stoploss_min=stoploss_min, stoploss_max=stoploss_max, range=range)

Leveraged products

Get instrument information for leveraged products like Turbo's. Provide one or more filter criteria in the query parameters. When a filter value is not specified, the default value is used.

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | Mandatory account number
include_tick_sizes = true # bool | When set to true, the response will include a table with the TickSizes for the instrument, default = false (optional)
publisher = 'publisher_example' # str | Name of the publishing company, default is 'binckBank' (optional)
long_short = 'long_short_example' # str | Long or short, default is 'all' (both long and short) (optional)
category = 'category_example' # str | Category, default is 'indices' (optional)
type = 'type_example' # str | Specifies type (Turbo or XL), default is 'all' (both Turbo and XL) (optional)
stoploss_min = 3.4 # float | Specifies minimum stop loss (optional)
stoploss_max = 3.4 # float | Specifies maximum stop loss (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Leveraged products
    api_response = api_instance.instruments_get_leveraged_products(account_number, include_tick_sizes=include_tick_sizes, publisher=publisher, long_short=long_short, category=category, type=type, stoploss_min=stoploss_min, stoploss_max=stoploss_max, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_leveraged_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| Mandatory account number | 
 **include_tick_sizes** | **bool**| When set to true, the response will include a table with the TickSizes for the instrument, default &#x3D; false | [optional] 
 **publisher** | **str**| Name of the publishing company, default is &#39;binckBank&#39; | [optional] 
 **long_short** | **str**| Long or short, default is &#39;all&#39; (both long and short) | [optional] 
 **category** | **str**| Category, default is &#39;indices&#39; | [optional] 
 **type** | **str**| Specifies type (Turbo or XL), default is &#39;all&#39; (both Turbo and XL) | [optional] 
 **stoploss_min** | **float**| Specifies minimum stop loss | [optional] 
 **stoploss_max** | **float**| Specifies maximum stop loss | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**InstrumentsResponseModel**](InstrumentsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_list_contents**
> InstrumentsResponseModel instruments_get_list_contents(id, account_number, include_tick_sizes=include_tick_sizes, mic=mic, range=range)

Instrument list

Get a predefined list of instruments. List are a fast way to retrieve a group of instruments. Count in the response might be an 'educated guess'.

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id of the list
account_number = 'account_number_example' # str | Mandatory account number
include_tick_sizes = true # bool | When set to true, the response will include a table with the TickSizes for the instrument, default = false (optional)
mic = 'mic_example' # str | If specified, the response contains only instruments with this MarketIdentificationCode (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Instrument list
    api_response = api_instance.instruments_get_list_contents(id, account_number, include_tick_sizes=include_tick_sizes, mic=mic, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_list_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the list | 
 **account_number** | **str**| Mandatory account number | 
 **include_tick_sizes** | **bool**| When set to true, the response will include a table with the TickSizes for the instrument, default &#x3D; false | [optional] 
 **mic** | **str**| If specified, the response contains only instruments with this MarketIdentificationCode | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**InstrumentsResponseModel**](InstrumentsResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_read_kid_document**
> str instruments_read_kid_document(id, kid_id, account_number)

KID document

Get KID document. The document is a PDF file.

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Id of the equity to retrieve.
kid_id = 'kid_id_example' # str | Id of the Kid document.
account_number = 'account_number_example' # str | Mandatory account number

try:
    # KID document
    api_response = api_instance.instruments_read_kid_document(id, kid_id, account_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_read_kid_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the equity to retrieve. | 
 **kid_id** | **str**| Id of the Kid document. | 
 **account_number** | **str**| Mandatory account number | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: attachment/PDF

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_search_kid_document**
> KidResponseModel instruments_search_kid_document(id, account_number)

KID availability

Get KID document information for an instrument. Use this for instruments which have the isKidApplicable flag set to true. This endpoint searches for documentation. Still, it might be the case there is no documentation for a specific instrument, in the language of the customer. It can also be the case there are multiple documents for a certain instrument.

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
api_instance = swagger_client.InstrumentsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Id of the instrument.
account_number = 'account_number_example' # str | Mandatory account number

try:
    # KID availability
    api_response = api_instance.instruments_search_kid_document(id, account_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_search_kid_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the instrument. | 
 **account_number** | **str**| Mandatory account number | 

### Return type

[**KidResponseModel**](KidResponseModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

