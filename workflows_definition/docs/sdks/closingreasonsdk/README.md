# ClosingReasonSDK
(*closing_reason*)

### Available Operations

* [change_reason_status](#change_reason_status) - changeReasonStatus
* [create_closing_reason](#create_closing_reason) - createClosingReason
* [get_all_closing_reasons](#get_all_closing_reasons) - getAllClosingReasons

## change_reason_status

Change the status of a Closing Reason (eg. ACTIVE to INACTIVE).

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.closing_reason.change_reason_status(reason_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `reason_id`                                                                     | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `change_reason_status_req`                                                      | [Optional[models.ChangeReasonStatusReq]](../../models/changereasonstatusreq.md) | :heavy_minus_sign:                                                              | change the status of a closing reason                                           |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.ErrorResp | 400,500          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## create_closing_reason

A created Closing Reason is stored for the organization and will be displayed in the library of reasons.

### Example Usage

```python
import openapi
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.create_closing_reason(request={
    "status": openapi.ClosingReasonsStatus.ACTIVE,
    "title": "better offer",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ClosingReason](../../models/closingreason.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ClosingReason](../../models/closingreason.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_all_closing_reasons

Get all Closing Reasons defined in the organization by default all Active.

### Example Usage

```python
from openapi import SDK

s = SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.get_all_closing_reasons(include_inactive=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `include_inactive`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Filter Closing Reasons by status like active inactiv                | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.ClosingReasons](../../models/closingreasons.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
