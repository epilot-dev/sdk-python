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
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.WorkflowDefinition(
    flow=[
        shared.Section(
            name='string',
            order=1581.6,
            steps=[
                shared.Step(
                    name='string',
                    order=6545.76,
                    type=shared.ItemType.STEP,
                    due_date='2021-04-27T12:00:00.000Z',
                ),
            ],
            type=shared.ItemType.STEP,
        ),
    ],
    name='string',
    creation_time='2021-04-27T12:01:13.000Z',
    due_date='2021-04-27T12:00:00.000Z',
    last_update_time='2021-04-27T12:01:13.000Z',
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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete_definition

Delete Workflow Definition.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.delete_definition(definition_id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `definition_id`                     | *str*                               | :heavy_check_mark:                  | Id of the definition to de deleted. |


### Response

**[operations.DeleteDefinitionResponse](../../models/operations/deletedefinitionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 401              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get_definition

Get specific Definition by id from the Organization.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_definition(definition_id='string')

if res.workflow_definition is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `definition_id`                                            | *str*                                                      | :heavy_check_mark:                                         | Short uuid (length 8) to identify the Workflow Definition. |


### Response

**[operations.GetDefinitionResponse](../../models/operations/getdefinitionresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ErrorResp              | 400,401,500                   | application/json              |
| errors.DefinitionNotFoundResp | 404                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |

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
| errors.SDKError  | 4x-5xx           | */*              |

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
| errors.SDKError  | 4x-5xx           | */*              |

## get_workflow_closing_reasons

Returns all closing reasons defined for the workflow.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_workflow_closing_reasons(definition_id='string')

if res.closing_reasons_ids is not None:
    # handle response
    pass
```

### Parameters

| Parameter                   | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `definition_id`             | *str*                       | :heavy_check_mark:          | ID of a workflow definition |


### Response

**[operations.GetWorkflowClosingReasonsResponse](../../models/operations/getworkflowclosingreasonsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## set_workflow_closing_reasons

Sets which closing reasons are defined for this workflow, based on the entire closing reasons catalog.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.set_workflow_closing_reasons(closing_reasons_ids=shared.ClosingReasonsIds(
    reasons=[
        shared.ClosingReasonID(
            id='x739cew',
        ),
    ],
), definition_id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `closing_reasons_ids`                                                | [shared.ClosingReasonsIds](../../models/shared/closingreasonsids.md) | :heavy_check_mark:                                                   | set all closing reasons for a specific definition                    |
| `definition_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of a workflow definition                                          |


### Response

**[operations.SetWorkflowClosingReasonsResponse](../../models/operations/setworkflowclosingreasonsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_definition

Update Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.update_definition(workflow_definition=shared.WorkflowDefinition(
    flow=[
        shared.Section(
            name='string',
            order=8376.64,
            steps=[
                shared.Step(
                    name='string',
                    order=7832.36,
                    type=shared.ItemType.STEP,
                    due_date='2021-04-27T12:00:00.000Z',
                ),
            ],
            type=shared.ItemType.STEP,
        ),
    ],
    name='string',
    creation_time='2021-04-27T12:01:13.000Z',
    due_date='2021-04-27T12:00:00.000Z',
    last_update_time='2021-04-27T12:01:13.000Z',
), definition_id='string')

if res.workflow_definition is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `workflow_definition`                                                  | [shared.WorkflowDefinition](../../models/shared/workflowdefinition.md) | :heavy_check_mark:                                                     | Workflow Definition payload                                            |
| `definition_id`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | Short uuid (length 8) to identify the Workflow Definition.             |


### Response

**[operations.UpdateDefinitionResponse](../../models/operations/updatedefinitionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,401,500      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
