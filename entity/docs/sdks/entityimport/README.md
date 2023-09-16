# EntityImport

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

req = operations.ImportEntitiesRequest(
    entity_import_params=shared.EntityImportParams(
        s3_reference=shared.EntityImportParamsS3Reference(
            bucket='my-bucket',
            key='imports/my-import.json',
        ),
        schema='contact',
    ),
    job_id='abc123',
)

res = s.entity_import.import_entities(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ImportEntitiesRequest](../../models/operations/importentitiesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ImportEntitiesResponse](../../models/operations/importentitiesresponse.md)**

