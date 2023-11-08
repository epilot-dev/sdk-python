# Flows
(*.flows*)

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
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="",
)

req = components.AutomationFlowInput(
    entity_schema='submission',
    flow_name='Handle contact form',
    runs=7,
    trigger_conditions=[
        components.TriggerCondition(
            comparison=components.Comparison.EQUALS,
            source='string',
        'string',
        ),
    ],
    triggers=[
        components.APISubmissionTrigger(
            configuration=components.APISubmissionTriggerConfiguration(),
            type=components.APISubmissionTriggerType.API_SUBMISSION,
        ),
    ],
)

res = s.flows.create_flow(req)

if res.automation_flow is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.AutomationFlowInput](../../models/shared/automationflowinput.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateFlowResponse](../../models/operations/createflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_flow

Update automation flow by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.flows.delete_flow(flow_id='7791b04a-16d2-44a2-9af9-2d59c25c512f')

if res.automation_flow is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `flow_id`                            | *str*                                | :heavy_check_mark:                   | Automation Workflow ID               | 7791b04a-16d2-44a2-9af9-2d59c25c512f |


### Response

**[operations.DeleteFlowResponse](../../models/operations/deleteflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_flow

List available automation flows

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.flows.get_flow(flow_id='7791b04a-16d2-44a2-9af9-2d59c25c512f')

if res.automation_flow is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `flow_id`                            | *str*                                | :heavy_check_mark:                   | Automation Workflow ID               | 7791b04a-16d2-44a2-9af9-2d59c25c512f |


### Response

**[operations.GetFlowResponse](../../models/operations/getflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_flow

Update automation flow by id

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.flows.put_flow(flow_id='7791b04a-16d2-44a2-9af9-2d59c25c512f', automation_flow=components.AutomationFlowInput(
    entity_schema='submission',
    flow_name='Handle contact form',
    runs=7,
    trigger_conditions=[
        components.TriggerCondition(
            comparison=components.Comparison.NOT_EMPTY,
            source='string',
        2067.93,
        ),
    ],
    triggers=[
        components.FrontendSubmitTrigger(
            configuration=components.FrontendSubmitTriggerConfiguration(
                source_id='99',
            ),
            type=components.FrontendSubmitTriggerType.FRONTEND_SUBMISSION,
        ),
    ],
))

if res.automation_flow is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `flow_id`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | Automation Workflow ID                                                                 | 7791b04a-16d2-44a2-9af9-2d59c25c512f                                                   |
| `automation_flow`                                                                      | [Optional[components.AutomationFlowInput]](../../models/shared/automationflowinput.md) | :heavy_minus_sign:                                                                     | Automation flow to create                                                              |                                                                                        |


### Response

**[operations.PutFlowResponse](../../models/operations/putflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## search_flows

Search available automation flows

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.flows.search_flows(from_=253836, schema='submission', size=186991, trigger_source_id='600945fe-212e-4b97-acf7-391d64648384')

if res.search_automations_resp is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `from_`                                     | *Optional[int]*                             | :heavy_minus_sign:                          | Pagination: starting for results            |                                             |
| `schema`                                    | *Optional[str]*                             | :heavy_minus_sign:                          | Entity Schema                               | submission                                  |
| `size`                                      | *Optional[int]*                             | :heavy_minus_sign:                          | Pagination: max number of results to return |                                             |
| `trigger_source_id`                         | *Optional[str]*                             | :heavy_minus_sign:                          | Trigger source identifier                   | 600945fe-212e-4b97-acf7-391d64648384        |


### Response

**[operations.SearchFlowsResponse](../../models/operations/searchflowsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
