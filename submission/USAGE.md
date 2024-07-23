<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import components

s = epilot.Epilot()


res = s.submissions.create_submission(request=components.SubmissionPayload(
    entities=[
        components.SubmissionEntity(
            schema=components.Schema.SUBMISSION,
            description='Submission created via API',
            files=[
                components.Files(
                    s3ref=components.S3Reference(
                        bucket='epilot-user-content',
                        key='temp/123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
                    ),
                    filename='document.pdf',
                    additional_properties={

                    },
                ),
            ],
            additional_properties={
                'contact_first_name': 'First',
                'contact_last_name': 'Last',
                'contact_email': 'example@submission.com',
                'request': 'I would like to know more about electric vehicles',
            },
        ),
    ],
    organization_id='123',
    source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
    source_type='journey',
    journey_submit_id='123',
    opt_ins=[
        components.OptIn(
            identifier='example@email.com',
            topic='EMAIL_MARKETING',
        ),
    ],
))

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->