# openapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=workflows_definition
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ChangeReasonStatusRequest(
    change_reason_status_req=shared.ChangeReasonStatusReq(
        status=shared.ClosingReasonsStatus.ACTIVE,
    ),
    reason_id='string',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
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
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://workflows-definition.sls.epilot.io` | None |

For example:


```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
    server_idx=0
)

req = operations.ChangeReasonStatusRequest(
    change_reason_status_req=shared.ChangeReasonStatusReq(
        status=shared.ClosingReasonsStatus.ACTIVE,
    ),
    reason_id='string',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
    server_url="https://workflows-definition.sls.epilot.io"
)

req = operations.ChangeReasonStatusRequest(
    change_reason_status_req=shared.ChangeReasonStatusReq(
        status=shared.ClosingReasonsStatus.ACTIVE,
    ),
    reason_id='string',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
