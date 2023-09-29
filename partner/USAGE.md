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
        organization_id='Future likewise San',
        signed_up_email='Julius_Anderson66@gmail.com',
    ),
    token='CLI',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->