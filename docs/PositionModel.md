# PositionModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | [**InstrumentBriefModel**](InstrumentBriefModel.md) | Instrument information | 
**quantity** | **int** | Number of securities or contracts or nominal value | 
**currency** | **str** | Currency | 
**accrued_interest** | [**PositionAccruedInterest**](PositionAccruedInterest.md) | Accrued interest in case of a debt instrument | [optional] 
**average_historical_price** | **float** | Volume weighted average price paid at the time of purchase - for futures this is based on fixing price, if held overnight | [optional] 
**value_in_euro** | **float** | Value of the position expressed in the EURO currency | [optional] 
**margin** | [**PositionMargin**](PositionMargin.md) | Margin | [optional] 
**result** | [**PositionResult**](PositionResult.md) | Result expressed in mentioned currency of instrument | 
**result_in_euro** | [**PositionResult**](PositionResult.md) | Result expressed in the EURO currency | 
**value** | **float** | Value of the portfolio | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


