# Partners
(*partners*)

## Overview

Partners

### Available Operations

* [activate_partner](#activate_partner) - activatePartner
* [approve_partner](#approve_partner) - approvePartner
* [batch_get_assignable](#batch_get_assignable) - batchGet
* [get_partner_by_token](#get_partner_by_token) - getPartnerByToken
* [invite_partner_v2](#invite_partner_v2) - invitePartnerV2
* [reject_partner](#reject_partner) - rejectPartner
* [search_assignable](#search_assignable) - searchAssignables
* [search_geolocation_for_text](#search_geolocation_for_text) - searchGeolocationForText

## activate_partner

Activate partner using an invite token

### Example Usage

```python
from epilot_partner import Epilot

s = Epilot()


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `token`                                                                           | *str*                                                                             | :heavy_check_mark:                                                                | Invite Token                                                                      |
| `activate_partner_payload`                                                        | [Optional[models.ActivatePartnerPayload]](../../models/activatepartnerpayload.md) | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## approve_partner

Approve partner request

### Example Usage

```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.approve_partner(id="e45a6dc2-3795-43a3-ae0f-6b6760f310fc")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of partner                                                   | e45a6dc2-3795-43a3-ae0f-6b6760f310fc                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Partner](../../models/partner.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## batch_get_assignable

Search for assignable users from this organization by its ids


### Example Usage

```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.batch_get_assignable()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.RequestBody]](../../models/.md)                        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.BatchGetAssignableResponseBody](../../models/batchgetassignableresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_partner_by_token

Get partner by token

### Example Usage

```python
from epilot_partner import Epilot

s = Epilot()


res = s.partners.get_partner_by_token(token="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Invite Token                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.Partner](../../models/partner.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## invite_partner_v2

Invite a partner into collaboration. It will send an email to partner and ask to join into collaboration

### Example Usage

```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.invite_partner_v2(id="e45a6dc2-3795-43a3-ae0f-6b6760f310fc")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | The Id of partner                                                                     | e45a6dc2-3795-43a3-ae0f-6b6760f310fc                                                  |
| `partner_invitation_payload`                                                          | [Optional[models.PartnerInvitationPayload]](../../models/partnerinvitationpayload.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |                                                                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |


### Response

**[models.Partner](../../models/partner.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## reject_partner

Reject partner request

### Example Usage

```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.reject_partner(id="e45a6dc2-3795-43a3-ae0f-6b6760f310fc")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The Id of partner                                                   | e45a6dc2-3795-43a3-ae0f-6b6760f310fc                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Partner](../../models/partner.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_assignable

Search for assignable users/organizations from this organization and Partners

Results can include:
 - Users in your organization
 - Users in partner organizations
 - Partner organizations


### Example Usage

```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.search_assignable(request={
    "org_ids": [
        "123",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.SearchAssignableRequestBody](../../models/searchassignablerequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |


### Response

**[models.SearchAssignableResponseBody](../../models/searchassignableresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_geolocation_for_text

Converts a given string, in the format of an address, to geo-location latitude and longitude

### Example Usage

```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


res = s.partners.search_geolocation_for_text(request={
    "address": "Auweg 1, 93055 Regensburg, DE",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchGeolocation](../../models/searchgeolocation.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.Geolocation](../../models/geolocation.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
