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