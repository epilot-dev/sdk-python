<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)


res = s.partners.activate_partner(token='string', activate_partner_payload=shared.ActivatePartnerPayload(
    company_name='Company name',
    organization_id='string',
    signed_up_email='Lupe.Graham2@hotmail.com',
))

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->