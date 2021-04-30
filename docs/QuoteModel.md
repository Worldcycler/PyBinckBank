# QuoteModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | Security Id | 
**subscription_level** | **str** | Level of quote access | 
**open** | [**PriceModel**](PriceModel.md) | Open quote | [optional] 
**last** | [**PriceWithVolumeModel**](PriceWithVolumeModel.md) | Last quote | [optional] 
**close** | [**PriceWithVolumeModel**](PriceWithVolumeModel.md) | Close quote | [optional] 
**high** | [**PriceModel**](PriceModel.md) | High quote | [optional] 
**low** | [**PriceModel**](PriceModel.md) | Low quote | [optional] 
**impl_vol** | [**PriceModel**](PriceModel.md) | Implied volatility quote | [optional] 
**impl_div** | [**PriceModel**](PriceModel.md) | Implied dividend quote | [optional] 
**settlement** | [**PriceModel**](PriceModel.md) | Settlement quote | [optional] 
**open_interest** | [**VolumeModel**](VolumeModel.md) | Open interest quote | [optional] 
**theoretical_price** | [**PriceModel**](PriceModel.md) | Theoretical price quote | [optional] 
**impl_ir** | [**PriceModel**](PriceModel.md) | Implied interest rate quote | [optional] 
**cum_vol** | [**VolumeModel**](VolumeModel.md) | Cumulative volume quote | [optional] 
**bid** | [**list[PriceOrderBookModel]**](PriceOrderBookModel.md) | Bid book | 
**ask** | [**list[PriceOrderBookModel]**](PriceOrderBookModel.md) | Ask book | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


