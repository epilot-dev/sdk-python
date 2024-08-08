<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_submission
from epilot_submission import Epilot

async def main():
    s = Epilot()
    await s.submissions.create_submission_async(request={
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->