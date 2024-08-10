# Activity
(*activity*)

### Available Operations

* [get_entity_activity_feed](#get_entity_activity_feed) - getEntityActivityFeed

## get_entity_activity_feed

Get activity feed for an entity


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

s = Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.get_entity_activity_feed(request={
    "id": "5da0a718-c822-403d-9f5d-20d4584e0528",
    "slug": epilot_customer_portal.EntitySlug.CONTACT,
    "type": "SyncActivity",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.GetEntityActivityFeedRequest](../../models/getentityactivityfeedrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |


### Response

**[models.GetEntityActivityFeedResponseBody](../../models/getentityactivityfeedresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
