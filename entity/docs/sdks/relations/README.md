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
            attribute='Pickup',
            entity_id='1d83d924-8b56-4499-9f66-0d593cfe3d00',
        ),
    ],
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    id='6d87e69d-98cd-409b-b6d3-0b52c3610877',
    slug='contact',
)

res = s.relations.add_relations(req)

if res.relation_item is not None:
    # handle response
    pass
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
    attribute='compressing',
    entity_id='Representative',
    id='cd911519-f5b7-47b8-95b9-c58577ae4d21',
    slug='contact',
)

res = s.relations.delete_relation(req)

if res.status_code == 200:
    # handle response
    pass
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
    exclude_schemas=[
        'Tuna',
    ],
    id='515de5fe-136e-44ad-8ca5-7656a6a8afba',
    slug='contact',
)

res = s.relations.get_related_entities_count(req)

if res.get_related_entities_count is not None:
    # handle response
    pass
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
    id='e642d6bf-f2f7-41f9-8aa4-db0ec78f30e6',
    slug='contact',
)

res = s.relations.get_relations(req)

if res.get_relations_resp is not None:
    # handle response
    pass
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
        '_id',
        '_schema',
        '_title',
    ],
    id='80912f3e-8dbd-4dd4-8ecc-63e001b2fb33',
    slug='contact',
)

res = s.relations.get_relations_v2(req)

if res.get_relations_resp_with_pagination is not None:
    # handle response
    pass
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
    attribute='male',
    entity_id='Account',
    id='ff6a74da-3b01-4c38-94f8-c4b226143d8a',
    slug='contact',
)

res = s.relations.update_relation(req)

if res.relation_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateRelationRequest](../../models/operations/updaterelationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateRelationResponse](../../models/operations/updaterelationresponse.md)**

