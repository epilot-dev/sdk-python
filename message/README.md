# epilot-message

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=message
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
                "distinctio": 'quibusdam',
                "unde": 'nulla',
                "corrupti": 'illum',
            },
            send_status=shared.AddressSendStatus.REJECT,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "deserunt": 'suscipit',
                "iure": 'magnam',
                "debitis": 'ipsa',
            },
            send_status=shared.AddressSendStatus.ERROR,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "suscipit": 'molestiae',
                "minus": 'placeat',
            },
            send_status=shared.AddressSendStatus.COMPLAINT,
        ),
    ],
    cc=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "nisi": 'recusandae',
                "temporibus": 'ab',
                "quis": 'veritatis',
            },
            send_status=shared.AddressSendStatus.COMPLAINT,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "ipsam": 'repellendus',
            },
            send_status=shared.AddressSendStatus.ERROR,
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
            "at": 'at',
        },
        send_status=shared.AddressSendStatus.ERROR,
    ),
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    reply_to=shared.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error={
            "quod": 'quod',
            "esse": 'totam',
        },
        send_status=shared.AddressSendStatus.BOUNCE,
    ),
    subject='Request for solar panel price',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=shared.MessageRequestParamsThread(
        assigned_to=[
            'dicta',
            'nam',
            'officia',
        ],
        topic='occaecati',
    ),
    to=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error={
                "hic": 'optio',
                "totam": 'beatae',
                "commodi": 'molestiae',
            },
            send_status=shared.AddressSendStatus.DELIVERY,
        ),
    ],
)

res = s.drafts.create_draft(req)

if res.create_draft_201_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [drafts](docs/drafts/README.md)

* [create_draft](docs/drafts/README.md#create_draft) - createDraft
* [send_draft](docs/drafts/README.md#send_draft) - sendDraft

### [messages](docs/messages/README.md)

* [delete_message](docs/messages/README.md#delete_message) - deleteMessage
* [get_message](docs/messages/README.md#get_message) - getMessage
* [mark_read_message](docs/messages/README.md#mark_read_message) - markReadMessage
* [mark_unread_message](docs/messages/README.md#mark_unread_message) - markUnreadMessage
* [send_message](docs/messages/README.md#send_message) - sendMessage
* [trash_message](docs/messages/README.md#trash_message) - trashMessage
* [untrash_message](docs/messages/README.md#untrash_message) - untrashMessage
* [update_message](docs/messages/README.md#update_message) - updateMessage

### [threads](docs/threads/README.md)

* [assign_thread](docs/threads/README.md#assign_thread) - assignThread
* [delete_thread](docs/threads/README.md#delete_thread) - deleteThread
* [mark_read_thread](docs/threads/README.md#mark_read_thread) - markReadThread
* [mark_unread_thread](docs/threads/README.md#mark_unread_thread) - markUnreadThread
* [search_threads](docs/threads/README.md#search_threads) - searchThreads
* [trash_thread](docs/threads/README.md#trash_thread) - trashThread
* [untrash_thread](docs/threads/README.md#untrash_thread) - untrashThread
* [update_thread](docs/threads/README.md#update_thread) - updateThread
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
