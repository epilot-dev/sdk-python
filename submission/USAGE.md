<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot()

req = shared.SubmissionPayload(
    entities=[
        shared.SubmissionEntity(
            schema=shared.Schema.SUBMISSION,
            additional_properties={
                '_schema': 'string',
                'description': 'string',
                'contact_first_name': 'string',
                'contact_last_name': 'string',
                'contact_email': 'string',
                'request': 'string',
                'files': 'string',
            },
            files=[
                shared.Files(
                    s3ref=shared.S3Reference(
                        bucket='epilot-user-content',
                        key='temp/123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
                    ),
                    additional_properties={
                        'key': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    relation_tags=[
                        'string',
                    ],
                ),
            ],
        ),
    ],
    organization_id='123',
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
    ivy_opportunity_ids=[
        'string',
    ],
    journey_submit_id='123',
    opt_ins=[
        shared.OptIn(
            identifier='example@email.com',
            meta={
                'key': 'string',
            },
            topic='EMAIL_MARKETING',
        ),
    ],
)

res = s.submissions.create_submission(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->