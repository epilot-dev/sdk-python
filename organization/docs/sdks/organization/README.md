# organization

## Overview

Organization info

### Available Operations

* [get_organization](#get_organization) - getOrganization
* [update_organization](#update_organization) - updateOrganization

## get_organization

getOrganization

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetOrganizationRequest(
    org_id='739224',
)

res = s.organization.get_organization(req)

if res.organization is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetOrganizationRequest](../../models/operations/getorganizationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetOrganizationResponse](../../models/operations/getorganizationresponse.md)**


## update_organization

updateOrganization

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateOrganizationRequest(
    organization=shared.Organization(
        address=shared.OrganizationAddress(
            city='Laruecester',
            country='Suriname',
            postal_code='85846-6342',
            street='092 Jasper Skyway',
            street_number='placeat',
        ),
        email='someone@epilot.cloud',
        free_user_limit=50,
        id='739224',
        is_unlicensed_org=False,
        logo_thumbnail_url='https://epilot-playground-organization-data.s3.eu-central-1.amazonaws.com/epilot-logo.png',
        logo_url='https://epilot-playground-organization-data.s3.eu-central-1.amazonaws.com/epilot-logo.png',
        name='Epilot',
        phone='49123123123',
        pricing_tier='professional',
        signature='<p>Thanks</p>',
        style={
            "iusto": 'excepturi',
            "nisi": 'recusandae',
            "temporibus": 'ab',
        },
        symbol='EPI',
        type=shared.OrganizationType.VENDOR,
        website='https://epilot.cloud',
    ),
    org_id='739224',
)

res = s.organization.update_organization(req)

if res.organization is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateOrganizationRequest](../../models/operations/updateorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateOrganizationResponse](../../models/operations/updateorganizationresponse.md)**

