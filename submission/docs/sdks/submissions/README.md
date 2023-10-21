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
import epilot
from epilot.models import shared

s = epilot.Epilot()

req = shared.SubmissionPayload(
    ivy_opportunity_ids=[
        'string',
    ],
    entities=[
        shared.SubmissionEntity(
            additional_properties={
                "contact_first_name": 'string',
                "contact_last_name": 'string',
                "contact_email": 'string',
                "request": 'string',
                "files": 'string',
                "_schema": 'string',
                "description": 'string',
            },
            schema=shared.SubmissionEntitySchema.SUBMISSION,
            files=[
                shared.SubmissionEntityFiles(
                    additional_properties={
                        "key": 'string',
                    },
                    tags=[
                        'string',
                    ],
                    relation_tags=[
                        'string',
                    ],
                    s3ref=shared.S3Reference(
                        bucket='epilot-user-content',
                        key='temp/123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
                    ),
                ),
            ],
        ),
    ],
    journey_submit_id='123',
    opt_ins=[
        shared.OptIn(
            identifier='example@email.com',
            meta={
                "key": 'string',
            },
            topic='EMAIL_MARKETING',
        ),
    ],
    organization_id='123',
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
)

res = s.submissions.create_submission(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.SubmissionPayload](../../models/shared/submissionpayload.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateSubmissionResponse](../../models/operations/createsubmissionresponse.md)**

