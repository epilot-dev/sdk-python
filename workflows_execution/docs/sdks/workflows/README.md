# Workflows

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
* [search_steps](#search_steps) - searchSteps
* [update_execution](#update_execution) - updateExecution
* [update_step](#update_step) - updateStep

## create_execution

Create a Workflow Execution. Start a new workflow execution, based on a workflow definition (template).

### Example Usage

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
        'quo',
    ],
    contexts=[
        shared.WorkflowContext(
            id='2ddf7cc7-8ca1-4ba9-a8fc-816742cb7392',
            schema='perferendis',
            title='Mrs.',
        ),
    ],
    trigger=shared.TriggerType.AUTOMATIC,
    workflow_id='sed',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.WorkflowExecutionCreateReq](../../models/shared/workflowexecutioncreatereq.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateExecutionResponse](../../models/operations/createexecutionresponse.md)**


## create_step

Create a new step in current workflow execution.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateStepRequest(
    create_step_req=shared.CreateStepReq(
        automation_config=shared.AutomationConfig(
            execution_id='iste',
            execution_status='dolor',
            flow_id='natus',
        ),
        execution_type=shared.StepType.MANUAL,
        insertion_index=9437.49,
        name='Wilbur Kirlin',
        section_id='iure',
        status=shared.StepStatus.IN_PROGRESS,
    ),
    execution_id='quidem',
)

res = s.workflows.create_step(req)

if res.step is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateStepRequest](../../models/operations/createsteprequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateStepResponse](../../models/operations/createstepresponse.md)**


## delete_execution

Delete workflow execution by id. Workflow contexts will NOT be deleted.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteExecutionRequest(
    execution_id='architecto',
)

res = s.workflows.delete_execution(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteExecutionRequest](../../models/operations/deleteexecutionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.DeleteExecutionResponse](../../models/operations/deleteexecutionresponse.md)**


## delete_step

Deletes a step from a workflow execution.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteStepRequest(
    execution_id='ipsa',
    step_id='reiciendis',
)

res = s.workflows.delete_step(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteStepRequest](../../models/operations/deletesteprequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteStepResponse](../../models/operations/deletestepresponse.md)**


## get_closing_reason_execution

Shows all Closing Reasons defined at the moment of starting the Workflow Execution.
The Closing Reasons shown in the execution are just snapshots
from the state of the Definition when the instance was created.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetClosingReasonExecutionRequest(
    execution_id='est',
)

res = s.workflows.get_closing_reason_execution(req)

if res.closing_reason_resp is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetClosingReasonExecutionRequest](../../models/operations/getclosingreasonexecutionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetClosingReasonExecutionResponse](../../models/operations/getclosingreasonexecutionresponse.md)**


## get_execution

Get a full workflow execution, included steps information, by execution id.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetExecutionRequest(
    execution_id='mollitia',
)

res = s.workflows.get_execution(req)

if res.workflow_execution is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetExecutionRequest](../../models/operations/getexecutionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetExecutionResponse](../../models/operations/getexecutionresponse.md)**


## get_executions

Retrieve Workflow Executions. Optionally, you can filter them by context & schema. Please be aware, these executions are more light weight - steps are not loaded with all information.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetExecutionsRequest(
    context='laborum',
    schema='dolores',
)

res = s.workflows.get_executions(req)

if res.workflow_execution_slims is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetExecutionsRequest](../../models/operations/getexecutionsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetExecutionsResponse](../../models/operations/getexecutionsresponse.md)**


## search_executions

Search Workflow Executions by different filters.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SearchExecutionsReq(
    assigned_to='dolorem',
    include_done_workflows=False,
    name='Rose Rolfson',
    pagination=shared.ExecutionPaginationDynamo(
        creation_time='nemo',
        org_id='minima',
    ),
    sorting=shared.SearchSorting.DUE_DATE_DESC,
    status=shared.WorkflowStatus.STARTED,
)

res = s.workflows.search_executions(req)

if res.search_executions_resp is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SearchExecutionsReq](../../models/shared/searchexecutionsreq.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.SearchExecutionsResponse](../../models/operations/searchexecutionsresponse.md)**


## search_steps

Search workflow execution steps by different filters.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SearchStepsReq(
    assigned_to=4386.01,
    execution_name='culpa',
    include_done_workflows=False,
    manually_created=False,
    pagination=shared.SearchPagination(
        from_=9883.74,
        size=9589.5,
    ),
    sorting=shared.SearchSorting.A_Z,
    status=shared.SearchStepsReqStatus.COMPLETE,
    step_name='dolorem',
)

res = s.workflows.search_steps(req)

if res.search_steps_resp is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.SearchStepsReq](../../models/shared/searchstepsreq.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.SearchStepsResponse](../../models/operations/searchstepsresponse.md)**


## update_execution

Patches updates like assignees, status, closingReason for a single Workflow Execution.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateExecutionRequest(
    workflow_execution_update_req=shared.WorkflowExecutionUpdateReq(
        assigned_to=[
            'culpa',
        ],
        closed_by='consequuntur',
        closing_reason_description='repellat',
        completed_time='mollitia',
        contexts=[
            shared.WorkflowContext(
                id='94677392-51aa-452c-bf5a-d019da1ffe78',
                schema='voluptatibus',
                title='Mr.',
            ),
        ],
        due_date='omnis',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=7392.64,
            step_id='perferendis',
            time_period=shared.DynamicDueDateTimePeriod.DAYS,
        ),
        selected_closing_reasons=[
            shared.ClosingReason(
                id='74f15471-b5e6-4e13-b99d-488e1e91e450',
                title='Miss',
            ),
        ],
        status=shared.WorkflowStatus.CLOSED,
    ),
    execution_id='explicabo',
)

res = s.workflows.update_execution(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateExecutionRequest](../../models/operations/updateexecutionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateExecutionResponse](../../models/operations/updateexecutionresponse.md)**


## update_step

Patches various changes to a workflow execution step.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateStepRequest(
    update_step_req=shared.UpdateStepReq(
        assigned_to=[
            'deserunt',
        ],
        assigned_to_in_progress='distinctio',
        automation_config=shared.AutomationConfig(
            execution_id='quibusdam',
            execution_status='labore',
            flow_id='modi',
        ),
        completed_time='qui',
        due_date='aliquid',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
            number_of_units=5528.22,
            step_id='perferendis',
            time_period=shared.DynamicDueDateTimePeriod.DAYS,
        ),
        entity_ref_id='assumenda',
        name='Linda Corkery',
        position=shared.StepPositionAt(
            index=2700.08,
            section_id='facilis',
        ),
        started_time='tempore',
        status=shared.StepStatus.ASSIGNED,
        user_ids=[
            9621.89,
        ],
    ),
    execution_id='eum',
    step_id='non',
)

res = s.workflows.update_step(req)

if res.step is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateStepRequest](../../models/operations/updatesteprequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateStepResponse](../../models/operations/updatestepresponse.md)**

