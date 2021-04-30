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


class AccountModel(object):
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
        'name': 'str',
        'iban': 'str',
        'number': 'str',
        'type': 'str',
        'is_read_only': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'iban': 'iban',
        'number': 'number',
        'type': 'type',
        'is_read_only': 'isReadOnly'
    }

    def __init__(self, name=None, iban=None, number=None, type=None, is_read_only=None, _configuration=None):  # noqa: E501
        """AccountModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._iban = None
        self._number = None
        self._type = None
        self._is_read_only = None
        self.discriminator = None

        self.name = name
        if iban is not None:
            self.iban = iban
        self.number = number
        self.type = type
        self.is_read_only = is_read_only

    @property
    def name(self):
        """Gets the name of this AccountModel.  # noqa: E501

        The name of the account  # noqa: E501

        :return: The name of this AccountModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountModel.

        The name of the account  # noqa: E501

        :param name: The name of this AccountModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def iban(self):
        """Gets the iban of this AccountModel.  # noqa: E501

        The IBAN of the account  # noqa: E501

        :return: The iban of this AccountModel.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AccountModel.

        The IBAN of the account  # noqa: E501

        :param iban: The iban of this AccountModel.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def number(self):
        """Gets the number of this AccountModel.  # noqa: E501

        Accountnumber  # noqa: E501

        :return: The number of this AccountModel.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AccountModel.

        Accountnumber  # noqa: E501

        :param number: The number of this AccountModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def type(self):
        """Gets the type of this AccountModel.  # noqa: E501

        Type of account  # noqa: E501

        :return: The type of this AccountModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountModel.

        Type of account  # noqa: E501

        :param type: The type of this AccountModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["savings", "binckComplete", "fundCoach", "planEpargneAction", "planEpargneActionPme", "assetManagement", "savingsBroker", "assetManagementSelect"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def is_read_only(self):
        """Gets the is_read_only of this AccountModel.  # noqa: E501

        Scope for the account  # noqa: E501

        :return: The is_read_only of this AccountModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this AccountModel.

        Scope for the account  # noqa: E501

        :param is_read_only: The is_read_only of this AccountModel.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_read_only is None:
            raise ValueError("Invalid value for `is_read_only`, must not be `None`")  # noqa: E501

        self._is_read_only = is_read_only

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
        if issubclass(AccountModel, dict):
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
        if not isinstance(other, AccountModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountModel):
            return True

        return self.to_dict() != other.to_dict()
