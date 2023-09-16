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
        'at',
    ],
    closing_reasons=[
        shared.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-04-27T12:01:13.000Z',
    description='maiores',
    due_date='2021-04-27T12:00:00.000Z',
    dynamic_due_date=shared.DynamicDueDate(
        action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
        number_of_units=7991.59,
        step_id='quod',
        time_period=shared.DynamicDueDateTimePeriod.WEEKS,
    ),
    enable_ecp_workflow=False,
    flow=[
        shared.Step(
            assigned_to=[
                'porro',
            ],
            automation_config=shared.StepAutomationConfig(
                flow_id='dolorum',
            ),
            due_date='2021-04-27T12:00:00.000Z',
            dynamic_due_date=shared.DynamicDueDate(
                action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
                number_of_units=7206.33,
                step_id='officia',
                time_period=shared.DynamicDueDateTimePeriod.WEEKS,
            ),
            ecp=shared.ECPDetails(
                label='fugit',
            ),
            execution_type=shared.StepType.AUTOMATION,
            id='fc816742-cb73-4920-9929-396fea7596eb',
            name='Brenda Wisozk',
            order=6706.38,
            requirements=[
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='dolores',
                    type=shared.ItemType.STEP,
                ),
            ],
            type=shared.ItemType.STEP,
            user_ids=[
                1289.26,
            ],
        ),
    ],
    id='c5955907-aff1-4a3a-afa9-467739251aa5',
    last_update_time='2021-04-27T12:01:13.000Z',
    name='Angelica Dietrich',
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
        8209.94,
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
    definition_id='aut',
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
    definition_id='quasi',
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
    definition_id='error',
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
    definition_id='temporibus',
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
            'laborum',
        ],
        closing_reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
        creation_time='2021-04-27T12:01:13.000Z',
        description='quasi',
        due_date='2021-04-27T12:00:00.000Z',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
            number_of_units=9764.6,
            step_id='vero',
            time_period=shared.DynamicDueDateTimePeriod.WEEKS,
        ),
        enable_ecp_workflow=False,
        flow=[
            shared.Step(
                assigned_to=[
                    'voluptatibus',
                ],
                automation_config=shared.StepAutomationConfig(
                    flow_id='ipsa',
                ),
                due_date='2021-04-27T12:00:00.000Z',
                dynamic_due_date=shared.DynamicDueDate(
                    action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                    number_of_units=4511.59,
                    step_id='cum',
                    time_period=shared.DynamicDueDateTimePeriod.DAYS,
                ),
                ecp=shared.ECPDetails(
                    label='doloremque',
                ),
                execution_type=shared.StepType.MANUAL,
                id='4f15471b-5e6e-413b-99d4-88e1e91e450a',
                name='Benjamin O'Connell',
                order=2894.06,
                requirements=[
                    shared.StepRequirement(
                        condition=shared.StepRequirementCondition.CLOSED,
                        definition_id='modi',
                        type=shared.ItemType.STEP,
                    ),
                ],
                type=shared.ItemType.STEP,
                user_ids=[
                    5865.13,
                ],
            ),
        ],
        id='802d502a-94bb-44f6-bc96-9e9a3efa77df',
        last_update_time='2021-04-27T12:01:13.000Z',
        name='Keith Gulgowski',
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
            3965.06,
        ],
    ),
    definition_id='laborum',
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

