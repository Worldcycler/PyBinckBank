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


class KidResponseModel(object):
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
        'kid_collection': 'KidCollectionModel',
        'metadata': 'MetadataModel'
    }

    attribute_map = {
        'kid_collection': 'kidCollection',
        'metadata': 'metadata'
    }

    def __init__(self, kid_collection=None, metadata=None, _configuration=None):  # noqa: E501
        """KidResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._kid_collection = None
        self._metadata = None
        self.discriminator = None

        self.kid_collection = kid_collection
        self.metadata = metadata

    @property
    def kid_collection(self):
        """Gets the kid_collection of this KidResponseModel.  # noqa: E501

        Holds KID collection  # noqa: E501

        :return: The kid_collection of this KidResponseModel.  # noqa: E501
        :rtype: KidCollectionModel
        """
        return self._kid_collection

    @kid_collection.setter
    def kid_collection(self, kid_collection):
        """Sets the kid_collection of this KidResponseModel.

        Holds KID collection  # noqa: E501

        :param kid_collection: The kid_collection of this KidResponseModel.  # noqa: E501
        :type: KidCollectionModel
        """
        if self._configuration.client_side_validation and kid_collection is None:
            raise ValueError("Invalid value for `kid_collection`, must not be `None`")  # noqa: E501

        self._kid_collection = kid_collection

    @property
    def metadata(self):
        """Gets the metadata of this KidResponseModel.  # noqa: E501

        API response meta data  # noqa: E501

        :return: The metadata of this KidResponseModel.  # noqa: E501
        :rtype: MetadataModel
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this KidResponseModel.

        API response meta data  # noqa: E501

        :param metadata: The metadata of this KidResponseModel.  # noqa: E501
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
        if issubclass(KidResponseModel, dict):
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
        if not isinstance(other, KidResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KidResponseModel):
            return True

        return self.to_dict() != other.to_dict()
