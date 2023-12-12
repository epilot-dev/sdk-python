# Notification
(*notification*)

## Overview

Notification

### Available Operations

* [create_notification](#create_notification) - createNotification
* [get_notification](#get_notification) - getNotification
* [get_notifications](#get_notifications) - getNotifications
* [get_total_unread](#get_total_unread) - getTotalUnread
* [mark_all_as_read](#mark_all_as_read) - markAllAsRead
* [mark_as_read](#mark_as_read) - markAsRead

## create_notification

Create a message that can be displayed in the notification panel.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.Notification(
    additional_properties={
        'key': 'string',
    },
    caller=shared.NotificationCallerContext(
        additional_properties={
            'key': 'string',
        },
        epilot_auth=shared.EpilotAuth(
            token=shared.Token(
                cognito_username='example@epilot.cloud',
                custom_ivy_user_id='10006129',
                email='example@epilot.cloud',
                sub='476e9b48-42f4-4234-a2b0-4668b34626ce',
            ),
        ),
    ),
    force_notify_users={
        '12345': 'string',
    },
    message=shared.Message(
        de='{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.',
        en='{{caller}} did something with {{contact.entity.id}} {{branch.name}}.',
    ),
    operations=[
        shared.EntityOperation(
            entity='d9fa50df-3a77-4db4-9782-9e5cd1039cd9',
            operation='updateEntity',
            params=shared.Params(
                slug='contact',
            ),
            payload={
                '_schema': 'string',
                '_org': 'string',
                'status': 'string',
            },
        ),
    ],
    organization_id='206801',
    payload={
        'entity': 'string',
    },
    redirect_url='https://epilot.cloud',
    title=shared.Title(
        de='Meine benutzerdefinierte Aktivität',
        en='My custom notification',
    ),
    type='workflow',
    visibility_user_ids=[
        '1',
        '2',
        '3',
        '4',
        '5',
    ],
)

res = s.notification.create_notification(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.Notification](../../models/shared/notification.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateNotificationResponse](../../models/operations/createnotificationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_notification

Get the details of a single notification.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.get_notification(id=3493.28)

if res.notification_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *float*            | :heavy_check_mark: | Notification Id    |


### Response

**[operations.GetNotificationResponse](../../models/operations/getnotificationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_notifications

Get notifications

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.get_notifications(after_id=436719, limit=707368)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `after_id`                     | *Optional[int]*                | :heavy_minus_sign:             | N/A                            |
| `limit`                        | *Optional[int]*                | :heavy_minus_sign:             | The numbers of items to return |


### Response

**[operations.GetNotificationsResponse](../../models/operations/getnotificationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_total_unread

Get total unread

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.get_total_unread()

if res.res is not None:
    # handle response
    pass
```


### Response

**[operations.GetTotalUnreadResponse](../../models/operations/gettotalunreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## mark_all_as_read

Mark all as read

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.mark_all_as_read()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.MarkAllAsReadResponse](../../models/operations/markallasreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## mark_as_read

Mark as read

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.mark_as_read(id=883397)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                      | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `id`                                           | *int*                                          | :heavy_check_mark:                             | Numeric ID of the notification to mark as read |


### Response

**[operations.MarkAsReadResponse](../../models/operations/markasreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
