# Workflows

### Available Operations

* [create_definition](#create_definition) - createDefinition
* [delete_definition](#delete_definition) - deleteDefinition
* [get_definition](#get_definition) - getDefinition
* [get_definitions](#get_definitions) - getDefinitions
* [get_max_allowed_limit](#get_max_allowed_limit) - getMaxAllowedLimit
* [get_workflow_closing_reasons](#get_workflow_closing_reasons) - getWorkflowClosingReasons
* [set_workflow_closing_reasons](#set_workflow_closing_reasons) - setWorkflowClosingReasons
* [update_definition](#update_definition) - updateDefinition

## create_definition

Create a Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.WorkflowDefinition(
    assigned_to=[
        'molestiae',
    ],
    closing_reasons=[
        shared.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-04-27T12:01:13.000Z',
    description='quod',
    due_date='2021-04-27T12:00:00.000Z',
    dynamic_due_date=shared.DynamicDueDate(
        action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
        number_of_units=4614.79,
        step_id='totam',
        time_period=shared.DynamicDueDateTimePeriod.MONTHS,
    ),
    enable_ecp_workflow=False,
    flow=[
        shared.Step(
            assigned_to=[
                'dicta',
            ],
            automation_config=shared.StepAutomationConfig(
                flow_id='nam',
            ),
            due_date='2021-04-27T12:00:00.000Z',
            dynamic_due_date=shared.DynamicDueDate(
                action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                number_of_units=5820.2,
                step_id='fugit',
                time_period=shared.DynamicDueDateTimePeriod.WEEKS,
            ),
            ecp=shared.ECPDetails(
                label='hic',
            ),
            execution_type=shared.StepType.AUTOMATION,
            id='816742cb-7392-4059-a939-6fea7596eb10',
            name='Carlton O'Hara',
            order=2103.82,
            requirements=[
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='corporis',
                    type=shared.ItemType.STEP,
                ),
            ],
            type=shared.ItemType.SECTION,
            user_ids=[
                3154.28,
            ],
        ),
    ],
    id='955907af-f1a3-4a2f-a946-7739251aa52c',
    last_update_time='2021-04-27T12:01:13.000Z',
    name='Mandy Hills',
    update_entity_attributes=[
        shared.UpdateEntityAttributes(
            source=shared.UpdateEntityAttributesSource.WORKFLOW_STATUS,
            target=shared.UpdateEntityAttributesTarget(
                entity_attribute='my_status',
                entity_schema='opportunity',
            ),
        ),
    ],
    user_ids=[
        971.01,
    ],
)

res = s.workflows.create_definition(req)

if res.workflow_definition is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.WorkflowDefinition](../../models/shared/workflowdefinition.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateDefinitionResponse](../../models/operations/createdefinitionresponse.md)**


## delete_definition

Delete Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteDefinitionRequest(
    definition_id='error',
)

res = s.workflows.delete_definition(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteDefinitionRequest](../../models/operations/deletedefinitionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteDefinitionResponse](../../models/operations/deletedefinitionresponse.md)**


## get_definition

Get specific Definition by id from the Organization.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDefinitionRequest(
    definition_id='temporibus',
)

res = s.workflows.get_definition(req)

if res.workflow_definition is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetDefinitionRequest](../../models/operations/getdefinitionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetDefinitionResponse](../../models/operations/getdefinitionresponse.md)**


## get_definitions

Retrieve all Workflow Definitions from an Organization

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.workflows.get_definitions()

if res.workflow_definitions is not None:
    # handle response
```


### Response

**[operations.GetDefinitionsResponse](../../models/operations/getdefinitionsresponse.md)**


## get_max_allowed_limit

Get limits and number of created executions for an Organization.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.workflows.get_max_allowed_limit()

if res.max_allowed_limit is not None:
    # handle response
```


### Response

**[operations.GetMaxAllowedLimitResponse](../../models/operations/getmaxallowedlimitresponse.md)**


## get_workflow_closing_reasons

Returns all closing reasons defined for the workflow.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkflowClosingReasonsRequest(
    definition_id='laborum',
)

res = s.workflows.get_workflow_closing_reasons(req)

if res.closing_reasons_ids is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetWorkflowClosingReasonsRequest](../../models/operations/getworkflowclosingreasonsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetWorkflowClosingReasonsResponse](../../models/operations/getworkflowclosingreasonsresponse.md)**


## set_workflow_closing_reasons

Sets which closing reasons are defined for this workflow, based on the entire closing reasons catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SetWorkflowClosingReasonsRequest(
    closing_reasons_ids=shared.ClosingReasonsIds(
        reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
    ),
    definition_id='quasi',
)

res = s.workflows.set_workflow_closing_reasons(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.SetWorkflowClosingReasonsRequest](../../models/operations/setworkflowclosingreasonsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.SetWorkflowClosingReasonsResponse](../../models/operations/setworkflowclosingreasonsresponse.md)**


## update_definition

Update Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateDefinitionRequest(
    workflow_definition=shared.WorkflowDefinition(
        assigned_to=[
            'reiciendis',
        ],
        closing_reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
        creation_time='2021-04-27T12:01:13.000Z',
        description='voluptatibus',
        due_date='2021-04-27T12:00:00.000Z',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
            number_of_units=4686.51,
            step_id='praesentium',
            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
        ),
        enable_ecp_workflow=False,
        flow=[
            shared.Section(
                id='97b0074f-1547-41b5-a6e1-3b99d488e1e9',
                name='Patti Gottlieb MD',
                order=8423.42,
                steps=[
                    shared.Step(
                        assigned_to=[
                            'explicabo',
                        ],
                        automation_config=shared.StepAutomationConfig(
                            flow_id='deserunt',
                        ),
                        due_date='2021-04-27T12:00:00.000Z',
                        dynamic_due_date=shared.DynamicDueDate(
                            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                            number_of_units=8413.86,
                            step_id='labore',
                            time_period=shared.DynamicDueDateTimePeriod.DAYS,
                        ),
                        ecp=shared.ECPDetails(
                            label='qui',
                        ),
                        execution_type=shared.StepType.MANUAL,
                        id='9802d502-a94b-4b4f-a3c9-69e9a3efa77d',
                        name='Jean Buckridge',
                        order=8137.98,
                        requirements=[
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='ea',
                                type=shared.ItemType.STEP,
                            ),
                        ],
                        type=shared.ItemType.SECTION,
                        user_ids=[
                            8811.04,
                        ],
                    ),
                ],
                type=shared.ItemType.STEP,
            ),
        ],
        id='95efb9ba-88f3-4a66-9970-74ba4469b6e2',
        last_update_time='2021-04-27T12:01:13.000Z',
        name='Danielle Bosco',
        update_entity_attributes=[
            shared.UpdateEntityAttributes(
                source=shared.UpdateEntityAttributesSource.CURRENT_SECTION,
                target=shared.UpdateEntityAttributesTarget(
                    entity_attribute='my_status',
                    entity_schema='opportunity',
                ),
            ),
        ],
        user_ids=[
            5518.16,
        ],
    ),
    definition_id='sint',
)

res = s.workflows.update_definition(req)

if res.workflow_definition is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateDefinitionRequest](../../models/operations/updatedefinitionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateDefinitionResponse](../../models/operations/updatedefinitionresponse.md)**

