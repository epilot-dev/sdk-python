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
* [patch_entity](#patch_entity) - patchEntity
* [search_entities](#search_entities) - searchEntities
* [update_entity](#update_entity) - updateEntity
* [upsert_entity](#upsert_entity) - upsertEntity
* [validate_entity](#validate_entity) - validateEntity

## autocomplete

Autocomplete entity attributes


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.autocomplete(attribute='_tags', input='<value>', size=10, slug='contact')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         | Example                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `attribute`                         | *str*                               | :heavy_check_mark:                  | Autocomplete attribute              | _tags                               |
| `input`                             | *Optional[str]*                     | :heavy_minus_sign:                  | Input to autocomplete               |                                     |
| `size`                              | *Optional[int]*                     | :heavy_minus_sign:                  | Maximum number of results to return |                                     |
| `slug`                              | *Optional[str]*                     | :heavy_minus_sign:                  | Limit results to entity schema      | contact                             |


### Response

**[operations.AutocompleteResponse](../../models/operations/autocompleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
import dateutil.parser
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.create_entity(slug='contact', entity=components.Entity(
    additional_properties={
        '_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
        '_org': '123',
        '_owners': '<value>',
        '_schema': 'contact',
        '_tags': '<value>',
        '_created_at': '2021-02-09T12:41:43.662Z',
        '_updated_at': '2021-02-09T12:41:43.662Z',
        '_acl': '<value>',
    },
    acl=components.EntityACL(
        delete=[
            'org:456',
        ],
        edit=[
            'org:456',
        ],
        view=[
            'org:456',
            'org:789',
        ],
    ),
    created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
    id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
    org='123',
    owners=[
        components.EntityOwner(
            org_id='123',
            user_id='123',
        ),
    ],
    schema='contact',
    tags=[
        'example',
        'mock',
    ],
    updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
), activity_id='01F130Q52Q6MWSNS8N2AVXV4JN', async_=False)

if res.entity_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                      | Example                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slug`                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                               | Entity Type                                                                                                                                                                                                                                                                                                                                                      | contact                                                                                                                                                                                                                                                                                                                                                          |
| `entity`                                                                                                                                                                                                                                                                                                                                                         | [Optional[components.Entity]](../../models/components/entity.md)                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                                                                                                                              | {<br/>"_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",<br/>"_org": "123",<br/>"_owners": [<br/>{<br/>"org_id": "123",<br/>"user_id": "123"<br/>}<br/>],<br/>"_schema": "contact",<br/>"_tags": [<br/>"example",<br/>"mock"<br/>],<br/>"_created_at": "2021-02-09T12:41:43.662Z",<br/>"_updated_at": "2021-02-09T12:41:43.662Z",<br/>"_acl": {<br/>"view": [<br/>"org:456",<br/>"org:789"<br/>],<br/>"edit": [<br/>"org:456"<br/>],<br/>"delete": [<br/>"org:456"<br/>]<br/>}<br/>} |
| `activity_id`                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                               | Activity to include in event feed                                                                                                                                                                                                                                                                                                                                | 01F130Q52Q6MWSNS8N2AVXV4JN                                                                                                                                                                                                                                                                                                                                       |
| `async_`                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                               | Don't wait for updated entity to become available in Search API. Useful for large migrations                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                  |


### Response

**[operations.CreateEntityResponse](../../models/operations/createentityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_entity

Deletes an Entity

## Activity

If no `activity_id` query parameter is provided, implicitly creates Activity of type `EntityDeleted`


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.delete_entity(id='3b4a567a-853a-474f-8030-3350a9970542', slug='contact', activity_id='01F130Q52Q6MWSNS8N2AVXV4JN')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `id`                              | *str*                             | :heavy_check_mark:                | Entity id                         |                                   |
| `slug`                            | *str*                             | :heavy_check_mark:                | Entity Type                       | contact                           |
| `activity_id`                     | *Optional[str]*                   | :heavy_minus_sign:                | Activity to include in event feed | 01F130Q52Q6MWSNS8N2AVXV4JN        |


### Response

**[operations.DeleteEntityResponse](../../models/operations/deleteentityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.get_entity(id='73700929-3a3f-4c9a-8a39-e5abedf44929', slug='contact', hydrate=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Entity id                                                                                            |                                                                                                      |
| `slug`                                                                                               | *str*                                                                                                | :heavy_check_mark:                                                                                   | Entity Type                                                                                          | contact                                                                                              |
| `hydrate`                                                                                            | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | When true, enables entity hydration to resolve nested $relation & $relation_ref references in-place. |                                                                                                      |


### Response

**[operations.GetEntityResponse](../../models/operations/getentityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_entity_v2

Gets Entity by id.

Supports `hydrate` and `fields` parameters to control the shape of the response.


### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.get_entity_v2(id='3289b8c6-6a56-4c12-b3bc-45143354f2a7', slug='contact', fields=[
    '_id',
    '_title',
    'first_name',
    'account',
    '!account.*._files',
    '**._product',
], hydrate=False)

if res.entity_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Entity id                                                                                            |                                                                                                      |
| `slug`                                                                                               | *str*                                                                                                | :heavy_check_mark:                                                                                   | Entity Type                                                                                          | contact                                                                                              |
| `fields`                                                                                             | List[*str*]                                                                                          | :heavy_minus_sign:                                                                                   | List of entity fields to include in results                                                          | [<br/>"_id",<br/>"_title",<br/>"first_name",<br/>"account",<br/>"!account.*._files",<br/>"**._product"<br/>] |
| `hydrate`                                                                                            | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | When true, enables entity hydration to resolve nested $relation & $relation_ref references in-place. |                                                                                                      |


### Response

**[operations.GetEntityV2Response](../../models/operations/getentityv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
import dateutil.parser
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.PatchEntityRequest(
    entity=components.Entity(
        additional_properties={
            '_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
            '_org': '123',
            '_owners': '<value>',
            '_schema': 'contact',
            '_tags': '<value>',
            '_created_at': '2021-02-09T12:41:43.662Z',
            '_updated_at': '2021-02-09T12:41:43.662Z',
            '_acl': '<value>',
        },
        acl=components.EntityACL(
            delete=[
                'org:456',
            ],
            edit=[
                'org:456',
            ],
            view=[
                'org:456',
                'org:789',
            ],
        ),
        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
        org='123',
        owners=[
            components.EntityOwner(
                org_id='123',
                user_id='123',
            ),
        ],
        schema='contact',
        tags=[
            'example',
            'mock',
        ],
        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
    ),
    id='cd6dc474-9915-44f5-99d5-806e999b7231',
    slug='contact',
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.entities.patch_entity(req)

if res.entity_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchEntityRequest](../../models/operations/patchentityrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PatchEntityResponse](../../models/operations/patchentityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = components.EntitySearchParams(
    q='_schema:contact AND status:active',
    aggs=components.Aggs(),
    fields=[
        '_id',
        '_title',
        'first_name',
        'account',
        '!account.*._files',
        '**._product',
    ],
    sort='_created_at:desc',
)

res = s.entities.search_entities(req)

if res.entity_search_results is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.EntitySearchParams](../../models/components/entitysearchparams.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.SearchEntitiesResponse](../../models/operations/searchentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
import dateutil.parser
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpdateEntityRequest(
    id='2d5d17df-5520-4987-bd5a-6b1d12df7446',
    slug='contact',
    entity=components.Entity(
        additional_properties={
            '_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
            '_org': '123',
            '_owners': '<value>',
            '_schema': 'contact',
            '_tags': '<value>',
            '_created_at': '2021-02-09T12:41:43.662Z',
            '_updated_at': '2021-02-09T12:41:43.662Z',
            '_acl': '<value>',
        },
        acl=components.EntityACL(
            delete=[
                'org:456',
            ],
            edit=[
                'org:456',
            ],
            view=[
                'org:456',
                'org:789',
            ],
        ),
        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
        org='123',
        owners=[
            components.EntityOwner(
                org_id='123',
                user_id='123',
            ),
        ],
        schema='contact',
        tags=[
            'example',
            'mock',
        ],
        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
    ),
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.entities.update_entity(req)

if res.entity_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateEntityRequest](../../models/operations/updateentityrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateEntityResponse](../../models/operations/updateentityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpsertEntityRequest(
    slug='contact',
    activity_id='01F130Q52Q6MWSNS8N2AVXV4JN',
)

res = s.entities.upsert_entity(req)

if res.entity_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpsertEntityRequest](../../models/operations/upsertentityrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpsertEntityResponse](../../models/operations/upsertentityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## validate_entity

Validates an entity against the schema.

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.entities.validate_entity(slug='contact', entity=components.Entity(
    additional_properties={
        '_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
        '_org': '123',
        '_owners': '<value>',
        '_schema': 'contact',
        '_tags': '<value>',
        '_created_at': '2021-02-09T12:41:43.662Z',
        '_updated_at': '2021-02-09T12:41:43.662Z',
        '_acl': '<value>',
    },
    acl=components.EntityACL(
        delete=[
            'org:456',
        ],
        edit=[
            'org:456',
        ],
        view=[
            'org:456',
            'org:789',
        ],
    ),
    created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
    id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
    org='123',
    owners=[
        components.EntityOwner(
            org_id='123',
            user_id='123',
        ),
    ],
    schema='contact',
    tags=[
        'example',
        'mock',
    ],
    updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
))

if res.entity_validation_result_success is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                      | Example                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slug`                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                               | Entity Type                                                                                                                                                                                                                                                                                                                                                      | contact                                                                                                                                                                                                                                                                                                                                                          |
| `entity`                                                                                                                                                                                                                                                                                                                                                         | [Optional[components.Entity]](../../models/components/entity.md)                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                                                                                                                              | {<br/>"_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",<br/>"_org": "123",<br/>"_owners": [<br/>{<br/>"org_id": "123",<br/>"user_id": "123"<br/>}<br/>],<br/>"_schema": "contact",<br/>"_tags": [<br/>"example",<br/>"mock"<br/>],<br/>"_created_at": "2021-02-09T12:41:43.662Z",<br/>"_updated_at": "2021-02-09T12:41:43.662Z",<br/>"_acl": {<br/>"view": [<br/>"org:456",<br/>"org:789"<br/>],<br/>"edit": [<br/>"org:456"<br/>],<br/>"delete": [<br/>"org:456"<br/>]<br/>}<br/>} |


### Response

**[operations.ValidateEntityResponse](../../models/operations/validateentityresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.EntityValidationResultError | 422                                | application/json                   |
| errors.SDKError                    | 4x-5xx                             | */*                                |
