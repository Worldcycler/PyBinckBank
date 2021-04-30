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


class TransactionModel(object):
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
        'account_currency': 'str',
        'number': 'int',
        'transaction_date': 'datetime',
        'settlement_date': 'datetime',
        'mutation_type': 'str',
        'balance_mutation': 'float',
        'mutated_balance': 'float',
        'instrument': 'InstrumentBriefModel',
        'price': 'float',
        'quantity': 'float',
        'exchange': 'str',
        'total_costs': 'float',
        'currency': 'str',
        'net_amount': 'float',
        'currency_rate': 'float',
        'transaction_cost_components': 'list[TransactionCostComponentModel]'
    }

    attribute_map = {
        'account_currency': 'accountCurrency',
        'number': 'number',
        'transaction_date': 'transactionDate',
        'settlement_date': 'settlementDate',
        'mutation_type': 'mutationType',
        'balance_mutation': 'balanceMutation',
        'mutated_balance': 'mutatedBalance',
        'instrument': 'instrument',
        'price': 'price',
        'quantity': 'quantity',
        'exchange': 'exchange',
        'total_costs': 'totalCosts',
        'currency': 'currency',
        'net_amount': 'netAmount',
        'currency_rate': 'currencyRate',
        'transaction_cost_components': 'transactionCostComponents'
    }

    def __init__(self, account_currency=None, number=None, transaction_date=None, settlement_date=None, mutation_type=None, balance_mutation=None, mutated_balance=None, instrument=None, price=None, quantity=None, exchange=None, total_costs=None, currency=None, net_amount=None, currency_rate=None, transaction_cost_components=None, _configuration=None):  # noqa: E501
        """TransactionModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_currency = None
        self._number = None
        self._transaction_date = None
        self._settlement_date = None
        self._mutation_type = None
        self._balance_mutation = None
        self._mutated_balance = None
        self._instrument = None
        self._price = None
        self._quantity = None
        self._exchange = None
        self._total_costs = None
        self._currency = None
        self._net_amount = None
        self._currency_rate = None
        self._transaction_cost_components = None
        self.discriminator = None

        self.account_currency = account_currency
        self.number = number
        self.transaction_date = transaction_date
        if settlement_date is not None:
            self.settlement_date = settlement_date
        self.mutation_type = mutation_type
        if balance_mutation is not None:
            self.balance_mutation = balance_mutation
        if mutated_balance is not None:
            self.mutated_balance = mutated_balance
        if instrument is not None:
            self.instrument = instrument
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if exchange is not None:
            self.exchange = exchange
        if total_costs is not None:
            self.total_costs = total_costs
        self.currency = currency
        if net_amount is not None:
            self.net_amount = net_amount
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if transaction_cost_components is not None:
            self.transaction_cost_components = transaction_cost_components

    @property
    def account_currency(self):
        """Gets the account_currency of this TransactionModel.  # noqa: E501

        Currency code for an account  # noqa: E501

        :return: The account_currency of this TransactionModel.  # noqa: E501
        :rtype: str
        """
        return self._account_currency

    @account_currency.setter
    def account_currency(self, account_currency):
        """Sets the account_currency of this TransactionModel.

        Currency code for an account  # noqa: E501

        :param account_currency: The account_currency of this TransactionModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_currency is None:
            raise ValueError("Invalid value for `account_currency`, must not be `None`")  # noqa: E501

        self._account_currency = account_currency

    @property
    def number(self):
        """Gets the number of this TransactionModel.  # noqa: E501

        State the uniqueness of this number for an account  # noqa: E501

        :return: The number of this TransactionModel.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TransactionModel.

        State the uniqueness of this number for an account  # noqa: E501

        :param number: The number of this TransactionModel.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def transaction_date(self):
        """Gets the transaction_date of this TransactionModel.  # noqa: E501

        The transaction date is the date when the transaction is effective  # noqa: E501

        :return: The transaction_date of this TransactionModel.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this TransactionModel.

        The transaction date is the date when the transaction is effective  # noqa: E501

        :param transaction_date: The transaction_date of this TransactionModel.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this TransactionModel.  # noqa: E501

        The date on which the transfer between two parties is executed  # noqa: E501

        :return: The settlement_date of this TransactionModel.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this TransactionModel.

        The date on which the transfer between two parties is executed  # noqa: E501

        :param settlement_date: The settlement_date of this TransactionModel.  # noqa: E501
        :type: datetime
        """

        self._settlement_date = settlement_date

    @property
    def mutation_type(self):
        """Gets the mutation_type of this TransactionModel.  # noqa: E501

        Enumerated value of the mutation type  # noqa: E501

        :return: The mutation_type of this TransactionModel.  # noqa: E501
        :rtype: str
        """
        return self._mutation_type

    @mutation_type.setter
    def mutation_type(self, mutation_type):
        """Sets the mutation_type of this TransactionModel.

        Enumerated value of the mutation type  # noqa: E501

        :param mutation_type: The mutation_type of this TransactionModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mutation_type is None:
            raise ValueError("Invalid value for `mutation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "repayment", "conversion", "excerciseCall", "excercisePut", "assignmentCall", "assignmentPut", "settlementDividend", "deposit", "emissionAllocation", "internalBooking", "transferOutOfSecurities", "notificationOfRedemption", "outstandingBooking", "securityTransfer", "conversionClaims", "conversionDividend", "cashSettlement", "adjustment", "assignmentCoupon", "internalTransfer", "externalTransfer", "cashTransferToPartnerBank", "cashTransferFromPartnerBank", "openingBuy", "openingBuyFutures", "openingSell", "openingSellFuture", "regulation", "creditInterest", "debitInterest", "closingBuy", "closingBuyFuture", "closingSell", "closingSellFuture", "assignmentClaim", "assignmentDividend", "couponPayment", "dividendPayment", "settlementCosts", "sell", "buy", "liquidationTransfer", "extensionOpenDeposit", "extensionOpenTransferOut", "extensionCloseDeposit", "extensionCloseTransferOut", "settlementBuy", "settlementSell", "securitiesLendingDividendPayment", "securitiesLendingCouponPayment", "securitiesLendingInterestPayment", "onlineMoneyTransfer", "taxReclaimPayment"]  # noqa: E501
        if (self._configuration.client_side_validation and
                mutation_type not in allowed_values):
            raise ValueError(
                "Invalid value for `mutation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mutation_type, allowed_values)
            )

        self._mutation_type = mutation_type

    @property
    def balance_mutation(self):
        """Gets the balance_mutation of this TransactionModel.  # noqa: E501

        Total amount when the transaction is completed  # noqa: E501

        :return: The balance_mutation of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._balance_mutation

    @balance_mutation.setter
    def balance_mutation(self, balance_mutation):
        """Sets the balance_mutation of this TransactionModel.

        Total amount when the transaction is completed  # noqa: E501

        :param balance_mutation: The balance_mutation of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._balance_mutation = balance_mutation

    @property
    def mutated_balance(self):
        """Gets the mutated_balance of this TransactionModel.  # noqa: E501

        Total amount when the transaction is completed  # noqa: E501

        :return: The mutated_balance of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._mutated_balance

    @mutated_balance.setter
    def mutated_balance(self, mutated_balance):
        """Sets the mutated_balance of this TransactionModel.

        Total amount when the transaction is completed  # noqa: E501

        :param mutated_balance: The mutated_balance of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._mutated_balance = mutated_balance

    @property
    def instrument(self):
        """Gets the instrument of this TransactionModel.  # noqa: E501

        The instrument object  # noqa: E501

        :return: The instrument of this TransactionModel.  # noqa: E501
        :rtype: InstrumentBriefModel
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this TransactionModel.

        The instrument object  # noqa: E501

        :param instrument: The instrument of this TransactionModel.  # noqa: E501
        :type: InstrumentBriefModel
        """

        self._instrument = instrument

    @property
    def price(self):
        """Gets the price of this TransactionModel.  # noqa: E501

        The price of one instrument  # noqa: E501

        :return: The price of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TransactionModel.

        The price of one instrument  # noqa: E501

        :param price: The price of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this TransactionModel.  # noqa: E501

        The number of financial instruments to buy or sell  # noqa: E501

        :return: The quantity of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this TransactionModel.

        The number of financial instruments to buy or sell  # noqa: E501

        :param quantity: The quantity of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def exchange(self):
        """Gets the exchange of this TransactionModel.  # noqa: E501

        Name of the exchange where this instrument was handled  # noqa: E501

        :return: The exchange of this TransactionModel.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this TransactionModel.

        Name of the exchange where this instrument was handled  # noqa: E501

        :param exchange: The exchange of this TransactionModel.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def total_costs(self):
        """Gets the total_costs of this TransactionModel.  # noqa: E501

        All costs for this transaction  # noqa: E501

        :return: The total_costs of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._total_costs

    @total_costs.setter
    def total_costs(self, total_costs):
        """Sets the total_costs of this TransactionModel.

        All costs for this transaction  # noqa: E501

        :param total_costs: The total_costs of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._total_costs = total_costs

    @property
    def currency(self):
        """Gets the currency of this TransactionModel.  # noqa: E501

        Transaction currency. This currency was used to complete this transaction  # noqa: E501

        :return: The currency of this TransactionModel.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionModel.

        Transaction currency. This currency was used to complete this transaction  # noqa: E501

        :param currency: The currency of this TransactionModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def net_amount(self):
        """Gets the net_amount of this TransactionModel.  # noqa: E501

        The total amount for this transaction without the costs  # noqa: E501

        :return: The net_amount of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this TransactionModel.

        The total amount for this transaction without the costs  # noqa: E501

        :param net_amount: The net_amount of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def currency_rate(self):
        """Gets the currency_rate of this TransactionModel.  # noqa: E501

        The exchange rate used for the transaction currency  # noqa: E501

        :return: The currency_rate of this TransactionModel.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this TransactionModel.

        The exchange rate used for the transaction currency  # noqa: E501

        :param currency_rate: The currency_rate of this TransactionModel.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def transaction_cost_components(self):
        """Gets the transaction_cost_components of this TransactionModel.  # noqa: E501

        All Cost components for this transactions  # noqa: E501

        :return: The transaction_cost_components of this TransactionModel.  # noqa: E501
        :rtype: list[TransactionCostComponentModel]
        """
        return self._transaction_cost_components

    @transaction_cost_components.setter
    def transaction_cost_components(self, transaction_cost_components):
        """Sets the transaction_cost_components of this TransactionModel.

        All Cost components for this transactions  # noqa: E501

        :param transaction_cost_components: The transaction_cost_components of this TransactionModel.  # noqa: E501
        :type: list[TransactionCostComponentModel]
        """

        self._transaction_cost_components = transaction_cost_components

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
        if issubclass(TransactionModel, dict):
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
        if not isinstance(other, TransactionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionModel):
            return True

        return self.to_dict() != other.to_dict()
