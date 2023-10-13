<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AddAssignmentRequest(
    role_id='123:owner',
    user_id='1',
)

res = s.assignments.add_assignment(req)

if res.assignment is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->