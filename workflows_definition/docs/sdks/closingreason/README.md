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
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ChangeReasonStatusRequest(
    change_reason_status_req=shared.ChangeReasonStatusReq(
        status=shared.ClosingReasonsStatus.ACTIVE,
    ),
    reason_id='regional',
)

res = s.closing_reason.change_reason_status(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ChangeReasonStatusRequest](../../models/operations/changereasonstatusrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ChangeReasonStatusResponse](../../models/operations/changereasonstatusresponse.md)**


## create_closing_reason

A created Closing Reason is stored for the organization and will be displayed in the library of reasons.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ClosingReason(
    status=shared.ClosingReasonsStatus.ACTIVE,
    title='unlined',
)

res = s.closing_reason.create_closing_reason(req)

if res.closing_reason is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.ClosingReason](../../models/shared/closingreason.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateClosingReasonResponse](../../models/operations/createclosingreasonresponse.md)**


## get_all_closing_reasons

Get all Closing Reasons defined in the organization by default all Active.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetAllClosingReasonsRequest()

res = s.closing_reason.get_all_closing_reasons(req)

if res.closing_reasons is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAllClosingReasonsRequest](../../models/operations/getallclosingreasonsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetAllClosingReasonsResponse](../../models/operations/getallclosingreasonsresponse.md)**

