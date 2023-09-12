# files

## Overview

Files API

### Available Operations

* [delete_file](#delete_file) - deleteFile
* [download_file](#download_file) - downloadFile
* [download_files](#download_files) - downloadFiles
* [download_s3_file](#download_s3_file) - downloadS3File
* [preview_file](#preview_file) - previewFile
* [preview_public_file](#preview_public_file) - previewPublicFile
* [preview_s3_file](#preview_s3_file) - previewS3File
* [preview_s3_file_get](#preview_s3_file_get) - previewS3FileGet
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
        cookie_auth="",
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

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DeleteFilePayload](../../models/shared/deletefilepayload.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**


## download_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
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

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DownloadFileRequest](../../models/operations/downloadfilerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DownloadFileResponse](../../models/operations/downloadfileresponse.md)**


## download_files

Generate pre-signed download S3 urls for multiple files

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)

req = [
    shared.DownloadFilesPayload(
        id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
        version=0,
    ),
]

res = s.files.download_files(req)

if res.download_files_200_application_json_objects is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [list[shared.DownloadFilesPayload]](../../models//.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.DownloadFilesResponse](../../models/operations/downloadfilesresponse.md)**


## download_s3_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
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

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DownloadS3FileRequest](../../models/operations/downloads3filerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DownloadS3FileResponse](../../models/operations/downloads3fileresponse.md)**


## preview_file

Generate thumbnail preview for a file entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PreviewFileRequest](../../models/operations/previewfilerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PreviewFileResponse](../../models/operations/previewfileresponse.md)**


## preview_public_file

Generate thumbnail preview for a public file entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)

req = operations.PreviewPublicFileRequest(
    h=544883,
    id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
    org_id='illum',
    version=423655,
    w=623564,
)

res = s.files.preview_public_file(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PreviewPublicFileRequest](../../models/operations/previewpublicfilerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PreviewPublicFileResponse](../../models/operations/previewpublicfileresponse.md)**


## preview_s3_file

Generate thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)

req = operations.PreviewS3FileRequest(
    s3_reference=shared.S3Reference(
        bucket='epilot-files-prod',
        key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
    ),
    h=645894,
    w=384382,
)

res = s.files.preview_s3_file(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PreviewS3FileRequest](../../models/operations/previews3filerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PreviewS3FileResponse](../../models/operations/previews3fileresponse.md)**


## preview_s3_file_get

Get thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)

req = operations.PreviewS3FileGetRequest(
    bucket='iure',
    h=297534,
    key='debitis',
    w=56713,
)

res = s.files.preview_s3_file_get(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PreviewS3FileGetRequest](../../models/operations/previews3filegetrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PreviewS3FileGetResponse](../../models/operations/previews3filegetresponse.md)**


## save_file

Create / Update a permanent File entity

Makes file object permanent

Saves metadata to file entity


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
    ),
)

req = {
    "tempora": 'suscipit',
}

res = s.files.save_file(req)

if res.file_entity is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.SaveFileResponse](../../models/operations/savefileresponse.md)**


## upload_file

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
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

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UploadFileRequest](../../models/operations/uploadfilerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**


## upload_file_public

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="",
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

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.UploadFilePayload](../../models/shared/uploadfilepayload.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.UploadFilePublicResponse](../../models/operations/uploadfilepublicresponse.md)**

