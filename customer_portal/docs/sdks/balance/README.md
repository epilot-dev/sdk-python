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

req = operations.GetCustomerBalanceRequest(
    customer_entity_id='1e3f0d58-69d2-4dbb-9a43-3ee63d862e8e',
)

res = s.balance.get_customer_balance(req, operations.GetCustomerBalanceSecurity(
    epilot_auth="",
))

if res.balance is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCustomerBalanceRequest](../../models/operations/getcustomerbalancerequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.GetCustomerBalanceSecurity](../../models/operations/getcustomerbalancesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.GetCustomerBalanceResponse](../../models/operations/getcustomerbalanceresponse.md)**

