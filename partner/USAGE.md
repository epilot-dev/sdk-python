<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.ActivatePartnerRequest(
    activate_partner_payload=shared.ActivatePartnerPayload(
        company_name='Company name',
        organization_id='corrupti',
        signed_up_email='Micheal_Sporer@yahoo.com',
    ),
    token='corrupti',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->