# Relations
(*relations*)

## Overview

Entity Relationships

### Available Operations

* [add_relations](#add_relations) - addRelations
* [delete_relation](#delete_relation) - deleteRelation
* [get_related_entities_count](#get_related_entities_count) - getRelatedEntitiesCount
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
                'Forward',
            ],
            attribute='Swedish Hatchback Luxurious',
            entity_id='9248b564-99df-4660-9593-cfe3d006d87e',
            reverse=False,
        ),
    ],
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    async_=False,
    id='69d98cd0-9bf6-4d30-b52c-36108777da47',
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
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    async_=False,
    attribute='whiteboard sandal',
    entity_id='quasi South Southeast',
    id='f5b77b85-5b9c-4585-b7ae-4d21f6044e25',
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


## get_related_entities_count

Returns the amount of unique related entities for an entity - includes direct and reverse relations.


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetRelatedEntitiesCountRequest(
    id='3a515de5-fe13-46e4-ad0c-a57656a6a8af',
    slug='contact',
)

res = s.relations.get_related_entities_count(req)

if res.get_related_entities_count is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetRelatedEntitiesCountRequest](../../models/operations/getrelatedentitiescountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetRelatedEntitiesCountResponse](../../models/operations/getrelatedentitiescountresponse.md)**


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
    id='e642d6bf-f2f7-41f9-8aa4-db0ec78f30e6',
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
        'up',
    ],
    from_=117939,
    hydrate=False,
    id='2f3e8dbd-dd40-4ecc-a3e0-01b2fb330d42',
    include_reverse=False,
    query='THX iterate',
    size=534143,
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
            'Androgyne',
        ],
    ),
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    async_=False,
    attribute='imperturbable female during',
    entity_id='HDD Gasoline',
    id='3b01c385-4f8c-44b2-a614-3d8a0d332324',
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

