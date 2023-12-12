# Balance
(*balance*)

### Available Operations

* [get_customer_balance](#get_customer_balance) - getCustomerBalance

## get_customer_balance

Get total balance across all contracts and orders of a customer entity.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


res = s.balance.get_customer_balance("<YOUR_BEARER_TOKEN_HERE>")

if res.balance is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `security`                                                                                     | [operations.GetCustomerBalanceSecurity](../../models/operations/getcustomerbalancesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.GetCustomerBalanceResponse](../../models/operations/getcustomerbalanceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
