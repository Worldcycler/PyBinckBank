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


class SettingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def settings_get_settings(self, account_number, **kwargs):  # noqa: E501
        """All  # noqa: E501

        Get the trading settings for the specified account. If the settings return an empty list, trading is not allowed. This can be the case for a savings account, or if the account is not fully activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_get_settings(account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_number: The account number. (required)
        :return: SettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settings_get_settings_with_http_info(account_number, **kwargs)  # noqa: E501
        else:
            (data) = self.settings_get_settings_with_http_info(account_number, **kwargs)  # noqa: E501
            return data

    def settings_get_settings_with_http_info(self, account_number, **kwargs):  # noqa: E501
        """All  # noqa: E501

        Get the trading settings for the specified account. If the settings return an empty list, trading is not allowed. This can be the case for a savings account, or if the account is not fully activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_get_settings_with_http_info(account_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_number: The account number. (required)
        :return: SettingsResponse
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
                    " to method settings_get_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_number' is set
        if self.api_client.client_side_validation and ('account_number' not in params or
                                                       params['account_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_number` when calling `settings_get_settings`")  # noqa: E501

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
            '/accounts/{accountNumber}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
