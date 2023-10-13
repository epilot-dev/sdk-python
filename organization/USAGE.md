<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetOrganizationRequest(
    org_id='739224',
)

res = s.organization.get_organization(req)

if res.organization is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->