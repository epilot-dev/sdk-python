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
* [get_relations_v3](#get_relations_v3) - getRelationsV3
* [update_relation](#update_relation) - updateRelation

## add_relations

Relates one or more entities to parent entity by adding items to a relation attribute

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.AddRelationsRequest(
    id='acd6b1d8-3d92-448b-9649-9df660d593cf',
    slug='contact',
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_relation

Removes relation between two entities

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.DeleteRelationRequest(
    attribute='<value>',
    entity_id='<value>',
    id='84afcd91-1519-4f5b-b7b8-55b9c58577ae',
    slug='contact',
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_related_entities_count

Returns the amount of unique related entities for an entity - includes direct and reverse relations.


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.get_related_entities_count(id='3a515de5-fe13-46e4-ad0c-a57656a6a8af', slug='contact', exclude_schemas=[
    'contact',
])

if res.get_related_entities_count is not None:
    # handle response
    pass
```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `id`                              | *str*                             | :heavy_check_mark:                | Entity id                         |                                   |
| `slug`                            | *str*                             | :heavy_check_mark:                | Entity Type                       | contact                           |
| `exclude_schemas`                 | List[*str*]                       | :heavy_minus_sign:                | Filter results to exclude schemas |                                   |


### Response

**[operations.GetRelatedEntitiesCountResponse](../../models/operations/getrelatedentitiescountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_relations

Returns 1st level direct relations for an entity.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_relations_v2

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetRelationsV2Request(
    id='80912f3e-8dbd-4dd4-8ecc-63e001b2fb33',
    slug='contact',
    fields=[
        '_id',
        '_title',
        'first_name',
        'account',
        '!account.*._files',
        '**._product',
    ],
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_relations_v3

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetRelationsV3Request(
    id='6e35e8b4-d75d-4f84-a79c-6a8b45571a04',
    slug='contact',
)

res = s.relations.get_relations_v3(req)

if res.get_relations_resp_with_pagination is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetRelationsV3Request](../../models/operations/getrelationsv3request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetRelationsV3Response](../../models/operations/getrelationsv3response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_relation

Updates an existing relation between two entities.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpdateRelationRequest(
    attribute='<value>',
    entity_id='<value>',
    id='90bd69bf-f6a7-44da-bb01-c3854f8c4b22',
    slug='contact',
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
