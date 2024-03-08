# Workflows
(*workflows*)

## Overview

Interact with workflow executions - start / close / retrieve one or all / search / delete

### Available Operations

* [create_execution](#create_execution) - createExecution
* [create_step](#create_step) - createStep
* [delete_execution](#delete_execution) - deleteExecution
* [delete_step](#delete_step) - deleteStep
* [get_closing_reason_execution](#get_closing_reason_execution) - getClosingReasonExecution
* [get_execution](#get_execution) - getExecution
* [get_executions](#get_executions) - getExecutions
* [search_executions](#search_executions) - searchExecutions
* [~~search_steps~~](#search_steps) - searchSteps :warning: **Deprecated**
* [update_execution](#update_execution) - updateExecution
* [update_step](#update_step) - updateStep

## create_execution

Create a Workflow Execution. Start a new workflow execution, based on a workflow definition (template).

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.WorkflowExecutionCreateReq(
    workflow_id='j3f23fh23uif98',
    contexts=[
        shared.WorkflowContext(
            id='3fa3fa86-0907-4642-a57e-0fe30a19874d',
            schema='contact',
            title='<value>',
        ),
        shared.WorkflowContext(
            id='3a6d42fa-5070-4723-b90f-41ead4303e33',
            schema='opportunity',
            title='<value>',
        ),
    ],
    trigger=shared.TriggerType.AUTOMATIC,
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.WorkflowExecutionCreateReq](../../models/shared/workflowexecutioncreatereq.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateExecutionResponse](../../models/operations/createexecutionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## create_step

Create a new step in current workflow execution.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.create_step(create_step_req=shared.CreateStepReq(
    name='<value>',
), execution_id='<value>')

if res.step is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `create_step_req`                                            | [shared.CreateStepReq](../../models/shared/createstepreq.md) | :heavy_check_mark:                                           | Workflow Execution Step payload                              |
| `execution_id`                                               | *str*                                                        | :heavy_check_mark:                                           | Id of the execution                                          |


### Response

**[operations.CreateStepResponse](../../models/operations/createstepresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete_execution

Delete workflow execution by id. Workflow contexts will NOT be deleted.

### Example Usage

```python
import epilot

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.delete_execution(execution_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                          | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `execution_id`                     | *str*                              | :heavy_check_mark:                 | Id of the execution to de deleted. |


### Response

**[operations.DeleteExecutionResponse](../../models/operations/deleteexecutionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete_step

Deletes a step from a workflow execution.

### Example Usage

```python
import epilot

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.delete_step(execution_id='<value>', step_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `execution_id`                                                 | *str*                                                          | :heavy_check_mark:                                             | Id of the execution                                            |
| `step_id`                                                      | *str*                                                          | :heavy_check_mark:                                             | Short uuid (length 6) to identify the Workflow Execution Step. |


### Response

**[operations.DeleteStepResponse](../../models/operations/deletestepresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_closing_reason_execution

Shows all Closing Reasons defined at the moment of starting the Workflow Execution.
The Closing Reasons shown in the execution are just snapshots
from the state of the Definition when the instance was created.


### Example Usage

```python
import epilot

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_closing_reason_execution(execution_id='<value>')

if res.closing_reason_resp is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `execution_id`      | *str*               | :heavy_check_mark:  | Id of the execution |


### Response

**[operations.GetClosingReasonExecutionResponse](../../models/operations/getclosingreasonexecutionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_execution

Get a full workflow execution, included steps information, by execution id.

### Example Usage

```python
import epilot

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_execution(execution_id='<value>')

if res.workflow_execution is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `execution_id`      | *str*               | :heavy_check_mark:  | Id of the execution |


### Response

**[operations.GetExecutionResponse](../../models/operations/getexecutionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_executions

Retrieve Workflow Executions. Optionally, you can filter them by context & schema. Please be aware, these executions are more light weight - steps are not loaded with all information.

### Example Usage

```python
import epilot

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_executions(context='<value>', schema='<value>')

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `context`           | *Optional[str]*     | :heavy_minus_sign:  | Id of an Entity     |
| `schema`            | *Optional[str]*     | :heavy_minus_sign:  | Schema of an Entity |


### Response

**[operations.GetExecutionsResponse](../../models/operations/getexecutionsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## search_executions

Search Workflow Executions by different filters.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.SearchExecutionsReq()

res = s.workflows.search_executions(req)

if res.search_executions_resp is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SearchExecutionsReq](../../models/shared/searchexecutionsreq.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.SearchExecutionsResponse](../../models/operations/searchexecutionsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## ~~search_steps~~

Search workflow execution steps by different filters.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.SearchStepsReq()

res = s.workflows.search_steps(req)

if res.search_steps_resp is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.SearchStepsReq](../../models/shared/searchstepsreq.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.SearchStepsResponse](../../models/operations/searchstepsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update_execution

Patches updates like assignees, status, closingReason for a single Workflow Execution.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.update_execution(workflow_execution_update_req=shared.WorkflowExecutionUpdateReq(), execution_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `workflow_execution_update_req`                                                        | [shared.WorkflowExecutionUpdateReq](../../models/shared/workflowexecutionupdatereq.md) | :heavy_check_mark:                                                                     | Patch Updates for Workflow Execution payload.                                          |
| `execution_id`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | Id of the execution                                                                    |


### Response

**[operations.UpdateExecutionResponse](../../models/operations/updateexecutionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update_step

Patches various changes to a workflow execution step.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.update_step(update_step_req=shared.UpdateStepReq(), execution_id='<value>', step_id='<value>')

if res.step is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `update_step_req`                                              | [shared.UpdateStepReq](../../models/shared/updatestepreq.md)   | :heavy_check_mark:                                             | Workflow Execution Step payload                                |
| `execution_id`                                                 | *str*                                                          | :heavy_check_mark:                                             | Id of the execution                                            |
| `step_id`                                                      | *str*                                                          | :heavy_check_mark:                                             | Short uuid (length 6) to identify the Workflow Execution Step. |


### Response

**[operations.UpdateStepResponse](../../models/operations/updatestepresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
