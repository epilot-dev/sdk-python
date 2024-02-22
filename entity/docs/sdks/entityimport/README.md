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
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entity_import.import_entities(entity_import_params=components.EntityImportParams(
    s3_reference=components.S3Reference(
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
| `entity_import_params`                                                                                        | [Optional[components.EntityImportParams]](../../models/components/entityimportparams.md)                      | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `job_id`                                                                                                      | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | The ID of the import job. This ID is used to track the progress and fetch the result of the import operation. | abc123                                                                                                        |


### Response

**[operations.ImportEntitiesResponse](../../models/operations/importentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
