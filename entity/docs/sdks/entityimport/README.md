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
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.entity_import.import_entities(entity_import_params=shared.EntityImportParams(
    s3_reference=shared.EntityImportParamsS3Reference(
        bucket='my-bucket',
        key='imports/my-import.json',
    ),
    schema='contact',
), job_id='abc123')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `entity_import_params`                                                                                        | [Optional[shared.EntityImportParams]](../../models/shared/entityimportparams.md)                              | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `job_id`                                                                                                      | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | The ID of the import job. This ID is used to track the progress and fetch the result of the import operation. | abc123                                                                                                        |


### Response

**[operations.ImportEntitiesResponse](../../models/operations/importentitiesresponse.md)**

