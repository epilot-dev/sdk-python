# availability_api

## Overview

Provides endpoints for querying products availability by a set of predefined dimensions.


### Available Operations

* [dollar_availability_check](#dollar_availability_check) - availabilityCheck

## dollar_availability_check

The availability check endpoint

### Example Usage

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
            location=shared.AvailabilityLocation(
                city='Belleville',
                country='Greenland',
                postal_code='60389',
                street='188 Krajcik Spring',
                street_number='quod',
            ),
        ),
        products=[
            'totam',
            'porro',
        ],
    ),
    x_ivy_org_id='dolorum',
)

res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
```
