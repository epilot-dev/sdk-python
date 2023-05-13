<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.AddAssignmentRequest(
    role_id='123:owner',
    user_id='1',
)

res = s.assignments.add_assignment(req)

if res.assignment is not None:
    # handle response
```
<!-- End SDK Example Usage -->