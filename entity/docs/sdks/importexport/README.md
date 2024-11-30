# ImportExport
(*import_export*)

## Overview

Import and Export entities via portable files (CSV)

### Available Operations

* [export_entities](#export_entities) - exportEntities
* [import_entities](#import_entities) - Import Entities

## export_entities

Export entity data in a CSV-format. The export will export data as close as possible to what is visible on Entity UI tables.
The values exported as in some cases, transformed to human-readable values.

To force the export of raw values, use the `#` prefix in front of your field name when specifying the field on the `fields` param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    s.import_export.export_entities(request={
        "entity_search_params": {
            "q": "_schema:contact AND status:active",
            "fields": [
                "_id",
                "_title",
                "first_name",
                "account",
                "!account.*._files",
                "**._product",
            ],
        },
        "job_id": "abc123",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ExportEntitiesRequest](../../models/exportentitiesrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## import_entities

This endpoint enables the import of entities into the platform.
The entities should be provided in a CSV format inside an S3 bucket.
This API will return the `job_id`` which can be used to fetch the status of the import process.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    s.import_export.import_entities(request={
        "entity_import_params": {
            "s3_reference": {
                "bucket": "my-bucket",
                "key": "imports/my-import.json",
            },
            "schema_": "contact",
        },
        "job_id": "abc123",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ImportEntitiesRequest](../../models/importentitiesrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |