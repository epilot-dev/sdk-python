# Bulk
(*bulk*)

## Overview

Bulk job for triggering automation executions

### Available Operations

* [bulk_trigger_executions](#bulk_trigger_executions) - bulkTriggerExecutions
* [get_bulk_job](#get_bulk_job) - getBulkJob
* [patch_bulk_job](#patch_bulk_job) - patchBulkJob

## bulk_trigger_executions

Create a bulk job that triggers multiple automation executions

### Example Usage

```python
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.bulk.bulk_trigger_executions(request={})

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BulkTriggerRequest](../../models/bulktriggerrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BulkTriggerJob](../../models/bulktriggerjob.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_bulk_job

Get the status of a bulk job that triggers multiple automation executions

### Example Usage

```python
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.bulk.get_bulk_job(job_id="8c086140-f33e-4bb7-a993-50c0f2402c7b")

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

**[models.BulkTriggerJob](../../models/bulktriggerjob.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_bulk_job

Approve / Cancel bulk job that triggers multiple automation executions

### Example Usage

```python
import epilot_automation
from epilot_automation import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.bulk.patch_bulk_job(job_id="8c086140-f33e-4bb7-a993-50c0f2402c7b", patch_bulk_job_request={
        "action": epilot_automation.Action.APPROVE,
        "task_token": "b35a6c51-2a15-4ef1-9623-20db37b0744f",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `job_id`                                                                    | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         | 8c086140-f33e-4bb7-a993-50c0f2402c7b                                        |
| `patch_bulk_job_request`                                                    | [Optional[models.PatchBulkJobRequest]](../../models/patchbulkjobrequest.md) | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.BulkTriggerJob](../../models/bulktriggerjob.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |