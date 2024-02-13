# Files
(*files*)

## Overview

Files API

### Available Operations

* [access_public_link](#access_public_link) - accessPublicLink
* [delete_file](#delete_file) - deleteFile
* [download_file](#download_file) - downloadFile
* [download_files](#download_files) - downloadFiles
* [download_s3_file](#download_s3_file) - downloadS3File
* [generate_public_link](#generate_public_link) - generatePublicLink
* [get_all_public_links_for_file](#get_all_public_links_for_file) - getAllPublicLinksForFile
* [preview_file](#preview_file) - previewFile
* [preview_public_file](#preview_public_file) - previewPublicFile
* [preview_s3_file](#preview_s3_file) - previewS3File
* [preview_s3_file_get](#preview_s3_file_get) - previewS3FileGet
* [revoke_public_link](#revoke_public_link) - revokePublicLink
* [save_file](#save_file) - saveFile
* [save_file_v2](#save_file_v2) - saveFileV2
* [upload_file](#upload_file) - uploadFile
* [upload_file_public](#upload_file_public) - uploadFilePublic
* [upload_file_v2](#upload_file_v2) - uploadFileV2
* [verify_custom_download_url](#verify_custom_download_url) - verifyCustomDownloadUrl

## access_public_link

Redirects to a accessible signed url for the respective file associated to the public link

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.access_public_link(filename='invoice-2023-12.pdf', id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `filename`                           | *str*                                | :heavy_check_mark:                   | N/A                                  | invoice-2023-12.pdf                  |
| `id`                                 | *str*                                | :heavy_check_mark:                   | N/A                                  | 13d22918-36bd-4227-9ad4-2cb978788c8d |


### Response

**[operations.AccessPublicLinkResponse](../../models/operations/accesspubliclinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_file

Delete file entity

### Example Usage

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

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DeleteFilePayload](../../models/shared/deletefilepayload.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## download_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.download_file(id='ef7d985c-2385-44f4-9c71-ae06a52264f8', attachment=False, version=925360)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    | ef7d985c-2385-44f4-9c71-ae06a52264f8                                                                   |
| `attachment`                                                                                           | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Controls the Content-Disposition header to control browser behaviour. Set to true to trigger download. |                                                                                                        |
| `version`                                                                                              | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | index of file version                                                                                  |                                                                                                        |


### Response

**[operations.DownloadFileResponse](../../models/operations/downloadfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## download_files

Generate pre-signed download S3 urls for multiple files

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = [
    shared.DownloadFilesPayload(
        id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
        version=0,
    ),
]

res = s.files.download_files(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [List[shared.DownloadFilesPayload]](../../models/.md) | :heavy_check_mark:                                    | The request object to use for the request.            |


### Response

**[operations.DownloadFilesResponse](../../models/operations/downloadfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## download_s3_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.download_s3_file(s3_bucket='string', s3_key='string', attachment=False)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `s3_bucket`                                                                                            | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `s3_key`                                                                                               | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `attachment`                                                                                           | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Controls the Content-Disposition header to control browser behaviour. Set to true to trigger download. |


### Response

**[operations.DownloadS3FileResponse](../../models/operations/downloads3fileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## generate_public_link

Generates a public link to access the private files


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.generate_public_link(id='ef7d985c-2385-44f4-9c71-ae06a52264f8')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | N/A                                  | ef7d985c-2385-44f4-9c71-ae06a52264f8 |


### Response

**[operations.GeneratePublicLinkResponse](../../models/operations/generatepubliclinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_all_public_links_for_file

Not yet implemented; This API would fetches all the public links that are previously generated for a file

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.get_all_public_links_for_file(id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | N/A                                  | 13d22918-36bd-4227-9ad4-2cb978788c8d |


### Response

**[operations.GetAllPublicLinksForFileResponse](../../models/operations/getallpubliclinksforfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## preview_file

Generate thumbnail preview for a file entity

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.preview_file(id='ef7d985c-2385-44f4-9c71-ae06a52264f8', h=427171, version=171541, w=89142)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | N/A                                  | ef7d985c-2385-44f4-9c71-ae06a52264f8 |
| `h`                                  | *Optional[int]*                      | :heavy_minus_sign:                   | height                               |                                      |
| `version`                            | *Optional[int]*                      | :heavy_minus_sign:                   | index of file version                |                                      |
| `w`                                  | *Optional[int]*                      | :heavy_minus_sign:                   | width                                |                                      |


### Response

**[operations.PreviewFileResponse](../../models/operations/previewfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## preview_public_file

Generate thumbnail preview for a public file entity

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PreviewPublicFileRequest(
    id='ef7d985c-2385-44f4-9c71-ae06a52264f8',
)

res = s.files.preview_public_file(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PreviewPublicFileRequest](../../models/operations/previewpublicfilerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PreviewPublicFileResponse](../../models/operations/previewpublicfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## preview_s3_file

Generate thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.preview_s3_file(s3_reference=shared.S3Reference(
    bucket='epilot-files-prod',
    key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
), h=240917, w=724428)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `s3_reference`                                                     | [Optional[shared.S3Reference]](../../models/shared/s3reference.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `h`                                                                | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | height                                                             |
| `w`                                                                | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | width                                                              |


### Response

**[operations.PreviewS3FileResponse](../../models/operations/previews3fileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## preview_s3_file_get

Get thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.preview_s3_file_get(bucket='string', key='string', h=40814, w=119215)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `bucket`           | *str*              | :heavy_check_mark: | s3 bucket          |
| `key`              | *str*              | :heavy_check_mark: | s3 key             |
| `h`                | *Optional[int]*    | :heavy_minus_sign: | height             |
| `w`                | *Optional[int]*    | :heavy_minus_sign: | width              |


### Response

**[operations.PreviewS3FileGetResponse](../../models/operations/previews3filegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## revoke_public_link

Not yet implemented; This operation would revokes a given public link by ID

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.revoke_public_link(id='13d22918-36bd-4227-9ad4-2cb978788c8d')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | N/A                                  | 13d22918-36bd-4227-9ad4-2cb978788c8d |


### Response

**[operations.RevokePublicLinkResponse](../../models/operations/revokepubliclinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.SaveS3FilePayload(
    s3ref=shared.S3Reference(
        bucket='epilot-files-prod',
        key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
    ),
    filename='document.pdf',
)

res = s.files.save_file(req)

if res.file_entity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [Union[shared.SaveS3FilePayload, shared.SaveCustomFilePayload]](../../models/shared/savefilepayload.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |


### Response

**[operations.SaveFileResponse](../../models/operations/savefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## save_file_v2

Create / Update a permanent File entity

Makes file object permanent

Saves metadata to file entity


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.SaveFilePayloadV2(
    filename='document.pdf',
    s3ref=shared.SaveFilePayloadV2S3ref(
        bucket='epilot-files-prod',
        key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
    ),
)

res = s.files.save_file_v2(req)

if res.file_entity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.SaveFilePayloadV2](../../models/shared/savefilepayloadv2.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.SaveFileV2Response](../../models/operations/savefilev2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upload_file

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.upload_file(upload_file_payload=shared.UploadFilePayload(
    filename='document.pdf',
    mime_type='application/pdf',
), file_entity_id='ef7d985c-2385-44f4-9c71-ae06a52264f8')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `upload_file_payload`                                                          | [Optional[shared.UploadFilePayload]](../../models/shared/uploadfilepayload.md) | :heavy_minus_sign:                                                             | N/A                                                                            |                                                                                |
| `file_entity_id`                                                               | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | file entity id                                                                 | ef7d985c-2385-44f4-9c71-ae06a52264f8                                           |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upload_file_public

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.UploadFilePayload(
    filename='document.pdf',
    mime_type='application/pdf',
)

res = s.files.upload_file_public(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.UploadFilePayload](../../models/shared/uploadfilepayload.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.UploadFilePublicResponse](../../models/operations/uploadfilepublicresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upload_file_v2

Create pre-signed S3 URL to upload a file to keep temporarily (one week). - v2

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.upload_file_v2(upload_file_payload=shared.UploadFilePayload(
    filename='document.pdf',
    mime_type='application/pdf',
), file_entity_id='ef7d985c-2385-44f4-9c71-ae06a52264f8')

if res.file_upload is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `upload_file_payload`                                                          | [Optional[shared.UploadFilePayload]](../../models/shared/uploadfilepayload.md) | :heavy_minus_sign:                                                             | N/A                                                                            |                                                                                |
| `file_entity_id`                                                               | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | file entity id                                                                 | ef7d985c-2385-44f4-9c71-ae06a52264f8                                           |


### Response

**[operations.UploadFileV2Response](../../models/operations/uploadfilev2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## verify_custom_download_url

Verify a pre-signed custom download url for a file

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.VerifyCustomDownloadURLPayload(
    custom_download_url='https://some-api-url.com?file_id=123&expires_at=1699273500029&signature=abcdefg',
)

res = s.files.verify_custom_download_url(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.VerifyCustomDownloadURLPayload](../../models/shared/verifycustomdownloadurlpayload.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.VerifyCustomDownloadURLResponse](../../models/operations/verifycustomdownloadurlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
