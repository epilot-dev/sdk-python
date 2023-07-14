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
        '9bd9d8d6-9a67-44e0-b467-cc8796ed151a',
        '05dfc2dd-f7cc-478c-a1ba-928fc816742c',
        'b7392059-2939-46fe-a759-6eb10faaa235',
    ],
    id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.activity.attach_activity(req)

if res.activity_item is not None:
    # handle response
```
<!-- End SDK Example Usage -->