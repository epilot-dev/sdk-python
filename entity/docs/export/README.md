# export

## Overview

Export and Import entities via files

### Available Operations

* [export_entities](#export_entities) - exportEntities
* [import_entities](#import_entities) - importEntities

## export_entities

create export file of entities

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
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
    job_id='nihil',
    language='sit',
)

res = s.export.export_entities(req)

if res.status_code == 200:
    # handle response
```

## import_entities

import entity data from

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ImportEntitiesRequest(
    entity_import_params=shared.EntityImportParams(
        s3_reference=shared.EntityImportParamsS3Reference(
            bucket='epilot-files-prod',
            key='123/4d689aeb-1497-4410-a9fe-b36ca9ac4389/document.pdf',
        ),
        schema='contact',
    ),
    job_id='expedita',
)

res = s.export.import_entities(req)

if res.status_code == 200:
    # handle response
```
