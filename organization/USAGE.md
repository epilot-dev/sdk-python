<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateOrganizationRequest()

res = s.organization.create_organization(req)

if res.organization is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->