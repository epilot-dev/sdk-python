# Submissions
(*submissions*)

## Overview

Journey Submission

### Available Operations

* [create_submission](#create_submission) - createSubmission

## create_submission

Creates a submission from a public facing Journey


### Example Usage

```python
import epilot_submission
from epilot_submission import Epilot

s = Epilot()


s.submissions.create_submission(request={
    "entities": [
        epilot_submission.SubmissionEntity(
            schema_=epilot_submission.Schema.SUBMISSION,
            description="Submission created via API",
            files=[
                epilot_submission.Files(
                    s3ref={
                        "bucket": "epilot-user-content",
                        "key": "temp/123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
                    },
                    filename="document.pdf",
                    **{

                    },
                ),
            ],
            **{
                "contact_first_name": "First",
                "contact_last_name": "Last",
                "contact_email": "example@submission.com",
                "request": "I would like to know more about electric vehicles",
            },
        ),
    ],
    "organization_id": "123",
    "source_id": "ce99875f-fba9-4fe2-a8f9-afaf52059051",
    "source_type": "journey",
    "journey_submit_id": "123",
    "opt_ins": [
        {
            "identifier": "example@email.com",
            "topic": "EMAIL_MARKETING",
        },
    ],
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SubmissionPayload](../../models/submissionpayload.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
