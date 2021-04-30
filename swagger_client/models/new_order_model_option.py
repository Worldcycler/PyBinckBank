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


class NewOrderModelOption(object):
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
        'condition': 'str',
        'leg1': 'NewOrderModelOptionLeg',
        'leg2': 'NewOrderModelOptionLeg'
    }

    attribute_map = {
        'condition': 'condition',
        'leg1': 'leg1',
        'leg2': 'leg2'
    }

    def __init__(self, condition=None, leg1=None, leg2=None, _configuration=None):  # noqa: E501
        """NewOrderModelOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition = None
        self._leg1 = None
        self._leg2 = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        self.leg1 = leg1
        if leg2 is not None:
            self.leg2 = leg2

    @property
    def condition(self):
        """Gets the condition of this NewOrderModelOption.  # noqa: E501

        Combination strategy. Pay or Receive  # noqa: E501

        :return: The condition of this NewOrderModelOption.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this NewOrderModelOption.

        Combination strategy. Pay or Receive  # noqa: E501

        :param condition: The condition of this NewOrderModelOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["pay", "receive"]  # noqa: E501
        if (self._configuration.client_side_validation and
                condition not in allowed_values):
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def leg1(self):
        """Gets the leg1 of this NewOrderModelOption.  # noqa: E501

        The information about the first leg  # noqa: E501

        :return: The leg1 of this NewOrderModelOption.  # noqa: E501
        :rtype: NewOrderModelOptionLeg
        """
        return self._leg1

    @leg1.setter
    def leg1(self, leg1):
        """Sets the leg1 of this NewOrderModelOption.

        The information about the first leg  # noqa: E501

        :param leg1: The leg1 of this NewOrderModelOption.  # noqa: E501
        :type: NewOrderModelOptionLeg
        """
        if self._configuration.client_side_validation and leg1 is None:
            raise ValueError("Invalid value for `leg1`, must not be `None`")  # noqa: E501

        self._leg1 = leg1

    @property
    def leg2(self):
        """Gets the leg2 of this NewOrderModelOption.  # noqa: E501

        For a strategy the second leg is required  # noqa: E501

        :return: The leg2 of this NewOrderModelOption.  # noqa: E501
        :rtype: NewOrderModelOptionLeg
        """
        return self._leg2

    @leg2.setter
    def leg2(self, leg2):
        """Sets the leg2 of this NewOrderModelOption.

        For a strategy the second leg is required  # noqa: E501

        :param leg2: The leg2 of this NewOrderModelOption.  # noqa: E501
        :type: NewOrderModelOptionLeg
        """

        self._leg2 = leg2

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
        if issubclass(NewOrderModelOption, dict):
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
        if not isinstance(other, NewOrderModelOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewOrderModelOption):
            return True

        return self.to_dict() != other.to_dict()