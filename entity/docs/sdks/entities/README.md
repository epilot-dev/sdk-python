# Entities
(*entities*)

## Overview

CRUD Access for Entities

### Available Operations

* [autocomplete](#autocomplete) - autocomplete
* [create_entity](#create_entity) - createEntity
* [delete_entity](#delete_entity) - deleteEntity
* [get_entity](#get_entity) - getEntity
* [patch_entity](#patch_entity) - patchEntity
* [search_entities](#search_entities) - searchEntities
* [update_entity](#update_entity) - updateEntity
* [upsert_entity](#upsert_entity) - upsertEntity

## autocomplete

Autocomplete entity attributes


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.AutocompleteRequest(
    attribute='_tags',
    slug='contact',
)

res = s.entities.autocomplete(req)

if res.autocomplete_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.AutocompleteRequest](../../models/operations/autocompleterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.AutocompleteResponse](../../models/operations/autocompleteresponse.md)**


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
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.CreateEntityRequest(
    request_body={
        "_updated_at": 'Industrial',
        "_acl": 'Implementation',
        "_id": 'Future',
        "_org": 'Southeast',
        "_owners": 'Tandem',
        "_schema": 'male',
        "_tags": 'North',
        "_created_at": 'Beach',
    },
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    slug='contact',
)

res = s.entities.create_entity(req)

if res.entity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateEntityRequest](../../models/operations/createentityrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateEntityResponse](../../models/operations/createentityresponse.md)**


## delete_entity

Deletes an Entity

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityDeleted`


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteEntityRequest(
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    id='3b4a567a-853a-474f-8030-3350a9970542',
    slug='contact',
)

res = s.entities.delete_entity(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteEntityRequest](../../models/operations/deleteentityrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteEntityResponse](../../models/operations/deleteentityresponse.md)**


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
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetEntityRequest(
    id='73700929-3a3f-4c9a-8a39-e5abedf44929',
    slug='contact',
)

res = s.entities.get_entity(req)

if res.get_entity_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetEntityRequest](../../models/operations/getentityrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetEntityResponse](../../models/operations/getentityresponse.md)**


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
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.PatchEntityRequest(
    request_body={
        "_tags": 'fuchsia',
        "_created_at": 'Account',
        "_updated_at": 'engage',
        "_acl": 'Cis',
        "_id": 'solutions',
        "_org": 'founder',
        "_owners": 'Southeast',
        "_schema": 'Cab',
    },
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    id='06e999b7-2319-4d9e-8290-d19da9e1f40d',
    slug='contact',
)

res = s.entities.patch_entity(req)

if res.entity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchEntityRequest](../../models/operations/patchentityrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PatchEntityResponse](../../models/operations/patchentityresponse.md)**


## search_entities

Search for entities. Supports ordering and pagination. Lucene query syntax supported for complex querying.

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
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.EntitySearchParams(
    aggs=shared.EntitySearchParamsAggs(),
    fields_=[
        '_id',
        '_title',
        'first_name',
    ],
    q='_schema:contact AND status:active',
    sort='_created_at:desc',
)

res = s.entities.search_entities(req)

if res.entity_search_results is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.EntitySearchParams](../../models/shared/entitysearchparams.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.SearchEntitiesResponse](../../models/operations/searchentitiesresponse.md)**


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
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateEntityRequest(
    request_body={
        "_updated_at": 'Hartmann',
        "_acl": 'invoice',
        "_id": 'fathom',
        "_org": 'Nepal',
        "_owners": 'indexing',
        "_schema": 'male',
        "_tags": 'Profound',
        "_created_at": 'policy',
    },
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    id='1d12df74-462a-498e-a7ff-ce36a4e49616',
    slug='contact',
)

res = s.entities.update_entity(req)

if res.entity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateEntityRequest](../../models/operations/updateentityrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateEntityResponse](../../models/operations/updateentityresponse.md)**


## upsert_entity

Create or update an entity using `unique_key`

- If no entities are matched, a new entity is created.
- If exactly one entity is matched, a `PATCH`-style update is applied to the existing entity.
- If more than one entity is matched a `409` Error is returned

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityCreated` or `EntityUpdated`


### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpsertEntityRequest(
    request_body=operations.UpsertEntityRequestBody(
        entity={
            "_created_at": 'West',
            "_updated_at": 'close',
            "_acl": 'Infrastructure',
            "_id": 'music',
            "_org": 'astride',
            "_owners": 'Designer',
            "_schema": 'strategic',
            "_tags": 'along',
        },
        unique_key=[
            '_id',
        ],
    ),
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
    slug='contact',
)

res = s.entities.upsert_entity(req)

if res.entity_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpsertEntityRequest](../../models/operations/upsertentityrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpsertEntityResponse](../../models/operations/upsertentityresponse.md)**

