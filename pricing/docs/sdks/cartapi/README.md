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
