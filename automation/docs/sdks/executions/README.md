# Executions

## Overview

Automation executions

### Available Operations

* [cancel_execution](#cancel_execution) - cancelExecution
* [get_execution](#get_execution) - getExecution
* [get_executions](#get_executions) - getExecutions
* [retrigger_action](#retrigger_action) - retriggerAction
* [start_execution](#start_execution) - startExecution

## cancel_execution

Cancel automation execution

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.CancelExecutionRequest(
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.cancel_execution(req)

if res.automation_execution is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CancelExecutionRequest](../../models/operations/cancelexecutionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CancelExecutionResponse](../../models/operations/cancelexecutionresponse.md)**


## get_execution

Get automation execution

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetExecutionRequest(
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.get_execution(req)

if res.automation_execution is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetExecutionRequest](../../models/operations/getexecutionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetExecutionResponse](../../models/operations/getexecutionresponse.md)**


## get_executions

List automation executions

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetExecutionsRequest(
    entity_id='e3d3ebac-baab-4395-abf4-50b5bf1f8b74',
    from_=548814,
    size=592845,
)

res = s.executions.get_executions(req)

if res.get_executions_resp is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetExecutionsRequest](../../models/operations/getexecutionsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetExecutionsResponse](../../models/operations/getexecutionsresponse.md)**


## retrigger_action

Retry a specific automation execution action which failed / is stuck.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.RetriggerActionRequest(
    retry_req=shared.RetryReq(
        retry_strategy=shared.RetryStrategy.RETRY_AND_STOP,
    ),
    action_id='9ec3711b-db63-449c-b894-54d5bb622a8f',
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.retrigger_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RetriggerActionRequest](../../models/operations/retriggeractionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.RetriggerActionResponse](../../models/operations/retriggeractionresponse.md)**


## start_execution

Start new automation execution

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.StartExecutionRequestInput(
    entity_id='e3d3ebac-baab-4395-abf4-50b5bf1f8b74',
)

res = s.executions.start_execution(req)

if res.automation_execution is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.StartExecutionRequestInput](../../models/shared/startexecutionrequestinput.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.StartExecutionResponse](../../models/operations/startexecutionresponse.md)**

