# partners

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

## activate_partner

Activate partner using an invite token

### Example Usage

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
        organization_id='illum',
        signed_up_email='Linda.Oberbrunner@yahoo.com',
    ),
    token='magnam',
)

res = s.partners.activate_partner(req)

if res.status_code == 200:
    # handle response
```

## approve_partner

Approve partner request

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.ApprovePartnerRequest(
    id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc',
)

res = s.partners.approve_partner(req)

if res.partner is not None:
    # handle response
```

## batch_get_assignable

Search for assignable users from this organization by its ids


### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = [
    operations.BatchGetAssignableRequestBody(
        org_id='ipsa',
        user_id='delectus',
    ),
    operations.BatchGetAssignableRequestBody(
        org_id='tempora',
        user_id='suscipit',
    ),
    operations.BatchGetAssignableRequestBody(
        org_id='molestiae',
        user_id='minus',
    ),
    operations.BatchGetAssignableRequestBody(
        org_id='placeat',
        user_id='voluptatum',
    ),
]

res = s.partners.batch_get_assignable(req)

if res.batch_get_assignable_200_application_json_object is not None:
    # handle response
```

## get_partner_by_token

Get partner by token

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetPartnerByTokenRequest(
    token='iusto',
)

res = s.partners.get_partner_by_token(req)

if res.partner is not None:
    # handle response
```

## invite_partner

Create a new partner in partner directory and send an invite email to accept request

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.InvitePartnerRequest(
    partner_invitation_payload=shared.PartnerInvitationPayload(
        language=shared.PartnerInvitationPayloadLanguage.DE,
    ),
    id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc',
)

res = s.partners.invite_partner(req)

if res.partner is not None:
    # handle response
```

## reject_partner

Reject partner request

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.RejectPartnerRequest(
    id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc',
)

res = s.partners.reject_partner(req)

if res.partner is not None:
    # handle response
```

## resend_partner_invitation

Resend partner invitation email

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.ResendPartnerInvitationRequest(
    request_body=operations.ResendPartnerInvitationRequestBody(
        language=operations.ResendPartnerInvitationRequestBodyLanguage.EN,
    ),
    id='e45a6dc2-3795-43a3-ae0f-6b6760f310fc',
)

res = s.partners.resend_partner_invitation(req)

if res.partner is not None:
    # handle response
```

## search_assignable

Search for assignable users/organizations from this organization and Partners

Results can include:
 - Users in your organization
 - Users in partner organizations
 - Partner organizations


### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        as_organization="YOUR_API_KEY_HERE",
    ),
)

req = operations.SearchAssignableRequestBody(
    from_=925597,
    org_ids=[
        '123',
        '123',
        '123',
        '123',
    ],
    q='ab',
    size=337396,
    types=[
        operations.SearchAssignableRequestBodyTypes.PARTNER_USER,
    ],
)

res = s.partners.search_assignable(req)

if res.search_assignable_200_application_json_object is not None:
    # handle response
```
