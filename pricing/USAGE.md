<!-- Start SDK Example Usage -->
```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DollarAvailabilityCheckRequest(
    availability_check_params=shared.AvailabilityCheckParams(
        filters=shared.AvailabilityFilters(
            available_date=dateutil.parser.parse('2017-07-21').date(),
            location=shared.AvailabilityLocation(
                city='Laruecester',
                country='Suriname',
                postal_code='85846-6342',
                street='092 Jasper Skyway',
                street_number='placeat',
            ),
        ),
        products=[
            'iusto',
            'excepturi',
            'nisi',
        ],
    ),
    x_ivy_org_id='recusandae',
)

res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
```
<!-- End SDK Example Usage -->