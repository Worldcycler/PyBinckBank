# coding: utf-8

"""
    BinckBank.OpenApi

      BinckBank OpenAPI is an API Platform to access BinckBank's trading services.    Curious? Request your access key after reading the documentation on Github: https://github.com/binckbank-api/client-js#binck-openapi-documentation      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.transactions_api import TransactionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_transactions_get_transactions(self):
        """Test case for transactions_get_transactions

        All  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()