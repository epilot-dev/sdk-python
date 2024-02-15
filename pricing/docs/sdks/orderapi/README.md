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
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    currency='EUR',
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
| errors.SDKError  | 4x-5xx           | */*              |

## put_order

Update an existing Order

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.put_order(order_payload=shared.OrderPayload(
    currency='EUR',
    source_type='journey',
), id='<value>')

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
| errors.SDKError  | 4x-5xx           | */*              |
