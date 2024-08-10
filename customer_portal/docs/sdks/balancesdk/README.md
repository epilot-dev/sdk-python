# BalanceSDK
(*balance*)

### Available Operations

* [get_customer_balance](#get_customer_balance) - getCustomerBalance

## get_customer_balance

Get total balance across all contracts and orders of a customer entity.

### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.balance.get_customer_balance()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.Balance](../../models/balance.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
