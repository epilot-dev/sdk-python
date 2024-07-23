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
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.create_definition(request=components.WorkflowDefinition(
    flow=[
        components.Section(
            name='Initial Information Gathering',
            order=1,
            steps=[
                components.Step(
                    name='Call client and confirm address and product',
                    order=1,
                    type=components.ItemType.STEP,
                    assigned_to=[
                        '123482',
                    ],
                    due_date='2021-04-27T12:00:00.000Z',
                ),
                components.Step(
                    name='Check product availability',
                    order=2,
                    type=components.ItemType.STEP,
                    assigned_to=[
                        '123482',
                    ],
                    due_date='2021-04-27T12:00:00.000Z',
                ),
                components.Step(
                    name='Send email confirming contact with the client',
                    order=3,
                    type=components.ItemType.STEP,
                    assigned_to=[
                        '123482',
                    ],
                    due_date='2021-04-27T12:00:00.000Z',
                ),
            ],
            type=components.ItemType.SECTION,
        ),
        components.Section(
            name='Print and send catalog',
            order=2,
            steps=[
                components.Step(
                    name='<value>',
                    order=4108.47,
                    type=components.ItemType.STEP,
                    due_date='2021-04-27T12:00:00.000Z',
                ),
            ],
            type=components.ItemType.STEP,
        ),
    ],
    name='Lead Qualification',
    assigned_to=[
        '952802',
        '80225',
    ],
    closing_reasons=[
        components.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-04-27T12:01:13.000Z',
    description='Lead Qualification description',
    due_date='2022-08-04T12:00:00.000Z',
    last_update_time='2021-04-27T12:01:13.000Z',
    update_entity_attributes=[
        components.UpdateEntityAttributes(
            source=components.Source.CURRENT_SECTION,
            target=components.Target(
                entity_attribute='my_status',
                entity_schema='opportunity',
            ),
        ),
    ],
))

if res.workflow_definition is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.WorkflowDefinition](../../models/components/workflowdefinition.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateDefinitionResponse](../../models/operations/createdefinitionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## delete_definition

Delete Workflow Definition.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.delete_definition(definition_id='CustomerRequest')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         | Example                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `definition_id`                     | *str*                               | :heavy_check_mark:                  | Id of the definition to de deleted. | CustomerRequest                     |


### Response

**[operations.DeleteDefinitionResponse](../../models/operations/deletedefinitionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get_definition

Get specific Definition by id from the Organization.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_definition(definition_id='7hj28a')

if res.workflow_definition is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `definition_id`                                            | *str*                                                      | :heavy_check_mark:                                         | Short uuid (length 8) to identify the Workflow Definition. | 7hj28a                                                     |


### Response

**[operations.GetDefinitionResponse](../../models/operations/getdefinitionresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ErrorResp              | 400,401,500                   | application/json              |
| errors.DefinitionNotFoundResp | 404                           | application/json              |
| errors.SDKError               | 4xx-5xx                       | */*                           |

## get_definitions

Retrieve all Workflow Definitions from an Organization

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_definitions()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetDefinitionsResponse](../../models/operations/getdefinitionsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get_max_allowed_limit

Get limits and number of created executions for an Organization.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_max_allowed_limit()

if res.max_allowed_limit is not None:
    # handle response
    pass

```


### Response

**[operations.GetMaxAllowedLimitResponse](../../models/operations/getmaxallowedlimitresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get_workflow_closing_reasons

Returns all closing reasons defined for the workflow.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_workflow_closing_reasons(definition_id='fxcwfw')

if res.closing_reasons_ids is not None:
    # handle response
    pass

```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 | Example                     |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `definition_id`             | *str*                       | :heavy_check_mark:          | ID of a workflow definition | fxcwfw                      |


### Response

**[operations.GetWorkflowClosingReasonsResponse](../../models/operations/getworkflowclosingreasonsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## set_workflow_closing_reasons

Sets which closing reasons are defined for this workflow, based on the entire closing reasons catalog.

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.set_workflow_closing_reasons(closing_reasons_ids=components.ClosingReasonsIds(
    reasons=[
        components.ClosingReasonID(
            id='x739cew',
        ),
    ],
), definition_id='7889')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `closing_reasons_ids`                                                        | [components.ClosingReasonsIds](../../models/components/closingreasonsids.md) | :heavy_check_mark:                                                           | set all closing reasons for a specific definition                            |                                                                              |
| `definition_id`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | ID of a workflow definition                                                  | 7889                                                                         |


### Response

**[operations.SetWorkflowClosingReasonsResponse](../../models/operations/setworkflowclosingreasonsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_definition

Update Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.update_definition(workflow_definition=components.WorkflowDefinition(
    flow=[
        components.Section(
            name='Initial Information Gathering',
            order=1,
            steps=[
                components.Step(
                    name='Call client and confirm address and product',
                    order=1,
                    type=components.ItemType.STEP,
                    assigned_to=[
                        '8988',
                    ],
                    due_date='2021-04-27T12:00:00.000Z',
                    id='2hja82a',
                ),
                components.Step(
                    name='Check product availability',
                    order=2,
                    type=components.ItemType.STEP,
                    assigned_to=[
                        '8988',
                    ],
                    due_date='2021-04-27T12:00:00.000Z',
                    id='ga92ha2',
                ),
                components.Step(
                    name='Send email confirming contact with the client',
                    order=3,
                    type=components.ItemType.STEP,
                    assigned_to=[
                        '8988',
                    ],
                    due_date='2021-04-27T12:00:00.000Z',
                    id='jga92ha',
                ),
            ],
            type=components.ItemType.SECTION,
            id='5892na2',
        ),
        components.Section(
            name='Print and send catalog',
            order=2,
            steps=[
                components.Step(
                    name='<value>',
                    order=4279.02,
                    type=components.ItemType.SECTION,
                    due_date='2021-04-27T12:00:00.000Z',
                ),
            ],
            type=components.ItemType.STEP,
            id='0a7g22a',
        ),
    ],
    name='Lead Qualification',
    assigned_to=[
        '952802',
        '80225',
    ],
    closing_reasons=[
        components.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-08-04T21:13:50.373Z',
    due_date='2022-08-04T12:00:00.000Z',
    id='25n2k52ja',
    last_update_time='2021-08-04T21:13:50.373Z',
    update_entity_attributes=[
        components.UpdateEntityAttributes(
            source=components.Source.CURRENT_STEP,
            target=components.Target(
                entity_attribute='my_status',
                entity_schema='opportunity',
            ),
        ),
    ],
), definition_id='7hj28a')

if res.workflow_definition is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `workflow_definition`                                                          | [components.WorkflowDefinition](../../models/components/workflowdefinition.md) | :heavy_check_mark:                                                             | Workflow Definition payload                                                    |                                                                                |
| `definition_id`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | Short uuid (length 8) to identify the Workflow Definition.                     | 7hj28a                                                                         |


### Response

**[operations.UpdateDefinitionResponse](../../models/operations/updatedefinitionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
