# notification

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


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = {
    "vel": 'error',
    "deserunt": 'suscipit',
    "iure": 'magnam',
    "debitis": 'ipsa',
}

res = s.notification.create_notification(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateNotificationResponse](../../models/operations/createnotificationresponse.md)**


## get_notification

Get the details of a single notification.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetNotificationRequest(
    id=9636.63,
)

res = s.notification.get_notification(req)

if res.notification_item is not None:
    # handle response
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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetNotificationsRequest(
    after_id=272656,
    limit=383441,
)

res = s.notification.get_notifications(req)

if res.get_notifications_200_application_json_object is not None:
    # handle response
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


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.notification.get_total_unread()

if res.get_total_unread_200_text_plain_number is not None:
    # handle response
```


### Response

**[operations.GetTotalUnreadResponse](../../models/operations/gettotalunreadresponse.md)**


## mark_all_as_read

Mark all as read

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.notification.mark_all_as_read()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.MarkAllAsReadResponse](../../models/operations/markallasreadresponse.md)**


## mark_as_read

Mark as read

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.MarkAsReadRequest(
    id=477665,
)

res = s.notification.mark_as_read(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.MarkAsReadRequest](../../models/operations/markasreadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.MarkAsReadResponse](../../models/operations/markasreadresponse.md)**
