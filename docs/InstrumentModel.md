# InstrumentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identification of the instrument | 
**name** | **str** | Name of the instrument | 
**symbol** | **str** | Symbol of the instrument | 
**isincode** | **str** | ISIN-code of the instrument | [optional] 
**type** | **str** | OptionType of the instrument | 
**market_identification_code** | **str** | Market Identification Code of the instrument | [optional] 
**derivatives_info** | [**DerivativesInfoModel**](DerivativesInfoModel.md) | Derivative serie information | [optional] 
**srd_info** | [**SrdInfoModel**](SrdInfoModel.md) | Srd or Srd class information:  Searching for an Srd will return a class. Ordering can done on both this class or the underlying equity.  Positions and transactions report the SRD class. To get information about the underlying equity, the SRD can be retrieved using the instruments endpoint. | [optional] 
**bond_info** | [**BondInfoModel**](BondInfoModel.md) | Bond only information | [optional] 
**leveraged_product** | [**LeveragedProductInfoModel**](LeveragedProductInfoModel.md) | Leveraged Product information | [optional] 
**currency** | **str** | Currency of the instrument | 
**price_decimals** | **int** | Number of decimals used to format the price - this is the maximum number of decimals, price can come with less, if higher than a certain limit | 
**ticker_symbol** | **str** | Ticker symbol of the instrument | 
**is_tradable** | **bool** | Indicates if orders for this instrument can be processed | 
**is_kid_applicable** | **bool** | Indicates whether KID document must be shown before placing an order | 
**tick_size_collection** | [**TickSizesModel**](TickSizesModel.md) | Table containing tick sizes for minimal prize movement | [optional] 
**has_options** | **bool** | Indicates whether there exists at least one non-cancelled, non-expired, tradable option for this security, either  an underlying value or an option class, with a valid listing (for the company/label) for which  the account is allowed to trade | 
**has_futures** | **bool** | Indicates whether there exists at least one non-cancelled, non-expired, tradable future for this instrument  , either an underlying value or a future class, with a valid listing (for the company/label) for which the account  is allowed to trade. | 
**has_srd** | **bool** | Indicates whether there exists at least one non-cancelled, non-expired, tradable srd for this security, either an  underlying value or an srd class, with a valid listing (for the company/label) for which the account  is allowed to trade. | 
**has_leveraged_products** | **bool** | Indicates whether there exists at least one non-cancelled, non-expired, tradable, visible leveraged  product for which the account is allowed to trade. | 
**has_order_modifications** | **bool** | Indicates if orders for the instrument can be modified | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


