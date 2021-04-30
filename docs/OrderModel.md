# OrderModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The identification of the order | 
**instrument** | [**InstrumentBriefModel**](InstrumentBriefModel.md) | Attributes of the financial instrument ordered | 
**type** | **str** | The price type of the order | 
**status_history** | [**list[StatusHistory]**](StatusHistory.md) | Status history of the order, populated when requested with \&quot;includeStatusHistory !&#x3D; false\&quot; | [optional] 
**currency** | **str** | The currency of the security | 
**duration** | **str** | Specifies the term for which the order is in effect | 
**line** | **int** | Line number of this order in case of a multi line order | [optional] 
**side** | **str** | Buy or sell - not available when bid (IPO) | [optional] 
**executed_quantity** | **float** | Number of executed instruments (equities), nominal value (odds) or number of contracts (options and futures) | [optional] 
**limit_price** | **float** | Value of the order&#39;s limit | [optional] 
**average_price** | **float** | Average price of all fills on this order | [optional] 
**quantity** | **float** | Quantity ordered | 
**expiration_date** | **datetime** | Expiration date for a good till date order | [optional] 
**last_status** | **str** | Status of the order last executed | 
**last_status_date_time** | **datetime** | Indicates the date and time of the last status change | 
**stop_price** | **float** | Stop price for a stop or stop limit order | [optional] 
**fixing_price** | **float** | Fixing price of the order | [optional] 
**condition** | **str** | Pay or receive condition, only applicable for multi-leg orders | [optional] 
**reference_id** | **str** | Reference Id supplied at registration time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


