<!-- Start SDK Example Usage -->


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
```
<!-- End SDK Example Usage -->