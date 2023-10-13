# Export
(*export*)

## Overview

Export and Import entities via files

### Available Operations

* [export_entities](#export_entities) - exportEntities

## export_entities

create export file of entities

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ExportEntitiesRequest(
    entity_search_params=shared.EntitySearchParams(
        aggs=shared.EntitySearchParamsAggs(),
        fields_=[
            '_id',
            '_title',
            'first_name',
        ],
        q='_schema:contact AND status:active',
        sort='_created_at:desc',
    ),
    job_id='abc123',
)

res = s.export.export_entities(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ExportEntitiesRequest](../../models/operations/exportentitiesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ExportEntitiesResponse](../../models/operations/exportentitiesresponse.md)**

