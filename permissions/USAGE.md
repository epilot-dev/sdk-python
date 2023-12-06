<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.assignments.add_assignment(role_id='123:owner', user_id='1')

if res.assignment is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->