# coding: utf-8

"""
    BinckBank.OpenApi

      BinckBank OpenAPI is an API Platform to access BinckBank's trading services.    Curious? Request your access key after reading the documentation on Github: https://github.com/binckbank-api/client-js#binck-openapi-documentation      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TransactionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transactions_get_transactions(self, account_number, **kwargs):  # noqa: E501
        """All  # noqa: E501

        Get the transactions for an account. The response not only includes the executed orders, but also withdrawals and deposits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transactions_get_transactions(account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_number: An account number (required)
        :param str range: Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21)
        :param datetime from_date: Date from which to filter. Format YYYY-MM-DD
        :param datetime to_date: Date to which to filter. Format YYYY-MM-DD
        :param str mutation_group: Mutation groups (with enums)<br />  BuyAndSell includes : <br />    AssignmentCall<br />    AssignmentPut<br />    ExcerciseCall<br />    ExcercisePut<br />    Buy<br />    OpeningBuy  <br />    OpeningBuyFutures<br />    Sell<br />    OpeningSell<br />    OpeningSellFutures<br />    ClosingBuy<br />    ClosingBuyFutures<br />    ClosingSell<br />    ClosingSellFutures<br />  Cost includes : <br />    SettlementCosts<br />  CouponPayment includes : <br />    SecuritiesLendingCouponPayment<br />    CouponPayment<br />  DividendPayment includes : <br />    SecuritiesLendingDividendPayment<br />    DividendPayment<br />  InterestPayment includes : <br />    CreditInterest<br />    DebitInterest<br />  MoneyTransfer includes : <br />    ExternalTransfer<br />    InternalTransfer<br />    OnlineMoneyTransfer<br />    Regulation<br />  PositionMutation includes : <br />    Buy<br />    Sell<br />
        :param str currency: 3-letter currency code (ISO 4217)
        :return: TransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transactions_get_transactions_with_http_info(account_number, **kwargs)  # noqa: E501
        else:
            (data) = self.transactions_get_transactions_with_http_info(account_number, **kwargs)  # noqa: E501
            return data

    def transactions_get_transactions_with_http_info(self, account_number, **kwargs):  # noqa: E501
        """All  # noqa: E501

        Get the transactions for an account. The response not only includes the executed orders, but also withdrawals and deposits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transactions_get_transactions_with_http_info(account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_number: An account number (required)
        :param str range: Paging parameter to retrieve a subset of the complete collection. Format is &lt;offset&gt;-&lt;limit&gt;.   Both values are an offset from the first entry of the complete collection. The first entry has offset '0'.  (e.g. 12-21)
        :param datetime from_date: Date from which to filter. Format YYYY-MM-DD
        :param datetime to_date: Date to which to filter. Format YYYY-MM-DD
        :param str mutation_group: Mutation groups (with enums)<br />  BuyAndSell includes : <br />    AssignmentCall<br />    AssignmentPut<br />    ExcerciseCall<br />    ExcercisePut<br />    Buy<br />    OpeningBuy  <br />    OpeningBuyFutures<br />    Sell<br />    OpeningSell<br />    OpeningSellFutures<br />    ClosingBuy<br />    ClosingBuyFutures<br />    ClosingSell<br />    ClosingSellFutures<br />  Cost includes : <br />    SettlementCosts<br />  CouponPayment includes : <br />    SecuritiesLendingCouponPayment<br />    CouponPayment<br />  DividendPayment includes : <br />    SecuritiesLendingDividendPayment<br />    DividendPayment<br />  InterestPayment includes : <br />    CreditInterest<br />    DebitInterest<br />  MoneyTransfer includes : <br />    ExternalTransfer<br />    InternalTransfer<br />    OnlineMoneyTransfer<br />    Regulation<br />  PositionMutation includes : <br />    Buy<br />    Sell<br />
        :param str currency: 3-letter currency code (ISO 4217)
        :return: TransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_number', 'range', 'from_date', 'to_date', 'mutation_group', 'currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transactions_get_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_number' is set
        if self.api_client.client_side_validation and ('account_number' not in params or
                                                       params['account_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_number` when calling `transactions_get_transactions`")  # noqa: E501

        if self.api_client.client_side_validation and ('range' in params and not re.search(r'[0-9]+-[0-9]*', params['range'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `range` when calling `transactions_get_transactions`, must conform to the pattern `/[0-9]+-[0-9]*/`")  # noqa: E501
        if self.api_client.client_side_validation and ('currency' in params and not re.search(r'^[a-zA-Z]{3}$', params['currency'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency` when calling `transactions_get_transactions`, must conform to the pattern `/^[a-zA-Z]{3}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'account_number' in params:
            path_params['accountNumber'] = params['account_number']  # noqa: E501

        query_params = []
        if 'range' in params:
            query_params.append(('range', params['range']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'mutation_group' in params:
            query_params.append(('mutationGroup', params['mutation_group']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountNumber}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
