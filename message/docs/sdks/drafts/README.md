# Drafts
(*drafts*)

### Available Operations

* [create_draft](#create_draft) - createDraft
* [send_draft](#send_draft) - sendDraft

## create_draft

Create a new draft

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.MessageRequestParams(
    from_=components.Address(
        address='messaging@epilot.cloud',
        name='epilot',
    ),
    subject='Request for solar panel price',
    html='<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>',
    parent_id='44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2',
    text='We at ABC GmbH would like to request a price quote for the solar panel.',
    thread=components.Thread(
        topic='CUSTOMER_MESSAGE',
        assigned_to=[
            '206801',
            '200109',
        ],
    ),
)

res = s.drafts.create_draft(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.MessageRequestParams](../../models/components/messagerequestparams.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateDraftResponse](../../models/operations/createdraftresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## send_draft

Send the existing draft to the recipients

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.send_draft()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.SendDraftResponse](../../models/operations/senddraftresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
