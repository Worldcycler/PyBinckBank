# swagger_client.TransactionsApi

All URIs are relative to *http://api.sandbox.binck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_get_transactions**](TransactionsApi.md#transactions_get_transactions) | **GET** /accounts/{accountNumber}/transactions | All


# **transactions_get_transactions**
> TransactionsResponse transactions_get_transactions(account_number, range=range, from_date=from_date, to_date=to_date, mutation_group=mutation_group, currency=currency)

All

Get the transactions for an account. The response not only includes the executed orders, but also withdrawals and deposits.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | An account number
range = 'range_example' # str | Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21) (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Date from which to filter. Format YYYY-MM-DD (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Date to which to filter. Format YYYY-MM-DD (optional)
mutation_group = 'mutation_group_example' # str | Mutation groups (with enums)<br />  BuyAndSell includes : <br />    AssignmentCall<br />    AssignmentPut<br />    ExcerciseCall<br />    ExcercisePut<br />    Buy<br />    OpeningBuy  <br />    OpeningBuyFutures<br />    Sell<br />    OpeningSell<br />    OpeningSellFutures<br />    ClosingBuy<br />    ClosingBuyFutures<br />    ClosingSell<br />    ClosingSellFutures<br />  Cost includes : <br />    SettlementCosts<br />  CouponPayment includes : <br />    SecuritiesLendingCouponPayment<br />    CouponPayment<br />  DividendPayment includes : <br />    SecuritiesLendingDividendPayment<br />    DividendPayment<br />  InterestPayment includes : <br />    CreditInterest<br />    DebitInterest<br />  MoneyTransfer includes : <br />    ExternalTransfer<br />    InternalTransfer<br />    OnlineMoneyTransfer<br />    Regulation<br />  PositionMutation includes : <br />    Buy<br />    Sell<br /> (optional)
currency = 'currency_example' # str | 3-letter currency code (ISO 4217) (optional)

try:
    # All
    api_response = api_instance.transactions_get_transactions(account_number, range=range, from_date=from_date, to_date=to_date, mutation_group=mutation_group, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| An account number | 
 **range** | **str**| Paging parameter to retrieve a subset of the complete collection. Format is &amp;lt;offset&amp;gt;-&amp;lt;limit&amp;gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset &#39;0&#39;.  (e.g. 12-21) | [optional] 
 **from_date** | **datetime**| Date from which to filter. Format YYYY-MM-DD | [optional] 
 **to_date** | **datetime**| Date to which to filter. Format YYYY-MM-DD | [optional] 
 **mutation_group** | **str**| Mutation groups (with enums)&lt;br /&gt;  BuyAndSell includes : &lt;br /&gt;    AssignmentCall&lt;br /&gt;    AssignmentPut&lt;br /&gt;    ExcerciseCall&lt;br /&gt;    ExcercisePut&lt;br /&gt;    Buy&lt;br /&gt;    OpeningBuy  &lt;br /&gt;    OpeningBuyFutures&lt;br /&gt;    Sell&lt;br /&gt;    OpeningSell&lt;br /&gt;    OpeningSellFutures&lt;br /&gt;    ClosingBuy&lt;br /&gt;    ClosingBuyFutures&lt;br /&gt;    ClosingSell&lt;br /&gt;    ClosingSellFutures&lt;br /&gt;  Cost includes : &lt;br /&gt;    SettlementCosts&lt;br /&gt;  CouponPayment includes : &lt;br /&gt;    SecuritiesLendingCouponPayment&lt;br /&gt;    CouponPayment&lt;br /&gt;  DividendPayment includes : &lt;br /&gt;    SecuritiesLendingDividendPayment&lt;br /&gt;    DividendPayment&lt;br /&gt;  InterestPayment includes : &lt;br /&gt;    CreditInterest&lt;br /&gt;    DebitInterest&lt;br /&gt;  MoneyTransfer includes : &lt;br /&gt;    ExternalTransfer&lt;br /&gt;    InternalTransfer&lt;br /&gt;    OnlineMoneyTransfer&lt;br /&gt;    Regulation&lt;br /&gt;  PositionMutation includes : &lt;br /&gt;    Buy&lt;br /&gt;    Sell&lt;br /&gt; | [optional] 
 **currency** | **str**| 3-letter currency code (ISO 4217) | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

