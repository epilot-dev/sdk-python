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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
    trigger=shared.TriggerTypeEnum.MANUAL,
    workflow_id='praesentium',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
```

## create_step

Create a new step in current workflow execution.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateStepRequest(
    create_step_req=shared.CreateStepReq(
        automation_config=shared.AutomationConfig(
            execution_id='voluptatibus',
            execution_status='ipsa',
            flow_id='omnis',
        ),
        execution_type=shared.StepTypeEnum.MANUAL,
        insertion_index=7392.64,
        name='Sharon Kiehn',
        section_id='dicta',
        status=shared.StepStatusEnum.ASSIGNED,
    ),
    execution_id='dolore',
)

res = s.workflows.create_step(req)

if res.step is not None:
    # handle response
```

## delete_execution

Delete workflow execution by id. Workflow contexts will NOT be deleted.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteExecutionRequest(
    execution_id='iusto',
)

res = s.workflows.delete_execution(req)

if res.status_code == 200:
    # handle response
```

## delete_step

Deletes a step from a workflow execution.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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

## get_closing_reason_execution

Shows all Closing Reasons defined at the moment of starting the Workflow Execution.
The Closing Reasons shown in the execution are just snapshots
from the state of the Definition when the instance was created.


### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetClosingReasonExecutionRequest(
    execution_id='enim',
)

res = s.workflows.get_closing_reason_execution(req)

if res.closing_reason_resp is not None:
    # handle response
```

## get_execution

Get a full workflow execution, included steps information, by execution id.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetExecutionRequest(
    execution_id='accusamus',
)

res = s.workflows.get_execution(req)

if res.workflow_execution is not None:
    # handle response
```

## get_executions

Retrieve Workflow Executions. Optionally, you can filter them by context & schema. Please be aware, these executions are more light weight - steps are not loaded with all information.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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

## search_executions

Search Workflow Executions by different filters.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
    sorting=shared.SearchSortingEnum.DUE_DATE_DESC,
    status=shared.WorkflowStatusEnum.CLOSED,
)

res = s.workflows.search_executions(req)

if res.search_executions_resp is not None:
    # handle response
```

## search_steps

Search workflow execution steps by different filters.

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
    sorting=shared.SearchSortingEnum.TRIGGER_DATE_DESC,
    status=shared.SearchStepsReqStatusEnum.OPEN,
    step_name='enim',
)

res = s.workflows.search_steps(req)

if res.search_steps_resp is not None:
    # handle response
```

## update_execution

Patches updates like assignees, status, closingReason for a single Workflow Execution.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateExecutionRequest(
    workflow_execution_update_req=shared.WorkflowExecutionUpdateReq(
        assigned_to=[
            'est',
        ],
        closed_by='quibusdam',
        closing_reason_description='explicabo',
        contexts=[
            shared.WorkflowContext(
                id='bd442698-02d5-402a-94bb-4f63c969e9a3',
                schema='debitis',
                title='Dr.',
            ),
            shared.WorkflowContext(
                id='a77dfb14-cd66-4ae3-95ef-b9ba88f3a669',
                schema='omnis',
                title='Ms.',
            ),
            shared.WorkflowContext(
                id='074ba446-9b6e-4214-9959-890afa563e25',
                schema='quasi',
                title='Ms.',
            ),
        ],
        due_date='doloribus',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeConditionEnum.STEP_CLOSED,
            number_of_units=2603.41,
            step_id='maxime',
            time_period=shared.DynamicDueDateTimePeriodEnum.WEEKS,
        ),
        selected_closing_reasons=[
            shared.ClosingReason(
                id='711e5b7f-d2ed-4028-921c-ddc692601fb5',
                title='Ms.',
            ),
            shared.ClosingReason(
                id='6b0d5f0d-30c5-4fbb-a587-053202c73d5f',
                title='Dr.',
            ),
            shared.ClosingReason(
                id='9b90c289-09b3-4fe4-9a8d-9cbf48633323',
                title='Dr.',
            ),
        ],
        status=shared.WorkflowStatusEnum.DONE,
    ),
    execution_id='cum',
)

res = s.workflows.update_execution(req)

if res.status_code == 200:
    # handle response
```

## update_step

Patches various changes to a workflow execution step.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateStepRequest(
    update_step_req=shared.UpdateStepReq(
        assigned_to=[
            'dignissimos',
            'reiciendis',
        ],
        assigned_to_in_progress='amet',
        automation_config=shared.AutomationConfig(
            execution_id='dolorum',
            execution_status='numquam',
            flow_id='veritatis',
        ),
        due_date='ipsa',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeConditionEnum.WORKFLOW_STARTED,
            number_of_units=4344.17,
            step_id='odio',
            time_period=shared.DynamicDueDateTimePeriodEnum.DAYS,
        ),
        entity_ref_id='accusamus',
        name='Jan Hodkiewicz',
        position=shared.StepPositionAt(
            index=5424.99,
            section_id='sit',
        ),
        status=shared.StepStatusEnum.IN_PROGRESS,
        user_ids=[
            7438.35,
        ],
    ),
    execution_id='dolorum',
    step_id='iusto',
)

res = s.workflows.update_step(req)

if res.step is not None:
    # handle response
```
