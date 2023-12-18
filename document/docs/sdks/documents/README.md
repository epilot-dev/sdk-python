# Documents
(*documents*)

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
from epilot.models import components, operations

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.GenerateDocumentRequestBody(
    context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
    language='de',
    template_document=operations.TemplateDocument(
        filename='my-template-{{order.order_number}}.docx',
        s3ref=components.S3Reference(
            bucket='document-api-prod',
            key='uploads/my-template.pdf',
        ),
    ),
    user_id='100321',
)

res = s.documents.generate_document(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GenerateDocumentRequestBody](../../models/operations/generatedocumentrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GenerateDocumentResponse](../../models/operations/generatedocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
from epilot.models import components, operations

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.generate_document_v2(request_body=operations.GenerateDocumentV2RequestBody(
    context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
    template_document=operations.GenerateDocumentV2TemplateDocument(
        filename='my-template-{{order.order_number}}.docx',
        s3ref=components.S3Reference(
            bucket='document-api-prod',
            key='uploads/my-template.pdf',
        ),
    ),
    user_id='100321',
    variable_payload=operations.VariablePayload(),
), job_id='string', mode=operations.Mode.FULL_GENERATION)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                                                                                                                   | [Optional[operations.GenerateDocumentV2RequestBody]](../../models/operations/generatedocumentv2requestbody.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                              |
| `job_id`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                               | Job ID for tracking the status of document generation action                                                                                                                                                                                                     |
| `mode`                                                                                                                                                                                                                                                           | [Optional[operations.Mode]](../../models/operations/mode.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                               | Type of mode used for document generation flow.<br/>Partial - Will have a intermediate step for users to validate and replace the variable values before generating the final document.<br/>Full - Goes through all the steps for the full generation of final document<br/> |


### Response

**[operations.GenerateDocumentV2Response](../../models/operations/generatedocumentv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
