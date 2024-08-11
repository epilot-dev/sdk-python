# Executions
(*executions*)

## Overview

Automation executions

### Available Operations

* [cancel_execution](#cancel_execution) - cancelExecution
* [get_execution](#get_execution) - getExecution
* [get_executions](#get_executions) - getExecutions
* [resume_execution_with_token](#resume_execution_with_token) - resumeExecutionWithToken
* [retrigger_action](#retrigger_action) - retriggerAction
* [start_execution](#start_execution) - startExecution

## cancel_execution

Cancel automation execution

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.executions.cancel_execution(execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 9baf184f-bc81-4128-bca3-d974c90a12c4                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.AutomationExecution](../../models/automationexecution.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_execution

Get automation execution

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.executions.get_execution(execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 9baf184f-bc81-4128-bca3-d974c90a12c4                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.AutomationExecution](../../models/automationexecution.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_executions

List automation executions

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.executions.get_executions(entity_id="e3d3ebac-baab-4395-abf4-50b5bf1f8b74")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entity_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | e3d3ebac-baab-4395-abf4-50b5bf1f8b74                                |
| `from_`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Pagination: starting for results                                    |                                                                     |
| `size`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Pagination: max number of results to return                         |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetExecutionsResp](../../models/getexecutionsresp.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## resume_execution_with_token

Resume a paused automation execution using a unique resume token.

This public API is normally called when a user lands on a confirmation page via email link.

Example link: https://automation.epilot.io/confirm-email?token=eyJraWQiOiJrZXkifQ...


### Example Usage

```python
from epilot_automation import Epilot

s = Epilot()


res = s.executions.resume_execution_with_token(request={
    "resume_token": "eyJraWQiOiJrZXkifQ==",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ResumeReq](../../models/resumereq.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ResumeResp](../../models/resumeresp.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrigger_action

Retry a specific automation execution action which failed / is stuck.

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.executions.retrigger_action(action_id="9ec3711b-db63-449c-b894-54d5bb622a8f", execution_id="9baf184f-bc81-4128-bca3-d974c90a12c4")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `action_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Id of Action to retry.                                              | 9ec3711b-db63-449c-b894-54d5bb622a8f                                |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Execution Id                                                        | 9baf184f-bc81-4128-bca3-d974c90a12c4                                |
| `retry_req`                                                         | [Optional[models.RetryReq]](../../models/retryreq.md)               | :heavy_minus_sign:                                                  | Retry request details.                                              |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## start_execution

Start new automation execution

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.executions.start_execution(request={
    "entity_id": "e3d3ebac-baab-4395-abf4-50b5bf1f8b74",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.StartExecutionRequest](../../models/startexecutionrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.AutomationExecution](../../models/automationexecution.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
