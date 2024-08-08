# epilot-pricing

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=pricing
```

Poetry
```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=pricing
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import dateutil.parser
from epilot_pricing import Epilot

async def main():
    s = Epilot(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.catalog_api.dollar_private_search_catalog_async(request={
        "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
        "availability": {
            "location": {},
            "available_date": dateutil.parser.parse("2017-07-21").date(),
        },
        "from_": 0,
        "size": 200,
        "sort": "description ASC",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [catalog_api](docs/sdks/catalogapi/README.md)

* [dollar_private_search_catalog](docs/sdks/catalogapi/README.md#dollar_private_search_catalog) - privateSearchCatalog
* [dollar_search_catalog](docs/sdks/catalogapi/README.md#dollar_search_catalog) - searchCatalog

### [external_integrations_api](docs/sdks/externalintegrationsapi/README.md)

* [dollar_compute_price](docs/sdks/externalintegrationsapi/README.md#dollar_compute_price) - calculatePricingDetails
* [dollar_delete_credentials](docs/sdks/externalintegrationsapi/README.md#dollar_delete_credentials) - deleteCredentials
* [dollar_get_credentials](docs/sdks/externalintegrationsapi/README.md#dollar_get_credentials) - getCredentials
* [dollar_save_credentials](docs/sdks/externalintegrationsapi/README.md#dollar_save_credentials) - saveCredentials
* [dollar_search_providers](docs/sdks/externalintegrationsapi/README.md#dollar_search_providers) - searchProviders
* [dollar_search_streets](docs/sdks/externalintegrationsapi/README.md#dollar_search_streets) - searchStreets

### [order_api](docs/sdks/orderapi/README.md)

* [dollar_calculate_pricing_details](docs/sdks/orderapi/README.md#dollar_calculate_pricing_details) - calculatePricingDetails
* [create_order](docs/sdks/orderapi/README.md#create_order) - createOrder
* [put_order](docs/sdks/orderapi/README.md#put_order) - putOrder

### [availability_api](docs/sdks/availabilityapi/README.md)

* [dollar_availability_check](docs/sdks/availabilityapi/README.md#dollar_availability_check) - availabilityCheck
* [dollar_validate_availability_file](docs/sdks/availabilityapi/README.md#dollar_validate_availability_file) - validateAvailabilityFile

### [cart_api](docs/sdks/cartapi/README.md)

* [dollar_checkout_cart](docs/sdks/cartapi/README.md#dollar_checkout_cart) - checkoutCart
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import dateutil.parser
from epilot.utils import BackoffStrategy, RetryConfig
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import dateutil.parser
from epilot.utils import BackoffStrategy, RetryConfig
from epilot_pricing import Epilot

s = Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

### Example

```python
import dateutil.parser
from epilot_pricing import Epilot, models

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

except models.Error as e:
    # handle exception
    raise(e)
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
| 0 | `https://pricing-api.sls.epilot.io` | None |
| 1 | `https://pricing-api.sls.epilot.io` | None |

#### Example

```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot(
    server_idx=1,
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot(
    server_url="https://pricing-api.sls.epilot.io",
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

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
from epilot_pricing import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_pricing import Epilot
from epilot_pricing.httpclient import AsyncHttpClient
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

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |

To authenticate with the API the `epilot_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

if res is not None:
    # handle response
    pass

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot()


res = s.catalog_api.dollar_search_catalog(catalog_search={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
}, x_ivy_org_id="739224")

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from epilot_pricing import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_pricing"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
