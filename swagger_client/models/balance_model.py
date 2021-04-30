# coding: utf-8

"""
    BinckBank.OpenApi

      BinckBank OpenAPI is an API Platform to access BinckBank's trading services.    Curious? Request your access key after reading the documentation on Github: https://github.com/binckbank-api/client-js#binck-openapi-documentation      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class BalanceModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'assets_total_value': 'float',
        'cash_balance': 'float',
        'portfolio_value': 'float',
        'available_spending_limit': 'float',
        'available_spending_limit_srd': 'float',
        'cash_balances_collection': 'CashBalancesCollectionModel'
    }

    attribute_map = {
        'assets_total_value': 'assetsTotalValue',
        'cash_balance': 'cashBalance',
        'portfolio_value': 'portfolioValue',
        'available_spending_limit': 'availableSpendingLimit',
        'available_spending_limit_srd': 'availableSpendingLimitSrd',
        'cash_balances_collection': 'cashBalancesCollection'
    }

    def __init__(self, assets_total_value=None, cash_balance=None, portfolio_value=None, available_spending_limit=None, available_spending_limit_srd=None, cash_balances_collection=None, _configuration=None):  # noqa: E501
        """BalanceModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assets_total_value = None
        self._cash_balance = None
        self._portfolio_value = None
        self._available_spending_limit = None
        self._available_spending_limit_srd = None
        self._cash_balances_collection = None
        self.discriminator = None

        self.assets_total_value = assets_total_value
        self.cash_balance = cash_balance
        self.portfolio_value = portfolio_value
        if available_spending_limit is not None:
            self.available_spending_limit = available_spending_limit
        if available_spending_limit_srd is not None:
            self.available_spending_limit_srd = available_spending_limit_srd
        self.cash_balances_collection = cash_balances_collection

    @property
    def assets_total_value(self):
        """Gets the assets_total_value of this BalanceModel.  # noqa: E501

        Assets total value in Euro  # noqa: E501

        :return: The assets_total_value of this BalanceModel.  # noqa: E501
        :rtype: float
        """
        return self._assets_total_value

    @assets_total_value.setter
    def assets_total_value(self, assets_total_value):
        """Sets the assets_total_value of this BalanceModel.

        Assets total value in Euro  # noqa: E501

        :param assets_total_value: The assets_total_value of this BalanceModel.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and assets_total_value is None:
            raise ValueError("Invalid value for `assets_total_value`, must not be `None`")  # noqa: E501

        self._assets_total_value = assets_total_value

    @property
    def cash_balance(self):
        """Gets the cash_balance of this BalanceModel.  # noqa: E501

        Total cash balance in Euro  # noqa: E501

        :return: The cash_balance of this BalanceModel.  # noqa: E501
        :rtype: float
        """
        return self._cash_balance

    @cash_balance.setter
    def cash_balance(self, cash_balance):
        """Sets the cash_balance of this BalanceModel.

        Total cash balance in Euro  # noqa: E501

        :param cash_balance: The cash_balance of this BalanceModel.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and cash_balance is None:
            raise ValueError("Invalid value for `cash_balance`, must not be `None`")  # noqa: E501

        self._cash_balance = cash_balance

    @property
    def portfolio_value(self):
        """Gets the portfolio_value of this BalanceModel.  # noqa: E501

        Portfolio value  # noqa: E501

        :return: The portfolio_value of this BalanceModel.  # noqa: E501
        :rtype: float
        """
        return self._portfolio_value

    @portfolio_value.setter
    def portfolio_value(self, portfolio_value):
        """Sets the portfolio_value of this BalanceModel.

        Portfolio value  # noqa: E501

        :param portfolio_value: The portfolio_value of this BalanceModel.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and portfolio_value is None:
            raise ValueError("Invalid value for `portfolio_value`, must not be `None`")  # noqa: E501

        self._portfolio_value = portfolio_value

    @property
    def available_spending_limit(self):
        """Gets the available_spending_limit of this BalanceModel.  # noqa: E501

        Spending power  # noqa: E501

        :return: The available_spending_limit of this BalanceModel.  # noqa: E501
        :rtype: float
        """
        return self._available_spending_limit

    @available_spending_limit.setter
    def available_spending_limit(self, available_spending_limit):
        """Sets the available_spending_limit of this BalanceModel.

        Spending power  # noqa: E501

        :param available_spending_limit: The available_spending_limit of this BalanceModel.  # noqa: E501
        :type: float
        """

        self._available_spending_limit = available_spending_limit

    @property
    def available_spending_limit_srd(self):
        """Gets the available_spending_limit_srd of this BalanceModel.  # noqa: E501

        Spending power for SRD  # noqa: E501

        :return: The available_spending_limit_srd of this BalanceModel.  # noqa: E501
        :rtype: float
        """
        return self._available_spending_limit_srd

    @available_spending_limit_srd.setter
    def available_spending_limit_srd(self, available_spending_limit_srd):
        """Sets the available_spending_limit_srd of this BalanceModel.

        Spending power for SRD  # noqa: E501

        :param available_spending_limit_srd: The available_spending_limit_srd of this BalanceModel.  # noqa: E501
        :type: float
        """

        self._available_spending_limit_srd = available_spending_limit_srd

    @property
    def cash_balances_collection(self):
        """Gets the cash_balances_collection of this BalanceModel.  # noqa: E501

        Collection of one or more cash accounts per currency  # noqa: E501

        :return: The cash_balances_collection of this BalanceModel.  # noqa: E501
        :rtype: CashBalancesCollectionModel
        """
        return self._cash_balances_collection

    @cash_balances_collection.setter
    def cash_balances_collection(self, cash_balances_collection):
        """Sets the cash_balances_collection of this BalanceModel.

        Collection of one or more cash accounts per currency  # noqa: E501

        :param cash_balances_collection: The cash_balances_collection of this BalanceModel.  # noqa: E501
        :type: CashBalancesCollectionModel
        """
        if self._configuration.client_side_validation and cash_balances_collection is None:
            raise ValueError("Invalid value for `cash_balances_collection`, must not be `None`")  # noqa: E501

        self._cash_balances_collection = cash_balances_collection

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BalanceModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BalanceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BalanceModel):
            return True

        return self.to_dict() != other.to_dict()