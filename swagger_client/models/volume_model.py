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


class VolumeModel(object):
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
        'volume': 'int',
        'tags': 'str'
    }

    attribute_map = {
        'volume': 'volume',
        'tags': 'tags'
    }

    def __init__(self, volume=None, tags=None, _configuration=None):  # noqa: E501
        """VolumeModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._volume = None
        self._tags = None
        self.discriminator = None

        self.volume = volume
        if tags is not None:
            self.tags = tags

    @property
    def volume(self):
        """Gets the volume of this VolumeModel.  # noqa: E501

        Quote Volume  # noqa: E501

        :return: The volume of this VolumeModel.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this VolumeModel.

        Quote Volume  # noqa: E501

        :param volume: The volume of this VolumeModel.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    @property
    def tags(self):
        """Gets the tags of this VolumeModel.  # noqa: E501

        Tags for Market (M), Cancel (O), MarketOpen (O), ExcludeIntraday (X)  # noqa: E501

        :return: The tags of this VolumeModel.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VolumeModel.

        Tags for Market (M), Cancel (O), MarketOpen (O), ExcludeIntraday (X)  # noqa: E501

        :param tags: The tags of this VolumeModel.  # noqa: E501
        :type: str
        """

        self._tags = tags

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
        if issubclass(VolumeModel, dict):
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
        if not isinstance(other, VolumeModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeModel):
            return True

        return self.to_dict() != other.to_dict()
