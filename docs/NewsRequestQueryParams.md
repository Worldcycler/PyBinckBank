# NewsRequestQueryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Mandatory account number | 
**from_date** | **datetime** | Optional start date, if left out, fromDate will be today. If no instrument ids are supplied, only dates from the  last month are accepted, otherwise only dates from the last week are accepted. | [optional] 
**to_date** | **datetime** | Optional end date, do not combine with instruments. | [optional] 
**instrument_ids** | **str** | Optional ids of the instruments to retrieve.  If there are multiple ids, separate them by commas. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


