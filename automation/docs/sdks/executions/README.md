# Executions
(*executions*)

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
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.executions.cancel_execution(execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4')

if res.automation_execution is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `execution_id`                       | *str*                                | :heavy_check_mark:                   | N/A                                  | 9baf184f-bc81-4128-bca3-d974c90a12c4 |


### Response

**[operations.CancelExecutionResponse](../../models/operations/cancelexecutionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_execution

Get automation execution

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.executions.get_execution(execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4')

if res.automation_execution is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `execution_id`                       | *str*                                | :heavy_check_mark:                   | N/A                                  | 9baf184f-bc81-4128-bca3-d974c90a12c4 |


### Response

**[operations.GetExecutionResponse](../../models/operations/getexecutionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_executions

List automation executions

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.executions.get_executions(entity_id='e3d3ebac-baab-4395-abf4-50b5bf1f8b74', from_=964899, size=653722)

if res.get_executions_resp is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `entity_id`                                 | *Optional[str]*                             | :heavy_minus_sign:                          | N/A                                         | e3d3ebac-baab-4395-abf4-50b5bf1f8b74        |
| `from_`                                     | *Optional[int]*                             | :heavy_minus_sign:                          | Pagination: starting for results            |                                             |
| `size`                                      | *Optional[int]*                             | :heavy_minus_sign:                          | Pagination: max number of results to return |                                             |


### Response

**[operations.GetExecutionsResponse](../../models/operations/getexecutionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## retrigger_action

Retry a specific automation execution action which failed / is stuck.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    epilot_auth="",
)


res = s.executions.retrigger_action(action_id='9ec3711b-db63-449c-b894-54d5bb622a8f', execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4', retry_req=components.RetryReq())

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `action_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Id of Action to retry.                                               | 9ec3711b-db63-449c-b894-54d5bb622a8f                                 |
| `execution_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | Execution Id                                                         | 9baf184f-bc81-4128-bca3-d974c90a12c4                                 |
| `retry_req`                                                          | [Optional[components.RetryReq]](../../models/components/retryreq.md) | :heavy_minus_sign:                                                   | Retry request details.                                               |                                                                      |


### Response

**[operations.RetriggerActionResponse](../../models/operations/retriggeractionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## start_execution

Start new automation execution

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="",
)

req = components.StartExecutionRequest(
    entity_id='e3d3ebac-baab-4395-abf4-50b5bf1f8b74',
)

res = s.executions.start_execution(req)

if res.automation_execution is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.StartExecutionRequest](../../models/components/startexecutionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.StartExecutionResponse](../../models/operations/startexecutionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
