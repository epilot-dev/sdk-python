<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateOrganizationRequest(
    organization_detail=components.OrganizationDetail(
        email_address='epilot@epilot.cloud',
        name='epilot',
        pricing_tier_id='01GEKHZHSN19KK10ZS92Y3WY9B',
        type='Vendor',
    ),
    owner_user=components.OwnerUser(
        email_address='ny.huynhthi@axonactive.com',
        full_name='Ny Huynh',
    ),
)

res = s.organization.create_organization(req)

if res.organization is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->