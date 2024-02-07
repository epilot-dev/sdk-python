<!-- Start SDK Example Usage [usage] -->
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
    additional_properties={
        'key': 'string',
    },
    caller=shared.NotificationCallerContext(
        additional_properties={
            'key': 'string',
        },
        epilot_auth=shared.EpilotAuth(
            token=shared.Token(
                cognito_username='example@epilot.cloud',
                custom_ivy_user_id='10006129',
                email='example@epilot.cloud',
                sub='476e9b48-42f4-4234-a2b0-4668b34626ce',
            ),
        ),
    ),
    force_notify_users={
        '12345': 'string',
    },
    operations=[
        shared.EntityOperation(
            entity='d9fa50df-3a77-4db4-9782-9e5cd1039cd9',
            operation='updateEntity',
            params=shared.Params(
                slug='contact',
            ),
            payload={
                '_schema': 'string',
                '_org': 'string',
                'status': 'string',
            },
        ),
    ],
    organization_id='206801',
    payload={
        'entity': 'string',
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

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->