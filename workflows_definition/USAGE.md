<!-- Start SDK Example Usage -->


```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ChangeReasonStatusRequest(
    change_reason_status_req=shared.ChangeReasonStatusReq(
        status=shared.ClosingReasonsStatus.ACTIVE,
    ),
    reason_id='sky bluetooth',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->