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
* [remove_relations](#remove_relations) - removeRelations
* [update_relation](#update_relation) - updateRelation

## add_relations

Relates one or more entities to parent entity by adding items to a relation attribute

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.add_relations(request={
    "id": "acd6b1d8-3d92-448b-9649-9df660d593cf",
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AddRelationsRequest](../../models/addrelationsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.RelationItem](../../models/relationitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_relation

Removes relation between two entities

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.relations.delete_relation(request={
    "attribute": "<value>",
    "entity_id": "<value>",
    "id": "84afcd91-1519-4f5b-b7b8-55b9c58577ae",
    "slug": "contact",
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.DeleteRelationRequest](../../models/deleterelationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_related_entities_count

Returns the amount of unique related entities for an entity - includes direct and reverse relations.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.get_related_entities_count(request={
    "id": "3a515de5-fe13-46e4-ad0c-a57656a6a8af",
    "slug": "contact",
    "exclude_schemas": [
        "file,message",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.GetRelatedEntitiesCountRequest](../../models/getrelatedentitiescountrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |


### Response

**[models.GetRelatedEntitiesCount](../../models/getrelatedentitiescount.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_relations

Returns 1st level direct relations for an entity.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.get_relations(request={
    "id": "e642d6bf-f2f7-41f9-8aa4-db0ec78f30e6",
    "slug": "contact",
    "exclude_schemas": [
        "file,message",
    ],
    "include_schemas": [
        "contact,account",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetRelationsRequest](../../models/getrelationsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.GetRelationsResp]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_relations_v2

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.get_relations_v2(request={
    "id": "80912f3e-8dbd-4dd4-8ecc-63e001b2fb33",
    "slug": "contact",
    "fields": [
        "_id",
        "_title",
        "first_name",
        "account",
        "!account.*._files",
        "**._product",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetRelationsV2Request](../../models/getrelationsv2request.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.GetRelationsRespWithPagination](../../models/getrelationsrespwithpagination.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_relations_v3

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.get_relations_v3(request={
    "id": "6e35e8b4-d75d-4f84-a79c-6a8b45571a04",
    "slug": "contact",
    "exclude_schemas": [
        "file,message",
    ],
    "include_schemas": [
        "contact,account",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetRelationsV3Request](../../models/getrelationsv3request.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.GetRelationsRespWithPagination](../../models/getrelationsrespwithpagination.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## remove_relations

Disassociate one or more entities to parent entity by removing items to a relation attribute

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.relations.remove_relations(request={
    "id": "ade2716c-d611-44c6-a235-b563ce20d945",
    "slug": "contact",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.RemoveRelationsRequest](../../models/removerelationsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_relation

Updates an existing relation between two entities.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.relations.update_relation(request={
    "attribute": "<value>",
    "entity_id": "<value>",
    "id": "90bd69bf-f6a7-44da-bb01-c3854f8c4b22",
    "slug": "contact",
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.UpdateRelationRequest](../../models/updaterelationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.RelationItem](../../models/relationitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
