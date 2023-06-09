# relations

## Overview

Entity Relationships

### Available Operations

* [add_relations](#add_relations) - addRelations
* [delete_relation](#delete_relation) - deleteRelation
* [get_relations](#get_relations) - getRelations
* [get_relations_v2](#get_relations_v2) - getRelationsV2
* [update_relation](#update_relation) - updateRelation

## add_relations

Relates one or more entities to parent entity by adding items to a relation attribute

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AddRelationsRequest(
    request_body=[
        shared.RelationItem(
            tags=[
                'neque',
                'sed',
                'vel',
            ],
            attribute='libero',
            entity_id='5a73429c-db1a-4842-abb6-79d2322715bf',
            reverse=False,
        ),
    ],
    async_=False,
    id='0cbb1e31-b8b9-40f3-843a-1108e0adcf4b',
    slug='contact',
)

res = s.relations.add_relations(req)

if res.relation_item is not None:
    # handle response
```

## delete_relation

Removes relation between two entities

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteRelationRequest(
    async_=False,
    attribute='cupiditate',
    entity_id='qui',
    id='1879fce9-53f7-43ef-bfbc-7abd74dd39c0',
    slug='contact',
)

res = s.relations.delete_relation(req)

if res.status_code == 200:
    # handle response
```

## get_relations

Returns 1st level direct relations for an entity.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetRelationsRequest(
    hydrate=False,
    id='f5d2cff7-c70a-4456-a6d4-36813f16d9f5',
    include_reverse=False,
    slug='contact',
)

res = s.relations.get_relations(req)

if res.get_relations_resp is not None:
    # handle response
```

## get_relations_v2

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetRelationsV2Request(
    fields_=[
        'quisquam',
        'saepe',
        'ea',
        'impedit',
    ],
    from_=359271,
    hydrate=False,
    id='56146c3e-250f-4b00-8c42-e141aac366c8',
    include_reverse=False,
    query='assumenda',
    size=860552,
    slug='contact',
)

res = s.relations.get_relations_v2(req)

if res.get_relations_resp_with_pagination is not None:
    # handle response
```

## update_relation

Updates an existing relation between two entities.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateRelationRequest(
    request_body=operations.UpdateRelationRequestBody(
        tags=[
            'libero',
            'quasi',
        ],
    ),
    async_=False,
    attribute='tempora',
    entity_id='numquam',
    id='29074747-78a7-4bd4-a6d2-8c10ab3cdca4',
    slug='contact',
)

res = s.relations.update_relation(req)

if res.relation_item is not None:
    # handle response
```
