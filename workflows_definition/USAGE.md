<!-- Start SDK Example Usage [usage] -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='string', change_reason_status_req=shared.ChangeReasonStatusReq(
    status=shared.ClosingReasonsStatus.ACTIVE,
))

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->