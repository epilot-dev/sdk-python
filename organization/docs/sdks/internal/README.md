# Internal
(*internal*)

### Available Operations

* [create_organization](#create_organization) - createOrganization

## create_organization

createOrganization

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateOrganizationRequest(
    organization_detail=components.OrganizationDetail(
        name='epilot',
        pricing_tier_id='01GEKHZHSN19KK10ZS92Y3WY9B',
        type='Vendor',
        email_address='epilot@epilot.cloud',
    ),
    owner_user=components.OwnerUser(
        email_address='ny.huynhthi@axonactive.com',
        full_name='Ny Huynh',
    ),
)

res = s.internal.create_organization(req)

if res.organization is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.CreateOrganizationRequest](../../models/components/createorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateOrganizationResponse](../../models/operations/createorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
