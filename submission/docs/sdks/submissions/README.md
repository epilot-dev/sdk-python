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
        'Automotive',
    ],
    entities=[
        {
            "contact_last_name": 'Bike',
            "contact_email": 'Shoes',
            "request": 'Incredible',
            "files": 'Borders',
            "_schema": 'synergistic',
            "description": 'versus',
            "contact_first_name": 'blah',
        },
    ],
    journey_submit_id='123',
    opt_ins=[
        shared.OptIn(
            identifier='example@email.com',
            meta={
                "Bicycle": 'Applications',
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

