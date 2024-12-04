# NotificationSDK
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
import epilot_notification
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    s.notification.create_notification(request={
        "message": {
            "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
            "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
        },
        "title": {
            "de": "Meine benutzerdefinierte Aktivität",
            "en": "My custom notification",
        },
        "type": "workflow",
        "caller": epilot_notification.NotificationCallerContext(
            epilot_auth={
                "token": {
                    "cognito_username": "example@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "example@epilot.cloud",
                    "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                },
            },
            **{

            },
        ),
        "force_notify_users": {
            "12345": {
                "email": False,
                "in_app": False,
            },
        },
        "operations": [
            {
                "entity": "f5d37d47-2ec1-43c9-9d5a-0796f80cd327",
                "operation": "updateEntity",
                "params": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "slug": "contact",
                },
                "payload": {
                    "_schema": "contact",
                    "_org": "123",
                    "status": "Inactive",
                },
            },
            {
                "entity": "638cc898-deab-4ed7-aa16-4479c188ee32",
                "operation": "updateEntity",
                "params": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "slug": "contact",
                },
                "payload": {
                    "_schema": "contact",
                    "_org": "123",
                    "status": "Inactive",
                },
            },
            {
                "entity": "63eb0bd2-4ffc-44f4-8323-dcbe87d6bb56",
                "operation": "updateEntity",
                "params": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "slug": "contact",
                },
                "payload": {
                    "_schema": "contact",
                    "_org": "123",
                    "status": "Inactive",
                },
            },
        ],
        "organization_id": "206801",
        "payload": {
            "entity": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "schema": "contact",
            },
        },
        "read_state": False,
        "redirect_url": "https://epilot.cloud",
        "visibility_user_ids": [
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Notification](../../models/notification.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_notification

Get the details of a single notification.

### Example Usage

```python
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.notification.get_notification(id=3493.28)

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | Notification Id                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.NotificationItem](../../models/notificationitem.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_notifications

Get notifications

### Example Usage

```python
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.notification.get_notifications()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The numbers of items to return                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `no_hydrate`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | When true, the payload will not be hydrated with the entity data. This is useful when the client does not need the entity data and wants to save on API calls (performance gain). When false, the payload will be hydrated with the entity data. This is useful when the client needs the entity data to display the notification (e.g. to show the name of the contact in the notification message), but can have a significative performance impact.<br/><br/>This endpoint will eventually be deprecated in favor of GET /v2/notification/notifications which no longer hydrates the payload by default.<br/> |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Response

**[models.GetNotificationsResponseBody](../../models/getnotificationsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_notifications_v2

Get notifications items. These items may eventually contain entities within their payload, which can be hydrated by the client if desired by calling the Entity API directly.

### Example Usage

```python
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.notification.get_notifications_v2()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `after_id`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Base64 encoded cursor to be used for pagination                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The numbers of items to return                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNotificationsV2ResponseBody](../../models/getnotificationsv2responsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_total_unread

Get total unread

### Example Usage

```python
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.notification.get_total_unread()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## mark_all_as_read

Mark all as read

### Example Usage

```python
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    s.notification.mark_all_as_read()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## mark_as_read

Mark as read

### Example Usage

```python
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    s.notification.mark_as_read(id=883397)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Numeric ID of the notification to mark as read                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |