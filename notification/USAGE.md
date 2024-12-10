<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_notification
from epilot_notification import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:
    epilot.notification.create_notification(request={
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
        await epilot.notification.create_notification_async(request={
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->