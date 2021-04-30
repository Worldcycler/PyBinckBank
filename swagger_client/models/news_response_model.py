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


class NewsResponseModel(object):
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
        'news_collection': 'NewsCollectionModel',
        'news_subscription_collection': 'NewsSubscriptionCollectionModel',
        'paging': 'PagingModel',
        'count': 'int',
        'metadata': 'MetadataModel'
    }

    attribute_map = {
        'news_collection': 'newsCollection',
        'news_subscription_collection': 'newsSubscriptionCollection',
        'paging': 'paging',
        'count': 'count',
        'metadata': 'metadata'
    }

    def __init__(self, news_collection=None, news_subscription_collection=None, paging=None, count=None, metadata=None, _configuration=None):  # noqa: E501
        """NewsResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._news_collection = None
        self._news_subscription_collection = None
        self._paging = None
        self._count = None
        self._metadata = None
        self.discriminator = None

        self.news_collection = news_collection
        self.news_subscription_collection = news_subscription_collection
        if paging is not None:
            self.paging = paging
        self.count = count
        self.metadata = metadata

    @property
    def news_collection(self):
        """Gets the news_collection of this NewsResponseModel.  # noqa: E501

        News items  # noqa: E501

        :return: The news_collection of this NewsResponseModel.  # noqa: E501
        :rtype: NewsCollectionModel
        """
        return self._news_collection

    @news_collection.setter
    def news_collection(self, news_collection):
        """Sets the news_collection of this NewsResponseModel.

        News items  # noqa: E501

        :param news_collection: The news_collection of this NewsResponseModel.  # noqa: E501
        :type: NewsCollectionModel
        """
        if self._configuration.client_side_validation and news_collection is None:
            raise ValueError("Invalid value for `news_collection`, must not be `None`")  # noqa: E501

        self._news_collection = news_collection

    @property
    def news_subscription_collection(self):
        """Gets the news_subscription_collection of this NewsResponseModel.  # noqa: E501

        News subscriptions granted  # noqa: E501

        :return: The news_subscription_collection of this NewsResponseModel.  # noqa: E501
        :rtype: NewsSubscriptionCollectionModel
        """
        return self._news_subscription_collection

    @news_subscription_collection.setter
    def news_subscription_collection(self, news_subscription_collection):
        """Sets the news_subscription_collection of this NewsResponseModel.

        News subscriptions granted  # noqa: E501

        :param news_subscription_collection: The news_subscription_collection of this NewsResponseModel.  # noqa: E501
        :type: NewsSubscriptionCollectionModel
        """
        if self._configuration.client_side_validation and news_subscription_collection is None:
            raise ValueError("Invalid value for `news_subscription_collection`, must not be `None`")  # noqa: E501

        self._news_subscription_collection = news_subscription_collection

    @property
    def paging(self):
        """Gets the paging of this NewsResponseModel.  # noqa: E501

        Paging information  # noqa: E501

        :return: The paging of this NewsResponseModel.  # noqa: E501
        :rtype: PagingModel
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this NewsResponseModel.

        Paging information  # noqa: E501

        :param paging: The paging of this NewsResponseModel.  # noqa: E501
        :type: PagingModel
        """

        self._paging = paging

    @property
    def count(self):
        """Gets the count of this NewsResponseModel.  # noqa: E501

        Number of entries in the complete collection  # noqa: E501

        :return: The count of this NewsResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NewsResponseModel.

        Number of entries in the complete collection  # noqa: E501

        :param count: The count of this NewsResponseModel.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def metadata(self):
        """Gets the metadata of this NewsResponseModel.  # noqa: E501

        API response meta data  # noqa: E501

        :return: The metadata of this NewsResponseModel.  # noqa: E501
        :rtype: MetadataModel
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NewsResponseModel.

        API response meta data  # noqa: E501

        :param metadata: The metadata of this NewsResponseModel.  # noqa: E501
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
        if issubclass(NewsResponseModel, dict):
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
        if not isinstance(other, NewsResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewsResponseModel):
            return True

        return self.to_dict() != other.to_dict()
