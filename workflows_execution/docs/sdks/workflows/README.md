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
import epilot_workflows_execution
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.create_execution(request={
    "workflow_id": "j3f23fh23uif98",
    "contexts": [
        {
            "id": "3fa3fa86-0907-4642-a57e-0fe30a19874d",
            "schema_": "contact",
            "title": "<value>",
        },
        {
            "id": "3a6d42fa-5070-4723-b90f-41ead4303e33",
            "schema_": "opportunity",
            "title": "<value>",
        },
    ],
    "trigger": epilot_workflows_execution.TriggerType.AUTOMATIC,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.WorkflowExecutionCreateReq](../../models/workflowexecutioncreatereq.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |


### Response

**[models.WorkflowExecution](../../models/workflowexecution.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## create_step

Create a new step in current workflow execution.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.create_step(execution_id="wd56125gah", create_step_req={
    "name": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd56125gah                                                          |
| `create_step_req`                                                   | [models.CreateStepReq](../../models/createstepreq.md)               | :heavy_check_mark:                                                  | Workflow Execution Step payload                                     |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Step](../../models/step.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## delete_execution

Delete workflow execution by id. Workflow contexts will NOT be deleted.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.workflows.delete_execution(execution_id="CustomerRequest")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution to de deleted.                                  | CustomerRequest                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## delete_step

Deletes a step from a workflow execution.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.workflows.delete_step(execution_id="wd56125gah", step_id="7hj28a")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd56125gah                                                          |
| `step_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Short uuid (length 6) to identify the Workflow Execution Step.      | 7hj28a                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_closing_reason_execution

Shows all Closing Reasons defined at the moment of starting the Workflow Execution.
The Closing Reasons shown in the execution are just snapshots
from the state of the Definition when the instance was created.


### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_closing_reason_execution(execution_id="wd561")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd561                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.ClosingReasonResp](../../models/closingreasonresp.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_execution

Get a full workflow execution, included steps information, by execution id.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_execution(execution_id="wd561")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd561                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.WorkflowExecution](../../models/workflowexecution.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_executions

Retrieve Workflow Executions. Optionally, you can filter them by context & schema. Please be aware, these executions are more light weight - steps are not loaded with all information.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_executions(context="2843c005-c5b0-4df2-94ee-1ca2ddd998ac", schema="contact")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `context`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Id of an Entity                                                     | 2843c005-c5b0-4df2-94ee-1ca2ddd998ac                                |
| `schema_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Schema of an Entity                                                 | contact                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[List[models.WorkflowExecutionSlim]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## search_executions

Search Workflow Executions by different filters.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.search_executions(request={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchExecutionsReq](../../models/searchexecutionsreq.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SearchExecutionsResp](../../models/searchexecutionsresp.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## ~~search_steps~~

Search workflow execution steps by different filters.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.search_steps(request={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchStepsReq](../../models/searchstepsreq.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SearchStepsResp](../../models/searchstepsresp.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## update_execution

Patches updates like assignees, status, closingReason for a single Workflow Execution.

### Example Usage

```python
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.workflows.update_execution(execution_id="wd561", workflow_execution_update_req={})

# Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `execution_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | Id of the execution                                                             | wd561                                                                           |
| `workflow_execution_update_req`                                                 | [models.WorkflowExecutionUpdateReq](../../models/workflowexecutionupdatereq.md) | :heavy_check_mark:                                                              | Patch Updates for Workflow Execution payload.                                   |                                                                                 |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## update_step

Patches various changes to a workflow execution step.

### Example Usage

```python
import epilot_workflows_execution
from epilot_workflows_execution import Epilot

s = Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.update_step(execution_id="wd56125gah", step_id="7hj28a", update_step_req={
    "assigned_to": [
        "10010730",
    ],
    "dynamic_due_date": {
        "number_of_units": 2,
        "time_period": epilot_workflows_execution.TimePeriod.WEEKS,
        "action_type_condition": epilot_workflows_execution.ActionTypeCondition.STEP_CLOSED,
        "step_id": "optional",
    },
    "name": "Static Duedate",
    "position": {
        "index": 0,
    },
    "status": epilot_workflows_execution.StepStatus.UNASSIGNED,
    "step_id": "string",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd56125gah                                                          |
| `step_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Short uuid (length 6) to identify the Workflow Execution Step.      | 7hj28a                                                              |
| `update_step_req`                                                   | [models.UpdateStepReq](../../models/updatestepreq.md)               | :heavy_check_mark:                                                  | Workflow Execution Step payload                                     |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Step](../../models/step.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
