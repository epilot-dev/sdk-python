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
from epilot_file import Epilot

s = Epilot()


s.files.access_public_link(filename="invoice-2023-12.pdf", id="13d22918-36bd-4227-9ad4-2cb978788c8d")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | invoice-2023-12.pdf                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 13d22918-36bd-4227-9ad4-2cb978788c8d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_file

Delete file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


s.files.delete_file(request={
    "s3ref": {
        "bucket": "epilot-files-prod",
        "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
    },
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeleteFilePayload](../../models/deletefilepayload.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## download_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.download_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    | ef7d985c-2385-44f4-9c71-ae06a52264f8                                                                   |
| `attachment`                                                                                           | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Controls the Content-Disposition header to control browser behaviour. Set to true to trigger download. |                                                                                                        |
| `version`                                                                                              | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | index of file version                                                                                  |                                                                                                        |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |                                                                                                        |


### Response

**[models.DownloadFileResponseBody](../../models/downloadfileresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## download_files

Generate pre-signed download S3 urls for multiple files

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.download_files(request=[
    {
        "id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
        "version": 0,
    },
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.DownloadFilesPayload]](../../models/.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.ResponseBody]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## download_s3_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.download_s3_file(s3_bucket="<value>", s3_key="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `s3_bucket`                                                                                            | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `s3_key`                                                                                               | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `attachment`                                                                                           | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Controls the Content-Disposition header to control browser behaviour. Set to true to trigger download. |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[models.DownloadS3FileResponseBody](../../models/downloads3fileresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## generate_public_link

Generates a public link to access the private files


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.generate_public_link(id="ef7d985c-2385-44f4-9c71-ae06a52264f8")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | ef7d985c-2385-44f4-9c71-ae06a52264f8                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[str](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_all_public_links_for_file

Not yet implemented; This API would fetches all the public links that are previously generated for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.get_all_public_links_for_file(id="13d22918-36bd-4227-9ad4-2cb978788c8d")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 13d22918-36bd-4227-9ad4-2cb978788c8d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.GetAllPublicLinksForFileResponseBody](../../models/getallpubliclinksforfileresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## preview_file

Generate thumbnail preview for a file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


s.files.preview_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | ef7d985c-2385-44f4-9c71-ae06a52264f8                                |
| `h`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | height                                                              |                                                                     |
| `version`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | index of file version                                               |                                                                     |
| `w`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | width                                                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## preview_public_file

Generate thumbnail preview for a public file entity

### Example Usage

```python
from epilot_file import Epilot

s = Epilot()


s.files.preview_public_file(request={
    "id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.PreviewPublicFileRequest](../../models/previewpublicfilerequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## preview_s3_file

Generate thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


s.files.preview_s3_file(s3_reference={
    "bucket": "epilot-files-prod",
    "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `h`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | height                                                              |
| `w`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | width                                                               |
| `s3_reference`                                                      | [Optional[models.S3Reference]](../../models/s3reference.md)         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## preview_s3_file_get

Get thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


s.files.preview_s3_file_get(bucket="<value>", key="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bucket`                                                            | *str*                                                               | :heavy_check_mark:                                                  | s3 bucket                                                           |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | s3 key                                                              |
| `h`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | height                                                              |
| `w`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | width                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## revoke_public_link

Not yet implemented; This operation would revokes a given public link by ID

### Example Usage

```python
from epilot_file import Epilot

s = Epilot()


res = s.files.revoke_public_link(id="13d22918-36bd-4227-9ad4-2cb978788c8d")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 13d22918-36bd-4227-9ad4-2cb978788c8d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[str](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## save_file

Create / Update a permanent File entity

Makes file object permanent

Saves metadata to file entity


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.save_file(request=epilot_file.SaveS3FilePayload(
    s3ref={
        "bucket": "epilot-files-prod",
        "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
    },
    tags=[
        "string",
    ],
    access_control=epilot_file.SaveS3FilePayloadAccessControl.PRIVATE,
    document_type=epilot_file.SaveS3FilePayloadDocumentType.DOCUMENT,
    file_entity_id="string",
    filename="document.pdf",
    relations=[
        {
            "entity_id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
            "schema_": "contact",
        },
    ],
    **{

    },
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SaveFilePayload](../../models/savefilepayload.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.FileEntity](../../models/fileentity.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## save_file_v2

Create / Update a permanent File entity

Makes file object permanent

Saves metadata to file entity


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.save_file_v2(request=epilot_file.SaveFilePayloadV2(
    filename="document.pdf",
    s3ref={
        "bucket": "epilot-files-prod",
        "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
    },
    tags=[
        "string",
    ],
    access_control=epilot_file.SaveFilePayloadV2AccessControl.PRIVATE,
    document_type=epilot_file.SaveFilePayloadV2DocumentType.DOCUMENT,
    file_entity_id="string",
    **{

    },
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SaveFilePayloadV2](../../models/savefilepayloadv2.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.FileEntity](../../models/fileentity.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## upload_file

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.upload_file(file_entity_id="ef7d985c-2385-44f4-9c71-ae06a52264f8", upload_file_payload={
    "filename": "document.pdf",
    "index_tag": "2f6a377c8e78",
    "metadata": {
        "color": "blue",
    },
    "mime_type": "application/pdf",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `file_entity_id`                                                        | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | file entity id                                                          | ef7d985c-2385-44f4-9c71-ae06a52264f8                                    |
| `upload_file_payload`                                                   | [Optional[models.UploadFilePayload]](../../models/uploadfilepayload.md) | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |


### Response

**[models.UploadFileResponseBody](../../models/uploadfileresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## upload_file_public

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the createFile operation to store file file permanently.


### Example Usage

```python
from epilot_file import Epilot

s = Epilot()


res = s.files.upload_file_public(request={
    "filename": "document.pdf",
    "index_tag": "2f6a377c8e78",
    "metadata": {
        "color": "blue",
    },
    "mime_type": "application/pdf",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.UploadFilePayload](../../models/uploadfilepayload.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UploadFilePublicResponseBody](../../models/uploadfilepublicresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## upload_file_v2

Create pre-signed S3 URL to upload a file to keep temporarily (one week). - v2

Use the createFile operation to store file file permanently.


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.upload_file_v2(file_entity_id="ef7d985c-2385-44f4-9c71-ae06a52264f8", upload_file_payload={
    "filename": "document.pdf",
    "index_tag": "2f6a377c8e78",
    "metadata": {
        "color": "blue",
    },
    "mime_type": "application/pdf",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `file_entity_id`                                                        | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | file entity id                                                          | ef7d985c-2385-44f4-9c71-ae06a52264f8                                    |
| `upload_file_payload`                                                   | [Optional[models.UploadFilePayload]](../../models/uploadfilepayload.md) | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |


### Response

**[models.FileUpload](../../models/fileupload.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## verify_custom_download_url

Verify a pre-signed custom download url for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

s = Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
)


res = s.files.verify_custom_download_url(request={
    "custom_download_url": "https://some-api-url.com?file_id=123&expires_at=1699273500029&signature=abcdefg",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.VerifyCustomDownloadURLPayload](../../models/verifycustomdownloadurlpayload.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |


### Response

**[models.VerifyCustomDownloadURLResponseBody](../../models/verifycustomdownloadurlresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
