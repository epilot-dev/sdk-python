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
                '_schema': 'submission',
                'description': 'Submission created via API',
                'contact_first_name': 'First',
                'contact_last_name': 'Last',
                'contact_email': 'example@submission.com',
                'request': 'I would like to know more about electric vehicles',
                'files': '<value>',
            },
            description='Submission created via API',
            files=[
                shared.Files(
                    s3ref=shared.S3Reference(
                        bucket='epilot-user-content',
                        key='temp/123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
                    ),
                    filename='document.pdf',
                ),
            ],
        ),
    ],
    organization_id='123',
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
    journey_submit_id='123',
)

res = s.submissions.create_submission(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->