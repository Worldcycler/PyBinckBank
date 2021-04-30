# InstrumentsQueryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Mandatory account number | 
**instrument_type** | **str** | Additional optional filter on instrument type. Cannot be used alone. | [optional] 
**search_text** | **str** | Case insensitive search text, minimum length 2. Cannot be used in combination with &#39;Isin&#39;. | [optional] 
**isin** | **str** | Selection on isinCode. Cannot be used in combination with &#39;SearchText&#39;. | [optional] 
**mic** | **str** | Additional optional selection on Market Identification Code, to be used only in combination with &#39;Isin&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


