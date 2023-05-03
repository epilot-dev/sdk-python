<!-- Start SDK Example Usage -->
```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "provident": 'distinctio',
    "quibusdam": 'unde',
    "nulla": 'corrupti',
}

res = s.notification.create_notification(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->