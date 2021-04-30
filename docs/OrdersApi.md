# swagger_client.OrdersApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_cancel_order**](OrdersApi.md#orders_cancel_order) | **DELETE** /accounts/{accountNumber}/orders/{number} | Cancellation
[**orders_get_historical_orders**](OrdersApi.md#orders_get_historical_orders) | **GET** /accounts/{accountNumber}/orders/history | History
[**orders_get_order**](OrdersApi.md#orders_get_order) | **GET** /accounts/{accountNumber}/orders/{number} | Order info
[**orders_get_orders**](OrdersApi.md#orders_get_orders) | **GET** /accounts/{accountNumber}/orders | Recent
[**orders_modify_order**](OrdersApi.md#orders_modify_order) | **PATCH** /accounts/{accountNumber}/orders/{number} | Modification
[**orders_preview_modify_order**](OrdersApi.md#orders_preview_modify_order) | **POST** /accounts/{accountNumber}/orders/{number}/preview | Validate modification
[**orders_preview_order**](OrdersApi.md#orders_preview_order) | **POST** /accounts/{accountNumber}/orders/preview | Validate new
[**orders_preview_order_costs**](OrdersApi.md#orders_preview_order_costs) | **POST** /accounts/{accountNumber}/orders/costs | Costs
[**orders_register_order**](OrdersApi.md#orders_register_order) | **POST** /accounts/{accountNumber}/orders | New


# **orders_cancel_order**
> OrderResponse orders_cancel_order(account_number, number)

Cancellation

Cancel an order. Allowed for open orders.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number used to register the order.
number = 789 # int | The order number for this account.

try:
    # Cancellation
    api_response = api_instance.orders_cancel_order(account_number, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number used to register the order. | 
 **number** | **int**| The order number for this account. | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get_historical_orders**
> OrdersResponse orders_get_historical_orders(account_number, year, month, range=range)

History

Get all the historical orders of an account. The response contains the historical orders of the requested month. If there is no order yet, the collection will be empty.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number.
year = 789 # int | The year for which the historical orders should be retrieved
month = 789 # int | The month for which the historical orders should be retrieved
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # History
    api_response = api_instance.orders_get_historical_orders(account_number, year, month, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get_historical_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number. | 
 **year** | **int**| The year for which the historical orders should be retrieved | 
 **month** | **int**| The month for which the historical orders should be retrieved | 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get_order**
> OrderResponse orders_get_order(account_number, number, include_status_history=include_status_history)

Order info

Get a specific order for an account. If the order has multiple legs, multiple order objects are returned.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number used to register the order.
number = 789 # int | The order number for this account.
include_status_history = true # bool | When set to True, order will include a detailed status history overview. When set to False, the response doesn't contain the status history, but the request will be handled faster. Default is True. (optional)

try:
    # Order info
    api_response = api_instance.orders_get_order(account_number, number, include_status_history=include_status_history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number used to register the order. | 
 **number** | **int**| The order number for this account. | 
 **include_status_history** | **bool**| When set to True, order will include a detailed status history overview. When set to False, the response doesn&#39;t contain the status history, but the request will be handled faster. Default is True. | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get_orders**
> OrdersResponse orders_get_orders(account_number, status=status, include_status_history=include_status_history, range=range)

Recent

Get all active/recent orders of an account. The response contains the active, cancelled and recent orders. If there is no order, the collection will be empty.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number.
status = 'status_example' # str | Status 'all' will select all the orders. Other possible values are 'open', 'executed' and 'canceled'. (optional)
include_status_history = true # bool | When set to True, orders will include a detailed status history overview. When set to false the response doesn't contain the status history, but the request will be handled faster. Default is True. (optional)
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)

try:
    # Recent
    api_response = api_instance.orders_get_orders(account_number, status=status, include_status_history=include_status_history, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number. | 
 **status** | **str**| Status &#39;all&#39; will select all the orders. Other possible values are &#39;open&#39;, &#39;executed&#39; and &#39;canceled&#39;. | [optional] 
 **include_status_history** | **bool**| When set to True, orders will include a detailed status history overview. When set to false the response doesn&#39;t contain the status history, but the request will be handled faster. Default is True. | [optional] 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_modify_order**
> OrderResponse orders_modify_order(account_number, number, modified_order)

Modification

Modify an existing order. First, make sure the modification is valid by doing a preview.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | An account number.
number = 789 # int | The order number.
modified_order = swagger_client.ModifyOrderModel() # ModifyOrderModel | Modifications to be used for the order.

try:
    # Modification
    api_response = api_instance.orders_modify_order(account_number, number, modified_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| An account number. | 
 **number** | **int**| The order number. | 
 **modified_order** | [**ModifyOrderModel**](ModifyOrderModel.md)| Modifications to be used for the order. | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_preview_modify_order**
> PreviewOrderResponse orders_preview_modify_order(account_number, number, modified_order)

Validate modification

Validate the modification of an order. This allows you to validate an order modification without sending it to the market. The order will not be created.  The response will contain information about if the order can be processed.  It also might include warnings to show to the customer. And confirmations, which are warnings to be approved by the customer, before placing the order modification.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | An account number.
number = 789 # int | The order number.
modified_order = swagger_client.ModifyOrderModel() # ModifyOrderModel | Modifications to be used for the order.

try:
    # Validate modification
    api_response = api_instance.orders_preview_modify_order(account_number, number, modified_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_preview_modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| An account number. | 
 **number** | **int**| The order number. | 
 **modified_order** | [**ModifyOrderModel**](ModifyOrderModel.md)| Modifications to be used for the order. | 

### Return type

[**PreviewOrderResponse**](PreviewOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_preview_order**
> PreviewOrderResponse orders_preview_order(account_number, new_order)

Validate new

Preview an order. This allows you to validate an order without sending it to the market. The order will not be created. The response will contain information about if the order can be processed.  It also includes warnings to show to the customer. And confirmations, which are warnings to be approved by the customer, before placing the order.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number to register the order.
new_order = swagger_client.NewOrderModel() # NewOrderModel | Specifications to be used for the order.

try:
    # Validate new
    api_response = api_instance.orders_preview_order(account_number, new_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_preview_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number to register the order. | 
 **new_order** | [**NewOrderModel**](NewOrderModel.md)| Specifications to be used for the order. | 

### Return type

[**PreviewOrderResponse**](PreviewOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_preview_order_costs**
> OrderCostsResponse orders_preview_order_costs(account_number, new_order)

Costs

Preview the costs for an order. This allows you to check costs for an order without sending it to the market.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | The account number to register the order.
new_order = swagger_client.NewOrderModel() # NewOrderModel | Specifications to be used for the order.

try:
    # Costs
    api_response = api_instance.orders_preview_order_costs(account_number, new_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_preview_order_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The account number to register the order. | 
 **new_order** | [**NewOrderModel**](NewOrderModel.md)| Specifications to be used for the order. | 

### Return type

[**OrderCostsResponse**](OrderCostsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_register_order**
> OrderResponse orders_register_order(account_number, new_order)

New

Register an order to sent to the market. This order will be sent to the market and executed according to the specifications. Something to be aware of: the response of this call might arrive after the order event from the realtime feed.

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | An account number to register the order.
new_order = swagger_client.NewOrderModel() # NewOrderModel | Specifications to be used for the order.

try:
    # New
    api_response = api_instance.orders_register_order(account_number, new_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_register_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| An account number to register the order. | 
 **new_order** | [**NewOrderModel**](NewOrderModel.md)| Specifications to be used for the order. | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

