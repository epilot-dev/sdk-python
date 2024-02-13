# Deprecated
(*deprecated*)

### Available Operations

* [~~dollar_create_opportunity~~](#dollar_create_opportunity) - createOpportunity :warning: **Deprecated**

## ~~dollar_create_opportunity~~

This API is Deprecated. Please use the Entity API or Submission API to create opportunities.

Enables the creation of a new opportunity. During the creation of an opportunity, an unique customer-readable `opportunity_number` will be generated.
The `opportunity_number` can be used to universally identify an opportunity within epilot platform.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.deprecated.dollar_create_opportunity(opportunity=shared.OpportunityInput(
    additional_properties={
        '$ref': '#/components/examples/opportunity',
    },
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
), x_ivy_org_id='string')

if res.opportunity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `opportunity`                                                      | [shared.OpportunityInput](../../models/shared/opportunityinput.md) | :heavy_check_mark:                                                 | N/A                                                                | {"$ref":"#/components/examples/opportunity"}                       |
| `x_ivy_org_id`                                                     | *str*                                                              | :heavy_check_mark:                                                 | The target Organization Id represented by the caller               |                                                                    |


### Response

**[operations.DollarCreateOpportunityResponse](../../models/operations/dollarcreateopportunityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
