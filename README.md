# swagger-client
  BinckBank OpenAPI is an API Platform to access BinckBank's trading services.    Curious? Request your access key after reading the documentation on Github: https://github.com/binckbank-api/client-js#binck-openapi-documentation    

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://api.sandbox.binck.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**accounts_get_account**](docs/AccountsApi.md#accounts_get_account) | **GET** /accounts/{accountNumber} | Account info
*AccountsApi* | [**accounts_get_accounts**](docs/AccountsApi.md#accounts_get_accounts) | **GET** /accounts | All
*BalancesApi* | [**balances_get_account_balances**](docs/BalancesApi.md#balances_get_account_balances) | **GET** /accounts/{accountNumber}/balances | Balance info
*InstrumentsApi* | [**instruments_get_bonds**](docs/InstrumentsApi.md#instruments_get_bonds) | **GET** /instruments/bonds | Bonds
*InstrumentsApi* | [**instruments_get_certificates**](docs/InstrumentsApi.md#instruments_get_certificates) | **GET** /instruments/certificates | Certificates
*InstrumentsApi* | [**instruments_get_derivatives**](docs/InstrumentsApi.md#instruments_get_derivatives) | **GET** /instruments/derivatives | Derivatives
*InstrumentsApi* | [**instruments_get_instrument**](docs/InstrumentsApi.md#instruments_get_instrument) | **GET** /instruments/{id} | Instrument info
*InstrumentsApi* | [**instruments_get_instruments**](docs/InstrumentsApi.md#instruments_get_instruments) | **GET** /instruments | Find instrument
*InstrumentsApi* | [**instruments_get_leveraged_products**](docs/InstrumentsApi.md#instruments_get_leveraged_products) | **GET** /instruments/leveragedproducts | Leveraged products
*InstrumentsApi* | [**instruments_get_list_contents**](docs/InstrumentsApi.md#instruments_get_list_contents) | **GET** /instruments/lists/{id} | Instrument list
*InstrumentsApi* | [**instruments_read_kid_document**](docs/InstrumentsApi.md#instruments_read_kid_document) | **GET** /instruments/{id}/kid/{kidId} | KID document
*InstrumentsApi* | [**instruments_search_kid_document**](docs/InstrumentsApi.md#instruments_search_kid_document) | **GET** /instruments/{id}/kid | KID availability
*NewsApi* | [**news_get_news**](docs/NewsApi.md#news_get_news) | **GET** /news | All
*OrdersApi* | [**orders_cancel_order**](docs/OrdersApi.md#orders_cancel_order) | **DELETE** /accounts/{accountNumber}/orders/{number} | Cancellation
*OrdersApi* | [**orders_get_historical_orders**](docs/OrdersApi.md#orders_get_historical_orders) | **GET** /accounts/{accountNumber}/orders/history | History
*OrdersApi* | [**orders_get_order**](docs/OrdersApi.md#orders_get_order) | **GET** /accounts/{accountNumber}/orders/{number} | Order info
*OrdersApi* | [**orders_get_orders**](docs/OrdersApi.md#orders_get_orders) | **GET** /accounts/{accountNumber}/orders | Recent
*OrdersApi* | [**orders_modify_order**](docs/OrdersApi.md#orders_modify_order) | **PATCH** /accounts/{accountNumber}/orders/{number} | Modification
*OrdersApi* | [**orders_preview_modify_order**](docs/OrdersApi.md#orders_preview_modify_order) | **POST** /accounts/{accountNumber}/orders/{number}/preview | Validate modification
*OrdersApi* | [**orders_preview_order**](docs/OrdersApi.md#orders_preview_order) | **POST** /accounts/{accountNumber}/orders/preview | Validate new
*OrdersApi* | [**orders_preview_order_costs**](docs/OrdersApi.md#orders_preview_order_costs) | **POST** /accounts/{accountNumber}/orders/costs | Costs
*OrdersApi* | [**orders_register_order**](docs/OrdersApi.md#orders_register_order) | **POST** /accounts/{accountNumber}/orders | New
*PerformancesApi* | [**performances_get_performance**](docs/PerformancesApi.md#performances_get_performance) | **GET** /accounts/{accountNumber}/performances/{year} | Year
*PerformancesApi* | [**performances_get_performances**](docs/PerformancesApi.md#performances_get_performances) | **GET** /accounts/{accountNumber}/performances | All
*PositionsApi* | [**positions_get_position**](docs/PositionsApi.md#positions_get_position) | **GET** /accounts/{accountNumber}/positions/{instrumentId} | Position info
*PositionsApi* | [**positions_get_positions**](docs/PositionsApi.md#positions_get_positions) | **GET** /accounts/{accountNumber}/positions | All
*QuotesApi* | [**quotes_get_historical_quotes**](docs/QuotesApi.md#quotes_get_historical_quotes) | **GET** /quotes/{instrumentId}/history | History
*QuotesApi* | [**quotes_get_quotes**](docs/QuotesApi.md#quotes_get_quotes) | **GET** /quotes | Latest
*SessionsApi* | [**sessions_end_session**](docs/SessionsApi.md#sessions_end_session) | **DELETE** /sessions | Sign out
*SessionsApi* | [**sessions_get_sessions**](docs/SessionsApi.md#sessions_get_sessions) | **GET** /sessions | All
*SettingsApi* | [**settings_get_settings**](docs/SettingsApi.md#settings_get_settings) | **GET** /accounts/{accountNumber}/settings | All
*TransactionsApi* | [**transactions_get_transactions**](docs/TransactionsApi.md#transactions_get_transactions) | **GET** /accounts/{accountNumber}/transactions | All
*VersionApi* | [**version_get_version**](docs/VersionApi.md#version_get_version) | **GET** /version | API version


## Documentation For Models

 - [AccountModel](docs/AccountModel.md)
 - [AccountNumberQueryParam](docs/AccountNumberQueryParam.md)
 - [AccountsCollectionModel](docs/AccountsCollectionModel.md)
 - [AccountsResponse](docs/AccountsResponse.md)
 - [BalanceModel](docs/BalanceModel.md)
 - [BalancesCollectionModel](docs/BalancesCollectionModel.md)
 - [BalancesResponse](docs/BalancesResponse.md)
 - [BondInfoModel](docs/BondInfoModel.md)
 - [BondsQueryParams](docs/BondsQueryParams.md)
 - [CashBalanceModel](docs/CashBalanceModel.md)
 - [CashBalancesCollectionModel](docs/CashBalancesCollectionModel.md)
 - [CertificatesQueryParams](docs/CertificatesQueryParams.md)
 - [CurrencyQueryParams](docs/CurrencyQueryParams.md)
 - [DateRangeQueryParams](docs/DateRangeQueryParams.md)
 - [DerivativeClassInfoModel](docs/DerivativeClassInfoModel.md)
 - [DerivativeSeriesInfoModel](docs/DerivativeSeriesInfoModel.md)
 - [DerivativesCollectionModel](docs/DerivativesCollectionModel.md)
 - [DerivativesInfoModel](docs/DerivativesInfoModel.md)
 - [DerivativesResponseModel](docs/DerivativesResponseModel.md)
 - [ErrorMessageModel](docs/ErrorMessageModel.md)
 - [HistoricalOrdersQueryParams](docs/HistoricalOrdersQueryParams.md)
 - [HistoricalQuoteModel](docs/HistoricalQuoteModel.md)
 - [HistoricalQuoteRequestQueryParams](docs/HistoricalQuoteRequestQueryParams.md)
 - [HistoricalQuotesCollectionModel](docs/HistoricalQuotesCollectionModel.md)
 - [HistoricalQuotesResponseModel](docs/HistoricalQuotesResponseModel.md)
 - [InstrumentBriefModel](docs/InstrumentBriefModel.md)
 - [InstrumentDerivativesQueryParams](docs/InstrumentDerivativesQueryParams.md)
 - [InstrumentModel](docs/InstrumentModel.md)
 - [InstrumentsCollectionModel](docs/InstrumentsCollectionModel.md)
 - [InstrumentsQueryParams](docs/InstrumentsQueryParams.md)
 - [InstrumentsResponseModel](docs/InstrumentsResponseModel.md)
 - [KidCollectionModel](docs/KidCollectionModel.md)
 - [KidInfoModel](docs/KidInfoModel.md)
 - [KidResponseModel](docs/KidResponseModel.md)
 - [LeveragedProductInfoModel](docs/LeveragedProductInfoModel.md)
 - [LeveragedProductsQueryParams](docs/LeveragedProductsQueryParams.md)
 - [LogoffResponse](docs/LogoffResponse.md)
 - [MetadataModel](docs/MetadataModel.md)
 - [ModifyOrderModel](docs/ModifyOrderModel.md)
 - [MutationGroupQueryParams](docs/MutationGroupQueryParams.md)
 - [NewOrderModel](docs/NewOrderModel.md)
 - [NewOrderModelCash](docs/NewOrderModelCash.md)
 - [NewOrderModelFuture](docs/NewOrderModelFuture.md)
 - [NewOrderModelOption](docs/NewOrderModelOption.md)
 - [NewOrderModelOptionLeg](docs/NewOrderModelOptionLeg.md)
 - [NewOrderModelSrd](docs/NewOrderModelSrd.md)
 - [NewsCollectionModel](docs/NewsCollectionModel.md)
 - [NewsItemModel](docs/NewsItemModel.md)
 - [NewsRequestQueryParams](docs/NewsRequestQueryParams.md)
 - [NewsResponseModel](docs/NewsResponseModel.md)
 - [NewsSubscriptionCollectionModel](docs/NewsSubscriptionCollectionModel.md)
 - [NewsSubscriptionModel](docs/NewsSubscriptionModel.md)
 - [OrderCostsCollectionModel](docs/OrderCostsCollectionModel.md)
 - [OrderCostsForCategoryModel](docs/OrderCostsForCategoryModel.md)
 - [OrderCostsForLegModel](docs/OrderCostsForLegModel.md)
 - [OrderCostsForSubCategoryModel](docs/OrderCostsForSubCategoryModel.md)
 - [OrderCostsResponse](docs/OrderCostsResponse.md)
 - [OrderModel](docs/OrderModel.md)
 - [OrderResponse](docs/OrderResponse.md)
 - [OrdersCollectionModel](docs/OrdersCollectionModel.md)
 - [OrdersQueryParams](docs/OrdersQueryParams.md)
 - [OrdersResponse](docs/OrdersResponse.md)
 - [PaginationQueryParam](docs/PaginationQueryParam.md)
 - [PagingModel](docs/PagingModel.md)
 - [PerformanceCollectionModel](docs/PerformanceCollectionModel.md)
 - [PerformanceDetailModel](docs/PerformanceDetailModel.md)
 - [PerformanceSummaryModel](docs/PerformanceSummaryModel.md)
 - [PerformancesQueryParams](docs/PerformancesQueryParams.md)
 - [PerformancesResponse](docs/PerformancesResponse.md)
 - [PositionAccruedInterest](docs/PositionAccruedInterest.md)
 - [PositionMargin](docs/PositionMargin.md)
 - [PositionModel](docs/PositionModel.md)
 - [PositionResponse](docs/PositionResponse.md)
 - [PositionResult](docs/PositionResult.md)
 - [PositionsCollectionModel](docs/PositionsCollectionModel.md)
 - [PositionsResponse](docs/PositionsResponse.md)
 - [PreviewOrderModel](docs/PreviewOrderModel.md)
 - [PreviewOrderResponse](docs/PreviewOrderResponse.md)
 - [PriceModel](docs/PriceModel.md)
 - [PriceOrderBookModel](docs/PriceOrderBookModel.md)
 - [PriceWithVolumeModel](docs/PriceWithVolumeModel.md)
 - [QuoteModel](docs/QuoteModel.md)
 - [QuoteRequestQueryParams](docs/QuoteRequestQueryParams.md)
 - [QuotesCollectionModel](docs/QuotesCollectionModel.md)
 - [QuotesResponseModel](docs/QuotesResponseModel.md)
 - [SessionModel](docs/SessionModel.md)
 - [SessionsCollectionModel](docs/SessionsCollectionModel.md)
 - [SessionsResponse](docs/SessionsResponse.md)
 - [SettingsCollectionModel](docs/SettingsCollectionModel.md)
 - [SettingsModel](docs/SettingsModel.md)
 - [SettingsResponse](docs/SettingsResponse.md)
 - [SrdInfoModel](docs/SrdInfoModel.md)
 - [StatusHistory](docs/StatusHistory.md)
 - [TickSizeStepModel](docs/TickSizeStepModel.md)
 - [TickSizesModel](docs/TickSizesModel.md)
 - [TradingProductModel](docs/TradingProductModel.md)
 - [TransactionCostComponentModel](docs/TransactionCostComponentModel.md)
 - [TransactionModel](docs/TransactionModel.md)
 - [TransactionsCollectionModel](docs/TransactionsCollectionModel.md)
 - [TransactionsResponse](docs/TransactionsResponse.md)
 - [VersionModel](docs/VersionModel.md)
 - [VolumeModel](docs/VolumeModel.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://login.sandbox.binck.com/am/oauth2/realms/{realm}/authorize
- **Scopes**: 
 - **read**: Read access to account(s) with portfolio.
 - **write**: Access to ordering.
 - **internal**: Internal use.
 - **news**: Access to news.
 - **quotes**: Access to quotes.


## Author


