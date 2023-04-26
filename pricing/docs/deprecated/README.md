# deprecated

### Available Operations

* [dollar_create_opportunity](#dollar_create_opportunity) - createOpportunity

## dollar_create_opportunity

This API is Deprecated. Please use the Entity API or Submission API to create opportunities.

Enables the creation of a new opportunity. During the creation of an opportunity, an unique customer-readable `opportunity_number` will be generated.
The `opportunity_number` can be used to universally identify an opportunity within epilot platform.


### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DollarCreateOpportunityRequest(
    request_body={
        "saepe": "fuga",
        "in": "corporis",
        "iste": "iure",
        "saepe": "quidem",
    },
    x_ivy_org_id="architecto",
)

res = s.deprecated.dollar_create_opportunity(req)

if res.opportunity is not None:
    # handle response
```
