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

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.create_execution(workflow_id="j3f23fh23uif98", contexts=[
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
    ], trigger=epilot_workflows_execution.TriggerType.AUTOMATIC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `workflow_id`                                                                                                           | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `assigned_to`                                                                                                           | List[*str*]                                                                                                             | :heavy_minus_sign:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| `contexts`                                                                                                              | List[[models.WorkflowContext](../../models/workflowcontext.md)]                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `trigger`                                                                                                               | [Optional[models.TriggerType]](../../models/triggertype.md)                                                             | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.WorkflowExecution](../../models/workflowexecution.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## create_step

Create a new step in current workflow execution.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.create_step(execution_id="wd56125gah", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `execution_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | Id of the execution                                                   | wd56125gah                                                            |
| `name`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |                                                                       |
| `automation_config`                                                   | [Optional[models.AutomationConfig]](../../models/automationconfig.md) | :heavy_minus_sign:                                                    | Configuration for automation execution to run                         |                                                                       |
| `execution_type`                                                      | [Optional[models.StepType]](../../models/steptype.md)                 | :heavy_minus_sign:                                                    | N/A                                                                   |                                                                       |
| `insertion_index`                                                     | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | N/A                                                                   |                                                                       |
| `section_id`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |                                                                       |
| `status`                                                              | [Optional[models.StepStatus]](../../models/stepstatus.md)             | :heavy_minus_sign:                                                    | N/A                                                                   |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.Step](../../models/step.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## delete_execution

Delete workflow execution by id. Workflow contexts will NOT be deleted.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.workflows.delete_execution(execution_id="CustomerRequest")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution to de deleted.                                  | CustomerRequest                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## delete_step

Deletes a step from a workflow execution.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.workflows.delete_step(execution_id="wd56125gah", step_id="7hj28a")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd56125gah                                                          |
| `step_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Short uuid (length 6) to identify the Workflow Execution Step.      | 7hj28a                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_closing_reason_execution

Shows all Closing Reasons defined at the moment of starting the Workflow Execution.
The Closing Reasons shown in the execution are just snapshots
from the state of the Definition when the instance was created.


### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.get_closing_reason_execution(execution_id="wd561")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd561                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClosingReasonResp](../../models/closingreasonresp.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_execution

Get a full workflow execution, included steps information, by execution id.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.get_execution(execution_id="wd561")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Id of the execution                                                 | wd561                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WorkflowExecution](../../models/workflowexecution.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_executions

Retrieve Workflow Executions. Optionally, you can filter them by context & schema. Please be aware, these executions are more light weight - steps are not loaded with all information.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.get_executions(context="2843c005-c5b0-4df2-94ee-1ca2ddd998ac", schema="contact")

    # Handle response
    print(res)

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

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## search_executions

Search Workflow Executions by different filters.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.search_executions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchExecutionsReq](../../models/searchexecutionsreq.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchExecutionsResp](../../models/searchexecutionsresp.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## ~~search_steps~~

Search workflow execution steps by different filters.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.search_steps()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchStepsReq](../../models/searchstepsreq.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchStepsResp](../../models/searchstepsresp.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## update_execution

Patches updates like assignees, status, closingReason for a single Workflow Execution.

### Example Usage

```python
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.workflows.update_execution(execution_id="wd561")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `execution_id`                                                                            | *str*                                                                                     | :heavy_check_mark:                                                                        | Id of the execution                                                                       | wd561                                                                                     |
| `assigned_to`                                                                             | List[*str*]                                                                               | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `closed_by`                                                                               | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | id of the user / partner user who is closing the workflow. For partner pass orgId_userId. |                                                                                           |
| `closing_reason_description`                                                              | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `completed_time`                                                                          | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Completed time of the workflow execution                                                  |                                                                                           |
| `contexts`                                                                                | List[[models.WorkflowContext](../../models/workflowcontext.md)]                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `due_date`                                                                                | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `dynamic_due_date`                                                                        | [Optional[models.DynamicDueDate]](../../models/dynamicduedate.md)                         | :heavy_minus_sign:                                                                        | set a Duedate for a step then a specific                                                  |                                                                                           |
| `selected_closing_reasons`                                                                | List[[models.ClosingReason](../../models/closingreason.md)]                               | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `status`                                                                                  | [Optional[models.WorkflowStatus]](../../models/workflowstatus.md)                         | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## update_step

Patches various changes to a workflow execution step.

### Example Usage

```python
import epilot_workflows_execution
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.update_step(execution_id="wd56125gah", step_id_param="7hj28a", assigned_to=[
        "10010730",
    ], dynamic_due_date={
        "number_of_units": 2,
        "time_period": epilot_workflows_execution.TimePeriod.WEEKS,
        "action_type_condition": epilot_workflows_execution.ActionTypeCondition.STEP_CLOSED,
        "step_id": "optional",
    }, name="Static Duedate", position={
        "index": 0,
    }, status=epilot_workflows_execution.StepStatus.UNASSIGNED, step_id="string")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              | Example                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `execution_id`                                                                                                                                                           | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | Id of the execution                                                                                                                                                      | wd56125gah                                                                                                                                                               |
| `step_id_param`                                                                                                                                                          | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | Short uuid (length 6) to identify the Workflow Execution Step.                                                                                                           | 7hj28a                                                                                                                                                                   |
| `assigned_to`                                                                                                                                                            | List[*str*]                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `assigned_to_in_progress`                                                                                                                                                | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The user which moved the step/task to the IN_PROGRESS state. The user should also be present in the assignedTo property of the step/task                                 |                                                                                                                                                                          |
| `automation_config`                                                                                                                                                      | [Optional[models.AutomationConfig]](../../models/automationconfig.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                       | Configuration for automation execution to run                                                                                                                            |                                                                                                                                                                          |
| `completed_time`                                                                                                                                                         | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `due_date`                                                                                                                                                               | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `dynamic_due_date`                                                                                                                                                       | [Optional[models.DynamicDueDate]](../../models/dynamicduedate.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                       | set a Duedate for a step then a specific                                                                                                                                 |                                                                                                                                                                          |
| `entity_ref_id`                                                                                                                                                          | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>This field is deprecated. Please use stepId |                                                                                                                                                                          |
| `name`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `position`                                                                                                                                                               | [Optional[models.StepPositionAt]](../../models/steppositionat.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `started_time`                                                                                                                                                           | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `status`                                                                                                                                                                 | [Optional[models.StepStatus]](../../models/stepstatus.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `step_id`                                                                                                                                                                | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |                                                                                                                                                                          |
| `user_ids`                                                                                                                                                               | List[*float*]                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                       | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>This field is deprecated. Please use assignedTo |                                                                                                                                                                          |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |                                                                                                                                                                          |

### Response

**[models.Step](../../models/step.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400, 401, 500    | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |