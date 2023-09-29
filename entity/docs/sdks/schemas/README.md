# Schemas
(*schemas*)

## Overview

Model Entities

### Available Operations

* [delete_schema](#delete_schema) - deleteSchema
* [get_schema](#get_schema) - getSchema
* [get_schema_versions](#get_schema_versions) - getSchemaVersions
* [list_schema_blueprints](#list_schema_blueprints) - listSchemaBlueprints
* [list_schemas](#list_schemas) - listSchemas
* [list_taxonomy_classifications_for_schema](#list_taxonomy_classifications_for_schema) - listTaxonomyClassificationsForSchema
* [put_schema](#put_schema) - putSchema

## delete_schema

Delete a schema, or a specific version of a schema

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteSchemaRequest(
    slug='contact',
)

res = s.schemas.delete_schema(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSchemaRequest](../../models/operations/deleteschemarequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSchemaResponse](../../models/operations/deleteschemaresponse.md)**


## get_schema

By default gets the latest version of the Schema and to get the specific version of schema pass the id.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetSchemaRequest(
    id='3bcef047-7721-42cd-8bca-92e24545d526',
    slug='contact',
)

res = s.schemas.get_schema(req)

if res.entity_schema_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSchemaRequest](../../models/operations/getschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSchemaResponse](../../models/operations/getschemaresponse.md)**


## get_schema_versions

Get all versions of this schema ordered by the latest versions including drafts.

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetSchemaVersionsRequest(
    drafts_from=8135.81,
    drafts_size=8621.33,
    slug='contact',
    versions_from=8101.78,
    versions_size=8257.35,
)

res = s.schemas.get_schema_versions(req)

if res.get_schema_versions_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetSchemaVersionsRequest](../../models/operations/getschemaversionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetSchemaVersionsResponse](../../models/operations/getschemaversionsresponse.md)**


## list_schema_blueprints

List canonical versions of all available schemas

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.schemas.list_schema_blueprints()

if res.list_schema_blueprints_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListSchemaBlueprintsResponse](../../models/operations/listschemablueprintsresponse.md)**


## list_schemas

Get the latest versions of all schemas

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ListSchemasRequest(
    unpublished=False,
)

res = s.schemas.list_schemas(req)

if res.list_schemas_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListSchemasRequest](../../models/operations/listschemasrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListSchemasResponse](../../models/operations/listschemasresponse.md)**


## list_taxonomy_classifications_for_schema

List taxonomy classifications for a given schema

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ListTaxonomyClassificationsForSchemaRequest(
    query='Gasoline Torrance tesla',
    size=8668.67,
    slug='contact',
    taxonomy_slug='purpose',
)

res = s.schemas.list_taxonomy_classifications_for_schema(req)

if res.list_taxonomy_classifications_for_schema_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.ListTaxonomyClassificationsForSchemaRequest](../../models/operations/listtaxonomyclassificationsforschemarequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.ListTaxonomyClassificationsForSchemaResponse](../../models/operations/listtaxonomyclassificationsforschemaresponse.md)**


## put_schema

Create or update a schema with a new version

### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.PutSchemaRequest(
    entity_schema=shared.EntitySchema(
        attributes=[
            [],
        ],
        blueprint='a93c7b74-037c-43b9-94a9-6166aa0e2336',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    '535d6bf8-fcc1-4de0-b32d-65715210cf50',
                ],
                attributes=[
                    [],
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "modi": 'Home',
                    },
                ],
            ),
        ],
        dialog_config={
            "eveniet": 'Strategist',
        },
        draft=False,
        enable_setting=[
            '360_features',
        ],
        explicit_search_mappings={
            "vel": shared.SearchMappings(
                fields_={
                    "distinctio": 'warmly',
                },
                index=False,
                type=shared.SearchMappingsType.TEXT,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '0dd287b6-15b3-4e0e-a8c6-d1668543e4eb',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='<ID>',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='Wooden',
                    key='<key>',
                ),
                label='deposit Pakistan XSS',
                order=834474,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "aut": 'protocol',
        },
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            create_view=[],
            edit_view=[],
            list_item=shared.EntitySchemaUIConfigListItem(
                summary_attributes=[
                    [],
                ],
            ),
            sharing=shared.EntitySchemaUIConfigSharing(
                show_sharing_button=True,
            ),
            single_view=[],
            table_view=[],
        ),
        version=784166,
    ),
    draft=False,
    slug='contact',
)

res = s.schemas.put_schema(req)

if res.entity_schema_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PutSchemaRequest](../../models/operations/putschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PutSchemaResponse](../../models/operations/putschemaresponse.md)**

