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


class TickSizesModel(object):
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
        'tick_sizes': 'list[TickSizeStepModel]'
    }

    attribute_map = {
        'tick_sizes': 'tickSizes'
    }

    def __init__(self, tick_sizes=None, _configuration=None):  # noqa: E501
        """TickSizesModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tick_sizes = None
        self.discriminator = None

        if tick_sizes is not None:
            self.tick_sizes = tick_sizes

    @property
    def tick_sizes(self):
        """Gets the tick_sizes of this TickSizesModel.  # noqa: E501

        TickSizeStep collection  # noqa: E501

        :return: The tick_sizes of this TickSizesModel.  # noqa: E501
        :rtype: list[TickSizeStepModel]
        """
        return self._tick_sizes

    @tick_sizes.setter
    def tick_sizes(self, tick_sizes):
        """Sets the tick_sizes of this TickSizesModel.

        TickSizeStep collection  # noqa: E501

        :param tick_sizes: The tick_sizes of this TickSizesModel.  # noqa: E501
        :type: list[TickSizeStepModel]
        """

        self._tick_sizes = tick_sizes

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
        if issubclass(TickSizesModel, dict):
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
        if not isinstance(other, TickSizesModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TickSizesModel):
            return True

        return self.to_dict() != other.to_dict()