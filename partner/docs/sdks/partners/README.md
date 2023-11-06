# Partners
(*partners*)

## Overview

Partners

### Available Operations

* [activate_partner](#activate_partner) - activatePartner
* [approve_partner](#approve_partner) - approvePartner
* [batch_get_assignable](#batch_get_assignable) - batchGet
* [get_partner_by_token](#get_partner_by_token) - getPartnerByToken
* [invite_partner](#invite_partner) - invitePartner
* [reject_partner](#reject_partner) - rejectPartner
* [resend_partner_invitation](#resend_partner_invitation) - resendPartnerInvitation
* [search_assignable](#search_assignable) - searchAssignables
* [search_geolocation_for_text](#search_geolocation_for_text) - searchGeolocationForText

## activate_partner

Activate partner using an invite token

### Example Usage

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

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `token`                                                                                  | *str*                                                                                    | :heavy_check_mark:                                                                       | Invite Token                                                                             |
| `activate_partner_payload`                                                               | [Optional[shared.ActivatePartnerPayload]](../../models/shared/activatepartnerpayload.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |


### Response

**[operations.ActivatePartnerResponse](../../models/operations/activatepartnerresponse.md)**


## approve_partner

Approve partner request

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)


res = s.partners.approve_partner(id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc')

if res.partner is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | The Id of partner                    | e45a6dc2-3795-43a3-ae0f-6b6760f310fc |


### Response

**[operations.ApprovePartnerResponse](../../models/operations/approvepartnerresponse.md)**


## batch_get_assignable

Search for assignable users from this organization by its ids


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)

req = [
    operations.BatchGetAssignableRequestBody(
        user_id='string',
    ),
]

res = s.partners.batch_get_assignable(req)

if res.batch_get_assignable_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[operations.BatchGetAssignableRequestBody]](../../models//.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[operations.BatchGetAssignableResponse](../../models/operations/batchgetassignableresponse.md)**


## get_partner_by_token

Get partner by token

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)


res = s.partners.get_partner_by_token(token='string')

if res.partner is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `token`            | *str*              | :heavy_check_mark: | Invite Token       |


### Response

**[operations.GetPartnerByTokenResponse](../../models/operations/getpartnerbytokenresponse.md)**


## invite_partner

Create a new partner in partner directory and send an invite email to accept request

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)


res = s.partners.invite_partner(id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc', partner_invitation_payload=shared.PartnerInvitationPayload())

if res.partner is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `id`                                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The Id of partner                                                                            | e45a6dc2-3795-43a3-ae0f-6b6760f310fc                                                         |
| `partner_invitation_payload`                                                                 | [Optional[shared.PartnerInvitationPayload]](../../models/shared/partnerinvitationpayload.md) | :heavy_minus_sign:                                                                           | N/A                                                                                          |                                                                                              |


### Response

**[operations.InvitePartnerResponse](../../models/operations/invitepartnerresponse.md)**


## reject_partner

Reject partner request

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)


res = s.partners.reject_partner(id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc')

if res.partner is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | The Id of partner                    | e45a6dc2-3795-43a3-ae0f-6b6760f310fc |


### Response

**[operations.RejectPartnerResponse](../../models/operations/rejectpartnerresponse.md)**


## resend_partner_invitation

Resend partner invitation email

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)


res = s.partners.resend_partner_invitation(id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc', request_body=operations.ResendPartnerInvitationRequestBody())

if res.partner is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The Id of partner                                                                                                        | e45a6dc2-3795-43a3-ae0f-6b6760f310fc                                                                                     |
| `request_body`                                                                                                           | [Optional[operations.ResendPartnerInvitationRequestBody]](../../models/operations/resendpartnerinvitationrequestbody.md) | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |


### Response

**[operations.ResendPartnerInvitationResponse](../../models/operations/resendpartnerinvitationresponse.md)**


## search_assignable

Search for assignable users/organizations from this organization and Partners

Results can include:
 - Users in your organization
 - Users in partner organizations
 - Partner organizations


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)

req = operations.SearchAssignableRequestBody(
    org_ids=[
        '123',
    ],
    types=[
        operations.SearchAssignableRequestBodyTypes.PARTNER_USER,
    ],
)

res = s.partners.search_assignable(req)

if res.search_assignable_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.SearchAssignableRequestBody](../../models/operations/searchassignablerequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SearchAssignableResponse](../../models/operations/searchassignableresponse.md)**


## search_geolocation_for_text

Converts a given string, in the format of an address, to geo-location latitude and longitude

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="",
    ),
)

req = shared.SearchGeolocation(
    address='Auweg 1, 93055 Regensburg, DE',
)

res = s.partners.search_geolocation_for_text(req)

if res.geolocation is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.SearchGeolocation](../../models/shared/searchgeolocation.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.SearchGeolocationForTextResponse](../../models/operations/searchgeolocationfortextresponse.md)**

