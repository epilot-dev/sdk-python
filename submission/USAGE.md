<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()


req = shared.SubmissionPayload(
    ivy_opportunity_ids=[
        "deserunt",
        "porro",
        "nulla",
    ],
    entities=[
        {
            "perspiciatis": "nulla",
            "nihil": "fuga",
            "facilis": "eum",
            "iusto": "ullam",
        },
        {
            "inventore": "sapiente",
            "enim": "eum",
            "voluptatum": "autem",
            "vel": "non",
        },
        {
            "similique": "reprehenderit",
            "molestiae": "quo",
        },
    ],
    journey_submit_id="123",
    opt_ins=[
        shared.OptIn(
            identifier="example@email.com",
            meta={
                "dicta": "est",
                "voluptatem": "consequatur",
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