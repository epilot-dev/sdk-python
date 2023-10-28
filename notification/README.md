# epilot-notification

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=notification
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
                "status": 'string',
                "_schema": 'string',
                "_org": 'string',
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [notification](docs/sdks/notification/README.md)

* [create_notification](docs/sdks/notification/README.md#create_notification) - createNotification
* [get_notification](docs/sdks/notification/README.md#get_notification) - getNotification
* [get_notifications](docs/sdks/notification/README.md#get_notifications) - getNotifications
* [get_total_unread](docs/sdks/notification/README.md#get_total_unread) - getTotalUnread
* [mark_all_as_read](docs/sdks/notification/README.md#mark_all_as_read) - markAllAsRead
* [mark_as_read](docs/sdks/notification/README.md#mark_as_read) - markAsRead
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://notification.sls.epilot.io` | None |

For example:


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
    server_idx=0
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
                "_schema": 'string',
                "_org": 'string',
                "status": 'string',
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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
    server_url="https://notification.sls.epilot.io"
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
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
