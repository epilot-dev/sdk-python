# epilot-submission

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=submission
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
                "contact_last_name": 'string',
                "contact_email": 'string',
                "request": 'string',
                "files": 'string',
                "_schema": 'string',
                "description": 'string',
                "contact_first_name": 'string',
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [submissions](docs/sdks/submissions/README.md)

* [create_submission](docs/sdks/submissions/README.md#create_submission) - createSubmission
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://submission.sls.epilot.io` | None |

For example:


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_idx=0
)

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


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_url="https://submission.sls.epilot.io"
)

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
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
