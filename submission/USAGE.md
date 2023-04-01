<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = shared.SubmissionPayload(
    ivy_opportunity_ids=[
        "provident",
        "distinctio",
        "quibusdam",
    ],
    entities=[
        {
            "corrupti": "illum",
            "vel": "error",
            "deserunt": "suscipit",
            "iure": "magnam",
        },
        {
            "ipsa": "delectus",
            "tempora": "suscipit",
            "molestiae": "minus",
            "placeat": "voluptatum",
        },
        {
            "excepturi": "nisi",
            "recusandae": "temporibus",
        },
    ],
    journey_submit_id="123",
    opt_ins=[
        shared.OptIn(
            identifier="example@email.com",
            meta={
                "veritatis": "deserunt",
                "perferendis": "ipsam",
            },
            topic="EMAIL_MARKETING",
        ),
    ],
    organization_id="123",
    source_id="ce99875f-fba9-4fe2-a8f9-afaf52059051",
    source_type="journey",
)
    
res = s.submissions.create_submission(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->