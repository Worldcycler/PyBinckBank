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


class OrdersQueryParams(object):
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
        'status': 'str',
        'include_status_history': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'include_status_history': 'includeStatusHistory'
    }

    def __init__(self, status=None, include_status_history=None, _configuration=None):  # noqa: E501
        """OrdersQueryParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._include_status_history = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if include_status_history is not None:
            self.include_status_history = include_status_history

    @property
    def status(self):
        """Gets the status of this OrdersQueryParams.  # noqa: E501

        Status 'all' will select all the orders. Other possible values are 'open', 'executed' and 'canceled'.  # noqa: E501

        :return: The status of this OrdersQueryParams.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrdersQueryParams.

        Status 'all' will select all the orders. Other possible values are 'open', 'executed' and 'canceled'.  # noqa: E501

        :param status: The status of this OrdersQueryParams.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                status is not None and not re.search(r'^all$|^open$|^executed$|^canceled$', status)):  # noqa: E501
            raise ValueError(r"Invalid value for `status`, must be a follow pattern or equal to `/^all$|^open$|^executed$|^canceled$/`")  # noqa: E501

        self._status = status

    @property
    def include_status_history(self):
        """Gets the include_status_history of this OrdersQueryParams.  # noqa: E501

        When set to True, orders will include a detailed status history overview. When set to false the response doesn't contain the status history, but the request will be handled faster. Default is True.  # noqa: E501

        :return: The include_status_history of this OrdersQueryParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_status_history

    @include_status_history.setter
    def include_status_history(self, include_status_history):
        """Sets the include_status_history of this OrdersQueryParams.

        When set to True, orders will include a detailed status history overview. When set to false the response doesn't contain the status history, but the request will be handled faster. Default is True.  # noqa: E501

        :param include_status_history: The include_status_history of this OrdersQueryParams.  # noqa: E501
        :type: bool
        """

        self._include_status_history = include_status_history

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
        if issubclass(OrdersQueryParams, dict):
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
        if not isinstance(other, OrdersQueryParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrdersQueryParams):
            return True

        return self.to_dict() != other.to_dict()
