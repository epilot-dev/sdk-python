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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.relations.add_relations(request={
        "id": "adbd394b-69d6-4053-8f30-68e99c0b63b2",
        "slug": "contact",
        "request_body": [
            {
                "attribute": "contacts",
                "entity_id": "e8878f62-2d3d-4c86-bfe7-01a4180ff048",
                "tags": [
                    "billing",
                ],
            },
            {
                "attribute": "contacts",
                "entity_id": "ee8a2af9-fb36-4981-b848-4e65275851af",
            },
            {
                "attribute": "opportunities",
                "entity_id": "30990430-a53d-41a2-83db-2de072dc4dd4",
            },
        ],
        "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
        "async_": False,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AddRelationsRequest](../../models/addrelationsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RelationItem](../../models/relationitem.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.AddRelationsResponseBody | 404                             | application/json                |
| models.SDKError                 | 4XX, 5XX                        | \*/\*                           |

## delete_relation

Removes relation between two entities

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.relations.delete_relation(request={
        "attribute": "<value>",
        "entity_id": "<id>",
        "id": "8ac911fb-7859-4557-9ed1-64e5e267dbdf",
        "slug": "contact",
        "activity_id": epilot_entity.ActivityIDQueryParam2.UNKNOWN,
        "async_": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.DeleteRelationRequest](../../models/deleterelationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.DeleteRelationResponseBody | 404                               | application/json                  |
| models.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## get_related_entities_count

Returns the amount of unique related entities for an entity - includes direct and reverse relations.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.relations.get_related_entities_count(request={
        "id": "355ef164-dc56-4668-bfa4-e3fd7d61cdc2",
        "slug": "contact",
        "exclude_schemas": [
            "file,message",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.GetRelatedEntitiesCountRequest](../../models/getrelatedentitiescountrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.GetRelatedEntitiesCount](../../models/getrelatedentitiescount.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.GetRelatedEntitiesCountResponseBody | 404                                        | application/json                           |
| models.SDKError                            | 4XX, 5XX                                   | \*/\*                                      |

## get_relations

Returns 1st level direct relations for an entity.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.relations.get_relations(request={
        "id": "e4dbff19-a4be-47f0-968a-88f5588bb2b0",
        "slug": "contact",
        "exclude_schemas": [
            "file,message",
        ],
        "from_": 0,
        "hydrate": False,
        "include_reverse": False,
        "include_schemas": [
            "contact,account",
        ],
        "size": 100,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetRelationsRequest](../../models/getrelationsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetRelationsResp]](../../models/.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.GetRelationsResponseBody | 404                             | application/json                |
| models.SDKError                 | 4XX, 5XX                        | \*/\*                           |

## get_relations_v2

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.relations.get_relations_v2(request={
        "id": "89238bd4-ec30-412b-b3d2-974896904e1c",
        "slug": "contact",
        "fields": [
            "_id",
            "_title",
            "first_name",
            "account",
            "!account.*._files",
            "**._product",
        ],
        "from_": 0,
        "hydrate": False,
        "include_reverse": False,
        "size": 50,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetRelationsV2Request](../../models/getrelationsv2request.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.GetRelationsRespWithPagination](../../models/getrelationsrespwithpagination.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.GetRelationsV2ResponseBody | 404                               | application/json                  |
| models.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## get_relations_v3

Returns 1st level direct relations for an entity with pagination.

You can control whether to return the full entity or just the relation item with the `?hydrate` query param.

Reverse relations i.e. entities referring to this entity are included with the `?include_reverse` query param.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.relations.get_relations_v3(request={
        "id": "63ebd5f4-7cab-457a-a4b6-817ae5a085c2",
        "slug": "contact",
        "exclude_schemas": [
            "file,message",
        ],
        "from_": 0,
        "hydrate": False,
        "include_reverse": False,
        "include_schemas": [
            "contact,account",
        ],
        "size": 100,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetRelationsV3Request](../../models/getrelationsv3request.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.GetRelationsRespWithPagination](../../models/getrelationsrespwithpagination.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.GetRelationsV3ResponseBody | 404                               | application/json                  |
| models.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## remove_relations

Disassociate one or more entities to parent entity by removing items to a relation attribute

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    epilot.relations.remove_relations(request={
        "id": "ae76d146-2553-4e09-b50a-48271be11c68",
        "slug": "contact",
        "request_body": [
            {
                "attribute": "contacts",
                "entity_id": "e8878f62-2d3d-4c86-bfe7-01a4180ff048",
                "tags": [
                    "billing",
                ],
            },
            {
                "attribute": "contacts",
                "entity_id": "ee8a2af9-fb36-4981-b848-4e65275851af",
            },
            {
                "attribute": "opportunities",
                "entity_id": "30990430-a53d-41a2-83db-2de072dc4dd4",
            },
        ],
        "activity_id": epilot_entity.ActivityIDQueryParam2.UNKNOWN,
        "async_": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.RemoveRelationsRequest](../../models/removerelationsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.RemoveRelationsResponseBody | 404                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## update_relation

Updates an existing relation between two entities.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.relations.update_relation(request={
        "attribute": "<value>",
        "entity_id": "<id>",
        "id": "9b6bfa4a-b135-4fcb-b213-8032260ae470",
        "slug": "contact",
        "request_body": {
            "tags": [
                "billing",
                "prepaid",
            ],
        },
        "activity_id": epilot_entity.ActivityIDQueryParam2.UNKNOWN,
        "async_": False,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.UpdateRelationRequest](../../models/updaterelationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.RelationItem](../../models/relationitem.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.UpdateRelationResponseBody | 404                               | application/json                  |
| models.SDKError                   | 4XX, 5XX                          | \*/\*                             |