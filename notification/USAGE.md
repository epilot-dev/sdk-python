<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = {
    "Gasoline": 'on',
}

res = s.notification.create_notification(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->