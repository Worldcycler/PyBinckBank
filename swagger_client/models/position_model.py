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


class PositionModel(object):
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
        'instrument': 'InstrumentBriefModel',
        'quantity': 'int',
        'currency': 'str',
        'accrued_interest': 'PositionAccruedInterest',
        'average_historical_price': 'float',
        'value_in_euro': 'float',
        'margin': 'PositionMargin',
        'result': 'PositionResult',
        'result_in_euro': 'PositionResult',
        'value': 'float'
    }

    attribute_map = {
        'instrument': 'instrument',
        'quantity': 'quantity',
        'currency': 'currency',
        'accrued_interest': 'accruedInterest',
        'average_historical_price': 'averageHistoricalPrice',
        'value_in_euro': 'valueInEuro',
        'margin': 'margin',
        'result': 'result',
        'result_in_euro': 'resultInEuro',
        'value': 'value'
    }

    def __init__(self, instrument=None, quantity=None, currency=None, accrued_interest=None, average_historical_price=None, value_in_euro=None, margin=None, result=None, result_in_euro=None, value=None, _configuration=None):  # noqa: E501
        """PositionModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instrument = None
        self._quantity = None
        self._currency = None
        self._accrued_interest = None
        self._average_historical_price = None
        self._value_in_euro = None
        self._margin = None
        self._result = None
        self._result_in_euro = None
        self._value = None
        self.discriminator = None

        self.instrument = instrument
        self.quantity = quantity
        self.currency = currency
        if accrued_interest is not None:
            self.accrued_interest = accrued_interest
        if average_historical_price is not None:
            self.average_historical_price = average_historical_price
        if value_in_euro is not None:
            self.value_in_euro = value_in_euro
        if margin is not None:
            self.margin = margin
        self.result = result
        self.result_in_euro = result_in_euro
        self.value = value

    @property
    def instrument(self):
        """Gets the instrument of this PositionModel.  # noqa: E501

        Instrument information  # noqa: E501

        :return: The instrument of this PositionModel.  # noqa: E501
        :rtype: InstrumentBriefModel
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this PositionModel.

        Instrument information  # noqa: E501

        :param instrument: The instrument of this PositionModel.  # noqa: E501
        :type: InstrumentBriefModel
        """
        if self._configuration.client_side_validation and instrument is None:
            raise ValueError("Invalid value for `instrument`, must not be `None`")  # noqa: E501

        self._instrument = instrument

    @property
    def quantity(self):
        """Gets the quantity of this PositionModel.  # noqa: E501

        Number of securities or contracts or nominal value  # noqa: E501

        :return: The quantity of this PositionModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PositionModel.

        Number of securities or contracts or nominal value  # noqa: E501

        :param quantity: The quantity of this PositionModel.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def currency(self):
        """Gets the currency of this PositionModel.  # noqa: E501

        Currency  # noqa: E501

        :return: The currency of this PositionModel.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PositionModel.

        Currency  # noqa: E501

        :param currency: The currency of this PositionModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def accrued_interest(self):
        """Gets the accrued_interest of this PositionModel.  # noqa: E501

        Accrued interest in case of a debt instrument  # noqa: E501

        :return: The accrued_interest of this PositionModel.  # noqa: E501
        :rtype: PositionAccruedInterest
        """
        return self._accrued_interest

    @accrued_interest.setter
    def accrued_interest(self, accrued_interest):
        """Sets the accrued_interest of this PositionModel.

        Accrued interest in case of a debt instrument  # noqa: E501

        :param accrued_interest: The accrued_interest of this PositionModel.  # noqa: E501
        :type: PositionAccruedInterest
        """

        self._accrued_interest = accrued_interest

    @property
    def average_historical_price(self):
        """Gets the average_historical_price of this PositionModel.  # noqa: E501

        Volume weighted average price paid at the time of purchase - for futures this is based on fixing price, if held overnight  # noqa: E501

        :return: The average_historical_price of this PositionModel.  # noqa: E501
        :rtype: float
        """
        return self._average_historical_price

    @average_historical_price.setter
    def average_historical_price(self, average_historical_price):
        """Sets the average_historical_price of this PositionModel.

        Volume weighted average price paid at the time of purchase - for futures this is based on fixing price, if held overnight  # noqa: E501

        :param average_historical_price: The average_historical_price of this PositionModel.  # noqa: E501
        :type: float
        """

        self._average_historical_price = average_historical_price

    @property
    def value_in_euro(self):
        """Gets the value_in_euro of this PositionModel.  # noqa: E501

        Value of the position expressed in the EURO currency  # noqa: E501

        :return: The value_in_euro of this PositionModel.  # noqa: E501
        :rtype: float
        """
        return self._value_in_euro

    @value_in_euro.setter
    def value_in_euro(self, value_in_euro):
        """Sets the value_in_euro of this PositionModel.

        Value of the position expressed in the EURO currency  # noqa: E501

        :param value_in_euro: The value_in_euro of this PositionModel.  # noqa: E501
        :type: float
        """

        self._value_in_euro = value_in_euro

    @property
    def margin(self):
        """Gets the margin of this PositionModel.  # noqa: E501

        Margin  # noqa: E501

        :return: The margin of this PositionModel.  # noqa: E501
        :rtype: PositionMargin
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this PositionModel.

        Margin  # noqa: E501

        :param margin: The margin of this PositionModel.  # noqa: E501
        :type: PositionMargin
        """

        self._margin = margin

    @property
    def result(self):
        """Gets the result of this PositionModel.  # noqa: E501

        Result expressed in mentioned currency of instrument  # noqa: E501

        :return: The result of this PositionModel.  # noqa: E501
        :rtype: PositionResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PositionModel.

        Result expressed in mentioned currency of instrument  # noqa: E501

        :param result: The result of this PositionModel.  # noqa: E501
        :type: PositionResult
        """
        if self._configuration.client_side_validation and result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def result_in_euro(self):
        """Gets the result_in_euro of this PositionModel.  # noqa: E501

        Result expressed in the EURO currency  # noqa: E501

        :return: The result_in_euro of this PositionModel.  # noqa: E501
        :rtype: PositionResult
        """
        return self._result_in_euro

    @result_in_euro.setter
    def result_in_euro(self, result_in_euro):
        """Sets the result_in_euro of this PositionModel.

        Result expressed in the EURO currency  # noqa: E501

        :param result_in_euro: The result_in_euro of this PositionModel.  # noqa: E501
        :type: PositionResult
        """
        if self._configuration.client_side_validation and result_in_euro is None:
            raise ValueError("Invalid value for `result_in_euro`, must not be `None`")  # noqa: E501

        self._result_in_euro = result_in_euro

    @property
    def value(self):
        """Gets the value of this PositionModel.  # noqa: E501

        Value of the portfolio  # noqa: E501

        :return: The value of this PositionModel.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PositionModel.

        Value of the portfolio  # noqa: E501

        :param value: The value of this PositionModel.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(PositionModel, dict):
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
        if not isinstance(other, PositionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PositionModel):
            return True

        return self.to_dict() != other.to_dict()
