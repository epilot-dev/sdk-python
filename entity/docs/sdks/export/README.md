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
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.export.export_entities(entity_search_params=components.EntitySearchParams(
    aggs=components.Aggs(),
    fields=[
        '_id',
        '_title',
        'first_name',
        'account',
        '!account.*._files',
        '**._product',
    ],
    q='_schema:contact AND status:active',
    sort='_created_at:desc',
), is_template=False, job_id='abc123', language='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `entity_search_params`                                                                   | [Optional[components.EntitySearchParams]](../../models/components/entitysearchparams.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |                                                                                          |
| `is_template`                                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Pass 'true' to generate import template                                                  |                                                                                          |
| `job_id`                                                                                 | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Export Job Id to get the result                                                          | abc123                                                                                   |
| `language`                                                                               | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Export headers translation language                                                      |                                                                                          |


### Response

**[operations.ExportEntitiesResponse](../../models/operations/exportentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
