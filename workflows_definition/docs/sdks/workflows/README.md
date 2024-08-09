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
import openapi
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.create_definition(request={
    "flow": [

    ],
    "name": "Lead Qualification",
    "assigned_to": [
        "952802",
        "80225",
    ],
    "closing_reasons": [
        {
            "id": "x739cew",
        },
    ],
    "creation_time": "2021-04-27T12:01:13.000Z",
    "description": "Lead Qualification description",
    "due_date": "2022-08-04T12:00:00.000Z",
    "last_update_time": "2021-04-27T12:01:13.000Z",
    "update_entity_attributes": [
        {
            "source": openapi.Source.CURRENT_SECTION,
            "target": {
                "entity_attribute": "my_status",
                "entity_schema": "opportunity",
            },
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.WorkflowDefinition](../../models/workflowdefinition.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.WorkflowDefinition](../../models/workflowdefinition.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## delete_definition

Delete Workflow Definition.

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.workflows.delete_definition(definition_id="CustomerRequest")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `definition_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Id of the definition to de deleted.                                 | CustomerRequest                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 401              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_definition

Get specific Definition by id from the Organization.

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_definition(definition_id="7hj28a")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `definition_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Short uuid (length 8) to identify the Workflow Definition.          | 7hj28a                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.WorkflowDefinition](../../models/workflowdefinition.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrorResp              | 400,401,500                   | application/json              |
| models.DefinitionNotFoundResp | 404                           | application/json              |
| models.SDKError               | 4xx-5xx                       | */*                           |

## get_definitions

Retrieve all Workflow Definitions from an Organization

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_definitions()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.WorkflowDefinition]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_max_allowed_limit

Get limits and number of created executions for an Organization.

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_max_allowed_limit()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.MaxAllowedLimit](../../models/maxallowedlimit.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 500              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## get_workflow_closing_reasons

Returns all closing reasons defined for the workflow.

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_workflow_closing_reasons(definition_id="fxcwfw")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `definition_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of a workflow definition                                         | fxcwfw                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.ClosingReasonsIds](../../models/closingreasonsids.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## set_workflow_closing_reasons

Sets which closing reasons are defined for this workflow, based on the entire closing reasons catalog.

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.workflows.set_workflow_closing_reasons(definition_id="7889", closing_reasons_ids={
    "reasons": [
        {
            "id": "x739cew",
        },
    ],
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `definition_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of a workflow definition                                         | 7889                                                                |
| `closing_reasons_ids`                                               | [models.ClosingReasonsIds](../../models/closingreasonsids.md)       | :heavy_check_mark:                                                  | set all closing reasons for a specific definition                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_definition

Update Workflow Definition.

### Example Usage

```python
import openapi
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.update_definition(definition_id="7hj28a", workflow_definition={
    "flow": [

    ],
    "name": "Lead Qualification",
    "assigned_to": [
        "952802",
        "80225",
    ],
    "closing_reasons": [
        {
            "id": "x739cew",
        },
    ],
    "creation_time": "2021-08-04T21:13:50.373Z",
    "due_date": "2022-08-04T12:00:00.000Z",
    "id": "25n2k52ja",
    "last_update_time": "2021-08-04T21:13:50.373Z",
    "update_entity_attributes": [
        {
            "source": openapi.Source.CURRENT_SECTION,
            "target": {
                "entity_attribute": "my_status",
                "entity_schema": "opportunity",
            },
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `definition_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Short uuid (length 8) to identify the Workflow Definition.          | 7hj28a                                                              |
| `workflow_definition`                                               | [models.WorkflowDefinition](../../models/workflowdefinition.md)     | :heavy_check_mark:                                                  | Workflow Definition payload                                         |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.WorkflowDefinition](../../models/workflowdefinition.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,401,500      | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
