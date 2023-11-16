# openapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=access_token
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AccessTokenParameters(
    assignments=[
        '123:owner',
    ],
    name='Postman Access Token',
)

res = s.access_tokens.create_access_token(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [access_tokens](docs/sdks/accesstokens/README.md)

* [create_access_token](docs/sdks/accesstokens/README.md#create_access_token) - createAccessToken
* [list_access_tokens](docs/sdks/accesstokens/README.md#list_access_tokens) - listAccessTokens
* [revoke_access_token](docs/sdks/accesstokens/README.md#revoke_access_token) - revokeAccessToken

### [public](docs/sdks/public/README.md)

* [get_access_token_jwks](docs/sdks/public/README.md#get_access_token_jwks) - getAccessTokenJwks
* [get_access_token_oidc](docs/sdks/public/README.md#get_access_token_oidc) - getAccessTokenOIDC
* [get_public_token_jwks](docs/sdks/public/README.md#get_public_token_jwks) - getPublicTokenJwks
* [get_public_token_oidc](docs/sdks/public/README.md#get_public_token_oidc) - getPublicTokenOIDC
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AccessTokenParameters(
    assignments=[
        '123:owner',
    ],
    name='Postman Access Token',
)

res = None
try:
    res = s.access_tokens.create_access_token(req)

except (errors.SDKError) as e:
    print(e) # handle exception


if res.object is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://access-token.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_idx=0,
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AccessTokenParameters(
    assignments=[
        '123:owner',
    ],
    name='Postman Access Token',
)

res = s.access_tokens.create_access_token(req)

if res.object is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_url="https://access-token.sls.epilot.io",
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AccessTokenParameters(
    assignments=[
        '123:owner',
    ],
    name='Postman Access Token',
)

res = s.access_tokens.create_access_token(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->
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
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AccessTokenParameters(
    assignments=[
        '123:owner',
    ],
    name='Postman Access Token',
)

res = s.access_tokens.create_access_token(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
