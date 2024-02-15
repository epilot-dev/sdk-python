<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.activate_partner(token='<value>', activate_partner_payload=shared.ActivatePartnerPayload(
    organization_id='<value>',
    signed_up_email='Lupe.Graham2@hotmail.com',
    company_name='Company name',
))

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->