# AvailabilityAPI
(*availability_api*)

## Overview

Provides endpoints for querying products availability by a set of predefined dimensions.


### Available Operations

* [dollar_availability_check](#dollar_availability_check) - availabilityCheck

## dollar_availability_check

The availability check endpoint

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="",
)


res = s.availability_api.dollar_availability_check(availability_check_params=shared.AvailabilityCheckParams(
    filters=shared.AvailabilityFilters(
        available_date=dateutil.parser.parse('2017-07-21').date(),
        location=shared.AvailabilityLocation(),
    ),
    products=[
        'string',
    ],
), x_ivy_org_id='string')

if res.availability_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `availability_check_params`                                                      | [shared.AvailabilityCheckParams](../../models/shared/availabilitycheckparams.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `x_ivy_org_id`                                                                   | *str*                                                                            | :heavy_check_mark:                                                               | The target Organization Id represented by the caller                             |


### Response

**[operations.DollarAvailabilityCheckResponse](../../models/operations/dollaravailabilitycheckresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 400-600          | */*              |
