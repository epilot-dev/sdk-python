# Entities
(*entities*)

## Overview

CRUD Access for Entities

### Available Operations

* [autocomplete](#autocomplete) - autocomplete
* [create_entity](#create_entity) - createEntity
* [delete_entity](#delete_entity) - deleteEntity
* [get_entity](#get_entity) - getEntity
* [get_entity_v2](#get_entity_v2) - getEntityV2
* [list_entities](#list_entities) - listEntities
* [patch_entity](#patch_entity) - patchEntity
* [search_entities](#search_entities) - searchEntities
* [update_entity](#update_entity) - updateEntity
* [upsert_entity](#upsert_entity) - upsertEntity
* [validate_entity](#validate_entity) - validateEntity

## autocomplete

Autocomplete entity attributes


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.autocomplete(request={
    "attribute": "_tags",
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AutocompleteRequest](../../models/autocompleterequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.AutocompleteResponseBody](../../models/autocompleteresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create_entity

Creates a new entity using a key.

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityCreated`

## Relations

To create a relation, store a property object that defines a `$relation` array.

Example:

```json
{
  "contacts": {
    "$relation": [
      { "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }
    ]
  }
}
```

The items in `$relation` support two properties:
- `entity_id` - The ID of the entity to link
- `_tags` - Tags or labels for the relation (optional)


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.create_entity(request={
    "slug": "contact",
    "entity": epilot_entity.EntityInput(
        acl=epilot_entity.EntityACL(
            delete=[
                "org:456",
            ],
            edit=[
                "org:456",
            ],
            view=[
                "org:456",
                "org:789",
            ],
            **{

            },
        ),
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        schema_="contact",
        tags=[
            "example",
            "mock",
        ],
        **{
            "_org": "123",
            "_owners": [
                {
                    "org_id": "123",
                    "user_id": "123",
                },
            ],
            "_created_at": "2021-02-09T12:41:43.662Z",
            "_updated_at": "2021-02-09T12:41:43.662Z",
        },
    ),
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateEntityRequest](../../models/createentityrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntityItem](../../models/entityitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_entity

Deletes an Entity

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityDeleted`


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.entities.delete_entity(request={
    "id": "3b4a567a-853a-474f-8030-3350a9970542",
    "slug": "contact",
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeleteEntityRequest](../../models/deleteentityrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_entity

Gets Entity and relations by id.

## Relations

When `hydrate=true`, relation attributes are replaced in-place with nested entity values.

Example:
```json
{
  "_id": "123",
  "name": "parent",
  "_tags": ["parent"],
  "contacts": {
    "$relation": [
      { "entity_id": "456", "_tags": ["primary"] },
      { "entity_id": "789", "_tags": ["secondary"] },
    ]
  },
  "addresses": {
    "$relation_ref": [
      { "entity_id": "123", "_tags": ["primary"], "path": "address.0" },
      { "entity_id": "234", "_tags": ["secondary"], "path": "address.0" },
    ]
  }
}
```

Becomes:
```json
{
  "_id": "123",
  "name": "parent",
  "_tags": ["parent"],
  "contacts": [
    {
      "$relation": { "entity_id": "456", "_tags": ["primary"] },
      "_id": "456",
      "name": "child 1",
      "_tags": ["child"]
    },
    {
      "$relation": { "entity_id": "789", "_tags": ["secondary"] },
      "_id": "789",
      "name": "child 2",
      "_tags": ["child"]
    }
  ],
  "addresses": [
    {
      "$relation_ref": { "entity_id": "123", "_tags": ["primary"], "path": "address.0" },
      "_id": "123",
      "address": "address 1",
      "_tags": ["child"]
    },
    {
      "$relation_ref": { "entity_id": "234", "_tags": ["secondary"], "path": "address.0" },
      "_id": "234",
      "address": "address 2",
      "_tags": ["child"]
    }
  ]
}
```


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.get_entity(request={
    "id": "73700929-3a3f-4c9a-8a39-e5abedf44929",
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetEntityRequest](../../models/getentityrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetEntityResponseBody](../../models/getentityresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_entity_v2

Gets Entity by id.

Supports `hydrate` and `fields` parameters to control the shape of the response.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.get_entity_v2(request={
    "id": "3289b8c6-6a56-4c12-b3bc-45143354f2a7",
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetEntityV2Request](../../models/getentityv2request.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntityItem](../../models/entityitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_entities

List entities that meet the specified conditions.

Supports the same options as entity search but utilizes filtering using a subset of [Elastic Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) and does not perform scoring.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.list_entities(request={
    "filter_": [

    ],
    "aggs": {},
    "fields": [
        "_id",
        "_title",
        "first_name",
        "account",
        "!account.*._files",
        "**._product",
    ],
    "sort": "_created_at:desc",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EntityListParams](../../models/entitylistparams.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListEntitiesResponse](../../models/listentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## patch_entity

Partially updates an entity with the passed in entity data.

- If an _updated_at is passed and the server contains a newer version of the entity a `409` Error is returned

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityUpdated`

## Relations

To create a relation, store a property that defines a `$relation` array.

Example:

```json
{
  "contacts": {
    "$relation": [
      { "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }
    ]
  }
}
```

The items in `$relation` support two properties:
- `entity_id` - The ID of the entity to link
- `_tags` - Tags or labels for the relation (optional)


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.patch_entity(request={
    "entity": epilot_entity.EntityInput(
        acl=epilot_entity.EntityACL(
            delete=[
                "org:456",
            ],
            edit=[
                "org:456",
            ],
            view=[
                "org:456",
                "org:789",
            ],
            **{

            },
        ),
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        schema_="contact",
        tags=[
            "example",
            "mock",
        ],
        **{
            "_org": "123",
            "_owners": [
                {
                    "org_id": "123",
                    "user_id": "123",
                },
            ],
            "_created_at": "2021-02-09T12:41:43.662Z",
            "_updated_at": "2021-02-09T12:41:43.662Z",
        },
    ),
    "id": "cd6dc474-9915-44f5-99d5-806e999b7231",
    "slug": "contact",
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PatchEntityRequest](../../models/patchentityrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntityItem](../../models/entityitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## search_entities

Search for entities. Supports ordering and pagination. [Lucene query syntax](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-string-syntax) supported for complex querying.

Passing comma-separated `x-epilot-org-id` is supported for cross-org entity search.

## Relations

When `hydrate=true`, relation attributes are replaced in-place with nested entity values.

Example:
```json
{
  "_id": "123",
  "name": "parent",
  "_tags": ["parent"],
  "contacts": {
    "$relation": [
      { "entity_id": "456", "_tags": ["primary"] },
      { "entity_id": "789", "_tags": ["secondary"] },
    ]
  },
  "addresses": {
    "$relation_ref": [
      { "entity_id": "123", "_tags": ["primary"], "path": "address.0" },
      { "entity_id": "234", "_tags": ["secondary"], "path": "address.0" },
    ]
  }
}
```

Becomes:
```json
{
  "_id": "123",
  "name": "parent",
  "_tags": ["parent"],
  "contacts": [
    {
      "$relation": { "entity_id": "456", "_tags": ["primary"] },
      "_id": "456",
      "name": "child 1",
      "_tags": ["child"]
    },
    {
      "$relation": { "entity_id": "789", "_tags": ["secondary"] },
      "_id": "789",
      "name": "child 2",
      "_tags": ["child"]
    }
  ],
  "addresses": [
    {
      "$relation_ref": { "entity_id": "123", "_tags": ["primary"], "path": "address.0" },
      "_id": "123",
      "address": "address 1",
      "_tags": ["child"]
    },
    {
      "$relation_ref": { "entity_id": "234", "_tags": ["secondary"], "path": "address.0" },
      "_id": "234",
      "address": "address 2",
      "_tags": ["child"]
    }
  ]
}
```


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.search_entities(request={
    "q": "_schema:contact AND status:active",
    "aggs": {},
    "fields": [
        "_id",
        "_title",
        "first_name",
        "account",
        "!account.*._files",
        "**._product",
    ],
    "sort": "_created_at:desc",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EntitySearchParams](../../models/entitysearchparams.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.SearchEntitiesResponse](../../models/searchentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_entity

Updates an Entity

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityUpdated`

## Relations

To create a relation, store a property that defines a `$relation` array.

Example:

```json
{
  "contacts": {
    "$relation": [
      { "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }
    ]
  }
}
```

The items in `$relation` support two properties:
- `entity_id` - The ID of the entity to link
- `_tags` - Tags or labels for the relation (optional)


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.update_entity(request={
    "id": "2d5d17df-5520-4987-bd5a-6b1d12df7446",
    "slug": "contact",
    "entity": epilot_entity.EntityInput(
        acl=epilot_entity.EntityACL(
            delete=[
                "org:456",
            ],
            edit=[
                "org:456",
            ],
            view=[
                "org:456",
                "org:789",
            ],
            **{

            },
        ),
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        schema_="contact",
        tags=[
            "example",
            "mock",
        ],
        **{
            "_org": "123",
            "_owners": [
                {
                    "org_id": "123",
                    "user_id": "123",
                },
            ],
            "_created_at": "2021-02-09T12:41:43.662Z",
            "_updated_at": "2021-02-09T12:41:43.662Z",
        },
    ),
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.UpdateEntityRequest](../../models/updateentityrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntityItem](../../models/entityitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## upsert_entity

Create or update an entity using `unique_key`

- If no entities are matched, a new entity is created.
- If exactly one entity is matched, a `PATCH`-style update is applied to the existing entity.

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityCreated` or `EntityUpdated`


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.upsert_entity(request={
    "slug": "contact",
    "request_body": {
        "entity": epilot_entity.EntityInput(
            acl=epilot_entity.EntityACL(
                delete=[
                    "org:456",
                ],
                edit=[
                    "org:456",
                ],
                view=[
                    "org:456",
                    "org:789",
                ],
                **{

                },
            ),
            id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            schema_="contact",
            tags=[
                "example",
                "mock",
            ],
            **{
                "_org": "123",
                "_owners": [
                    {
                        "org_id": "123",
                        "user_id": "123",
                    },
                ],
                "_created_at": "2021-02-09T12:41:43.662Z",
                "_updated_at": "2021-02-09T12:41:43.662Z",
            },
        ),
        "unique_key": [
            "_id",
        ],
    },
    "activity_id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.UpsertEntityRequest](../../models/upsertentityrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntityItem](../../models/entityitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## validate_entity

Validates an entity against the schema.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.validate_entity(request={
    "slug": "contact",
    "entity": epilot_entity.EntityInput(
        acl=epilot_entity.EntityACL(
            delete=[
                "org:456",
            ],
            edit=[
                "org:456",
            ],
            view=[
                "org:456",
                "org:789",
            ],
            **{

            },
        ),
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        schema_="contact",
        tags=[
            "example",
            "mock",
        ],
        **{
            "_org": "123",
            "_owners": [
                {
                    "org_id": "123",
                    "user_id": "123",
                },
            ],
            "_created_at": "2021-02-09T12:41:43.662Z",
            "_updated_at": "2021-02-09T12:41:43.662Z",
        },
    ),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ValidateEntityRequest](../../models/validateentityrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.EntityValidationResultSuccess](../../models/entityvalidationresultsuccess.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.EntityValidationResultError | 422                                | application/json                   |
| models.SDKError                    | 4xx-5xx                            | */*                                |
