<!-- Start SDK Example Usage [usage] -->
```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->