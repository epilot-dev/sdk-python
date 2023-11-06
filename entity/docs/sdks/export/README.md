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


res = s.export.export_entities(entity_search_params=shared.EntitySearchParams(
    aggs=shared.EntitySearchParamsAggs(),
    fields=[
        '_id',
        '_title',
        'first_name',
    ],
    q='_schema:contact AND status:active',
    sort='_created_at:desc',
), is_template=False, job_id='abc123', language='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `entity_search_params`                                                           | [Optional[shared.EntitySearchParams]](../../models/shared/entitysearchparams.md) | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `is_template`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Pass 'true' to generate import template                                          |                                                                                  |
| `job_id`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Export Job Id to get the result                                                  | abc123                                                                           |
| `language`                                                                       | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Export headers translation language                                              |                                                                                  |


### Response

**[operations.ExportEntitiesResponse](../../models/operations/exportentitiesresponse.md)**

