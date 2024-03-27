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
import epilot
from epilot.models import shared

s = epilot.Epilot()


res = s.cart_api.dollar_checkout_cart(checkout_cart=shared.CheckoutCart(), x_ivy_org_id='<value>')

if res.checkout_cart_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `checkout_cart`                                            | [shared.CheckoutCart](../../models/shared/checkoutcart.md) | :heavy_check_mark:                                         | N/A                                                        |
| `x_ivy_org_id`                                             | *str*                                                      | :heavy_check_mark:                                         | The target Organization Id represented by the caller       |


### Response

**[operations.DollarCheckoutCartResponse](../../models/operations/dollarcheckoutcartresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
