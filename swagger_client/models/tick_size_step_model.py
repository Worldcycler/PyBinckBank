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


class TickSizeStepModel(object):
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
        '_from': 'float',
        'size': 'float'
    }

    attribute_map = {
        '_from': 'from',
        'size': 'size'
    }

    def __init__(self, _from=None, size=None, _configuration=None):  # noqa: E501
        """TickSizeStepModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__from = None
        self._size = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if size is not None:
            self.size = size

    @property
    def _from(self):
        """Gets the _from of this TickSizeStepModel.  # noqa: E501

        From value for tick size  # noqa: E501

        :return: The _from of this TickSizeStepModel.  # noqa: E501
        :rtype: float
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TickSizeStepModel.

        From value for tick size  # noqa: E501

        :param _from: The _from of this TickSizeStepModel.  # noqa: E501
        :type: float
        """

        self.__from = _from

    @property
    def size(self):
        """Gets the size of this TickSizeStepModel.  # noqa: E501

        Tick size  # noqa: E501

        :return: The size of this TickSizeStepModel.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TickSizeStepModel.

        Tick size  # noqa: E501

        :param size: The size of this TickSizeStepModel.  # noqa: E501
        :type: float
        """

        self._size = size

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
        if issubclass(TickSizeStepModel, dict):
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
        if not isinstance(other, TickSizeStepModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TickSizeStepModel):
            return True

        return self.to_dict() != other.to_dict()
