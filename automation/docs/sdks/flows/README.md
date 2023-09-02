# flows

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
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.AutomationFlowInput(
    enabled=False,
    entity_schema='submission',
    flow_name='Handle contact form',
    runs=7,
    trigger_conditions=[
        shared.TriggerCondition(
            comparison=shared.Comparison.NOT_EMPTY,
            source='nulla',
            value=[
                'vel',
                'error',
                'deserunt',
                'suscipit',
            ],
        ),
        shared.TriggerCondition(
            comparison=shared.Comparison.ANY_OF,
            source='magnam',
            value=[
                9636.63,
            ],
        ),
        shared.TriggerCondition(
            comparison=shared.Comparison.ANY_OF,
            source='suscipit',
            value=7917.25,
        ),
        shared.TriggerCondition(
            comparison=shared.Comparison.IS_EMPTY,
            source='voluptatum',
            value=5680.45,
        ),
    ],
    triggers=[
        shared.ReceivedEmailTrigger(
            configuration=shared.ReceivedEmailTriggerConfiguration(
                message_type=shared.ReceivedEmailTriggerConfigurationMessageType.RECEIVED,
            ),
            type=shared.ReceivedEmailTriggerType.RECEIVED_EMAIL,
        ),
        shared.EntityManualTrigger(
            configuration=shared.EntityManualTriggerConfiguration(
                schema='submission',
            ),
            type=shared.EntityManualTriggerType.ENTITY_MANUAL,
        ),
    ],
)

res = s.flows.create_flow(req)

if res.automation_flow is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.AutomationFlowInput](../../models/shared/automationflowinput.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateFlowResponse](../../models/operations/createflowresponse.md)**


## delete_flow

Update automation flow by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteFlowRequest(
    flow_id='7791b04a-16d2-44a2-9af9-2d59c25c512f',
)

res = s.flows.delete_flow(req)

if res.automation_flow is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteFlowRequest](../../models/operations/deleteflowrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteFlowResponse](../../models/operations/deleteflowresponse.md)**


## get_flow

List available automation flows

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetFlowRequest(
    flow_id='7791b04a-16d2-44a2-9af9-2d59c25c512f',
)

res = s.flows.get_flow(req)

if res.automation_flow is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetFlowRequest](../../models/operations/getflowrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetFlowResponse](../../models/operations/getflowresponse.md)**


## put_flow

Update automation flow by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.PutFlowRequest(
    automation_flow_input=shared.AutomationFlowInput(
        enabled=False,
        entity_schema='submission',
        flow_name='Handle contact form',
        runs=7,
        trigger_conditions=[
            shared.TriggerCondition(
                comparison=shared.Comparison.ANY_OF,
                source='veritatis',
                value=[
                    'ipsam',
                ],
            ),
        ],
        triggers=[
            shared.ReceivedEmailTrigger(
                configuration=shared.ReceivedEmailTriggerConfiguration(
                    message_type=shared.ReceivedEmailTriggerConfigurationMessageType.RECEIVED,
                ),
                type=shared.ReceivedEmailTriggerType.RECEIVED_EMAIL,
            ),
            shared.EntityManualTrigger(
                configuration=shared.EntityManualTriggerConfiguration(
                    schema='submission',
                ),
                type=shared.EntityManualTriggerType.ENTITY_MANUAL,
            ),
            shared.FrontendSubmitTrigger(
                configuration=shared.FrontendSubmitTriggerConfiguration(
                    source_id='99',
                ),
                type=shared.FrontendSubmitTriggerType.FRONTEND_SUBMISSION,
            ),
            shared.ReceivedEmailTrigger(
                configuration=shared.ReceivedEmailTriggerConfiguration(
                    message_type=shared.ReceivedEmailTriggerConfigurationMessageType.RECEIVED,
                ),
                type=shared.ReceivedEmailTriggerType.RECEIVED_EMAIL,
            ),
        ],
    ),
    flow_id='7791b04a-16d2-44a2-9af9-2d59c25c512f',
)

res = s.flows.put_flow(req)

if res.automation_flow is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.PutFlowRequest](../../models/operations/putflowrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PutFlowResponse](../../models/operations/putflowresponse.md)**


## search_flows

Search available automation flows

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.SearchFlowsRequest(
    from_=870088,
    schema='submission',
    size=978619,
    trigger_source_id='600945fe-212e-4b97-acf7-391d64648384',
)

res = s.flows.search_flows(req)

if res.search_automations_resp is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.SearchFlowsRequest](../../models/operations/searchflowsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.SearchFlowsResponse](../../models/operations/searchflowsresponse.md)**
