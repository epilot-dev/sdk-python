# Activity
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
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

if res.activity_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Activity Id                                                            | 01F130Q52Q6MWSNS8N2AVXV4JN                                             |
| `entities`                                                             | List[*str*]                                                            | :heavy_minus_sign:                                                     | Comma-separated list of entities which the activity primarily concerns |                                                                        |


### Response

**[operations.AttachActivityResponse](../../models/operations/attachactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_activity

Create an activity that can be displayed in activity feeds.

- All activites are published as events on the event bus
- Entity mutations are always part of an activity


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.create_activity(activity=components.Activity(
    message='{{caller}} did something with {{entity payload.entity.id}}.',
    title='My custom activity',
    type='MyCustomActivity',
    payload={
        'entity': '<value>',
    },
), entities=[
    'cf25acc1-fe2b-48d1-825c-2f2569c1faff',
])

if res.activity_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `activity`                                                             | [Optional[components.Activity]](../../models/components/activity.md)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `entities`                                                             | List[*str*]                                                            | :heavy_minus_sign:                                                     | Comma-separated list of entities which the activity primarily concerns |


### Response

**[operations.CreateActivityResponse](../../models/operations/createactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_activity

Get activity by id

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.get_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', operations_from=826530, operations_size=369963)

if res.activity_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Activity Id                                                        | 01F130Q52Q6MWSNS8N2AVXV4JN                                         |
| `operations_from`                                                  | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Pagination offset for operations<br/>                              |                                                                    |
| `operations_size`                                                  | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Maximum number of operations to include in response (default: 10)<br/> |                                                                    |


### Response

**[operations.GetActivityResponse](../../models/operations/getactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_entity_activity_feed

Get activity feed for an entity


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetEntityActivityFeedRequest(
    id='591b83a9-db1e-4df0-8b99-bcaafe81677f',
    slug='contact',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
