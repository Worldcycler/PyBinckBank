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


class VersionModel(object):
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
        'current_version': 'str',
        'build_date': 'str',
        'metadata': 'MetadataModel'
    }

    attribute_map = {
        'current_version': 'currentVersion',
        'build_date': 'buildDate',
        'metadata': 'metadata'
    }

    def __init__(self, current_version=None, build_date=None, metadata=None, _configuration=None):  # noqa: E501
        """VersionModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_version = None
        self._build_date = None
        self._metadata = None
        self.discriminator = None

        self.current_version = current_version
        self.build_date = build_date
        self.metadata = metadata

    @property
    def current_version(self):
        """Gets the current_version of this VersionModel.  # noqa: E501

        Current version  # noqa: E501

        :return: The current_version of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this VersionModel.

        Current version  # noqa: E501

        :param current_version: The current_version of this VersionModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and current_version is None:
            raise ValueError("Invalid value for `current_version`, must not be `None`")  # noqa: E501

        self._current_version = current_version

    @property
    def build_date(self):
        """Gets the build_date of this VersionModel.  # noqa: E501

        Build date  # noqa: E501

        :return: The build_date of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._build_date

    @build_date.setter
    def build_date(self, build_date):
        """Sets the build_date of this VersionModel.

        Build date  # noqa: E501

        :param build_date: The build_date of this VersionModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and build_date is None:
            raise ValueError("Invalid value for `build_date`, must not be `None`")  # noqa: E501

        self._build_date = build_date

    @property
    def metadata(self):
        """Gets the metadata of this VersionModel.  # noqa: E501

        API response meta data  # noqa: E501

        :return: The metadata of this VersionModel.  # noqa: E501
        :rtype: MetadataModel
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VersionModel.

        API response meta data  # noqa: E501

        :param metadata: The metadata of this VersionModel.  # noqa: E501
        :type: MetadataModel
        """
        if self._configuration.client_side_validation and metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

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
        if issubclass(VersionModel, dict):
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
        if not isinstance(other, VersionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VersionModel):
            return True

        return self.to_dict() != other.to_dict()
