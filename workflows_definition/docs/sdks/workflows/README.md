# Workflows
(*workflows*)

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
        'string',
    ],
    closing_reasons=[
        shared.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-04-27T12:01:13.000Z',
    due_date='2021-04-27T12:00:00.000Z',
    dynamic_due_date=shared.DynamicDueDate(
        action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
        number_of_units=1581.6,
        time_period=shared.DynamicDueDateTimePeriod.WEEKS,
    ),
    flow=[
        shared.Section(
            name='string',
            order=768.01,
            steps=[
                shared.Step(
                    assigned_to=[
                        'string',
                    ],
                    automation_config=shared.StepAutomationConfig(
                        flow_id='string',
                    ),
                    due_date='2021-04-27T12:00:00.000Z',
                    dynamic_due_date=shared.DynamicDueDate(
                        action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                        number_of_units=8711.4,
                        time_period=shared.DynamicDueDateTimePeriod.DAYS,
                    ),
                    ecp=shared.ECPDetails(
                        journey=shared.StepJourney(),
                    ),
                    installer=shared.ECPDetails(
                        journey=shared.StepJourney(),
                    ),
                    journey=shared.StepJourney(),
                    name='string',
                    order=8841.45,
                    requirements=[
                        shared.StepRequirement(
                            condition=shared.StepRequirementCondition.CLOSED,
                            definition_id='string',
                            type=shared.ItemType.SECTION,
                        ),
                    ],
                    type=shared.ItemType.STEP,
                    user_ids=[
                        463.65,
                    ],
                ),
            ],
            type=shared.ItemType.STEP,
        ),
    ],
    last_update_time='2021-04-27T12:01:13.000Z',
    name='string',
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
        5488.16,
    ],
)

res = s.workflows.create_definition(req)

if res.workflow_definition is not None:
    # handle response
    pass
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
    definition_id='string',
)

res = s.workflows.delete_definition(req)

if res.status_code == 200:
    # handle response
    pass
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
    definition_id='string',
)

res = s.workflows.get_definition(req)

if res.workflow_definition is not None:
    # handle response
    pass
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
    pass
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
    pass
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
    definition_id='string',
)

res = s.workflows.get_workflow_closing_reasons(req)

if res.closing_reasons_ids is not None:
    # handle response
    pass
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
    definition_id='string',
)

res = s.workflows.set_workflow_closing_reasons(req)

if res.status_code == 200:
    # handle response
    pass
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
            'string',
        ],
        closing_reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
        creation_time='2021-04-27T12:01:13.000Z',
        due_date='2021-04-27T12:00:00.000Z',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=8376.64,
            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
        ),
        flow=[
            shared.Section(
                name='string',
                order=452.1,
                steps=[
                    shared.Step(
                        assigned_to=[
                            'string',
                        ],
                        automation_config=shared.StepAutomationConfig(
                            flow_id='string',
                        ),
                        due_date='2021-04-27T12:00:00.000Z',
                        dynamic_due_date=shared.DynamicDueDate(
                            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                            number_of_units=9991.65,
                            time_period=shared.DynamicDueDateTimePeriod.DAYS,
                        ),
                        ecp=shared.ECPDetails(
                            journey=shared.StepJourney(),
                        ),
                        installer=shared.ECPDetails(
                            journey=shared.StepJourney(),
                        ),
                        journey=shared.StepJourney(),
                        name='string',
                        order=4890.23,
                        requirements=[
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='string',
                                type=shared.ItemType.SECTION,
                            ),
                        ],
                        type=shared.ItemType.SECTION,
                        user_ids=[
                            3753.56,
                        ],
                    ),
                ],
                type=shared.ItemType.STEP,
            ),
        ],
        last_update_time='2021-04-27T12:01:13.000Z',
        name='string',
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
            3438.79,
        ],
    ),
    definition_id='string',
)

res = s.workflows.update_definition(req)

if res.workflow_definition is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateDefinitionRequest](../../models/operations/updatedefinitionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateDefinitionResponse](../../models/operations/updatedefinitionresponse.md)**

