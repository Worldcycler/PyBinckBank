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


class PerformancesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def performances_get_performance(self, year, account_number, **kwargs):  # noqa: E501
        """Year  # noqa: E501

        Get the financial performance information for an account, per year. Only applicable for the years the account was active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.performances_get_performance(year, account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: The year for the performance information. (required)
        :param str account_number: The account number. (required)
        :param bool on_position: Performances can be calculated on position level or on instrument level. When 'onPosition' set to true,  the performance of all individual instruments will be reported. If set to false, the performance of   derivative instruments is included in the performance of the underlying instrument.
        :return: PerformancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.performances_get_performance_with_http_info(year, account_number, **kwargs)  # noqa: E501
        else:
            (data) = self.performances_get_performance_with_http_info(year, account_number, **kwargs)  # noqa: E501
            return data

    def performances_get_performance_with_http_info(self, year, account_number, **kwargs):  # noqa: E501
        """Year  # noqa: E501

        Get the financial performance information for an account, per year. Only applicable for the years the account was active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.performances_get_performance_with_http_info(year, account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: The year for the performance information. (required)
        :param str account_number: The account number. (required)
        :param bool on_position: Performances can be calculated on position level or on instrument level. When 'onPosition' set to true,  the performance of all individual instruments will be reported. If set to false, the performance of   derivative instruments is included in the performance of the underlying instrument.
        :return: PerformancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'account_number', 'on_position']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method performances_get_performance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `performances_get_performance`")  # noqa: E501
        # verify the required parameter 'account_number' is set
        if self.api_client.client_side_validation and ('account_number' not in params or
                                                       params['account_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_number` when calling `performances_get_performance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'year' in params:
            path_params['year'] = params['year']  # noqa: E501
        if 'account_number' in params:
            path_params['accountNumber'] = params['account_number']  # noqa: E501

        query_params = []
        if 'on_position' in params:
            query_params.append(('onPosition', params['on_position']))  # noqa: E501

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
            '/accounts/{accountNumber}/performances/{year}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PerformancesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def performances_get_performances(self, account_number, **kwargs):  # noqa: E501
        """All  # noqa: E501

        Get the financial performance information for an account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.performances_get_performances(account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_number: The account number. (required)
        :return: PerformancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.performances_get_performances_with_http_info(account_number, **kwargs)  # noqa: E501
        else:
            (data) = self.performances_get_performances_with_http_info(account_number, **kwargs)  # noqa: E501
            return data

    def performances_get_performances_with_http_info(self, account_number, **kwargs):  # noqa: E501
        """All  # noqa: E501

        Get the financial performance information for an account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.performances_get_performances_with_http_info(account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_number: The account number. (required)
        :return: PerformancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method performances_get_performances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_number' is set
        if self.api_client.client_side_validation and ('account_number' not in params or
                                                       params['account_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_number` when calling `performances_get_performances`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_number' in params:
            path_params['accountNumber'] = params['account_number']  # noqa: E501

        query_params = []

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
            '/accounts/{accountNumber}/performances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PerformancesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
