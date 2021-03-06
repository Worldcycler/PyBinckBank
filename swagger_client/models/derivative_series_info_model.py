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


class DerivativeSeriesInfoModel(object):
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
        'instrument_id': 'str',
        'strike': 'float',
        'strike_decimals': 'int',
        'option_type': 'str',
        'contract_size': 'float',
        'expiration_date': 'datetime'
    }

    attribute_map = {
        'instrument_id': 'instrumentId',
        'strike': 'strike',
        'strike_decimals': 'strikeDecimals',
        'option_type': 'optionType',
        'contract_size': 'contractSize',
        'expiration_date': 'expirationDate'
    }

    def __init__(self, instrument_id=None, strike=None, strike_decimals=None, option_type=None, contract_size=None, expiration_date=None, _configuration=None):  # noqa: E501
        """DerivativeSeriesInfoModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instrument_id = None
        self._strike = None
        self._strike_decimals = None
        self._option_type = None
        self._contract_size = None
        self._expiration_date = None
        self.discriminator = None

        if instrument_id is not None:
            self.instrument_id = instrument_id
        if strike is not None:
            self.strike = strike
        if strike_decimals is not None:
            self.strike_decimals = strike_decimals
        if option_type is not None:
            self.option_type = option_type
        if contract_size is not None:
            self.contract_size = contract_size
        if expiration_date is not None:
            self.expiration_date = expiration_date

    @property
    def instrument_id(self):
        """Gets the instrument_id of this DerivativeSeriesInfoModel.  # noqa: E501

        Instrument Id of the serie  # noqa: E501

        :return: The instrument_id of this DerivativeSeriesInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this DerivativeSeriesInfoModel.

        Instrument Id of the serie  # noqa: E501

        :param instrument_id: The instrument_id of this DerivativeSeriesInfoModel.  # noqa: E501
        :type: str
        """

        self._instrument_id = instrument_id

    @property
    def strike(self):
        """Gets the strike of this DerivativeSeriesInfoModel.  # noqa: E501

        Strike price (options only)  # noqa: E501

        :return: The strike of this DerivativeSeriesInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this DerivativeSeriesInfoModel.

        Strike price (options only)  # noqa: E501

        :param strike: The strike of this DerivativeSeriesInfoModel.  # noqa: E501
        :type: float
        """

        self._strike = strike

    @property
    def strike_decimals(self):
        """Gets the strike_decimals of this DerivativeSeriesInfoModel.  # noqa: E501

        Number of decimals in strike price (options only)  # noqa: E501

        :return: The strike_decimals of this DerivativeSeriesInfoModel.  # noqa: E501
        :rtype: int
        """
        return self._strike_decimals

    @strike_decimals.setter
    def strike_decimals(self, strike_decimals):
        """Sets the strike_decimals of this DerivativeSeriesInfoModel.

        Number of decimals in strike price (options only)  # noqa: E501

        :param strike_decimals: The strike_decimals of this DerivativeSeriesInfoModel.  # noqa: E501
        :type: int
        """

        self._strike_decimals = strike_decimals

    @property
    def option_type(self):
        """Gets the option_type of this DerivativeSeriesInfoModel.  # noqa: E501

        Option type (put or call) (options only)  # noqa: E501

        :return: The option_type of this DerivativeSeriesInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this DerivativeSeriesInfoModel.

        Option type (put or call) (options only)  # noqa: E501

        :param option_type: The option_type of this DerivativeSeriesInfoModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["put", "call"]  # noqa: E501
        if (self._configuration.client_side_validation and
                option_type not in allowed_values):
            raise ValueError(
                "Invalid value for `option_type` ({0}), must be one of {1}"  # noqa: E501
                .format(option_type, allowed_values)
            )

        self._option_type = option_type

    @property
    def contract_size(self):
        """Gets the contract_size of this DerivativeSeriesInfoModel.  # noqa: E501

        Contract size  # noqa: E501

        :return: The contract_size of this DerivativeSeriesInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this DerivativeSeriesInfoModel.

        Contract size  # noqa: E501

        :param contract_size: The contract_size of this DerivativeSeriesInfoModel.  # noqa: E501
        :type: float
        """

        self._contract_size = contract_size

    @property
    def expiration_date(self):
        """Gets the expiration_date of this DerivativeSeriesInfoModel.  # noqa: E501

        Expiration date  # noqa: E501

        :return: The expiration_date of this DerivativeSeriesInfoModel.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this DerivativeSeriesInfoModel.

        Expiration date  # noqa: E501

        :param expiration_date: The expiration_date of this DerivativeSeriesInfoModel.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

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
        if issubclass(DerivativeSeriesInfoModel, dict):
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
        if not isinstance(other, DerivativeSeriesInfoModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivativeSeriesInfoModel):
            return True

        return self.to_dict() != other.to_dict()
