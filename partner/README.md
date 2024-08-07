# epilot-partner

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=partner
```

Poetry
```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=partner
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from epilot_partner import Epilot

s = Epilot()


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from epilot_partner import Epilot

async def main():
    s = Epilot()
    await s.partners.activate_partner_async(token="<value>", activate_partner_payload={
        "organization_id": "<value>",
        "signed_up_email": "Flavio.Ankunding@hotmail.com",
        "company_name": "Company name",
    })
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [partners](docs/sdks/partners/README.md)

* [activate_partner](docs/sdks/partners/README.md#activate_partner) - activatePartner
* [approve_partner](docs/sdks/partners/README.md#approve_partner) - approvePartner
* [batch_get_assignable](docs/sdks/partners/README.md#batch_get_assignable) - batchGet
* [get_partner_by_token](docs/sdks/partners/README.md#get_partner_by_token) - getPartnerByToken
* [invite_partner_v2](docs/sdks/partners/README.md#invite_partner_v2) - invitePartnerV2
* [reject_partner](docs/sdks/partners/README.md#reject_partner) - rejectPartner
* [search_assignable](docs/sdks/partners/README.md#search_assignable) - searchAssignables
* [search_geolocation_for_text](docs/sdks/partners/README.md#search_geolocation_for_text) - searchGeolocationForText
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from epilot.utils import BackoffStrategy, RetryConfig
from epilot_partner import Epilot

s = Epilot()


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

# Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from epilot.utils import BackoffStrategy, RetryConfig
from epilot_partner import Epilot

s = Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
)


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

# Use the SDK ...

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
from epilot_partner import Epilot, models

s = Epilot()


try:
    s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

except models.SDKError as e:
    # handle exception
    raise(e)

# Use the SDK ...

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://partner-directory-api.sls.epilot.io` | None |

#### Example

```python
from epilot_partner import Epilot

s = Epilot(
    server_idx=0,
)


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

# Use the SDK ...

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from epilot_partner import Epilot

s = Epilot(
    server_url="https://partner-directory-api.sls.epilot.io",
)


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

# Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from epilot_partner import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_partner import Epilot
from epilot_partner.httpclient import AsyncHttpClient
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

| Name              | Type              | Scheme            |
| ----------------- | ----------------- | ----------------- |
| `as_organization` | apiKey            | API key           |
| `epilot_auth`     | http              | HTTP Bearer       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot_partner
from epilot_partner import Epilot

s = Epilot(
    security=epilot_partner.Security(
        as_organization="<YOUR_API_KEY_HERE>",
    ),
)


s.partners.activate_partner(token="<value>", activate_partner_payload={
    "organization_id": "<value>",
    "signed_up_email": "Lupe.Graham2@hotmail.com",
    "company_name": "Company name",
})

# Use the SDK ...

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from epilot_partner import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_partner"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
