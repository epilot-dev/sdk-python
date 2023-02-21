<!-- Start SDK Example Usage -->
```python
import epilotapi
from epilotapi.models import operations, shared

s = epilotapi.EpilotAPI()
s.config_security(
    security=shared.Security(
        epilot_auth=shared.SchemeEpilotAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    )
)
   
req = operations.AttachActivityRequest(
    path_params=operations.AttachActivityPathParams(
        id="unde",
    ),
    query_params=operations.AttachActivityQueryParams(
        entities=[
            "porro",
            "nulla",
            "id",
        ],
    ),
)
    
res = s.activity.attach_activity(req)

if res.activity_item is not None:
    # handle response
```
<!-- End SDK Example Usage -->