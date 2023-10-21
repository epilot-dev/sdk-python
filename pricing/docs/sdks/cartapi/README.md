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
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DollarCheckoutCartRequest(
    checkout_cart=shared.CheckoutCart(
        shared.CartDto(
            additional_addresses=[
                shared.Address(
                    additional_properties={
                        "key": 'string',
                    },
                    tags=[
                        'billing',
                    ],
                ),
            ],
            billing_address=shared.Address(
                additional_properties={
                    "key": 'string',
                },
                tags=[
                    'billing',
                ],
            ),
            consents={
                "key": 'string',
            },
            customer=shared.Customer(),
            delivery_address=shared.Address(
                additional_properties={
                    "key": 'string',
                },
                tags=[
                    'billing',
                ],
            ),
            files=[
                'string',
            ],
            journey_data={
                "key": 'string',
            },
            line_items=[
                shared.PriceItemDtoInput(
                    price=shared.Price(
                        additional_properties={
                            "$ref": 'string',
                        },
                        tags=[
                            'string',
                        ],
                    shared.BillingPeriod.WEEKLY,
                    shared.SalesTax.NONTAXABLE,
                        [
                            shared.Tax(
                                additional_properties={
                                    "behavior": 'string',
                                    "region": 'string',
                                    "_schema": 'string',
                                    "_updated_at": 'string',
                                    "_id": 'string',
                                    "description": 'string',
                                    "region_label": 'string',
                                    "_org": 'string',
                                    "_tags": 'string',
                                    "_created_at": 'string',
                                    "type": 'string',
                                    "active": 'string',
                                },
                                created_at=dateutil.parser.isoparse('2021-07-18T16:49:23.890Z'),
                                id='8a718dcd-4d08-4ffa-b671-3e809e1b5095',
                                org='string',
                                schema='string',
                                tags=[
                                    'string',
                                ],
                                title='string',
                                updated_at=dateutil.parser.isoparse('2023-04-18T02:54:24.080Z'),
                                behavior=shared.TaxBehavior.INCLUSIVE_MIXED,
                                rate=1343.96,
                                type=shared.TaxType.VAT,
                            ),
                        ],
                    'string',
                        unit_amount_currency='EUR',
                    ),
                    product=shared.ProductInput(
                        additional_properties={
                            "$ref": 'string',
                        },
                        availability_files=[
                            shared.File(
                                dollar_relation=shared.EntityRelation(
                                    additional_properties={
                                        "key": 'string',
                                    },
                                    tags=[
                                        'string',
                                    ],
                                ),
                                additional_properties={
                                    "key": 'string',
                                },
                                created_at=dateutil.parser.isoparse('2021-12-13T21:52:33.452Z'),
                                id='<ID>',
                                org='string',
                                schema='string',
                                updated_at=dateutil.parser.isoparse('2022-10-07T05:49:24.603Z'),
                                filename='specialist.m3a',
                                mime_type='string',
                                versions=[
                                    shared.FileVersions(
                                        additional_properties={
                                            "key": 'string',
                                        },
                                        s3ref=shared.FileVersionsS3ref(
                                            bucket='string',
                                            key='<key>',
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        cross_sellable_products=shared.ProductCrossSellableProducts(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "key": 'string',
                                    },
                                    tags=[
                                        'string',
                                    ],
                                ),
                            ],
                        ),
                        feature=[
                            shared.ProductFeature(
                                tags=[
                                    'string',
                                ],
                            ),
                        ],
                        price_options=shared.ProductPriceOptions(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "key": 'string',
                                    },
                                    tags=[
                                        'string',
                                    ],
                                ),
                            ],
                        ),
                        product_downloads=shared.ProductProductDownloads(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "key": 'string',
                                    },
                                    tags=[
                                        'string',
                                    ],
                                ),
                            ],
                        ),
                        product_images=shared.ProductProductImages(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "key": 'string',
                                    },
                                    tags=[
                                        'string',
                                    ],
                                ),
                            ],
                        ),
                    ),
                    metadata=[
                        shared.MetaData1(),
                    ],
                ),
            ],
            metadata=[
                shared.MetaData1(),
            ],
            payment_method=shared.PaymentMethod(
                details={
                    "key": 'string',
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
    ),
    x_ivy_org_id='string',
)

res = s.cart_api.dollar_checkout_cart(req)

if res.checkout_cart_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DollarCheckoutCartRequest](../../models/operations/dollarcheckoutcartrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.DollarCheckoutCartResponse](../../models/operations/dollarcheckoutcartresponse.md)**

