# HistoricalQuoteRequestQueryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Mandatory account number | 
**from_date_time** | **datetime** | The start moment of historical quotes | 
**to_date_time** | **datetime** | The end moment of historical quotes, defaulting to the Current date and time according to UTC time standard | [optional] 
**interval** | **str** | Interval for historical quotes  Depending on the interval, the historical quotes collection returned will be limited to a certain period:  Max. number of days for one minute interval is 5.  Max. number of days for five minute interval is 20.  Max. number of days for ten minute interval is 20.  Max. number of days for fifteen minute interval is 60.  Max. number of days for one hour interval is 120.  Max. number of years for one day interval is 10.  Max. number of years for one week interval is 10. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


