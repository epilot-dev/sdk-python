# closing_reason

### Available Operations

* [change_reason_status](#change_reason_status) - changeReasonStatus
* [create_closing_reason](#create_closing_reason) - createClosingReason
* [get_all_closing_reasons](#get_all_closing_reasons) - getAllClosingReasons

## change_reason_status

Change the status of a Closing Reason (eg. ACTIVE to INACTIVE).

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ChangeReasonStatusRequest(
    change_reason_status_req=shared.ChangeReasonStatusReq(
        status=shared.ClosingReasonsStatusEnum.INACTIVE,
    ),
    reason_id='quibusdam',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
```

## create_closing_reason

A created Closing Reason is stored for the organization and will be displayed in the library of reasons.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.ClosingReason(
    creation_time='unde',
    id='d8d69a67-4e0f-4467-8c87-96ed151a05df',
    last_update_time='quo',
    status=shared.ClosingReasonsStatusEnum.ACTIVE,
    title='Dr.',
)

res = s.closing_reason.create_closing_reason(req)

if res.closing_reason is not None:
    # handle response
```

## get_all_closing_reasons

Get all Closing Reasons defined in the organization by default all Active.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetAllClosingReasonsRequest(
    include_inactive=False,
)

res = s.closing_reason.get_all_closing_reasons(req)

if res.closing_reasons is not None:
    # handle response
```
