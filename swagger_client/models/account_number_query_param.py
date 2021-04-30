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


class AccountNumberQueryParam(object):
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
        'account_number': 'str'
    }

    attribute_map = {
        'account_number': 'accountNumber'
    }

    def __init__(self, account_number=None, _configuration=None):  # noqa: E501
        """AccountNumberQueryParam - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_number = None
        self.discriminator = None

        self.account_number = account_number

    @property
    def account_number(self):
        """Gets the account_number of this AccountNumberQueryParam.  # noqa: E501

        Mandatory account number  # noqa: E501

        :return: The account_number of this AccountNumberQueryParam.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AccountNumberQueryParam.

        Mandatory account number  # noqa: E501

        :param account_number: The account_number of this AccountNumberQueryParam.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_number is not None and len(account_number) > 15):
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `15`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_number is not None and len(account_number) < 3):
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_number is not None and not re.search(r'[0-9a-zA-Z]{3,}', account_number)):  # noqa: E501
            raise ValueError(r"Invalid value for `account_number`, must be a follow pattern or equal to `/[0-9a-zA-Z]{3,}/`")  # noqa: E501

        self._account_number = account_number

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
        if issubclass(AccountNumberQueryParam, dict):
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
        if not isinstance(other, AccountNumberQueryParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountNumberQueryParam):
            return True

        return self.to_dict() != other.to_dict()