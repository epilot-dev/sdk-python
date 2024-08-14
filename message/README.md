# epilot-message

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=message
```

Poetry
```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=message
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_message
from epilot_message import Epilot

async def main():
    s = Epilot(
        security=epilot_message.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.drafts.create_draft_async(request=epilot_message.MessageRequestParams(
        from_={
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
        subject="Request for solar panel price",
        bcc=[
            {
                "address": "messaging@epilot.cloud",
                "name": "epilot",
            },
        ],
        cc=[
            {
                "address": "messaging@epilot.cloud",
                "name": "epilot",
            },
        ],
        file={
            "dollar_relation": [
                {
                    "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                    "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                    "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
                },
            ],
        },
        html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
        parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
        reply_to={
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
        text="We at ABC GmbH would like to request a price quote for the solar panel.",
        thread={
            "topic": "CUSTOMER_MESSAGE",
            "assigned_to": [
                "206801",
                "200109",
            ],
        },
        to=[
            {
                "address": "messaging@epilot.cloud",
                "name": "epilot",
            },
        ],
    ))
    if res is not None:
        # handle response
        pass

asyncio.run(main())
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

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
),
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_message
from epilot_message import Epilot

s = Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

### Example

```python
import epilot_message
from epilot_message import Epilot, models

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = None
try:
    res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
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
import epilot_message
from epilot_message import Epilot

s = Epilot(
    server_idx=0,
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    server_url="https://message.sls.epilot.io",
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from epilot_message import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_message import Epilot
from epilot_message.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Epilot(async_client=CustomClient(httpx.AsyncClient()))
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
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from epilot_message import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_message"))
```
<!-- End Debugging [debug] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
