# AvailabilityAPI
(*availability_api*)

## Overview

Provides endpoints for querying products availability by a set of predefined dimensions.


### Available Operations

* [dollar_availability_check](#dollar_availability_check) - availabilityCheck
* [dollar_validate_availability_file](#dollar_validate_availability_file) - validateAvailabilityFile

## dollar_availability_check

The availability check endpoint

### Example Usage

```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot()


res = s.availability_api.dollar_availability_check(x_ivy_org_id="<value>", availability_check_params={
    "filters": {
        "location": {
            "city": "Cologne",
            "postal_code": "57008",
            "street": "Media Park",
            "street_number": "8a",
        },
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "products": [
        "cd75456a-30e4-4912-95be-e743d5ea175b",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `x_ivy_org_id`                                                                                      | *str*                                                                                               | :heavy_check_mark:                                                                                  | The target Organization Id represented by the caller                                                |
| `availability_check_params`                                                                         | [models.AvailabilityCheckParams](../../models/availabilitycheckparams.md)                           | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `security`                                                                                          | [Optional[models.DollarAvailabilityCheckSecurity]](../../models/dollaravailabilitychecksecurity.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |


### Response

**[models.AvailabilityResult](../../models/availabilityresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_validate_availability_file

Validates an availability file, it returns an array of errors if the file is invalid

### Example Usage

```python
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.availability_api.dollar_validate_availability_file(x_epilot_org_id="739224", id="72c803b2-2e5d-4bd6-bffc-fad998bbbe36")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_epilot_org_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The target Organization Id represented by the caller                | 739224                                                              |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Product ID that the Availability File is attached to                | 72c803b2-2e5d-4bd6-bffc-fad998bbbe36                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.ValidateAvailabilityFileResult](../../models/validateavailabilityfileresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
