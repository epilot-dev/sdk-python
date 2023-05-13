<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CancelExecutionRequest(
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.cancel_execution(req)

if res.automation_execution is not None:
    # handle response
```
<!-- End SDK Example Usage -->