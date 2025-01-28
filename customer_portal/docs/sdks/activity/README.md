# Activity
(*activity*)

## Overview

### Available Operations

* [get_entity_activity_feed](#get_entity_activity_feed) - getEntityActivityFeed

## get_entity_activity_feed

Get activity feed for an entity


### Example Usage

```python
import epilot_customer_portal
from epilot_customer_portal import Epilot

with Epilot(
    security=epilot_customer_portal.Security(
        either_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.activity.get_entity_activity_feed(id="5da0a718-c822-403d-9f5d-20d4584e0528", slug=epilot_customer_portal.EntitySlug.CONTACT, from_=0, include_relations=False, size=25, type_="SyncActivity")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Entity id                                                            | 5da0a718-c822-403d-9f5d-20d4584e0528                                 |
| `slug`                                                               | [models.EntitySlug](../../models/entityslug.md)                      | :heavy_check_mark:                                                   | Entity Type                                                          | contact                                                              |
| `after`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Get activities after this timestamp                                  |                                                                      |
| `before`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | get activities before this timestamp                                 |                                                                      |
| `from_`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | start from page                                                      |                                                                      |
| `include_relations`                                                  | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Include activities from related entities                             |                                                                      |
| `size`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | max number of results to return                                      |                                                                      |
| `type`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Filter by activity type                                              | SyncActivity                                                         |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.GetEntityActivityFeedResponseBody](../../models/getentityactivityfeedresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |