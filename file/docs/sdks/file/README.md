# File
(*file*)

## Overview

Upload and Manage File Entities

### Available Operations

* [delete_file](#delete_file) - deleteFile
* [download_file](#download_file) - downloadFile
* [download_files](#download_files) - downloadFiles
* [download_s3_file](#download_s3_file) - downloadS3File
* [get_file](#get_file) - getFile
* [save_file_v2](#save_file_v2) - saveFileV2
* [upload_file_public](#upload_file_public) - uploadFilePublic
* [upload_file_v2](#upload_file_v2) - uploadFileV2
* [verify_custom_download_url](#verify_custom_download_url) - verifyCustomDownloadUrl

## delete_file

Delete a file entity by id

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.delete_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8", activity_id="01F130Q52Q6MWSNS8N2AVXV4JN")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                               | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                | ef7d985c-2385-44f4-9c71-ae06a52264f8                                                                                               |
| `activity_id`                                                                                                                      | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Activity to include in event feed                                                                                                  | 01F130Q52Q6MWSNS8N2AVXV4JN                                                                                                         |
| `strict`                                                                                                                           | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | When passed true, the response will contain only fields that match the schema, with non-matching fields included in `__additional` |                                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[models.FileEntity](../../models/fileentity.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## download_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.download_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8")

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## download_files

Bulk generate pre-signed download S3 urls for multiple files

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.download_files(request=[
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## download_s3_file

Generate pre-signed download S3 url for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.download_s3_file(s3_bucket="<value>", s3_key="<value>")

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_file

Get a file entity by id

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.get_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                               | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                | ef7d985c-2385-44f4-9c71-ae06a52264f8                                                                                               |
| `async_`                                                                                                                           | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | Don't wait for updated entity to become available in Search API. Useful for large migrations                                       |                                                                                                                                    |
| `source_url`                                                                                                                       | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | N/A                                                                                                                                |                                                                                                                                    |
| `strict`                                                                                                                           | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | When passed true, the response will contain only fields that match the schema, with non-matching fields included in `__additional` |                                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[models.FileEntity](../../models/fileentity.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## save_file_v2

Saves a permanent file entity. Updates an existing file entity when `_id` is passed.

Saves metadata to file entity and stores a version when `s3ref` or `source_url` is passed.


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.save_file_v2(request=epilot_file.SaveFileV2Request(
        save_file_payload_v2=epilot_file.SaveS3FilePayload(
            tags=[
                "string",
            ],
            access_control=epilot_file.SaveS3FilePayloadAccessControl.PRIVATE,
            filename="document.pdf",
            s3ref={
                "bucket": "epilot-prod-user-content",
                "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
            },
            type=epilot_file.FileType.DOCUMENT,
            **{

            },
        ),
        activity_id="01F130Q52Q6MWSNS8N2AVXV4JN",
    ))

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SaveFileV2Request](../../models/savefilev2request.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileEntity](../../models/fileentity.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## upload_file_public

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the saveFileV2 operation to store file file permanently.


### Example Usage

```python
from epilot_file import Epilot

with Epilot() as epilot:

    res = epilot.file.upload_file_public(request={
        "filename": "image.png",
        "mime_type": "image/png",
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## upload_file_v2

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the saveFileV2 operation to store file file permanently.


### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.upload_file_v2(file_entity_id="ef7d985c-2385-44f4-9c71-ae06a52264f8", upload_file_payload={
        "filename": "image.png",
        "mime_type": "image/png",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           | Example                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file_entity_id`                                                                                                                                      | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Use this parameter when uploading a file directly to an existing file entity.<br/><br/>Note: still requires calling saveFileV2 to save the file permanently.<br/> | ef7d985c-2385-44f4-9c71-ae06a52264f8                                                                                                                  |
| `upload_file_payload`                                                                                                                                 | [Optional[models.UploadFilePayload]](../../models/uploadfilepayload.md)                                                                               | :heavy_minus_sign:                                                                                                                                    | N/A                                                                                                                                                   |                                                                                                                                                       |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |                                                                                                                                                       |

### Response

**[models.FileUpload](../../models/fileupload.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## verify_custom_download_url

Verify a pre-signed custom download url for a file

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.file.verify_custom_download_url(request={
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |