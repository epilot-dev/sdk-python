<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "deserunt": "porro",
    "nulla": "id",
    "vero": "perspiciatis",
}
    
res = s.notification.create_notification(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->