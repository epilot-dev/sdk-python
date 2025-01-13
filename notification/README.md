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
            **{

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
                **{

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

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
