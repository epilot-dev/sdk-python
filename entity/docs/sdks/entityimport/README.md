# EntityImport
(*entity_import*)

### Available Operations

* [import_entities](#import_entities) - Import Entities

## import_entities

This endpoint enables the import of entities into the platform.
The entities should be provided in a CSV format inside an S3 bucket.
This API will return the `job_id`` which can be used to fetch the status of the import process.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.entity_import.import_entities(request={
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
