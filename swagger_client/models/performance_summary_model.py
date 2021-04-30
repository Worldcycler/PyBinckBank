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


class PerformanceSummaryModel(object):
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
        'year': 'str',
        'currency': 'str',
        'realized': 'float',
        'unrealized': 'float',
        'annual': 'float',
        'previous_years_total': 'float',
        'total': 'float'
    }

    attribute_map = {
        'year': 'year',
        'currency': 'currency',
        'realized': 'realized',
        'unrealized': 'unrealized',
        'annual': 'annual',
        'previous_years_total': 'previousYearsTotal',
        'total': 'total'
    }

    def __init__(self, year=None, currency=None, realized=None, unrealized=None, annual=None, previous_years_total=None, total=None, _configuration=None):  # noqa: E501
        """PerformanceSummaryModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._year = None
        self._currency = None
        self._realized = None
        self._unrealized = None
        self._annual = None
        self._previous_years_total = None
        self._total = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if currency is not None:
            self.currency = currency
        if realized is not None:
            self.realized = realized
        if unrealized is not None:
            self.unrealized = unrealized
        if annual is not None:
            self.annual = annual
        if previous_years_total is not None:
            self.previous_years_total = previous_years_total
        if total is not None:
            self.total = total

    @property
    def year(self):
        """Gets the year of this PerformanceSummaryModel.  # noqa: E501

        Year for this summary  # noqa: E501

        :return: The year of this PerformanceSummaryModel.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PerformanceSummaryModel.

        Year for this summary  # noqa: E501

        :param year: The year of this PerformanceSummaryModel.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def currency(self):
        """Gets the currency of this PerformanceSummaryModel.  # noqa: E501

        Currency for this summary  # noqa: E501

        :return: The currency of this PerformanceSummaryModel.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PerformanceSummaryModel.

        Currency for this summary  # noqa: E501

        :param currency: The currency of this PerformanceSummaryModel.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def realized(self):
        """Gets the realized of this PerformanceSummaryModel.  # noqa: E501

        Realized profit/loss  # noqa: E501

        :return: The realized of this PerformanceSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._realized

    @realized.setter
    def realized(self, realized):
        """Sets the realized of this PerformanceSummaryModel.

        Realized profit/loss  # noqa: E501

        :param realized: The realized of this PerformanceSummaryModel.  # noqa: E501
        :type: float
        """

        self._realized = realized

    @property
    def unrealized(self):
        """Gets the unrealized of this PerformanceSummaryModel.  # noqa: E501

        Unrealized profit/loss  # noqa: E501

        :return: The unrealized of this PerformanceSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._unrealized

    @unrealized.setter
    def unrealized(self, unrealized):
        """Sets the unrealized of this PerformanceSummaryModel.

        Unrealized profit/loss  # noqa: E501

        :param unrealized: The unrealized of this PerformanceSummaryModel.  # noqa: E501
        :type: float
        """

        self._unrealized = unrealized

    @property
    def annual(self):
        """Gets the annual of this PerformanceSummaryModel.  # noqa: E501

        Total this year  # noqa: E501

        :return: The annual of this PerformanceSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._annual

    @annual.setter
    def annual(self, annual):
        """Sets the annual of this PerformanceSummaryModel.

        Total this year  # noqa: E501

        :param annual: The annual of this PerformanceSummaryModel.  # noqa: E501
        :type: float
        """

        self._annual = annual

    @property
    def previous_years_total(self):
        """Gets the previous_years_total of this PerformanceSummaryModel.  # noqa: E501

        Including previous years  # noqa: E501

        :return: The previous_years_total of this PerformanceSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._previous_years_total

    @previous_years_total.setter
    def previous_years_total(self, previous_years_total):
        """Sets the previous_years_total of this PerformanceSummaryModel.

        Including previous years  # noqa: E501

        :param previous_years_total: The previous_years_total of this PerformanceSummaryModel.  # noqa: E501
        :type: float
        """

        self._previous_years_total = previous_years_total

    @property
    def total(self):
        """Gets the total of this PerformanceSummaryModel.  # noqa: E501

        Total  # noqa: E501

        :return: The total of this PerformanceSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PerformanceSummaryModel.

        Total  # noqa: E501

        :param total: The total of this PerformanceSummaryModel.  # noqa: E501
        :type: float
        """

        self._total = total

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
        if issubclass(PerformanceSummaryModel, dict):
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
        if not isinstance(other, PerformanceSummaryModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerformanceSummaryModel):
            return True

        return self.to_dict() != other.to_dict()
