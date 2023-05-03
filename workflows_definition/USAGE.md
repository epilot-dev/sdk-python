<!-- Start SDK Example Usage -->
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
    reason_id='provident',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->