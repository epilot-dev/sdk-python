<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.executions.cancel_execution(execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4')

if res.automation_execution is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->