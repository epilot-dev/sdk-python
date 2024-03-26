<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->