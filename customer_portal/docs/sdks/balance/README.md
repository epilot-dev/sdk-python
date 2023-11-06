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


res = s.balance.get_customer_balance("", customer_entity_id='1e3f0d58-69d2-4dbb-9a43-3ee63d862e8e')

if res.balance is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `security`                                                                                     | [operations.GetCustomerBalanceSecurity](../../models/operations/getcustomerbalancesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |                                                                                                |
| `customer_entity_id`                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Customer entity ID (contact or account)                                                        | 1e3f0d58-69d2-4dbb-9a43-3ee63d862e8e                                                           |


### Response

**[operations.GetCustomerBalanceResponse](../../models/operations/getcustomerbalanceresponse.md)**

