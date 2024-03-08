# Notification
(*notification*)

## Overview

Notification

### Available Operations

* [create_notification](#create_notification) - createNotification
* [get_notification](#get_notification) - getNotification
* [get_notifications](#get_notifications) - getNotifications
* [get_notifications_v2](#get_notifications_v2) - getNotificationsV2
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
    message=shared.Message(
        de='{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.',
        en='{{caller}} did something with {{contact.entity.id}} {{branch.name}}.',
    ),
    title=shared.Title(
        de='Meine benutzerdefinierte Aktivität',
        en='My custom notification',
    ),
    type='workflow',
    force_notify_users={
        '12345': '<value>',
    },
    organization_id='206801',
    payload={
        'entity': '<value>',
    },
    redirect_url='https://epilot.cloud',
    visibility_user_ids=[
        '1',
        '2',
        '3',
        '4',
        '5',
    ],
)

res = s.notification.create_notification(req)

if res is not None:
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
| errors.SDKError | 4x-5xx          | */*             |

## get_notification

Get the details of a single notification.

### Example Usage

```python
import epilot

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
| errors.SDKError | 4x-5xx          | */*             |

## get_notifications

Get notifications

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.get_notifications(after_id=436719, limit=707368, no_hydrate=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The numbers of items to return                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `no_hydrate`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | When true, the payload will not be hydrated with the entity data. This is useful when the client does not need the entity data and wants to save on API calls (performance gain). When false, the payload will be hydrated with the entity data. This is useful when the client needs the entity data to display the notification (e.g. to show the name of the contact in the notification message), but can have a significative performance impact.<br/><br/>This endpoint will eventually be deprecated in favor of GET /v2/notification/notifications which no longer hydrates the payload by default.<br/> |


### Response

**[operations.GetNotificationsResponse](../../models/operations/getnotificationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_notifications_v2

Get notifications items. These items may eventually contain entities within their payload, which can be hydrated by the client if desired by calling the Entity API directly.

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.get_notifications_v2(after_id=629883, limit=111070)

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

**[operations.GetNotificationsV2Response](../../models/operations/getnotificationsv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
| errors.SDKError | 4x-5xx          | */*             |

## mark_all_as_read

Mark all as read

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.mark_all_as_read()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.MarkAllAsReadResponse](../../models/operations/markallasreadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## mark_as_read

Mark as read

### Example Usage

```python
import epilot

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification.mark_as_read(id=883397)

if res is not None:
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
| errors.SDKError | 4x-5xx          | */*             |
