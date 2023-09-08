# activity

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
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AttachActivityRequest(
    entities=[
        'a05dfc2d-df7c-4c78-8a1b-a928fc816742',
    ],
    id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.activity.attach_activity(req)

if res.activity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.AttachActivityRequest](../../models/operations/attachactivityrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.AttachActivityResponse](../../models/operations/attachactivityresponse.md)**


## create_activity

Create an activity that can be displayed in activity feeds.

- All activites are published as events on the event bus
- Entity mutations are always part of an activity


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.CreateActivityRequest(
    activity=shared.Activity(
        message='{{caller}} did something with {{entity payload.entity.id}}.',
        payload={
            "impedit": 'cum',
        },
        title='My custom activity',
        type='MyCustomActivity',
    ),
    entities=[
        '73920592-9396-4fea-b596-eb10faaa2352',
    ],
)

res = s.activity.create_activity(req)

if res.activity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateActivityRequest](../../models/operations/createactivityrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateActivityResponse](../../models/operations/createactivityresponse.md)**


## get_activity

Get activity by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetActivityRequest(
    id='01F130Q52Q6MWSNS8N2AVXV4JN',
    operations_from=750686,
    operations_size=315428,
)

res = s.activity.get_activity(req)

if res.activity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetActivityRequest](../../models/operations/getactivityrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetActivityResponse](../../models/operations/getactivityresponse.md)**


## get_entity_activity_feed

Get activity feed for an entity


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

req = operations.GetEntityActivityFeedRequest(
    after=dateutil.parser.isoparse('2022-04-10T11:47:13.463Z'),
    before=dateutil.parser.isoparse('2022-06-06T21:04:34.044Z'),
    from_=38425,
    id='7aff1a3a-2fa9-4467-b392-51aa52c3f5ad',
    include_relations=False,
    size=13571,
    slug='contact',
    type='SyncActivity',
)

res = s.activity.get_entity_activity_feed(req)

if res.get_entity_activity_feed_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetEntityActivityFeedRequest](../../models/operations/getentityactivityfeedrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetEntityActivityFeedResponse](../../models/operations/getentityactivityfeedresponse.md)**

