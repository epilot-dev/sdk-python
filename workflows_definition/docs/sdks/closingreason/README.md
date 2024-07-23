# ClosingReason
(*closing_reason*)

### Available Operations

* [change_reason_status](#change_reason_status) - changeReasonStatus
* [create_closing_reason](#create_closing_reason) - createClosingReason
* [get_all_closing_reasons](#get_all_closing_reasons) - getAllClosingReasons

## change_reason_status

Change the status of a Closing Reason (eg. ACTIVE to INACTIVE).

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.change_reason_status(reason_id='<value>', change_reason_status_req=components.ChangeReasonStatusReq(
    status=components.ClosingReasonsStatus.ACTIVE,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `reason_id`                                                                                    | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `change_reason_status_req`                                                                     | [Optional[components.ChangeReasonStatusReq]](../../models/components/changereasonstatusreq.md) | :heavy_minus_sign:                                                                             | change the status of a closing reason                                                          |


### Response

**[operations.ChangeReasonStatusResponse](../../models/operations/changereasonstatusresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.ErrorResp | 400,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## create_closing_reason

A created Closing Reason is stored for the organization and will be displayed in the library of reasons.

### Example Usage

```python
import sdk
from sdk.models import components

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.create_closing_reason(request=components.ClosingReason(
    status=components.ClosingReasonsStatus.ACTIVE,
    title='better offer',
))

if res.closing_reason is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.ClosingReason](../../models/components/closingreason.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateClosingReasonResponse](../../models/operations/createclosingreasonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_all_closing_reasons

Get all Closing Reasons defined in the organization by default all Active.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.closing_reason.get_all_closing_reasons(include_inactive=True)

if res.closing_reasons is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `include_inactive`                                   | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Filter Closing Reasons by status like active inactiv | true                                                 |


### Response

**[operations.GetAllClosingReasonsResponse](../../models/operations/getallclosingreasonsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
