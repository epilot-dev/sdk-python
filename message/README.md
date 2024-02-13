# epilot-message

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=message
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [drafts](docs/sdks/drafts/README.md)

* [create_draft](docs/sdks/drafts/README.md#create_draft) - createDraft
* [send_draft](docs/sdks/drafts/README.md#send_draft) - sendDraft

### [messages](docs/sdks/messages/README.md)

* [delete_message](docs/sdks/messages/README.md#delete_message) - deleteMessage
* [get_message](docs/sdks/messages/README.md#get_message) - getMessage
* [get_message_v2](docs/sdks/messages/README.md#get_message_v2) - getMessageV2
* [mark_read_message](docs/sdks/messages/README.md#mark_read_message) - markReadMessage
* [mark_unread_message](docs/sdks/messages/README.md#mark_unread_message) - markUnreadMessage
* [send_message](docs/sdks/messages/README.md#send_message) - sendMessage
* [trash_message](docs/sdks/messages/README.md#trash_message) - trashMessage
* [untrash_message](docs/sdks/messages/README.md#untrash_message) - untrashMessage
* [update_message](docs/sdks/messages/README.md#update_message) - updateMessage

### [threads](docs/sdks/threads/README.md)

* [assign_thread](docs/sdks/threads/README.md#assign_thread) - assignThread
* [assign_users](docs/sdks/threads/README.md#assign_users) - assignUsers
* [delete_thread](docs/sdks/threads/README.md#delete_thread) - deleteThread
* [mark_read_thread](docs/sdks/threads/README.md#mark_read_thread) - markReadThread
* [mark_unread_thread](docs/sdks/threads/README.md#mark_unread_thread) - markUnreadThread
* [search_threads](docs/sdks/threads/README.md#search_threads) - searchThreads
* [trash_thread](docs/sdks/threads/README.md#trash_thread) - trashThread
* [untrash_thread](docs/sdks/threads/README.md#untrash_thread) - untrashThread
* [update_thread](docs/sdks/threads/README.md#update_thread) - updateThread
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import epilot
from epilot.models import components, errors

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = None
try:
    res = s.drafts.create_draft(req)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://message.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_idx=0,
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_url="https://message.sls.epilot.io",
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |
| `epilot_org`  | apiKey        | API key       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
