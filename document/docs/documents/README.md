# documents

## Overview

Document Generation

### Available Operations

* [generate_document](#generate_document) - generateDocument
* [generate_document_v2](#generate_document_v2) - generateDocumentV2

## generate_document

Builds document generated from input document with variables.

Supported input document types:
- .docx

Supported output document types:
- .pdf

Uses [Template Variables API](https://docs.epilot.io/api/template-variables) to replace variables in the document.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
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
```

## generate_document_v2

Builds document generated from input document with variables.

Supported input document types:
- .docx

Supported output document types:
- .pdf
- .docx but limited to only text based variables

Uses [Template Variables API](https://docs.epilot.io/api/template-variables) to replace variables in the document.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GenerateDocumentV2Request(
    request_body=operations.GenerateDocumentV2RequestBody(
        context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
        language=operations.GenerateDocumentV2RequestBodyLanguageEnum.DE,
        template_document=operations.GenerateDocumentV2RequestBodyTemplateDocument(
            filename='my-template-{{order.order_number}}.docx',
            s3ref=shared.S3Reference(
                bucket='document-api-prod',
                key='uploads/my-template.pdf',
            ),
        ),
        user_id='100321',
        variable_payload=operations.GenerateDocumentV2RequestBodyVariablePayload(
            additional_properties='corrupti',
        ),
    ),
    job_id='provident',
    mode=operations.GenerateDocumentV2ModeEnum.FULL_GENERATION,
)

res = s.documents.generate_document_v2(req)

if res.generate_document_v2_200_application_json_object is not None:
    # handle response
```
