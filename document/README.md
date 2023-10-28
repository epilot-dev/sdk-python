# epilot-document

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=document
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GenerateDocumentRequestBody(
    context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
    language='de',
    template_document=operations.GenerateDocumentRequestBodyTemplateDocument(
        filename='my-template-{{order.order_number}}.docx',
        s3ref=shared.S3Reference(
            bucket='document-api-prod',
            key='uploads/my-template.pdf',
        ),
    ),
    user_id='100321',
)

res = s.documents.generate_document(req)

if res.generate_document_200_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [documents](docs/sdks/documents/README.md)

* [generate_document](docs/sdks/documents/README.md#generate_document) - generateDocument
* [generate_document_v2](docs/sdks/documents/README.md#generate_document_v2) - generateDocumentV2
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
| 0 | `https://document.sls.epilot.io` | None |

For example:


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
    server_idx=0
)

req = operations.GenerateDocumentRequestBody(
    context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
    language='de',
    template_document=operations.GenerateDocumentRequestBodyTemplateDocument(
        filename='my-template-{{order.order_number}}.docx',
        s3ref=shared.S3Reference(
            bucket='document-api-prod',
            key='uploads/my-template.pdf',
        ),
    ),
    user_id='100321',
)

res = s.documents.generate_document(req)

if res.generate_document_200_application_json_object is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
    server_url="https://document.sls.epilot.io"
)

req = operations.GenerateDocumentRequestBody(
    context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
    language='de',
    template_document=operations.GenerateDocumentRequestBodyTemplateDocument(
        filename='my-template-{{order.order_number}}.docx',
        s3ref=shared.S3Reference(
            bucket='document-api-prod',
            key='uploads/my-template.pdf',
        ),
    ),
    user_id='100321',
)

res = s.documents.generate_document(req)

if res.generate_document_200_application_json_object is not None:
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
