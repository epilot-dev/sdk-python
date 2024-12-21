# Documents
(*documents*)

## Overview

Document Generation

### Available Operations

* [convert_document](#convert_document) - convertDocument
* [generate_document_v2](#generate_document_v2) - generateDocumentV2
* [get_template_meta](#get_template_meta) - getTemplateMeta

## convert_document

Converts a document to a different format.

Supported input document types:
- .docx

Supported output document types:
- .pdf


### Example Usage

```python
import epilot_document
from epilot_document import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.documents.convert_document(request={
        "input_document": {
            "s3ref": {
                "bucket": "document-api-prod",
                "key": "uploads/my-template.pdf",
            },
        },
        "output_format": epilot_document.OutputFormat.PDF,
        "output_filename": "converted.pdf",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.ConvertDocumentRequest](../../models/convertdocumentrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ConvertDocumentResponse](../../models/convertdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

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
from epilot_document import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.documents.generate_document_v2(document_generation_v2_request={
        "template_document": {
            "filename": "my-template-{{order.order_number}}.docx",
            "s3ref": {
                "bucket": "document-api-prod",
                "key": "uploads/my-template.pdf",
            },
        },
        "context_entity_id": "bcd0aab9-b544-42b0-8bfb-6d449d02eacc",
        "language": "en",
        "template_settings": {
            "custom_margins": {
                "bottom": 2.54,
                "top": 2.54,
            },
            "display_margin_guidelines": True,
            "enable_data_table_margin_autofix": False,
            "enabled_template_settings_persistence": False,
            "file_entity_id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
            "misconfigured_margins": False,
            "suggested_margins": {
                "bottom": 2.54,
                "top": 2.54,
            },
            "template_with_datatable": False,
        },
        "user_id": "100321",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_id`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Job ID for tracking the status of document generation action                                                                                                                                                                                                                            |
| `mode`                                                                                                                                                                                                                                                                                  | [Optional[models.Mode]](../../models/mode.md)                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Type of mode used for document generation flow:<br/>- partial_generation will have a intermediate step for users to validate and replace the variable values before generating the final document.<br/>- full_generation, goes through all the steps for the full generation of final document<br/> |
| `preview_mode`                                                                                                                                                                                                                                                                          | [Optional[models.PreviewMode]](../../models/previewmode.md)                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Type of mode used for document generation preview:<br/>- open - preview_url provides a link to open the file in a browser<br/>- download - preview_url provides a link to download the file<br/>                                                                                        |
| `document_generation_v2_request`                                                                                                                                                                                                                                                        | [Optional[models.DocumentGenerationV2Request]](../../models/documentgenerationv2request.md)                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                     |

### Response

**[models.DocumentGenerationV2Response](../../models/documentgenerationv2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_template_meta

Get metadata for a document template

Supported input document types:
- .docx


### Example Usage

```python
from epilot_document import Epilot

with Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.documents.get_template_meta(request={
        "template_document": {
            "s3ref": {
                "bucket": "document-api-prod",
                "key": "uploads/my-template.pdf",
            },
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DocumentMetaRequest](../../models/documentmetarequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentMetaResponse](../../models/documentmetaresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ErrorOutputError | 400, 403, 415           | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |