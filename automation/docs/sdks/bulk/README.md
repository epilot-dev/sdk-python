# Bulk
(*bulk*)

## Overview

Bulk job for triggering automation executions

### Available Operations

* [bulk_trigger_executions](#bulk_trigger_executions) - bulkTriggerExecutions
* [get_bulk_job](#get_bulk_job) - getBulkJob

## bulk_trigger_executions

Create a bulk job that triggers multiple automation executions

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.bulk.bulk_trigger_executions(request={
    "entity_ids": [
        "e3d3ebac-baab-4395-abf4-50b5bf1f8b74",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.TriggerExecutionsRequest](../../models/triggerexecutionsrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.TriggerExecutionsJob](../../models/triggerexecutionsjob.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## get_bulk_job

Get the status of a bulk job that triggers multiple automation executions

### Example Usage

```python
from epilot_automation import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.bulk.get_bulk_job(job_id="8c086140-f33e-4bb7-a993-50c0f2402c7b")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 8c086140-f33e-4bb7-a993-50c0f2402c7b                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TriggerExecutionsJob](../../models/triggerexecutionsjob.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
