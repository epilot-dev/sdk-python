# BalanceSDK
(*balance*)

## Overview

### Available Operations

* [get_customer_balance](#get_customer_balance) - getCustomerBalance

## get_customer_balance

Get total balance across all contracts and orders of a customer entity.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.balance.get_customer_balance()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Balance](../../models/balance.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |