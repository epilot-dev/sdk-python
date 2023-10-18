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
        "Marketing": 'program',
    },
    tags=[
        'Caesium',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                "male": 'overload',
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
                "Lawrencium": 'blue',
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
                    "$ref": 'choke',
                },
                tags=[
                    'juvenile',
                ],
            shared.BillingPeriod.WEEKLY,
            shared.SalesTax.NONTAXABLE,
                shared.PriceTax1(
                    dollar_relation=[
                        shared.EntityRelation(
                            additional_properties={
                                "Kenya": 'Bronze',
                            },
                            tags=[
                                'synthesize',
                            ],
                        ),
                    ],
                ),
            shared.PriceUnit1.M2,
                unit_amount_currency='EUR',
            ),
            currency='EUR',
            item_components=[
                shared.PriceItem(),
            ],
            metadata=[
                shared.MetaData1(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                "SAS": 'blue',
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
            "disastrous": 'Credit',
        },
        tags=[
            'Avon',
        ],
        billing_address=[
            shared.Address(
                additional_properties={
                    "East": 'commodi',
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
                    "Wooden": 'mariachi',
                },
                tags=[
                    'billing',
                ],
            ),
        ],
        line_items=[
            shared.CompositePriceItemInput(
                shared.CompositePrice(
                    additional_properties={
                        "$ref": 'beyond',
                    },
                    tags=[
                        'instantly',
                    ],
                    shared.CompositePricePriceComponents2(
                        dollar_relation=[
                            shared.PriceComponentRelation(
                                tags=[
                                    'Croatia',
                                ],
                            ),
                        ],
                    ),
                    unit_amount_currency='EUR',
                ),
                currency='EUR',
                item_components=[
                    shared.PriceItem(),
                ],
                metadata=[
                    shared.MetaData1(),
                ],
            ),
        ],
        payment_method=[
            shared.PaymentMethod(
                details={
                    "beseech": 'Litas',
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

