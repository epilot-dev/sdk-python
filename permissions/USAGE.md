<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.assignments.add_assignment(role_id='123:owner', user_id='1')

if res.assignment is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->