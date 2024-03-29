# epilot-file

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=file
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.DeleteFilePayload(
    s3ref=shared.S3Reference(
        bucket="epilot-files-prod",
        key="123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
    ),
)
    
res = s.files.delete_file(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### files

* `delete_file` - deleteFile
* `download_file` - downloadFile
* `download_s3_file` - downloadS3File
* `preview_file` - previewFile
* `preview_s3_file` - previewS3File
* `save_file` - saveFile
* `upload_file` - uploadFile
* `upload_file_public` - uploadFilePublic
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
