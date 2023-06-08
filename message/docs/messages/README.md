# messages

### Available Operations

* [delete_message](#delete_message) - deleteMessage
* [get_message](#get_message) - getMessage
* [mark_read_message](#mark_read_message) - markReadMessage
* [mark_unread_message](#mark_unread_message) - markUnreadMessage
* [send_message](#send_message) - sendMessage
* [trash_message](#trash_message) - trashMessage
* [untrash_message](#untrash_message) - untrashMessage
* [update_message](#update_message) - updateMessage

## delete_message

Immediately and permanently delete a message. This operation cannot be undone.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteMessageRequest(
    id='c3f5ad01-9da1-4ffe-b8f0-97b0074f1547',
)

res = s.messages.delete_message(req)

if res.status_code == 200:
    # handle response
```

## get_message

Get an email message by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetMessageRequest(
    id='1b5e6e13-b99d-4488-a1e9-1e450ad2abd4',
)

res = s.messages.get_message(req)

if res.get_message_201_application_json_object is not None:
    # handle response
```

## mark_read_message

Mark message as read

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.MarkReadMessageRequest(
    id='4269802d-502a-494b-b4f6-3c969e9a3efa',
)

res = s.messages.mark_read_message(req)

if res.status_code == 200:
    # handle response
```

## mark_unread_message

Mark message as unread

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.MarkUnreadMessageRequest(
    id='77dfb14c-d66a-4e39-9efb-9ba88f3a6699',
)

res = s.messages.mark_unread_message(req)

if res.status_code == 200:
    # handle response
```

## send_message

Send an email message

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.MessageRequestParams(
    bcc=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "nihil": 'magnam',
            },
            send_status=shared.AddressSendStatus.BOUNCE,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "labore": 'labore',
                "suscipit": 'natus',
                "nobis": 'eum',
            },
            send_status=shared.AddressSendStatus.ERROR,
        ),
    ],
    cc=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "magnam": 'et',
            },
            send_status=shared.AddressSendStatus.COMPLAINT,
        ),
    ],
    file=shared.AttachmentsRelation(
        dollar_relation=[
            shared.File(
                cid='fb222496-a1a5-4639-94f2-07b5e35e4068',
                entity_id='f820ce3b-07b0-45ae-bcc6-babb2f53f79f',
                filename='Produktinformationen_epilot360_Double_Opt_in.pdf',
                inline=False,
                is_message_attachment=False,
                send_as_link=False,
            ),
            shared.File(
                cid='fb222496-a1a5-4639-94f2-07b5e35e4068',
                entity_id='f820ce3b-07b0-45ae-bcc6-babb2f53f79f',
                filename='Produktinformationen_epilot360_Double_Opt_in.pdf',
                inline=False,
                is_message_attachment=False,
                send_as_link=False,
            ),
        ],
    ),
    from_=shared.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error={
            "quos": 'sint',
            "accusantium": 'mollitia',
            "reiciendis": 'mollitia',
        },
        send_status=shared.AddressSendStatus.DELIVERY,
    ),
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    reply_to=shared.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error={
            "dolor": 'necessitatibus',
            "odit": 'nemo',
        },
        send_status=shared.AddressSendStatus.SEND,
    ),
    subject='Request for solar panel price',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=shared.MessageRequestParamsThread(
        assigned_to=[
            'doloribus',
            'debitis',
        ],
        topic='eius',
    ),
    to=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "facilis": 'in',
                "architecto": 'architecto',
                "repudiandae": 'ullam',
            },
            send_status=shared.AddressSendStatus.BOUNCE,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "repellat": 'quibusdam',
                "sed": 'saepe',
            },
            send_status=shared.AddressSendStatus.ERROR,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "consequuntur": 'praesentium',
            },
            send_status=shared.AddressSendStatus.COMPLAINT,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "sunt": 'quo',
            },
            send_status=shared.AddressSendStatus.ERROR,
        ),
    ],
)

res = s.messages.send_message(req)

if res.send_message_201_application_json_object is not None:
    # handle response
```

## trash_message

Move a message to the trash

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.TrashMessageRequest(
    id='dc692601-fb57-46b0-95f0-d30c5fbb2587',
)

res = s.messages.trash_message(req)

if res.status_code == 200:
    # handle response
```

## untrash_message

Restore a trashed message

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UntrashMessageRequest(
    id='053202c7-3d5f-4e9b-90c2-8909b3fe49a8',
)

res = s.messages.untrash_message(req)

if res.status_code == 200:
    # handle response
```

## update_message

Update message metadata

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.messages.update_message()

if res.update_message_201_application_json_object is not None:
    # handle response
```
