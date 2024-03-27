# epilot-notification

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=notification
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [notification](docs/sdks/notification/README.md)

* [create_notification](docs/sdks/notification/README.md#create_notification) - createNotification
* [get_notification](docs/sdks/notification/README.md#get_notification) - getNotification
* [get_notifications](docs/sdks/notification/README.md#get_notifications) - getNotifications
* [get_notifications_v2](docs/sdks/notification/README.md#get_notifications_v2) - getNotificationsV2
* [get_total_unread](docs/sdks/notification/README.md#get_total_unread) - getTotalUnread
* [mark_all_as_read](docs/sdks/notification/README.md#mark_all_as_read) - markAllAsRead
* [mark_as_read](docs/sdks/notification/README.md#mark_as_read) - markAsRead
<!-- End Available Resources and Operations [operations] -->





<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import epilot
from epilot.models import errors, shared

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

res = None
try:
    res = s.notification.create_notification(req)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://notification.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_idx=0,
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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_url="https://notification.sls.epilot.io",
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
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |

To authenticate with the API the `epilot_auth` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
