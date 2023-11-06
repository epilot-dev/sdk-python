<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.organization.get_organization(org_id='739224')

if res.organization is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->