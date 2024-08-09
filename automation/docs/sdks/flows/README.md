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

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.flows.create_flow(request={
    "flow_name": "Handle contact form",
    "triggers": [

    ],
    "conditions": [
        {
            "statements": [
                {
                    "id": "1c8d3d9c-6d4c-4a83-aa22-aa0d630cbc2d",
                    "operation": epilot_automation.Operation.EQUALS,
                    "source": {
                        "attribute": "email",
                        "attribute_type": epilot_automation.AttributeType.TEXT,
                        "id": "trigger-id",
                        "origin": epilot_automation.Origin.TRIGGER,
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
            "comparison": epilot_automation.Comparison.EQUALS,
            "source": "billing_contact.email",
        },
    ],
    "version": 2,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AutomationFlowInput](../../models/automationflowinput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.AutomationFlow](../../models/automationflow.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_flow

Update automation flow by id

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.flows.delete_flow(flow_id="7791b04a-16d2-44a2-9af9-2d59c25c512f")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `flow_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Automation Workflow ID                                              | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.AutomationFlow](../../models/automationflow.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_flow

List available automation flows

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.flows.get_flow(flow_id="7791b04a-16d2-44a2-9af9-2d59c25c512f")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `flow_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Automation Workflow ID                                              | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.AutomationFlow](../../models/automationflow.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_flow

Update automation flow by id

### Example Usage

```python
import epilot_automation
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.flows.put_flow(flow_id="7791b04a-16d2-44a2-9af9-2d59c25c512f", automation_flow={
    "flow_name": "Handle contact form",
    "triggers": [

    ],
    "conditions": [
        {
            "statements": [
                {
                    "id": "1c8d3d9c-6d4c-4a83-aa22-aa0d630cbc2d",
                    "operation": epilot_automation.Operation.EQUALS,
                    "source": {
                        "attribute": "email",
                        "attribute_type": epilot_automation.AttributeType.TEXT,
                        "id": "trigger-id",
                        "origin": epilot_automation.Origin.TRIGGER,
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
            "comparison": epilot_automation.Comparison.NOT_EMPTY,
            "source": "billing_contact.email",
        },
    ],
    "version": 2,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `flow_id`                                                                   | *str*                                                                       | :heavy_check_mark:                                                          | Automation Workflow ID                                                      | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                        |
| `automation_flow`                                                           | [Optional[models.AutomationFlowInput]](../../models/automationflowinput.md) | :heavy_minus_sign:                                                          | Automation flow to create                                                   |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |


### Response

**[models.AutomationFlow](../../models/automationflow.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_flows

Search available automation flows

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.flows.search_flows(schema="submission", trigger_source_id="600945fe-212e-4b97-acf7-391d64648384")

if res is not None:
    # handle response
    pass

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
