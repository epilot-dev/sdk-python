<!-- Start SDK Example Usage -->


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
            "_schema": 'Bike',
            "description": 'Shoes',
            "contact_first_name": 'Incredible',
            "contact_last_name": 'Borders',
            "contact_email": 'synergistic',
            "request": 'versus',
            "files": 'blah',
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
<!-- End SDK Example Usage -->