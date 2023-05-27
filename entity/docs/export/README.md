# export

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
        epilot_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ExportEntitiesRequest(
    entity_search_params=shared.EntitySearchParams(
        aggs={
            "tempore": 'accusamus',
        },
        fields_=[
            'enim',
            'dolorem',
        ],
        from_=957451,
        hydrate=False,
        include_scores=False,
        q='_schema:contact AND status:active',
        size=518201,
        sort='_created_at:desc',
    ),
    is_template=False,
    job_id='abc123',
    language='nihil',
)

res = s.export.export_entities(req)

if res.status_code == 200:
    # handle response
```
