# OrderAPI
(*order_api*)

## Overview

This api enables the management of orders in epilot 360, providing features such as:
 - Automatic calculation of totals and price breakdowns for taxes on the Order entity
 - Product and pricing data validation


### Available Operations

* [create_order](#create_order) - createOrder
* [put_order](#put_order) - putOrder

## create_order

Create an order

### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.OrderPayloadInput(
    additional_properties={
        "key": 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                "key": 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    currency='EUR',
    delivery_address=[
        shared.Address(
            additional_properties={
                "key": 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            shared.Price(
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
                            "type": 'string',
                            "active": 'string',
                            "region_label": 'string',
                            "_org": 'string',
                            "_tags": 'string',
                            "_created_at": 'string',
                            "_id": 'string',
                            "description": 'string',
                            "behavior": 'string',
                            "region": 'string',
                            "_schema": 'string',
                            "_updated_at": 'string',
                        },
                        created_at=dateutil.parser.isoparse('2022-08-23T04:46:44.470Z'),
                        id='db7b9f9b-d21b-44f2-9723-407318b6c79c',
                        org='string',
                        schema='string',
                        tags=[
                            'string',
                        ],
                        title='string',
                        updated_at=dateutil.parser.isoparse('2022-08-04T04:36:14.538Z'),
                        behavior=shared.TaxBehavior.INCLUSIVE_LOWER,
                        rate=5305.72,
                        type=shared.TaxType.GST,
                    ),
                ],
            'string',
                unit_amount_currency='EUR',
            ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    shared.Price(
                        additional_properties={
                            "$ref": 'string',
                        },
                        tags=[
                            'string',
                        ],
                    shared.BillingPeriod.MONTHLY,
                    shared.SalesTax.STANDARD,
                        shared.PriceTax1(
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
                    shared.PriceUnit1.L,
                        unit_amount_currency='EUR',
                    ),
                    currency='EUR',
                    metadata=[
                        shared.MetaData1(),
                    ],
                ),
            ],
            metadata=[
                shared.MetaData1(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                "key": 'string',
            },
        ),
    ],
    source_type='journey',
)

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.OrderPayloadInput](../../models/shared/orderpayloadinput.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**


## put_order

Update an existing Order

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

req = operations.PutOrderRequest(
    order_payload_input=shared.OrderPayloadInput(
        additional_properties={
            "key": 'string',
        },
        tags=[
            'string',
        ],
        billing_address=[
            shared.Address(
                additional_properties={
                    "key": 'string',
                },
                tags=[
                    'billing',
                ],
            ),
        ],
        currency='EUR',
        delivery_address=[
            shared.Address(
                additional_properties={
                    "key": 'string',
                },
                tags=[
                    'billing',
                ],
            ),
        ],
        line_items=[
            shared.CompositePriceItemInput(
                shared.Price(
                    additional_properties={
                        "$ref": 'string',
                    },
                    tags=[
                        'string',
                    ],
                shared.BillingPeriod.EVERY_QUARTER,
                shared.SalesTax.STANDARD,
                    shared.PriceTax1(
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
                shared.PriceUnit1.KW,
                    unit_amount_currency='EUR',
                ),
                currency='EUR',
                item_components=[
                    shared.PriceItemInput(
                        shared.Price(
                            additional_properties={
                                "$ref": 'string',
                            },
                            tags=[
                                'string',
                            ],
                        shared.BillingPeriod.MONTHLY,
                        shared.SalesTax.REDUCED,
                            shared.PriceTax1(
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
                        shared.PriceUnit1.KWH,
                            unit_amount_currency='EUR',
                        ),
                        currency='EUR',
                        metadata=[
                            shared.MetaData1(),
                        ],
                    ),
                ],
                metadata=[
                    shared.MetaData1(),
                ],
            ),
        ],
        payment_method=[
            shared.PaymentMethod(
                details={
                    "key": 'string',
                },
            ),
        ],
        source_type='journey',
    ),
    id='<ID>',
)

res = s.order_api.put_order(req)

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.PutOrderRequest](../../models/operations/putorderrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.PutOrderResponse](../../models/operations/putorderresponse.md)**

