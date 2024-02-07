# Messages
(*messages*)

### Available Operations

* [delete_message](#delete_message) - deleteMessage
* [get_message](#get_message) - getMessage
* [get_message_v2](#get_message_v2) - getMessageV2
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
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.delete_message(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Message ID         |


### Response

**[operations.DeleteMessageResponse](../../models/operations/deletemessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_message

Get an email message by id

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.get_message(id='4d74976d-fb64-47fd-85e2-65eea140f5eb')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | Message ID                           | 4d74976d-fb64-47fd-85e2-65eea140f5eb |


### Response

**[operations.GetMessageResponse](../../models/operations/getmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_message_v2

- Fetches message by ID
- If the message html is omitted on the entity, then it keeps the content on the message as a signed url
  {
    ...
    _id: "4d74976d-fb64-47fd-85e2-65eea140f5eb",
    _schema: "message",
    _org: "org-123",
    html_omitted: true,
    html_download_url: "https://s3.eu-central-1.amazonaws.com/epilot-attachments/3f34ce73-089c-4d45-a5ee-c161234e41c3/3f34ce73-089c-4d45-a5ee-c161234e41c3.html"
  }


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.get_message_v2(id='4d74976d-fb64-47fd-85e2-65eea140f5eb')

if res.message_v2 is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | Message ID                           | 4d74976d-fb64-47fd-85e2-65eea140f5eb |


### Response

**[operations.GetMessageV2Response](../../models/operations/getmessagev2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## mark_read_message

Mark message as read

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.mark_read_message(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Message ID         |


### Response

**[operations.MarkReadMessageResponse](../../models/operations/markreadmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## mark_unread_message

Mark message as unread

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.mark_unread_message(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Message ID         |


### Response

**[operations.MarkUnreadMessageResponse](../../models/operations/markunreadmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## send_message

Send an email message

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.send_message(message_request_params=components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error=components.SendError(),
    ),
    subject='Request for solar panel price',
    bcc=[
        components.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=components.SendError(),
        ),
    ],
    cc=[
        components.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=components.SendError(),
        ),
    ],
    file=components.AttachmentsRelation(
        dollar_relation=[
            components.File(
                entity_id='f820ce3b-07b0-45ae-bcc6-babb2f53f79f',
                cid='fb222496-a1a5-4639-94f2-07b5e35e4068',
                filename='Produktinformationen_epilot360_Double_Opt_in.pdf',
            ),
        ],
    ),
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    reply_to=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
        send_error=components.SendError(),
    ),
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='string',
        assigned_to=[
            'string',
        ],
    ),
    to=[
        components.Address(
            address='messaging@epilot.cloud',
            name='epilot',
            send_error=components.SendError(),
        ),
    ],
), do_not_create_entities=False)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `message_request_params`                                                                                          | [Optional[components.MessageRequestParams]](../../models/components/messagerequestparams.md)                      | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `do_not_create_entities`                                                                                          | *Optional[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                | When true, this flag lets the caller to send only the message and by-pass creating the thread & message entities. |


### Response

**[operations.SendMessageResponse](../../models/operations/sendmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## trash_message

Move a message to the trash

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.trash_message(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Message ID         |


### Response

**[operations.TrashMessageResponse](../../models/operations/trashmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## untrash_message

Restore a trashed message

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.untrash_message(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Message ID         |


### Response

**[operations.UntrashMessageResponse](../../models/operations/untrashmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_message

Update message metadata

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.messages.update_message()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.UpdateMessageResponse](../../models/operations/updatemessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
