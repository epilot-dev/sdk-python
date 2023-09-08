# schemas

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
    id='f7c70a45-626d-4436-813f-16d9f5fce6c5',
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
    drafts_from=3331.45,
    drafts_size=3994.99,
    slug='contact',
    versions_from=811.01,
    versions_size=3018.31,
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
    query='ea',
    size=7752.2,
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
            shared.MultiSelectAttribute(
                purpose=[
                    'e250fb00-8c42-4e14-9aac-366c8dd6b144',
                ],
                allow_any=False,
                allow_extra_options=False,
                constraints=shared.MultiSelectAttributeConstraints(),
                default_value='explicabo',
                deprecated=False,
                disable_case_sensitive=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='provident',
                hidden=False,
                hide_label=False,
                icon='ipsa',
                info_helpers=shared.MultiSelectAttributeInfoHelpers(
                    hint_custom_component='molestiae',
                    hint_text='magnam',
                    hint_text_key='odio',
                    hint_tooltip_placement='top',
                ),
                label='eius',
                layout='full_width',
                name='Tamara Leffler',
                options=[
                    shared.MultiSelectAttributeOptions2(
                        title='Dr.',
                        value='ut',
                    ),
                ],
                order=0,
                placeholder='eum',
                preview_value_formatter='suscipit',
                protected=False,
                readonly=False,
                render_condition='assumenda',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.MultiSelectAttributeType.MULTISELECT,
                value_formatter='praesentium',
            ),
        ],
        blueprint='c10ab3cd-ca42-4519-84e5-23c7e0bc7178',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    'e4796f2a-70c6-4882-82aa-482562f222e9',
                ],
                attributes=[
                    shared.TagsAttribute(
                        purpose=[
                            '17ee17cb-e61e-46b7-b95b-c0ab3c20c4f3',
                        ],
                        constraints=shared.TagsAttributeConstraints(),
                        default_value='esse',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='blanditiis',
                        hidden=False,
                        hide_label=False,
                        icon='provident',
                        info_helpers=shared.TagsAttributeInfoHelpers(
                            hint_custom_component='a',
                            hint_text='nulla',
                            hint_text_key='quas',
                            hint_tooltip_placement='top',
                        ),
                        label='esse',
                        layout='full_width',
                        name='Lorene Mueller',
                        options=[
                            'possimus',
                        ],
                        order=0,
                        placeholder='quia',
                        preview_value_formatter='eveniet',
                        protected=False,
                        readonly=False,
                        render_condition='asperiores',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        suggestions=[
                            'facere',
                        ],
                        type=shared.TagsAttributeType.TAGS,
                        value_formatter='veritatis',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "consequuntur": 'quasi',
                    },
                ],
            ),
        ],
        dialog_config={
            "similique": 'culpa',
        },
        draft=False,
        enable_setting=[
            '360_features',
        ],
        explicit_search_mappings={
            "aliquid": shared.SearchMappings(
                fields_={
                    "tenetur": 'quae',
                },
                index=False,
                type=shared.SearchMappingsType.NESTED,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '674bdb04-f157-4560-82d6-8ea19f1d1705',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='1339d080-86a1-4840-b94c-26071f93f5f0',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='ea',
                    key='quaerat',
                ),
                label='consequuntur',
                order=831520,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "officia": 'maxime',
        },
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            create_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewType.REDIRECT,
            ),
            edit_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewType.REDIRECT,
            ),
            list_item=shared.EntitySchemaUIConfigListItem(
                summary_attributes=[
                    'email',
                ],
            ),
            sharing=shared.EntitySchemaUIConfigSharing(
                show_sharing_button=True,
            ),
            single_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewType.REDIRECT,
            ),
            table_view=shared.EntityDefaultTable(
                classic_view='quaerat',
                dropdown_items=[
                    shared.EntityDefaultTableDropdownItems2(
                        feature_flag='FF_MY_FEATURE_FLAG',
                        legacy=False,
                        title='Opportunities',
                        type=shared.EntityDefaultTableDropdownItems2Type.LINK,
                        uri='quod',
                    ),
                ],
                enable_thumbnails=False,
                navbar_actions=[
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='labore',
                                params=shared.EntityDefaultTableNavbarActionsOptionsParams(),
                            ),
                        ],
                        type='ab',
                    ),
                ],
                row_actions=[
                    'adipisci',
                ],
                view_type=shared.EntityDefaultTableViewType.DEFAULT,
            ),
        ),
        version=683573,
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

