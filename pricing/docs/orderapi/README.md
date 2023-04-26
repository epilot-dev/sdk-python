# order_api

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


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "reiciendis": "est",
}

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
```

## put_order

Update an existing Order

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PutOrderRequest(
    request_body={
        "laborum": "dolores",
        "dolorem": "corporis",
        "explicabo": "nobis",
    },
    id="5955907a-ff1a-43a2-ba94-67739251aa52",
)

res = s.order_api.put_order(req)

if res.order is not None:
    # handle response
```
