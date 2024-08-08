# CartAPI
(*cart_api*)

## Overview

Used to interact with a cart during a customer's checkout session, providing:
 - An unified data model to model a Shopping Cart
 - Product and pricing data validation
 - Checkout a cart into an order or quote


### Available Operations

* [dollar_checkout_cart](#dollar_checkout_cart) - checkoutCart

## dollar_checkout_cart

Checkouts a cart and executes the specified checkout `mode` process.

A Checkout implicitly finalizes the provided cart (if not transient from a fast-checkout) and behaves in one of the following modes:
- `create_order` (**default**): the payment happens at a later date or managed by 3rd-party CRM (SAP)
- `create_invoice`: the payment happens on the online checkout (paypal, stripe, adyen)
- `create_quote`: the checkout represents a price quote request

Fast checkout is also supported, by passing the Cart contents directly.
When a fast checkout is performed the cart is considered transient and there is no cart persistance.

If the checkout `mode` is omitted, the `mode` will default to `create_order`.


### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot()


res = s.cart_api.dollar_checkout_cart(x_ivy_org_id="<value>", checkout_cart={
    "cart": {
        "line_items": [
            {
                "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_VOLUME,
                "price": epilot_pricing.Price(
                    pricing_model=epilot_pricing.PricePricingModel.PER_UNIT,
                    tax={},
                    unit_amount_currency="EUR",
                    **{
                        "$ref": "#/components/examples/price",
                    },
                ),
                "product": epilot_pricing.ProductInput(
                    **{
                        "$ref": "#/components/examples/product",
                    },
                ),
                "external_fees_mappings": [
                    {
                        "amount_total": 1000,
                        "amount_total_decimal": "10.00",
                        "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                        "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    },
                ],
                "external_fees_metadata": {
                    "amount_total": 8160.76,
                    "amount_total_decimal": "<value>",
                    "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.MONTHLY,
                    "breakdown": {},
                    "currency": "EUR",
                },
                "price_id": "df240bab-9f71-4a9a-a9e1-59f18827dbf9",
                "price_mappings": [
                    {
                        "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                        "metadata": {
                            "journey_title": "energy journey",
                            "step_name": "avg consumption picker",
                        },
                        "name": "avg consumption",
                        "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                        "value": 1000.245,
                    },
                ],
                "product_id": "b7185fb7-b10f-4875-bda7-288631446555",
                "quantity": 3,
                "unit_amount_currency": "EUR",
            },
            {
                "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_VOLUME,
                "price": epilot_pricing.Price(
                    pricing_model=epilot_pricing.PricePricingModel.TIERED_FLATFEE,
                    tax={},
                    unit_amount_currency="EUR",
                    **{
                        "$ref": "#/components/examples/price",
                    },
                ),
                "product": epilot_pricing.ProductInput(
                    **{
                        "$ref": "#/components/examples/product",
                    },
                ),
                "external_fees_mappings": [
                    {
                        "amount_total": 1000,
                        "amount_total_decimal": "10.00",
                        "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                        "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    },
                ],
                "external_fees_metadata": {
                    "amount_total": 1072.49,
                    "amount_total_decimal": "<value>",
                    "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_6_MONTHS,
                    "breakdown": {},
                    "currency": "EUR",
                },
                "price_id": "7b028fdf-0b0a-4077-a8f1-d0cbbd14b7cf",
                "price_mappings": [
                    {
                        "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                        "metadata": {
                            "journey_title": "energy journey",
                            "step_name": "avg consumption picker",
                        },
                        "name": "avg consumption",
                        "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                        "value": 1000.245,
                    },
                ],
                "product_id": "607d2952-8f3e-484f-a82b-4880528b7f55",
                "quantity": 2,
                "unit_amount_currency": "EUR",
            },
        ],
        "additional_addresses": [
            epilot_pricing.Address(
                tags=[
                    "billing",
                ],
            ),
        ],
        "billing_address": epilot_pricing.Address(
            tags=[
                "billing",
            ],
            additional_info="headquarters office",
            city="new york city",
            country="united states",
            **{
                "street1": "wallstreet",
                "street2": 1,
                "country_code": "US",
            },
        ),
        "customer": {
            "company_name": "company limited",
            "email": "johndoe@company.com",
            "first_name": "john",
            "last_name": "doe",
            "phone": "+44233242423",
            "vat_id": "123892321",
        },
        "delivery_address": epilot_pricing.Address(
            tags=[
                "billing",
            ],
            additional_info="remote cowork place",
            city="berverly hills",
            country="california",
            **{
                "street1": "berverly hills avenue",
                "street2": "block 1",
                "country_code": "CA",
            },
        ),
        "source": {
            "http": "/app/v2/journey-builder/editor/db7f6940-994b-11ec-a46d-9f1824ff2939",
            "title": "Journey: PH Journey",
        },
        "source_id": "ce99875f-fba9-4fe2-a8f9-afaf52059051",
        "source_type": "journey",
    },
    "mode": epilot_pricing.CheckoutMode.CREATE_ORDER,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `x_ivy_org_id`                                                                            | *str*                                                                                     | :heavy_check_mark:                                                                        | The target Organization Id represented by the caller                                      |
| `checkout_cart`                                                                           | [models.CheckoutCart](../../models/checkoutcart.md)                                       | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `security`                                                                                | [Optional[models.DollarCheckoutCartSecurity]](../../models/dollarcheckoutcartsecurity.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |


### Response

**[models.CheckoutCartResult](../../models/checkoutcartresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
