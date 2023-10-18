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
                        "Florida": 'Diesel',
                    },
                    tags=[
                        'billing',
                    ],
                ),
            ],
            billing_address=shared.Address(
                additional_properties={
                    "quantifying": 'ASCII',
                },
                tags=[
                    'billing',
                ],
            ),
            consents={
                "program": 'gold',
            },
            customer=shared.Customer(),
            delivery_address=shared.Address(
                additional_properties={
                    "Towels": 'on',
                },
                tags=[
                    'billing',
                ],
            ),
            files=[
                'Shirt',
            ],
            journey_data={
                "primary": 'Salad',
            },
            line_items=[
                shared.PriceItemDtoInput(
                    price=shared.Price(
                        additional_properties={
                            "$ref": 'up',
                        },
                        tags=[
                            'before',
                        ],
                    shared.BillingPeriod.YEARLY,
                    shared.SalesTax.NONTAXABLE,
                        shared.PriceTax1(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "minima": 'Kansas',
                                    },
                                    tags=[
                                        'copy',
                                    ],
                                ),
                            ],
                        ),
                    'Borders',
                        unit_amount_currency='EUR',
                    ),
                    product=shared.ProductInput(
                        additional_properties={
                            "$ref": 'scarcely',
                        },
                        availability_files=[
                            shared.File(
                                dollar_relation=shared.EntityRelation(
                                    additional_properties={
                                        "Washington": 'Queenie',
                                    },
                                    tags=[
                                        'Dollar',
                                    ],
                                ),
                                additional_properties={
                                    "Newton": 'male',
                                },
                                created_at=dateutil.parser.isoparse('2022-04-24T12:21:58.835Z'),
                                id='<ID>',
                                org='deposit',
                                schema='Concrete',
                                updated_at=dateutil.parser.isoparse('2021-02-20T21:09:38.652Z'),
                                filename='southwest.wav',
                                mime_type='backing',
                                versions=[
                                    shared.FileVersions(
                                        additional_properties={
                                            "Saint": 'FTP',
                                        },
                                        s3ref=shared.FileVersionsS3ref(
                                            bucket='ionise',
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
                                        "port": 'illustrious',
                                    },
                                    tags=[
                                        'Baht',
                                    ],
                                ),
                            ],
                        ),
                        feature=[
                            shared.ProductFeature(
                                tags=[
                                    'male',
                                ],
                            ),
                        ],
                        price_options=shared.ProductPriceOptions(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "Fiat": 'synergize',
                                    },
                                    tags=[
                                        'black',
                                    ],
                                ),
                            ],
                        ),
                        product_downloads=shared.ProductProductDownloads(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "withdrawal": 'XSS',
                                    },
                                    tags=[
                                        'Cambridgeshire',
                                    ],
                                ),
                            ],
                        ),
                        product_images=shared.ProductProductImages(
                            dollar_relation=[
                                shared.EntityRelation(
                                    additional_properties={
                                        "because": 'Luettgen',
                                    },
                                    tags=[
                                        'Buckinghamshire',
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
                    "Automotive": 'upgrade',
                },
            ),
            source=shared.OrderSource(
                http='/app/v2/journey-builder/editor/db7f6940-994b-11ec-a46d-9f1824ff2939',
                title='Journey: PH Journey',
            ),
            source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
            source_type='journey',
            tags=[
                'maximize',
            ],
        ),
    ),
    x_ivy_org_id='invoice',
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

