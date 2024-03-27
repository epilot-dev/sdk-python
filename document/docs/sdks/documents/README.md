# Documents
(*documents*)

## Overview

Document Generation

### Available Operations

* [convert_document](#convert_document) - convertDocument
* [generate_document_v2](#generate_document_v2) - generateDocumentV2

## convert_document

Converts a document to a different format.

Supported input document types:
- .docx

Supported output document types:
- .pdf


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.ConvertDocumentRequest(
    input_document=components.InputDocument(
        s3ref=components.S3Reference(
            bucket='document-api-prod',
            key='uploads/my-template.pdf',
        ),
    ),
    output_format=components.OutputFormat.PDF,
    output_filename='converted.pdf',
)

res = s.documents.convert_document(req)

if res.convert_document_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.ConvertDocumentRequest](../../models/components/convertdocumentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ConvertDocumentResponse](../../models/operations/convertdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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


res = s.documents.generate_document_v2(document_generation_v2_request=components.DocumentGenerationV2Request(
    template_document=components.TemplateDocument(
        filename='my-template-{{order.order_number}}.docx',
    ),
    context_entity_id='bcd0aab9-b544-42b0-8bfb-6d449d02eacc',
    user_id='100321',
), job_id='<value>', mode=operations.Mode.FULL_GENERATION)

if res.document_generation_v2_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_generation_v2_request`                                                                                                                                                                                                                                                        | [Optional[components.DocumentGenerationV2Request]](../../models/components/documentgenerationv2request.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                     |
| `job_id`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Job ID for tracking the status of document generation action                                                                                                                                                                                                                            |
| `mode`                                                                                                                                                                                                                                                                                  | [Optional[operations.Mode]](../../models/operations/mode.md)                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Type of mode used for document generation flow:<br/>- partial_generation will have a intermediate step for users to validate and replace the variable values before generating the final document.<br/>- full_generation, goes through all the steps for the full generation of final document<br/> |


### Response

**[operations.GenerateDocumentV2Response](../../models/operations/generatedocumentv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
