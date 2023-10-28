# epilot-workflows-execution

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=workflows_execution
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.WorkflowExecutionCreateReq(
    assigned_to=[
        'string',
    ],
    contexts=[
        shared.WorkflowContext(
            id='<ID>',
            schema='string',
            title='string',
        ),
    ],
    workflow_id='string',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [workflows](docs/sdks/workflows/README.md)

* [create_execution](docs/sdks/workflows/README.md#create_execution) - createExecution
* [create_step](docs/sdks/workflows/README.md#create_step) - createStep
* [delete_execution](docs/sdks/workflows/README.md#delete_execution) - deleteExecution
* [delete_step](docs/sdks/workflows/README.md#delete_step) - deleteStep
* [get_closing_reason_execution](docs/sdks/workflows/README.md#get_closing_reason_execution) - getClosingReasonExecution
* [get_execution](docs/sdks/workflows/README.md#get_execution) - getExecution
* [get_executions](docs/sdks/workflows/README.md#get_executions) - getExecutions
* [search_executions](docs/sdks/workflows/README.md#search_executions) - searchExecutions
* [~~search_steps~~](docs/sdks/workflows/README.md#search_steps) - searchSteps :warning: **Deprecated**
* [update_execution](docs/sdks/workflows/README.md#update_execution) - updateExecution
* [update_step](docs/sdks/workflows/README.md#update_step) - updateStep
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
| 0 | `https://workflows-execution.sls.epilot.io` | None |

For example:


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
    server_idx=0
)

req = shared.WorkflowExecutionCreateReq(
    assigned_to=[
        'string',
    ],
    contexts=[
        shared.WorkflowContext(
            id='<ID>',
            schema='string',
            title='string',
        ),
    ],
    workflow_id='string',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
    server_url="https://workflows-execution.sls.epilot.io"
)

req = shared.WorkflowExecutionCreateReq(
    assigned_to=[
        'string',
    ],
    contexts=[
        shared.WorkflowContext(
            id='<ID>',
            schema='string',
            title='string',
        ),
    ],
    workflow_id='string',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
