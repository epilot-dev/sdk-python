# workflows

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
        'mollitia',
    ],
    contexts=[
        shared.WorkflowContext(
            id='a2fa9467-7392-451a-a52c-3f5ad019da1f',
            schema='voluptatibus',
            title='Dr.',
        ),
    ],
    trigger=shared.TriggerType.MANUAL,
    workflow_id='praesentium',
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
            execution_id='voluptatibus',
            execution_status='ipsa',
            flow_id='omnis',
        ),
        execution_type=shared.StepType.MANUAL,
        insertion_index=7392.64,
        name='Sharon Kiehn',
        section_id='dicta',
        status=shared.StepStatus.ASSIGNED,
    ),
    execution_id='dolore',
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
    execution_id='iusto',
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
    execution_id='dicta',
    step_id='harum',
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
    execution_id='enim',
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
    execution_id='accusamus',
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
    context='commodi',
    schema='repudiandae',
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
    assigned_to='quae',
    include_done_workflows=False,
    name='Alison Mann',
    pagination=shared.ExecutionPaginationDynamo(
        creation_time='modi',
        org_id='praesentium',
    ),
    sorting=shared.SearchSorting.DUE_DATE_DESC,
    status=shared.WorkflowStatus.CLOSED,
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
    assigned_to=939.4,
    execution_name='repudiandae',
    include_done_workflows=False,
    manually_created=False,
    pagination=shared.SearchPagination(
        from_=5759.47,
        size=831.12,
    ),
    sorting=shared.SearchSorting.TRIGGER_DATE_DESC,
    status=shared.SearchStepsReqStatus.OPEN,
    step_name='enim',
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
            'est',
        ],
        closed_by='quibusdam',
        closing_reason_description='explicabo',
        completed_time='deserunt',
        contexts=[
            shared.WorkflowContext(
                id='d4426980-2d50-42a9-8bb4-f63c969e9a3e',
                schema='a',
                title='Miss',
            ),
            shared.WorkflowContext(
                id='77dfb14c-d66a-4e39-9efb-9ba88f3a6699',
                schema='molestiae',
                title='Mr.',
            ),
            shared.WorkflowContext(
                id='74ba4469-b6e2-4141-9598-90afa563e251',
                schema='iure',
                title='Dr.',
            ),
        ],
        due_date='debitis',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=8061.94,
            step_id='deleniti',
            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
        ),
        selected_closing_reasons=[
            shared.ClosingReason(
                id='11e5b7fd-2ed0-4289-a1cd-dc692601fb57',
                title='Ms.',
            ),
            shared.ClosingReason(
                id='b0d5f0d3-0c5f-4bb2-9870-53202c73d5fe',
                title='Miss',
            ),
        ],
        status=shared.WorkflowStatus.CLOSED,
    ),
    execution_id='perspiciatis',
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
            'porro',
        ],
        assigned_to_in_progress='consequuntur',
        automation_config=shared.AutomationConfig(
            execution_id='blanditiis',
            execution_status='error',
            flow_id='eaque',
        ),
        completed_time='occaecati',
        due_date='rerum',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=9923.97,
            step_id='earum',
            time_period=shared.DynamicDueDateTimePeriod.DAYS,
        ),
        entity_ref_id='iste',
        name='Casey Stracke',
        position=shared.StepPositionAt(
            index=7301.22,
            section_id='delectus',
        ),
        started_time='quaerat',
        status=shared.StepStatus.COMPLETED,
        user_ids=[
            2123.9,
            2098.43,
        ],
    ),
    execution_id='dolor',
    step_id='qui',
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

