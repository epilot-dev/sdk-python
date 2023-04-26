<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetOrganizationRequest(
    org_id="739224",
)

res = s.organization.get_organization(req)

if res.organization is not None:
    # handle response
```
<!-- End SDK Example Usage -->