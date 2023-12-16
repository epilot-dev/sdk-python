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
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
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
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
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
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
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

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.OrderPayload](../../models/shared/orderpayload.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 400-600          | */*              |

## put_order

Update an existing Order

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.put_order(order_payload=shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
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
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            price=shared.Price(
            additional_properties={
                '$ref': 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.EVERY_QUARTER,
            tax=[
            shared.Tax(
                additional_properties={
                    '_id': 'string',
                    'type': 'string',
                    'description': 'string',
                    'behavior': 'string',
                    'active': 'string',
                    'region': 'string',
                    'region_label': 'string',
                    '_org': 'string',
                    '_schema': 'string',
                    '_tags': 'string',
                    '_created_at': 'string',
                    '_updated_at': 'string',
                },
                created_at=dateutil.parser.isoparse('2021-07-04T18:23:03.249Z'),
                id='10049643-f8ec-4f5e-9903-f16783587126',
                org='string',
                schema='string',
                tags=[
                    'string',
                ],
                title='string',
                updated_at=dateutil.parser.isoparse('2021-04-11T20:52:51.479Z'),
                behavior=shared.Behavior.INCLUSIVE_LOWER,
                rate=7376.37,
                type=shared.TaxType.VAT,
            ),
        ],
            unit=shared.PriceSchemas1.M2,
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
            },
        ),
    ],
    source_type='journey',
), id='string')

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `order_payload`                                            | [shared.OrderPayload](../../models/shared/orderpayload.md) | :heavy_check_mark:                                         | N/A                                                        |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | Order entity ID                                            |


### Response

**[operations.PutOrderResponse](../../models/operations/putorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 400-600          | */*              |
