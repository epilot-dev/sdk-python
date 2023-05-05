# executions

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
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CancelExecutionRequest(
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.cancel_execution(req)

if res.automation_execution is not None:
    # handle response
```

## get_execution

Get automation execution

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetExecutionRequest(
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.get_execution(req)

if res.automation_execution is not None:
    # handle response
```

## get_executions

List automation executions

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
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

## retrigger_action

Retry a specific automation execution action which failed / is stuck.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.RetriggerActionRequest(
    retry_req=shared.RetryReq(
        retry_strategy=shared.RetryStrategyEnum.RETRY_AND_STOP,
    ),
    action_id='9ec3711b-db63-449c-b894-54d5bb622a8f',
    execution_id='9baf184f-bc81-4128-bca3-d974c90a12c4',
)

res = s.executions.retrigger_action(req)

if res.status_code == 200:
    # handle response
```

## start_execution

Start new automation execution

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.StartExecutionRequestInput(
    entity_id='e3d3ebac-baab-4395-abf4-50b5bf1f8b74',
)

res = s.executions.start_execution(req)

if res.automation_execution is not None:
    # handle response
```
