# NewOrderModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The kind of order to be placed | 
**quantity** | **float** | The number of financial instruments to buy or sell | 
**duration** | **str** | Specifies the term for which the order is active - in general, duration is &#39;day&#39; for market orders | 
**expiration_date** | **datetime** | The date when the order will be expired, used in combination with duration GoodTillDateTime | [optional] 
**limit_price** | **float** | The highest price at which to buy or the lowest price at which to sell (only if type is limit or stopLimit) | [optional] 
**stop_price** | **float** | The trigger price to initiate a buy or sell order, applicable when type is stop or stopLimit | [optional] 
**cash** | [**NewOrderModelCash**](NewOrderModelCash.md) | For cash orders (equities), this field is required | [optional] 
**srd** | [**NewOrderModelSrd**](NewOrderModelSrd.md) | For SRD orders (equities, France), this field is required | [optional] 
**option** | [**NewOrderModelOption**](NewOrderModelOption.md) | For option orders, this field is required | [optional] 
**future** | [**NewOrderModelFuture**](NewOrderModelFuture.md) | For future orders, this field is required | [optional] 
**validation_code** | **str** | Order validation code (needs to be obtained by a preview order) | [optional] 
**reference_id** | **str** | Reference identifier available for 3rd parties. Max length 40 chars | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


