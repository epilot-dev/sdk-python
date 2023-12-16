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
import dateutil.parser
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.cart_api.dollar_checkout_cart(checkout_cart=shared.CheckoutCart(
    cart=shared.CartDto(
    additional_addresses=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    billing_address=shared.Address(
        additional_properties={
            'key': 'string',
        },
        tags=[
            'billing',
        ],
    ),
    consents={
        'key': 'string',
    },
    customer=shared.Customer(),
    delivery_address=shared.Address(
        additional_properties={
            'key': 'string',
        },
        tags=[
            'billing',
        ],
    ),
    files=[
        'string',
    ],
    journey_data={
        'key': 'string',
    },
    line_items=[
        shared.PriceItemDto(
            price=shared.Price(
                additional_properties={
                    '$ref': 'string',
                },
                tags=[
                    'string',
                ],
                billing_period=shared.BillingPeriod.WEEKLY,
                tax=shared.Price1(
                dollar_relation=[
                    shared.EntityRelation(
                        additional_properties={
                            'key': 'string',
                        },
                        tags=[
                            'string',
                        ],
                    ),
                ],
            ),
                unit='string',
                unit_amount_currency='EUR',
            ),
            product=shared.ProductInput(
                additional_properties={
                    '$ref': 'string',
                },
                availability_files=[
                    shared.File(
                        dollar_relation=shared.EntityRelation(
                            additional_properties={
                                'key': 'string',
                            },
                            tags=[
                                'string',
                            ],
                        ),
                        additional_properties={
                            'key': 'string',
                        },
                        created_at=dateutil.parser.isoparse('2021-07-18T16:49:23.890Z'),
                        id='<ID>',
                        org='string',
                        schema='string',
                        updated_at=dateutil.parser.isoparse('2022-07-14T15:24:21.428Z'),
                        filename='ascii_program_gold.wav',
                        mime_type='string',
                        versions=[
                            shared.Versions(
                                additional_properties={
                                    'key': 'string',
                                },
                                s3ref=shared.S3ref(
                                    bucket='string',
                                    key='<key>',
                                ),
                            ),
                        ],
                    ),
                ],
                cross_sellable_products=shared.CrossSellableProducts(
                    dollar_relation=[
                        shared.EntityRelation(
                            additional_properties={
                                'key': 'string',
                            },
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                feature=[
                    shared.Feature(
                        tags=[
                            'string',
                        ],
                    ),
                ],
                price_options=shared.PriceOptions(
                    dollar_relation=[
                        shared.EntityRelation(
                            additional_properties={
                                'key': 'string',
                            },
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                product_downloads=shared.ProductDownloads(
                    dollar_relation=[
                        shared.EntityRelation(
                            additional_properties={
                                'key': 'string',
                            },
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                product_images=shared.ProductImages(
                    dollar_relation=[
                        shared.EntityRelation(
                            additional_properties={
                                'key': 'string',
                            },
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
            ),
            metadata=[
                shared.One(),
            ],
        ),
    ],
    metadata=[
        shared.One(),
    ],
    payment_method=shared.PaymentMethod(
        details={
            'key': 'string',
        },
    ),
    source=shared.OrderSource(
        http='/app/v2/journey-builder/editor/db7f6940-994b-11ec-a46d-9f1824ff2939',
        title='Journey: PH Journey',
    ),
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
    tags=[
        'string',
    ],
),
), x_ivy_org_id='string')

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
| errors.SDKError  | 400-600          | */*              |
