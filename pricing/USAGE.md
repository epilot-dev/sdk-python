<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DollarAvailabilityCheckRequest(
    availability_check_params=shared.AvailabilityCheckParams(
        filters=shared.AvailabilityFilters(
            available_date="2017-07-21",
            location=shared.AvailabilityLocation(
                city="Larrychester",
                country="Suriname",
                postal_code="85846-6342",
                street="092 Schiller Junction",
                street_number="vel",
            ),
        ),
        products=[
            "deleniti",
            "similique",
            "reprehenderit",
        ],
    ),
    x_ivy_org_id="molestiae",
)
    
res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
```
<!-- End SDK Example Usage -->