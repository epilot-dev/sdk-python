<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

if res.activity_item is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->