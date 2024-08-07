# Drafts
(*drafts*)

### Available Operations

* [create_draft](#create_draft) - createDraft
* [send_draft](#send_draft) - sendDraft

## create_draft

Create a new draft

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.create_draft(request=epilot_message.MessageRequestParams(
    from_={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    subject="Request for solar panel price",
    bcc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    cc=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
    file={
        "dollar_relation": [
            {
                "entity_id": "f820ce3b-07b0-45ae-bcc6-babb2f53f79f",
                "cid": "fb222496-a1a5-4639-94f2-07b5e35e4068",
                "filename": "Produktinformationen_epilot360_Double_Opt_in.pdf",
            },
        ],
    },
    html="<div>We at ABC GmbH would like to request a price quote for the solar panel.</div>",
    parent_id="44d7a3eb-0cce-4bd3-a7cd-0b3e652de0c2",
    reply_to={
        "address": "messaging@epilot.cloud",
        "name": "epilot",
    },
    text="We at ABC GmbH would like to request a price quote for the solar panel.",
    thread={
        "topic": "CUSTOMER_MESSAGE",
        "assigned_to": [
            "206801",
            "200109",
        ],
    },
    to=[
        {
            "address": "messaging@epilot.cloud",
            "name": "epilot",
        },
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MessageRequestParams](../../models/messagerequestparams.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CreateDraftResponseBody](../../models/createdraftresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## send_draft

Send the existing draft to the recipients

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.drafts.send_draft()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SendDraftResponseBody](../../models/senddraftresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
