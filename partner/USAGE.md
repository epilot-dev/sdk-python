<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)

req = operations.ActivatePartnerRequest(
    activate_partner_payload=shared.ActivatePartnerPayload(
        company_name='Company name',
        organization_id='bah',
        signed_up_email='Taylor78@gmail.com',
    ),
    token='Advanced',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->