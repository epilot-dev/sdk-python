<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_notification
from epilot_notification import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.notification.create_notification(request=epilot_notification.Notification(
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
                "cognito_username": "n.ahmad@epilot.cloud",
                "custom_ivy_user_id": "10006129",
                "email": "n.ahmad@epilot.cloud",
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
            "entity": "d9fa50df-3a77-4db4-9782-9e5cd1039cd9",
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
    s = Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    await s.notification.create_notification_async(request=epilot_notification.Notification(
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
                    "cognito_username": "n.ahmad@epilot.cloud",
                    "custom_ivy_user_id": "10006129",
                    "email": "n.ahmad@epilot.cloud",
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
                "entity": "9d857a10-07f9-496b-b883-08c6d4312470",
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