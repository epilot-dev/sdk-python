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
<!-- End SDK Example Usage -->