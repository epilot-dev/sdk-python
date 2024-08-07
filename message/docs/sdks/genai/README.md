# GenAI
(*gen_ai*)

### Available Operations

* [generate_suggested_reply](#generate_suggested_reply) - generateSuggestedReply
* [get_gen_ai_feedback](#get_gen_ai_feedback) - getGenAIFeedback
* [get_info](#get_info) - getInfo
* [patch_info](#patch_info) - patchInfo

## generate_suggested_reply

Generate suggested reply of the message in the thread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.gen_ai.generate_suggested_reply(message_id="<value>", thread_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Message ID                                                          |
| `thread_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GenerateSuggestedReplyResponseBody](../../models/generatesuggestedreplyresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_gen_ai_feedback

Fetch the feedback list for genai

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.gen_ai.get_gen_ai_feedback(from_=0, size=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0                                                                   |
| `size`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Number of feedback to return                                        | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetGenAIFeedbackResponseBody](../../models/getgenaifeedbackresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_info

Get generated information of the thread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.gen_ai.get_info(thread_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `thread_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | Thread ID                                                             |
| `message_id`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Message ID, If not passed defaults to latest message ID in the thread |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.GetInfoResponse](../../models/getinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## patch_info

patch generated information of the thread

### Example Usage

```python
import epilot_message
from epilot_message import Epilot

s = Epilot(
    security=epilot_message.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.gen_ai.patch_info(message_id="<value>", thread_id="<value>", request_body={
    "created_at": 1612900000000,
    "error": "Failed to generate summary",
    "feedback": "Good summary",
    "next_steps": [
        "The agent should approve the refund",
    ],
    "progress": 100,
    "rating": "positive",
    "status": epilot_message.Status.COMPLETED,
    "summary": [
        "Customer is interested in solar panels",
    ],
    "tags": [
        "solar",
        "quote",
    ],
    "topics": [
        "Product enquiry",
    ],
    "updated_at": 1612900000000,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Message ID                                                          |
| `thread_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Thread ID                                                           |
| `request_body`                                                      | [models.PatchInfoRequestBody](../../models/patchinforequestbody.md) | :heavy_check_mark:                                                  | Request body for genai info update                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.PatchInfoResponseBody](../../models/patchinforesponsebody.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.PatchInfoGenAIResponseBody | 500                               | application/json                  |
| models.SDKError                   | 4xx-5xx                           | */*                               |
