# PreviewOrderModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_can_be_registered** | **bool** | True if the order can be placed | 
**expected_expiration_date** | **datetime** | For GTD en GTC orders the end date will be limited to about 2 weeks maximum | [optional] 
**position_effect** | **str** | Contains the position effect information (open, close) | [optional] 
**effect_on_spending_limit** | **float** | Effect of a successfully placed order on the spending limit of the account | [optional] 
**current_spending_limit** | **float** | The current spending limit of the account (before placing the order) | [optional] 
**new_spending_limit** | **float** | The new spending limit of the account (after placing the order) | [optional] 
**currency** | **str** | The currency of the spending limit | [optional] 
**old_risk_number** | **int** | Risk number before placing the order | [optional] 
**new_risk_number** | **int** | Risk number after successfully placing the order | [optional] 
**recommended_risk_number** | **int** | Recommended risk number | [optional] 
**warnings_to_be_shown** | **list[str]** | Warnings or error messages about the requested order that only needs to be shown | 
**warnings_to_be_confirmed** | **list[str]** | Warning messages about the requested order that explicitly need to be confirmed | 
**validation_code** | **str** | (Optional) validation code (only supplied when order can be registered) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


