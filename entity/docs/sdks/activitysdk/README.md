# ActivitySDK
(*activity*)

## Overview

Entity Events

### Available Operations

* [attach_activity](#attach_activity) - attachActivity
* [create_activity](#create_activity) - createActivity
* [get_activity](#get_activity) - getActivity
* [get_entity_activity_feed](#get_entity_activity_feed) - getEntityActivityFeed

## attach_activity

Attach existing activity to entity activity feeds

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.activity.attach_activity(request={
        "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.AttachActivityRequest](../../models/attachactivityrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.BaseActivityItem](../../models/baseactivityitem.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.AttachActivityResponseBody | 404                               | application/json                  |
| models.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## create_activity

Create an activity that can be displayed in activity feeds.

- All activites are published as events on the event bus
- Entity mutations are always part of an activity


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.activity.create_activity(request={
        "activity": {
            "message": "{{caller}} did something with {{entity payload.entity.id}}.",
            "title": "My custom activity",
            "type": "MyCustomActivity",
            "payload": {
                "entity": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "schema": "contact",
                },
            },
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateActivityRequest](../../models/createactivityrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.BaseActivityItem](../../models/baseactivityitem.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_activity

Get activity by id

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.activity.get_activity(request={
        "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetActivityRequest](../../models/getactivityrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ActivityItem](../../models/activityitem.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.GetActivityResponseBody | 404                            | application/json               |
| models.SDKError                | 4XX, 5XX                       | \*/\*                          |

## get_entity_activity_feed

Get activity feed for an entity


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.activity.get_entity_activity_feed(request={
        "id": "518ad1d0-b9ca-4e17-9ff0-7e4738e5f1ef",
        "slug": "contact",
        "type": "SyncActivity",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.GetEntityActivityFeedRequest](../../models/getentityactivityfeedrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GetEntityActivityFeedResponseBody](../../models/getentityactivityfeedresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.GetEntityActivityFeedActivityResponseBody | 404                                              | application/json                                 |
| models.SDKError                                  | 4XX, 5XX                                         | \*/\*                                            |