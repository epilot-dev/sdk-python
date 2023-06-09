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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AttachActivityRequest(
    entities=[
        'c5955907-aff1-4a3a-afa9-467739251aa5',
    ],
    id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.activity.attach_activity(req)

if res.activity_item is not None:
    # handle response
```

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
            "quo": 'sequi',
        },
        title='My custom activity',
        type='MyCustomActivity',
    ),
    entities=[
        '5ad019da-1ffe-478f-897b-0074f15471b5',
        'e6e13b99-d488-4e1e-91e4-50ad2abd4426',
        '9802d502-a94b-4b4f-a3c9-69e9a3efa77d',
        'fb14cd66-ae39-45ef-b9ba-88f3a6699707',
    ],
)

res = s.activity.create_activity(req)

if res.activity_item is not None:
    # handle response
```

## get_activity

Get activity by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetActivityRequest(
    id='01F130Q52Q6MWSNS8N2AVXV4JN',
    operations_from=301575,
    operations_size=716075,
)

res = s.activity.get_activity(req)

if res.activity_item is not None:
    # handle response
```

## get_entity_activity_feed

Get activity feed for an entity


### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetEntityActivityFeedRequest(
    after=dateutil.parser.isoparse('2022-06-04T18:23:50.695Z'),
    before=dateutil.parser.isoparse('2022-08-14T00:52:14.624Z'),
    from_=618016,
    id='b6e21419-5989-40af-a563-e2516fe4c8b7',
    size=100226,
    slug='contact',
    type='SyncActivity',
)

res = s.activity.get_entity_activity_feed(req)

if res.get_entity_activity_feed_200_application_json_object is not None:
    # handle response
```
