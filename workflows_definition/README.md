# openapi

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=workflows_definition
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [closing_reason](docs/sdks/closingreason/README.md)

* [change_reason_status](docs/sdks/closingreason/README.md#change_reason_status) - changeReasonStatus
* [create_closing_reason](docs/sdks/closingreason/README.md#create_closing_reason) - createClosingReason
* [get_all_closing_reasons](docs/sdks/closingreason/README.md#get_all_closing_reasons) - getAllClosingReasons

### [workflows](docs/sdks/workflows/README.md)

* [create_definition](docs/sdks/workflows/README.md#create_definition) - createDefinition
* [delete_definition](docs/sdks/workflows/README.md#delete_definition) - deleteDefinition
* [get_definition](docs/sdks/workflows/README.md#get_definition) - getDefinition
* [get_definitions](docs/sdks/workflows/README.md#get_definitions) - getDefinitions
* [get_max_allowed_limit](docs/sdks/workflows/README.md#get_max_allowed_limit) - getMaxAllowedLimit
* [get_workflow_closing_reasons](docs/sdks/workflows/README.md#get_workflow_closing_reasons) - getWorkflowClosingReasons
* [set_workflow_closing_reasons](docs/sdks/workflows/README.md#set_workflow_closing_reasons) - setWorkflowClosingReasons
* [update_definition](docs/sdks/workflows/README.md#update_definition) - updateDefinition
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

### Example

```python
import sdk
from sdk.models import components, errors

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

except errors.ErrorResp as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
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
| 0 | `https://workflows-definition.sls.epilot.io` | None |

#### Example

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    server_idx=0,
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import sdk
from sdk.models import components

s = sdk.SDK(
    server_url="https://workflows-definition.sls.epilot.io",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
