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


class DerivativeClassInfoModel(object):
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
        'underlying_instrument_id': 'str',
        'name': 'str',
        'symbol': 'str',
        'isincode': 'str',
        'market_identification_code': 'str',
        'currency': 'str',
        'type': 'str',
        'contract_size': 'float',
        'series': 'list[DerivativeSeriesInfoModel]'
    }

    attribute_map = {
        'underlying_instrument_id': 'underlyingInstrumentId',
        'name': 'name',
        'symbol': 'symbol',
        'isincode': 'isincode',
        'market_identification_code': 'marketIdentificationCode',
        'currency': 'currency',
        'type': 'type',
        'contract_size': 'contractSize',
        'series': 'series'
    }

    def __init__(self, underlying_instrument_id=None, name=None, symbol=None, isincode=None, market_identification_code=None, currency=None, type=None, contract_size=None, series=None, _configuration=None):  # noqa: E501
        """DerivativeClassInfoModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._underlying_instrument_id = None
        self._name = None
        self._symbol = None
        self._isincode = None
        self._market_identification_code = None
        self._currency = None
        self._type = None
        self._contract_size = None
        self._series = None
        self.discriminator = None

        if underlying_instrument_id is not None:
            self.underlying_instrument_id = underlying_instrument_id
        if name is not None:
            self.name = name
        if symbol is not None:
            self.symbol = symbol
        if isincode is not None:
            self.isincode = isincode
        if market_identification_code is not None:
            self.market_identification_code = market_identification_code
        if currency is not None:
            self.currency = currency
        if type is not None:
            self.type = type
        if contract_size is not None:
            self.contract_size = contract_size
        if series is not None:
            self.series = series

    @property
    def underlying_instrument_id(self):
        """Gets the underlying_instrument_id of this DerivativeClassInfoModel.  # noqa: E501

        Identification of the underlying instrument  # noqa: E501

        :return: The underlying_instrument_id of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._underlying_instrument_id

    @underlying_instrument_id.setter
    def underlying_instrument_id(self, underlying_instrument_id):
        """Sets the underlying_instrument_id of this DerivativeClassInfoModel.

        Identification of the underlying instrument  # noqa: E501

        :param underlying_instrument_id: The underlying_instrument_id of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """

        self._underlying_instrument_id = underlying_instrument_id

    @property
    def name(self):
        """Gets the name of this DerivativeClassInfoModel.  # noqa: E501

        Name of the class  # noqa: E501

        :return: The name of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DerivativeClassInfoModel.

        Name of the class  # noqa: E501

        :param name: The name of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def symbol(self):
        """Gets the symbol of this DerivativeClassInfoModel.  # noqa: E501

        Symbol of the class  # noqa: E501

        :return: The symbol of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this DerivativeClassInfoModel.

        Symbol of the class  # noqa: E501

        :param symbol: The symbol of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def isincode(self):
        """Gets the isincode of this DerivativeClassInfoModel.  # noqa: E501

        ISIN Code of the class  # noqa: E501

        :return: The isincode of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._isincode

    @isincode.setter
    def isincode(self, isincode):
        """Sets the isincode of this DerivativeClassInfoModel.

        ISIN Code of the class  # noqa: E501

        :param isincode: The isincode of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """

        self._isincode = isincode

    @property
    def market_identification_code(self):
        """Gets the market_identification_code of this DerivativeClassInfoModel.  # noqa: E501

        ISO MIC of the class  # noqa: E501

        :return: The market_identification_code of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._market_identification_code

    @market_identification_code.setter
    def market_identification_code(self, market_identification_code):
        """Sets the market_identification_code of this DerivativeClassInfoModel.

        ISO MIC of the class  # noqa: E501

        :param market_identification_code: The market_identification_code of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """

        self._market_identification_code = market_identification_code

    @property
    def currency(self):
        """Gets the currency of this DerivativeClassInfoModel.  # noqa: E501

        Currency of the class  # noqa: E501

        :return: The currency of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DerivativeClassInfoModel.

        Currency of the class  # noqa: E501

        :param currency: The currency of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def type(self):
        """Gets the type of this DerivativeClassInfoModel.  # noqa: E501

        Type of the class (option or future class)  # noqa: E501

        :return: The type of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DerivativeClassInfoModel.

        Type of the class (option or future class)  # noqa: E501

        :param type: The type of this DerivativeClassInfoModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["bond", "cashDividend", "certificate", "choiceDividend", "claim", "coupon", "discounter", "equity", "future", "futureClass", "index", "investmentFund", "ipo", "option", "optionClass", "otherLeveragedProduct", "speeder", "sprinter", "srd", "srdClass", "stockDividend", "structuredProduct", "tracker", "turbo", "unclassified", "warrant"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def contract_size(self):
        """Gets the contract_size of this DerivativeClassInfoModel.  # noqa: E501

        Contract Size of the class  # noqa: E501

        :return: The contract_size of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this DerivativeClassInfoModel.

        Contract Size of the class  # noqa: E501

        :param contract_size: The contract_size of this DerivativeClassInfoModel.  # noqa: E501
        :type: float
        """

        self._contract_size = contract_size

    @property
    def series(self):
        """Gets the series of this DerivativeClassInfoModel.  # noqa: E501

        Collection of series for this class  # noqa: E501

        :return: The series of this DerivativeClassInfoModel.  # noqa: E501
        :rtype: list[DerivativeSeriesInfoModel]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this DerivativeClassInfoModel.

        Collection of series for this class  # noqa: E501

        :param series: The series of this DerivativeClassInfoModel.  # noqa: E501
        :type: list[DerivativeSeriesInfoModel]
        """

        self._series = series

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
        if issubclass(DerivativeClassInfoModel, dict):
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
        if not isinstance(other, DerivativeClassInfoModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivativeClassInfoModel):
            return True

        return self.to_dict() != other.to_dict()
