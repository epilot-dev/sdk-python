<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AttachActivityRequest(
    entities=[
        'ee1dee63-2954-4671-8246-751c43fec091',
    ],
    id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.activity.attach_activity(req)

if res.activity_item is not None:
    # handle response
```
<!-- End SDK Example Usage -->