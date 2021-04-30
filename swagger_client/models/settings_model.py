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


class SettingsModel(object):
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
        'trading_allowed': 'list[TradingProductModel]'
    }

    attribute_map = {
        'trading_allowed': 'tradingAllowed'
    }

    def __init__(self, trading_allowed=None, _configuration=None):  # noqa: E501
        """SettingsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._trading_allowed = None
        self.discriminator = None

        self.trading_allowed = trading_allowed

    @property
    def trading_allowed(self):
        """Gets the trading_allowed of this SettingsModel.  # noqa: E501

        A list of products trading is allowed for  # noqa: E501

        :return: The trading_allowed of this SettingsModel.  # noqa: E501
        :rtype: list[TradingProductModel]
        """
        return self._trading_allowed

    @trading_allowed.setter
    def trading_allowed(self, trading_allowed):
        """Sets the trading_allowed of this SettingsModel.

        A list of products trading is allowed for  # noqa: E501

        :param trading_allowed: The trading_allowed of this SettingsModel.  # noqa: E501
        :type: list[TradingProductModel]
        """
        if self._configuration.client_side_validation and trading_allowed is None:
            raise ValueError("Invalid value for `trading_allowed`, must not be `None`")  # noqa: E501

        self._trading_allowed = trading_allowed

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
        if issubclass(SettingsModel, dict):
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
        if not isinstance(other, SettingsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsModel):
            return True

        return self.to_dict() != other.to_dict()
