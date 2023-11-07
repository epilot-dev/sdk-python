# Activity
(*.activity*)

### Available Operations

* [get_entity_activity_feed](#get_entity_activity_feed) - getEntityActivityFeed

## get_entity_activity_feed

Get activity feed for an entity


### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)

req = operations.GetEntityActivityFeedRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
    slug=components.EntitySlug.CONTACT,
    type='SyncActivity',
)

res = s.activity.get_entity_activity_feed(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetEntityActivityFeedRequest](../../models/operations/getentityactivityfeedrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetEntityActivityFeedResponse](../../models/operations/getentityactivityfeedresponse.md)**

