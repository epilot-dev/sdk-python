# Preview
(*preview*)

## Overview

Preview APIs

### Available Operations

* [preview_file](#preview_file) - previewFile
* [preview_public_file](#preview_public_file) - previewPublicFile
* [preview_s3_file](#preview_s3_file) - previewS3File
* [preview_s3_file_get](#preview_s3_file_get) - previewS3FileGet

## preview_file

Generate thumbnail preview for a file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    epilot.preview.preview_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8", version=0)

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## preview_public_file

Generate thumbnail preview for a public file entity

### Example Usage

```python
from epilot_file import Epilot

with Epilot() as epilot:

    epilot.preview.preview_public_file(id="ef7d985c-2385-44f4-9c71-ae06a52264f8", version=0)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | ef7d985c-2385-44f4-9c71-ae06a52264f8                                |
| `h`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | height                                                              |                                                                     |
| `org_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Org id                                                              |                                                                     |
| `version`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | index of file version                                               |                                                                     |
| `w`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | width                                                               |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## preview_s3_file

Generate thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    epilot.preview.preview_s3_file(s3_ref={
        "bucket": "epilot-prod-user-content",
        "key": "123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `h`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | height                                                              |
| `w`                                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | width                                                               |
| `s3_ref`                                                            | [Optional[models.S3Ref]](../../models/s3ref.md)                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## preview_s3_file_get

Get thumbnail preview from an s3 reference for a file entity

### Example Usage

```python
import epilot_file
from epilot_file import Epilot

with Epilot(
    security=epilot_file.Security(
        cookie_auth="<YOUR_API_KEY_HERE>",
    ),
) as epilot:

    epilot.preview.preview_s3_file_get(bucket="<value>", key="<key>")

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |