# TransactionModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_currency** | **str** | Currency code for an account | 
**number** | **int** | State the uniqueness of this number for an account | 
**transaction_date** | **datetime** | The transaction date is the date when the transaction is effective | 
**settlement_date** | **datetime** | The date on which the transfer between two parties is executed | [optional] 
**mutation_type** | **str** | Enumerated value of the mutation type | 
**balance_mutation** | **float** | Total amount when the transaction is completed | [optional] 
**mutated_balance** | **float** | Total amount when the transaction is completed | [optional] 
**instrument** | [**InstrumentBriefModel**](InstrumentBriefModel.md) | The instrument object | [optional] 
**price** | **float** | The price of one instrument | [optional] 
**quantity** | **float** | The number of financial instruments to buy or sell | [optional] 
**exchange** | **str** | Name of the exchange where this instrument was handled | [optional] 
**total_costs** | **float** | All costs for this transaction | [optional] 
**currency** | **str** | Transaction currency. This currency was used to complete this transaction | 
**net_amount** | **float** | The total amount for this transaction without the costs | [optional] 
**currency_rate** | **float** | The exchange rate used for the transaction currency | [optional] 
**transaction_cost_components** | [**list[TransactionCostComponentModel]**](TransactionCostComponentModel.md) | All Cost components for this transactions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


