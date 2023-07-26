# submissions

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
        'sapiente',
        'quo',
        'odit',
        'at',
    ],
    entities=[
        {
            "molestiae": 'quod',
            "quod": 'esse',
            "totam": 'porro',
            "dolorum": 'dicta',
        },
        {
            "officia": 'occaecati',
            "fugit": 'deleniti',
            "hic": 'optio',
        },
        {
            "beatae": 'commodi',
            "molestiae": 'modi',
            "qui": 'impedit',
        },
        {
            "esse": 'ipsum',
            "excepturi": 'aspernatur',
            "perferendis": 'ad',
        },
    ],
    journey_submit_id='123',
    opt_ins=[
        shared.OptIn(
            identifier='example@email.com',
            meta={
                "iste": 'dolor',
            },
            topic='EMAIL_MARKETING',
        ),
        shared.OptIn(
            identifier='example@email.com',
            meta={
                "laboriosam": 'hic',
                "saepe": 'fuga',
                "in": 'corporis',
            },
            topic='EMAIL_MARKETING',
        ),
        shared.OptIn(
            identifier='example@email.com',
            meta={
                "iure": 'saepe',
                "quidem": 'architecto',
                "ipsa": 'reiciendis',
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
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.SubmissionPayload](../../models/shared/submissionpayload.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateSubmissionResponse](../../models/operations/createsubmissionresponse.md)**

