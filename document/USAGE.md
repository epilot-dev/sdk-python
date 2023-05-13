<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
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
<!-- End SDK Example Usage -->