<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.DeleteFilePayload(
    s3ref=shared.S3Reference(
        bucket='epilot-files-prod',
        key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
    ),
)

res = s.files.delete_file(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->