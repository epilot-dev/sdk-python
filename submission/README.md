# epilot-submission

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=submission
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [submissions](docs/sdks/submissions/README.md)

* [create_submission](docs/sdks/submissions/README.md#create_submission) - createSubmission
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import epilot
from epilot.models import components, errors

s = epilot.Epilot()

res = None
try:
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

except errors.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://submission.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_idx=0,
)


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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_url="https://submission.sls.epilot.io",
)


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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
