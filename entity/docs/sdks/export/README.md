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
            'Northwest',
        ],
        from_=577630,
        hydrate=False,
        include_scores=False,
        q='_schema:contact AND status:active',
        size=727282,
        sort='_created_at:desc',
    ),
    is_template=False,
    job_id='abc123',
    language='Electronic',
)

res = s.export.export_entities(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ExportEntitiesRequest](../../models/operations/exportentitiesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ExportEntitiesResponse](../../models/operations/exportentitiesresponse.md)**

