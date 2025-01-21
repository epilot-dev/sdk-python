# Deprecated
(*deprecated*)

## Overview

Deprecated APIs

### Available Operations

* [~~save_file~~](#save_file) - saveFile :warning: **Deprecated**
* [~~upload_file~~](#upload_file) - uploadFile :warning: **Deprecated**

## ~~save_file~~

Create / Update a permanent File entity

Makes file object permanent

Saves metadata to file entity


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.deprecated.save_file(activity_id="01F130Q52Q6MWSNS8N2AVXV4JN", async_=False, save_file_payload=epilot_file.SaveFileFromSourceURLPayload(
        id="ef7d985c-2385-44f4-9c71-ae06a52264f8",
        manifest=[
            "123e4567-e89b-12d3-a456-426614174000",
        ],
        purpose=[
            "8d396871-95a0-4c9d-bb4d-9eda9c35776c",
            "da7cdf9a-01be-40c9-a29c-9a8f9f0de6f8",
        ],
        tags=[
            "tag1",
            "tag2",
        ],
        access_control=epilot_file.SaveFileFromSourceURLPayloadAccessControl.PRIVATE,
        custom_download_url="https://some-api-url.com/download?file_id=123",
        filename="document.pdf",
        mime_type="application/pdf",
        relations=[
            {
                "entity_id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
                "schema_": "contact",
            },
            {
                "entity_id": "ef7d985c-2385-44f4-9c71-ae06a52264f8",
                "schema_": "contact",
            },
        ],
        **{
            "s3ref": {
                "bucket": "epilot-prod-user-content",
                "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
            },
        },
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `activity_id`                                                                                | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Activity to include in event feed                                                            | 01F130Q52Q6MWSNS8N2AVXV4JN                                                                   |
| `async_`                                                                                     | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Don't wait for updated entity to become available in Search API. Useful for large migrations |                                                                                              |
| `save_file_payload`                                                                          | [Optional[models.SaveFilePayload]](../../models/savefilepayload.md)                          | :heavy_minus_sign:                                                                           | N/A                                                                                          |                                                                                              |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[models.FileEntity](../../models/fileentity.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~upload_file~~

Create pre-signed S3 URL to upload a file to keep temporarily (one week).

Use the saveFile operation to store file file permanently.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    res = epilot.deprecated.upload_file(file_entity_id="ef7d985c-2385-44f4-9c71-ae06a52264f8", upload_file_payload={
        "filename": "document.pdf",
        "index_tag": "2f6a377c8e78",
        "metadata": {
            "color": "blue",
        },
        "mime_type": "application/pdf",
    })

    # Handle response
    print(res)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |