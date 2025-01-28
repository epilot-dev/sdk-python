# Flows
(*flows*)

## Overview

Automation flows

### Available Operations

* [create_flow](#create_flow) - createFlow
* [delete_flow](#delete_flow) - deleteFlow
* [get_flow](#get_flow) - getFlow
* [put_flow](#put_flow) - putFlow
* [search_flows](#search_flows) - searchFlows

## create_flow

Create new automation flow

### Example Usage

```python
import epilot_automation
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.flows.create_flow(request={
        "flow_name": "Handle contact form",
        "triggers": [

        ],
        "manifest": [
            "123e4567-e89b-12d3-a456-426614174000",
        ],
        "conditions": [
            {
                "statements": [
                    {
                        "operation": epilot_automation.Operation.EQUALS,
                        "source": {
                            "attribute": "email",
                            "attribute_type": epilot_automation.AttributeType.TEXT,
                            "id": "trigger-id",
                            "origin": epilot_automation.ConditionStatementOrigin.TRIGGER,
                            "origin_type": epilot_automation.OriginType.ENTITY,
                            "schema_": "contact",
                        },
                        "values": [
                            "hello@epilot.cloud",
                        ],
                    },
                ],
            },
        ],
        "entity_schema": "submission",
        "runs": 7,
        "trigger_conditions": [
            {
                "comparison": epilot_automation.Comparison.ANY_OF,
                "source": "billing_contact.email",
            },
        ],
        "version": 2,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AutomationFlowInput](../../models/automationflowinput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutomationFlow](../../models/automationflow.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.CreateFlowResponseBody | 403                           | application/json              |
| models.APIError               | 4XX, 5XX                      | \*/\*                         |

## delete_flow

Update automation flow by id

### Example Usage

```python
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    epilot.flows.delete_flow(flow_id="7791b04a-16d2-44a2-9af9-2d59c25c512f")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `flow_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Automation Workflow ID                                              | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.DeleteFlowResponseBody | 403, 404                      | application/json              |
| models.APIError               | 4XX, 5XX                      | \*/\*                         |

## get_flow

List available automation flows

### Example Usage

```python
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.flows.get_flow(flow_id="7791b04a-16d2-44a2-9af9-2d59c25c512f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `flow_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Automation Workflow ID                                              | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AutomationFlow](../../models/automationflow.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.GetFlowResponseBody | 403, 404                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## put_flow

Update automation flow by id

### Example Usage

```python
import epilot_automation
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.flows.put_flow(flow_id="7791b04a-16d2-44a2-9af9-2d59c25c512f", flow_name="Handle contact form", triggers=[

    ], manifest=[
        "123e4567-e89b-12d3-a456-426614174000",
    ], conditions=[
        {
            "statements": [
                {
                    "operation": epilot_automation.Operation.EQUALS,
                    "source": {
                        "attribute": "email",
                        "attribute_type": epilot_automation.AttributeType.TEXT,
                        "id": "trigger-id",
                        "origin": epilot_automation.ConditionStatementOrigin.TRIGGER,
                        "origin_type": epilot_automation.OriginType.ENTITY,
                        "schema_": "contact",
                    },
                    "values": [
                        "hello@epilot.cloud",
                    ],
                },
            ],
        },
        {
            "statements": [
                {
                    "operation": epilot_automation.Operation.EQUALS,
                    "source": {
                        "attribute": "email",
                        "attribute_type": epilot_automation.AttributeType.TEXT,
                        "id": "trigger-id",
                        "origin": epilot_automation.ConditionStatementOrigin.TRIGGER,
                        "origin_type": epilot_automation.OriginType.ENTITY,
                        "schema_": "contact",
                    },
                    "values": [
                        "hello@epilot.cloud",
                    ],
                },
            ],
        },
    ], entity_schema="submission", runs=7, trigger_conditions=[
        {
            "comparison": epilot_automation.Comparison.EQUALS,
            "source": "billing_contact.email",
        },
    ], version=2)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `flow_id`                                                                    | *str*                                                                        | :heavy_check_mark:                                                           | Automation Workflow ID                                                       | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                         |
| `flow_name`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | A descriptive name for the Automation                                        | Handle contact form                                                          |
| `triggers`                                                                   | List[[models.AnyTriggerInput](../../models/anytriggerinput.md)]              | :heavy_check_mark:                                                           | N/A                                                                          |                                                                              |
| `manifest`                                                                   | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Source blueprint/manifest ID used when automation is created via blueprints. |                                                                              |
| `conditions`                                                                 | List[[models.ActionCondition](../../models/actioncondition.md)]              | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |
| `disable_details`                                                            | [Optional[models.DisableDetails]](../../models/disabledetails.md)            | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |
| `enabled`                                                                    | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Whether the automation is enabled or not                                     |                                                                              |
| `entity_schema`                                                              | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The triggering entity schema                                                 | submission                                                                   |
| `runs`                                                                       | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | Number of automation executions that ran                                     | 7                                                                            |
| `schedules`                                                                  | List[[models.ActionSchedule](../../models/actionschedule.md)]                | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |
| `system_flow`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Determines if the flow is a system generated flow                            |                                                                              |
| `trigger_conditions`                                                         | List[[models.TriggerCondition](../../models/triggercondition.md)]            | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |
| `version`                                                                    | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | Version of the flow                                                          | 2                                                                            |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.AutomationFlow](../../models/automationflow.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.PutFlowResponseBody | 403                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## search_flows

Search available automation flows

### Example Usage

```python
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.flows.search_flows(from_=0, schema="submission", size=25, trigger_source_id="600945fe-212e-4b97-acf7-391d64648384")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Pagination: starting for results                                    |                                                                     |
| `schema_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Entity Schema                                                       | submission                                                          |
| `size`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Pagination: max number of results to return                         |                                                                     |
| `trigger_source_id`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Trigger source identifier                                           | 600945fe-212e-4b97-acf7-391d64648384                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SearchAutomationsResp](../../models/searchautomationsresp.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |