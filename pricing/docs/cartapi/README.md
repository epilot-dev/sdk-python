# cart_api

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
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DollarCheckoutCartRequest(
    checkout_cart_input=shared.CheckoutCartInput(
        cart='nam',
        mode=shared.CheckoutMode.CREATE_INVOICE,
    ),
    x_ivy_org_id='occaecati',
)

res = s.cart_api.dollar_checkout_cart(req)

if res.checkout_cart_result is not None:
    # handle response
```
