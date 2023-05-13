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
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
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

## get_notification

Get the details of a single notification.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetNotificationRequest(
    id=9636.63,
)

res = s.notification.get_notification(req)

if res.notification_item is not None:
    # handle response
```

## get_notifications

Get notifications

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
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

## get_total_unread

Get total unread

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.notification.get_total_unread()

if res.get_total_unread_200_text_plain_number is not None:
    # handle response
```

## mark_all_as_read

Mark all as read

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.notification.mark_all_as_read()

if res.status_code == 200:
    # handle response
```

## mark_as_read

Mark as read

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.MarkAsReadRequest(
    id=477665,
)

res = s.notification.mark_as_read(req)

if res.status_code == 200:
    # handle response
```
