# epilot-entity

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=entity
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

if res.activity_item is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [activity](docs/sdks/activity/README.md)

* [attach_activity](docs/sdks/activity/README.md#attach_activity) - attachActivity
* [create_activity](docs/sdks/activity/README.md#create_activity) - createActivity
* [get_activity](docs/sdks/activity/README.md#get_activity) - getActivity
* [get_entity_activity_feed](docs/sdks/activity/README.md#get_entity_activity_feed) - getEntityActivityFeed

### [taxonomy](docs/sdks/taxonomy/README.md)

* [get_taxonomy](docs/sdks/taxonomy/README.md#get_taxonomy) - getTaxonomy
* [list_taxonomies](docs/sdks/taxonomy/README.md#list_taxonomies) - listTaxonomies
* [taxonomies_classifications_search](docs/sdks/taxonomy/README.md#taxonomies_classifications_search) - taxonomiesClassificationsSearch
* [taxonomy_autocomplete](docs/sdks/taxonomy/README.md#taxonomy_autocomplete) - taxonomyAutocomplete
* [update_classifications_for_taxonomy](docs/sdks/taxonomy/README.md#update_classifications_for_taxonomy) - updateClassificationsForTaxonomy

### [schemas](docs/sdks/schemas/README.md)

* [delete_schema](docs/sdks/schemas/README.md#delete_schema) - deleteSchema
* [get_schema](docs/sdks/schemas/README.md#get_schema) - getSchema
* [get_schema_versions](docs/sdks/schemas/README.md#get_schema_versions) - getSchemaVersions
* [list_schema_blueprints](docs/sdks/schemas/README.md#list_schema_blueprints) - listSchemaBlueprints
* [list_schemas](docs/sdks/schemas/README.md#list_schemas) - listSchemas
* [list_taxonomy_classifications_for_schema](docs/sdks/schemas/README.md#list_taxonomy_classifications_for_schema) - listTaxonomyClassificationsForSchema
* [put_schema](docs/sdks/schemas/README.md#put_schema) - putSchema

### [saved_views](docs/sdks/savedviews/README.md)

* [create_saved_view](docs/sdks/savedviews/README.md#create_saved_view) - createSavedView
* [delete_saved_view](docs/sdks/savedviews/README.md#delete_saved_view) - deleteSavedView
* [get_saved_view](docs/sdks/savedviews/README.md#get_saved_view) - getSavedView
* [list_favorite_views_for_user](docs/sdks/savedviews/README.md#list_favorite_views_for_user) - listFavoriteViewsForUser
* [list_saved_views](docs/sdks/savedviews/README.md#list_saved_views) - listSavedViews
* [update_saved_view](docs/sdks/savedviews/README.md#update_saved_view) - updateSavedView

### [entities](docs/sdks/entities/README.md)

* [autocomplete](docs/sdks/entities/README.md#autocomplete) - autocomplete
* [create_entity](docs/sdks/entities/README.md#create_entity) - createEntity
* [delete_entity](docs/sdks/entities/README.md#delete_entity) - deleteEntity
* [get_entity](docs/sdks/entities/README.md#get_entity) - getEntity
* [patch_entity](docs/sdks/entities/README.md#patch_entity) - patchEntity
* [search_entities](docs/sdks/entities/README.md#search_entities) - searchEntities
* [update_entity](docs/sdks/entities/README.md#update_entity) - updateEntity
* [upsert_entity](docs/sdks/entities/README.md#upsert_entity) - upsertEntity

### [relations](docs/sdks/relations/README.md)

* [add_relations](docs/sdks/relations/README.md#add_relations) - addRelations
* [delete_relation](docs/sdks/relations/README.md#delete_relation) - deleteRelation
* [get_related_entities_count](docs/sdks/relations/README.md#get_related_entities_count) - getRelatedEntitiesCount
* [get_relations](docs/sdks/relations/README.md#get_relations) - getRelations
* [get_relations_v2](docs/sdks/relations/README.md#get_relations_v2) - getRelationsV2
* [get_relations_v3](docs/sdks/relations/README.md#get_relations_v3) - getRelationsV3
* [update_relation](docs/sdks/relations/README.md#update_relation) - updateRelation

### [export](docs/sdks/export/README.md)

* [export_entities](docs/sdks/export/README.md#export_entities) - exportEntities

### [entity_import](docs/sdks/entityimport/README.md)

* [import_entities](docs/sdks/entityimport/README.md#import_entities) - Import Entities
<!-- End SDK Available Operations -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = None
try:
    res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

except (errors.SDKError) as e:
    print(e) # handle exception


if res.activity_item is not None:
    # handle response
    pass
```

<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://entity.sls.epilot.io` | None |

#### Example

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    server_idx=0,
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

if res.activity_item is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    server_url="https://entity.sls.epilot.io",
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

if res.activity_item is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |
| `epilot_org`  | apiKey        | API key       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.activity.attach_activity(id='01F130Q52Q6MWSNS8N2AVXV4JN', entities=[
    'ee1dee63-2954-4671-8246-751c43fec091',
])

if res.activity_item is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
