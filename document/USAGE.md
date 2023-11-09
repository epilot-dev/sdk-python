<!-- Start SDK Example Usage -->


```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    epilot_auth="",
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
<!-- End SDK Example Usage -->