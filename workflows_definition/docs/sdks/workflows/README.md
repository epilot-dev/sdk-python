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
        'Account',
    ],
    closing_reasons=[
        shared.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-04-27T12:01:13.000Z',
    description='Distributed analyzing synergy',
    due_date='2021-04-27T12:00:00.000Z',
    dynamic_due_date=shared.DynamicDueDate(
        action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
        number_of_units=2650.8,
        step_id='female Bahrain Nevada',
        time_period=shared.DynamicDueDateTimePeriod.WEEKS,
    ),
    enable_ecp_workflow=False,
    flow=[
        [],
    ],
    id='<ID>',
    last_update_time='2021-04-27T12:01:13.000Z',
    name='withdrawal Bahrain national',
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
        2732.95,
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
    definition_id='Expanded DNS Lead',
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
    definition_id='Pants Money Gorgeous',
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
    definition_id='Bedfordshire Account Account',
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
    definition_id='Tuna utilize',
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
            'Dollar',
        ],
        closing_reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
        creation_time='2021-04-27T12:01:13.000Z',
        description='Digitized 5th generation methodology',
        due_date='2021-04-27T12:00:00.000Z',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
            number_of_units=1623.12,
            step_id='Creative 5th',
            time_period=shared.DynamicDueDateTimePeriod.WEEKS,
        ),
        enable_ecp_workflow=False,
        flow=[
            [],
        ],
        id='<ID>',
        last_update_time='2021-04-27T12:01:13.000Z',
        name='Trigender responsive',
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
            8191.51,
        ],
    ),
    definition_id='farad',
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

