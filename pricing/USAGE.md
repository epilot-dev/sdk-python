<!-- Start SDK Example Usage -->


```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DollarAvailabilityCheckRequest(
    availability_check_params=shared.AvailabilityCheckParams(
        filters=shared.AvailabilityFilters(
            available_date=dateutil.parser.parse('2017-07-21').date(),
            location=shared.AvailabilityLocation(),
        ),
        products=[
            'Visionary',
        ],
    ),
    x_ivy_org_id='Smart',
)

res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->