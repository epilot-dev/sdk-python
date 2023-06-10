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
    id='fc2ddf7c-c78c-4a1b-a928-fc816742cb73',
)

res = s.messages.delete_message(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteMessageRequest](../../models/operations/deletemessagerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteMessageResponse](../../models/operations/deletemessageresponse.md)**


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
    id='92059293-96fe-4a75-96eb-10faaa2352c5',
)

res = s.messages.get_message(req)

if res.get_message_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetMessageRequest](../../models/operations/getmessagerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetMessageResponse](../../models/operations/getmessageresponse.md)**


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
    id='955907af-f1a3-4a2f-a946-7739251aa52c',
)

res = s.messages.mark_read_message(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.MarkReadMessageRequest](../../models/operations/markreadmessagerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.MarkReadMessageResponse](../../models/operations/markreadmessageresponse.md)**


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
    id='3f5ad019-da1f-4fe7-8f09-7b0074f15471',
)

res = s.messages.mark_unread_message(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.MarkUnreadMessageRequest](../../models/operations/markunreadmessagerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.MarkUnreadMessageResponse](../../models/operations/markunreadmessageresponse.md)**


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
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.DELIVERY,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.ERROR,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.REJECT,
        ),
    ],
    cc=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.SEND,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.DELIVERY,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.BOUNCE,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
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
        send_error=shared.AddressSendError(),
        send_status=shared.AddressSendStatus.ERROR,
    ),
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    reply_to=shared.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error=shared.AddressSendError(),
        send_status=shared.AddressSendStatus.DELIVERY,
    ),
    subject='Request for solar panel price',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=shared.MessageRequestParamsThread(
        assigned_to=[
            'rem',
            'voluptates',
            'quasi',
        ],
        topic='repudiandae',
    ),
    to=[
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.SEND,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.ERROR,
        ),
        shared.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=shared.AddressSendError(),
            send_status=shared.AddressSendStatus.DELIVERY,
        ),
    ],
)

res = s.messages.send_message(req)

if res.send_message_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.MessageRequestParams](../../models/shared/messagerequestparams.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.SendMessageResponse](../../models/operations/sendmessageresponse.md)**


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
    id='50ad2abd-4426-4980-ad50-2a94bb4f63c9',
)

res = s.messages.trash_message(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.TrashMessageRequest](../../models/operations/trashmessagerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TrashMessageResponse](../../models/operations/trashmessageresponse.md)**


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
    id='69e9a3ef-a77d-4fb1-8cd6-6ae395efb9ba',
)

res = s.messages.untrash_message(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UntrashMessageRequest](../../models/operations/untrashmessagerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UntrashMessageResponse](../../models/operations/untrashmessageresponse.md)**


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


### Response

**[operations.UpdateMessageResponse](../../models/operations/updatemessageresponse.md)**

