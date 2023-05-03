# files

## Overview

Files

### Available Operations

* [delete_file](#delete_file) - deleteFile
* [download_file](#download_file) - downloadFile
* [download_s3_file](#download_s3_file) - downloadS3File
* [preview_file](#preview_file) - previewFile
* [preview_s3_file](#preview_s3_file) - previewS3File
* [save_file](#save_file) - saveFile
* [upload_file](#upload_file) - uploadFile
* [upload_file_public](#upload_file_public) - uploadFilePublic

## delete_file

Delete file entity

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
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
```

## download_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DownloadFileRequest(
    attachment=False,
    id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
    version=548814,
)

res = s.files.download_file(req)

if res.download_file_200_application_json_object is not None:
    # handle response
```

## download_s3_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.DownloadS3FileRequest(
    attachment=False,
    s3_bucket='provident',
    s3_key='distinctio',
)

res = s.files.download_s3_file(req)

if res.download_s3_file_200_application_json_object is not None:
    # handle response
```

## preview_file

Generate thumbnail preview for a file entity

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PreviewFileRequest(
    h=844266,
    id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
    version=602763,
    w=857946,
)

res = s.files.preview_file(req)

if res.status_code == 200:
    # handle response
```

## preview_s3_file

Generate thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PreviewS3FileRequest(
    s3_reference=shared.S3Reference(
        bucket='epilot-files-prod',
        key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
    ),
    h=544883,
    w=847252,
)

res = s.files.preview_s3_file(req)

if res.status_code == 200:
    # handle response
```

## save_file

Create / Update a permanent File entity

Makes file object permanent

Saves metadata to file entity


### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "error": 'deserunt',
    "suscipit": 'iure',
}

res = s.files.save_file(req)

if res.file_entity is not None:
    # handle response
```

## upload_file

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.UploadFileRequest(
    upload_file_payload=shared.UploadFilePayload(
        filename='document.pdf',
        mime_type='application/pdf',
    ),
    file_entity_id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
)

res = s.files.upload_file(req)

if res.upload_file_201_application_json_object is not None:
    # handle response
```

## upload_file_public

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.UploadFilePayload(
    filename='document.pdf',
    mime_type='application/pdf',
)

res = s.files.upload_file_public(req)

if res.upload_file_public_201_application_json_object is not None:
    # handle response
```
