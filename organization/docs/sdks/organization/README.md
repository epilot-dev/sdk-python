# Organization
(*organization*)

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

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organization.get_organization(org_id='739224')

if res.organization is not None:
    # handle response
    pass

```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 | Example                     |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `org_id`                    | *str*                       | :heavy_check_mark:          | The Id of the organization. | 739224                      |


### Response

**[operations.GetOrganizationResponse](../../models/operations/getorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_organization

updateOrganization

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organization.update_organization(org_id='739224', organization=components.Organization(
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
    symbol='EPI',
    website='https://epilot.cloud',
))

if res.organization is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `org_id`                                                                     | *str*                                                                        | :heavy_check_mark:                                                           | The Id of the organization.                                                  | 739224                                                                       |
| `organization`                                                               | [Optional[components.Organization]](../../models/components/organization.md) | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |


### Response

**[operations.UpdateOrganizationResponse](../../models/operations/updateorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
