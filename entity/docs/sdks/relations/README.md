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
                'tempore',
            ],
            attribute='accusamus',
            entity_id='453f870b-326b-45a7-b429-cdb1a8422bb6',
            reverse=False,
        ),
        shared.RelationItem(
            tags=[
                'molestias',
                'temporibus',
            ],
            attribute='qui',
            entity_id='322715bf-0cbb-41e3-9b8b-90f3443a1108',
            reverse=False,
        ),
        shared.RelationItem(
            tags=[
                'consequatur',
                'est',
                'repellendus',
                'porro',
            ],
            attribute='doloribus',
            entity_id='4b921879-fce9-453f-b3ef-7fbc7abd74dd',
            reverse=False,
        ),
        shared.RelationItem(
            tags=[
                'natus',
            ],
            attribute='impedit',
            entity_id='0f5d2cff-7c70-4a45-a26d-436813f16d9f',
            reverse=False,
        ),
    ],
    async_=False,
    id='5fce6c55-6146-4c3e-a50f-b008c42e141a',
    slug='contact',
)

res = s.relations.add_relations(req)

if res.relation_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.AddRelationsRequest](../../models/operations/addrelationsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.AddRelationsResponse](../../models/operations/addrelationsresponse.md)**


## delete_relation

Removes relation between two entities

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteRelationRequest(
    async_=False,
    attribute='laborum',
    entity_id='placeat',
    id='366c8dd6-b144-4290-b474-778a7bd466d2',
    slug='contact',
)

res = s.relations.delete_relation(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteRelationRequest](../../models/operations/deleterelationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteRelationResponse](../../models/operations/deleterelationresponse.md)**


## get_relations

Returns 1st level direct relations for an entity.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetRelationsRequest(
    hydrate=False,
    id='8c10ab3c-dca4-4251-904e-523c7e0bc717',
    include_reverse=False,
    slug='contact',
)

res = s.relations.get_relations(req)

if res.get_relations_resp is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetRelationsRequest](../../models/operations/getrelationsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetRelationsResponse](../../models/operations/getrelationsresponse.md)**


## get_relations_v2

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetRelationsV2Request(
    fields_=[
        'accusamus',
        'aliquam',
        'odio',
    ],
    from_=577543,
    hydrate=False,
    id='6f2a70c6-8828-42aa-8825-62f222e9817e',
    include_reverse=False,
    query='accusamus',
    size=82971,
    slug='contact',
)

res = s.relations.get_relations_v2(req)

if res.get_relations_resp_with_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetRelationsV2Request](../../models/operations/getrelationsv2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetRelationsV2Response](../../models/operations/getrelationsv2response.md)**


## update_relation

Updates an existing relation between two entities.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateRelationRequest(
    request_body=operations.UpdateRelationRequestBody(
        tags=[
            'quod',
            'nam',
        ],
    ),
    async_=False,
    attribute='vero',
    entity_id='aliquid',
    id='1e6b7b95-bc0a-4b3c-a0c4-f3789fd871f9',
    slug='contact',
)

res = s.relations.update_relation(req)

if res.relation_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateRelationRequest](../../models/operations/updaterelationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateRelationResponse](../../models/operations/updaterelationresponse.md)**

