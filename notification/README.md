# epilot-notification

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=notification
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=notification
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import epilot_notification
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.notification.create_notification(request=epilot_notification.Notification(
        message={
            "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
            "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
        },
        title={
            "de": "Meine benutzerdefinierte Aktivität",
            "en": "My custom notification",
        },
        type="workflow",
        caller=epilot_notification.NotificationCallerContext(
            epilot_auth={
                "token": {
                    "cognito_username": "example@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "example@epilot.cloud",
                    "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                },
            },
        ),
        force_notify_users={
            "12345": {
                "email": False,
                "in_app": False,
            },
        },
        operations=[
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
        organization_id="206801",
        payload={
            "entity": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "schema": "contact",
            },
        },
        read_state=False,
        redirect_url="https://epilot.cloud",
        visibility_user_ids=[
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
    ))

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_notification
from epilot_notification import Epilot

async def main():
    async with Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as epilot:

        await epilot.notification.create_notification_async(request=epilot_notification.Notification(
            message={
                "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
                "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
            },
            title={
                "de": "Meine benutzerdefinierte Aktivität",
                "en": "My custom notification",
            },
            type="workflow",
            caller=epilot_notification.NotificationCallerContext(
                epilot_auth={
                    "token": {
                        "cognito_username": "example@epilot.cloud",
                        "custom_ivy_user_id": "10006129",
                        "email": "example@epilot.cloud",
                        "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                    },
                },
            ),
            force_notify_users={
                "12345": {
                    "email": False,
                    "in_app": False,
                },
            },
            operations=[
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
            organization_id="206801",
            payload={
                "entity": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "schema": "contact",
                },
            },
            read_state=False,
            redirect_url="https://epilot.cloud",
            visibility_user_ids=[
                "1",
                "2",
                "3",
                "4",
                "5",
            ],
        ))

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [notification](docs/sdks/notificationsdk/README.md)

* [create_notification](docs/sdks/notificationsdk/README.md#create_notification) - createNotification
* [get_notification](docs/sdks/notificationsdk/README.md#get_notification) - getNotification
* [get_notifications](docs/sdks/notificationsdk/README.md#get_notifications) - getNotifications
* [get_notifications_v2](docs/sdks/notificationsdk/README.md#get_notifications_v2) - getNotificationsV2
* [get_total_unread](docs/sdks/notificationsdk/README.md#get_total_unread) - getTotalUnread
* [mark_all_as_read](docs/sdks/notificationsdk/README.md#mark_all_as_read) - markAllAsRead
* [mark_as_read](docs/sdks/notificationsdk/README.md#mark_as_read) - markAsRead

</details>
<!-- End Available Resources and Operations [operations] -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

<!-- Start Summary [summary] -->
## Summary

Notification API: Notification API for epilot 360
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [epilot-notification](#epilot-notification)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [IDE Support](#ide-support)
  * [Authentication](#authentication)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      |
| ------------- | ---- | ----------- |
| `epilot_auth` | http | HTTP Bearer |

To authenticate with the API the `epilot_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import epilot_notification
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.notification.create_notification(request=epilot_notification.Notification(
        message={
            "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
            "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
        },
        title={
            "de": "Meine benutzerdefinierte Aktivität",
            "en": "My custom notification",
        },
        type="workflow",
        caller=epilot_notification.NotificationCallerContext(
            epilot_auth={
                "token": {
                    "cognito_username": "example@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "example@epilot.cloud",
                    "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                },
            },
        ),
        force_notify_users={
            "12345": {
                "email": False,
                "in_app": False,
            },
        },
        operations=[
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
        organization_id="206801",
        payload={
            "entity": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "schema": "contact",
            },
        },
        read_state=False,
        redirect_url="https://epilot.cloud",
        visibility_user_ids=[
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
    ))

    # Use the SDK ...

```
<!-- End Authentication [security] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import epilot_notification
from epilot_notification import Epilot
from epilot_notification.utils import BackoffStrategy, RetryConfig

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.notification.create_notification(request=epilot_notification.Notification(
        message={
            "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
            "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
        },
        title={
            "de": "Meine benutzerdefinierte Aktivität",
            "en": "My custom notification",
        },
        type="workflow",
        caller=epilot_notification.NotificationCallerContext(
            epilot_auth={
                "token": {
                    "cognito_username": "example@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "example@epilot.cloud",
                    "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                },
            },
        ),
        force_notify_users={
            "12345": {
                "email": False,
                "in_app": False,
            },
        },
        operations=[
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
        organization_id="206801",
        payload={
            "entity": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "schema": "contact",
            },
        },
        read_state=False,
        redirect_url="https://epilot.cloud",
        visibility_user_ids=[
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
    ),
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import epilot_notification
from epilot_notification import Epilot
from epilot_notification.utils import BackoffStrategy, RetryConfig

with Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.notification.create_notification(request=epilot_notification.Notification(
        message={
            "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
            "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
        },
        title={
            "de": "Meine benutzerdefinierte Aktivität",
            "en": "My custom notification",
        },
        type="workflow",
        caller=epilot_notification.NotificationCallerContext(
            epilot_auth={
                "token": {
                    "cognito_username": "example@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "example@epilot.cloud",
                    "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                },
            },
        ),
        force_notify_users={
            "12345": {
                "email": False,
                "in_app": False,
            },
        },
        operations=[
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
        organization_id="206801",
        payload={
            "entity": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "schema": "contact",
            },
        },
        read_state=False,
        redirect_url="https://epilot.cloud",
        visibility_user_ids=[
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
    ))

    # Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_notification_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| models.APIError | 4XX, 5XX    | \*/\*        |

### Example

```python
import epilot_notification
from epilot_notification import Epilot, models

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    try:

        epilot.notification.create_notification(request=epilot_notification.Notification(
            message={
                "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
                "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
            },
            title={
                "de": "Meine benutzerdefinierte Aktivität",
                "en": "My custom notification",
            },
            type="workflow",
            caller=epilot_notification.NotificationCallerContext(
                epilot_auth={
                    "token": {
                        "cognito_username": "example@epilot.cloud",
                        "custom_ivy_user_id": "10006129",
                        "email": "example@epilot.cloud",
                        "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                    },
                },
            ),
            force_notify_users={
                "12345": {
                    "email": False,
                    "in_app": False,
                },
            },
            operations=[
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
            organization_id="206801",
            payload={
                "entity": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "schema": "contact",
                },
            },
            read_state=False,
            redirect_url="https://epilot.cloud",
            visibility_user_ids=[
                "1",
                "2",
                "3",
                "4",
                "5",
            ],
        ))

        # Use the SDK ...

    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot_notification
from epilot_notification import Epilot

with Epilot(
    server_url="https://notification.sls.epilot.io",
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.notification.create_notification(request=epilot_notification.Notification(
        message={
            "de": "{{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}.",
            "en": "{{caller}} did something with {{contact.entity.id}} {{branch.name}}.",
        },
        title={
            "de": "Meine benutzerdefinierte Aktivität",
            "en": "My custom notification",
        },
        type="workflow",
        caller=epilot_notification.NotificationCallerContext(
            epilot_auth={
                "token": {
                    "cognito_username": "example@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "example@epilot.cloud",
                    "sub": "476e9b48-42f4-4234-a2b0-4668b34626ce",
                },
            },
        ),
        force_notify_users={
            "12345": {
                "email": False,
                "in_app": False,
            },
        },
        operations=[
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
        organization_id="206801",
        payload={
            "entity": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "schema": "contact",
            },
        },
        read_state=False,
        redirect_url="https://epilot.cloud",
        visibility_user_ids=[
            "1",
            "2",
            "3",
            "4",
            "5",
        ],
    ))

    # Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from epilot_notification import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_notification import Epilot
from epilot_notification.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Epilot(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from epilot_notification import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_notification"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
