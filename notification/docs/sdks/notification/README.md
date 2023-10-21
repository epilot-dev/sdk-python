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
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.Notification(
    additional_properties={
        "key": 'string',
    },
    caller=shared.NotificationCallerContext(
        additional_properties={
            "key": 'string',
        },
        epilot_auth=shared.NotificationCallerContextEpilotAuth(
            token=shared.NotificationCallerContextEpilotAuthToken(
                cognito_username='example@epilot.cloud',
                custom_ivy_user_id='10006129',
                email='example@epilot.cloud',
                sub='476e9b48-42f4-4234-a2b0-4668b34626ce',
            ),
        ),
    ),
    force_notify_users={
        "12345": 'string',
    },
    message=shared.NotificationMessage(
        de='{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.',
        en='{{caller}} did something with {{contact.entity.id}} {{branch.name}}.',
    ),
    operations=[
        shared.EntityOperation(
            entity='d9fa50df-3a77-4db4-9782-9e5cd1039cd9',
            operation='updateEntity',
            params=shared.EntityOperationParams(
                slug='contact',
            ),
            payload={
                "_org": 'string',
                "status": 'string',
                "_schema": 'string',
            },
        ),
    ],
    organization_id='206801',
    payload={
        "entity": 'string',
    },
    redirect_url='https://epilot.cloud',
    title=shared.NotificationTitle(
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


## get_notification

Get the details of a single notification.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetNotificationRequest(
    id=3493.28,
)

res = s.notification.get_notification(req)

if res.notification_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetNotificationRequest](../../models/operations/getnotificationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetNotificationResponse](../../models/operations/getnotificationresponse.md)**


## get_notifications

Get notifications

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetNotificationsRequest()

res = s.notification.get_notifications(req)

if res.get_notifications_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetNotificationsRequest](../../models/operations/getnotificationsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetNotificationsResponse](../../models/operations/getnotificationsresponse.md)**


## get_total_unread

Get total unread

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.notification.get_total_unread()

if res.get_total_unread_200_text_plain_number is not None:
    # handle response
    pass
```


### Response

**[operations.GetTotalUnreadResponse](../../models/operations/gettotalunreadresponse.md)**


## mark_all_as_read

Mark all as read

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.notification.mark_all_as_read()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.MarkAllAsReadResponse](../../models/operations/markallasreadresponse.md)**


## mark_as_read

Mark as read

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.MarkAsReadRequest(
    id=883397,
)

res = s.notification.mark_as_read(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.MarkAsReadRequest](../../models/operations/markasreadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.MarkAsReadResponse](../../models/operations/markasreadresponse.md)**

