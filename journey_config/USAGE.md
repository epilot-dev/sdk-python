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
    "provident": 'distinctio',
    "quibusdam": 'unde',
    "nulla": 'corrupti',
}

res = s.journeys.create_journey(req)

if res.journey_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->