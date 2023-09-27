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
        'iste',
    ],
    contexts=[
        shared.WorkflowContext(
            id='396fea75-96eb-410f-aaa2-352c5955907a',
            schema='doloribus',
            title='Dr.',
        ),
    ],
    trigger=shared.TriggerType.MANUAL,
    workflow_id='mollitia',
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
            execution_id='dolorem',
            execution_status='culpa',
            flow_id='consequuntur',
        ),
        execution_type=shared.StepType.AUTOMATION,
        insertion_index=6531.08,
        name='Francis Jerde',
        section_id='velit',
        status=shared.StepStatus.SKIPPED,
    ),
    execution_id='quia',
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
    execution_id='quis',
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
    execution_id='vitae',
    step_id='laborum',
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
    execution_id='animi',
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
    execution_id='enim',
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
    context='odit',
    schema='quo',
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
    assigned_to='sequi',
    include_done_workflows=False,
    name='Vernon Ondricka Sr.',
    pagination=shared.ExecutionPaginationDynamo(
        creation_time='error',
        org_id='temporibus',
    ),
    sorting=shared.SearchSorting.TRIGGER_DATE_ASC,
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
    assigned_to=9719.45,
    execution_name='voluptatibus',
    include_done_workflows=False,
    manually_created=False,
    pagination=shared.SearchPagination(
        from_=8781.94,
        size=4686.51,
    ),
    sorting=shared.SearchSorting.DUE_DATE_DESC,
    status=shared.SearchStepsReqStatus.NEXT_OPEN_ITEM_IN_WORKFLOW,
    step_name='ipsa',
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
            'omnis',
        ],
        closed_by='voluptate',
        closing_reason_description='cum',
        completed_time='perferendis',
        contexts=[
            shared.WorkflowContext(
                id='074f1547-1b5e-46e1-bb99-d488e1e91e45',
                schema='consequatur',
                title='Miss',
            ),
        ],
        due_date='quibusdam',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=6471.74,
            step_id='distinctio',
            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
        ),
        selected_closing_reasons=[
            shared.ClosingReason(
                id='44269802-d502-4a94-bb4f-63c969e9a3ef',
                title='Miss',
            ),
        ],
        status=shared.WorkflowStatus.DONE,
    ),
    execution_id='in',
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
            'illum',
        ],
        assigned_to_in_progress='maiores',
        automation_config=shared.AutomationConfig(
            execution_id='rerum',
            execution_status='dicta',
            flow_id='magnam',
        ),
        completed_time='cumque',
        due_date='facere',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=3965.06,
            step_id='laborum',
            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
        ),
        entity_ref_id='non',
        name='Jon Tillman',
        position=shared.StepPositionAt(
            index=5884.65,
            section_id='nam',
        ),
        started_time='id',
        status=shared.StepStatus.COMPLETED,
        user_ids=[
            5332.06,
        ],
    ),
    execution_id='sapiente',
    step_id='amet',
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

