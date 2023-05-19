# drafts

### Available Operations

* [create_draft](#create_draft) - createDraft
* [send_draft](#send_draft) - sendDraft

## create_draft

Create a new draft

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.MessageRequestParams(
    bcc=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "cum": 'esse',
                "ipsum": 'excepturi',
                "aspernatur": 'perferendis',
                "ad": 'natus',
            },
            send_status=shared.AddressSendStatus.SEND,
        ),
    ],
    cc=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "natus": 'laboriosam',
            },
            send_status=shared.AddressSendStatus.ERROR,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "fuga": 'in',
                "corporis": 'iste',
                "iure": 'saepe',
                "quidem": 'architecto',
            },
            send_status=shared.AddressSendStatus.SEND,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "est": 'mollitia',
                "laborum": 'dolores',
                "dolorem": 'corporis',
                "explicabo": 'nobis',
            },
            send_status=shared.AddressSendStatus.DELIVERY,
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
            "minima": 'excepturi',
            "accusantium": 'iure',
        },
        send_status=shared.AddressSendStatus.COMPLAINT,
    ),
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    reply_to=shared.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error={
            "sapiente": 'architecto',
            "mollitia": 'dolorem',
            "culpa": 'consequuntur',
            "repellat": 'mollitia',
        },
        send_status=shared.AddressSendStatus.COMPLAINT,
    ),
    subject='Request for solar panel price',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=shared.MessageRequestParamsThread(
        assigned_to=[
            'commodi',
            'quam',
        ],
        topic='molestiae',
    ),
    to=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "quia": 'quis',
                "vitae": 'laborum',
                "animi": 'enim',
            },
            send_status=shared.AddressSendStatus.SEND,
        ),
    ],
)

res = s.drafts.create_draft(req)

if res.create_draft_201_application_json_object is not None:
    # handle response
```

## send_draft

Send the existing draft to the recipients

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.drafts.send_draft()

if res.send_draft_201_application_json_object is not None:
    # handle response
```
