# Internal
(*internal*)

### Available Operations

* [get_gen_ai_feedback](#get_gen_ai_feedback) - getGenAIFeedback

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


res = s.internal.get_gen_ai_feedback(from_=0, size=10)

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
