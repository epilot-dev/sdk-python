# Schemas

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
    id='c556146c-3e25-40fb-808c-42e141aac366',
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
    drafts_from=7521.35,
    drafts_size=5573.69,
    slug='contact',
    versions_from=8296.03,
    versions_size=8605.52,
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
    query='voluptas',
    size=7270.44,
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
            shared.DateAttribute(
                purpose=[
                    '44290747-4778-4a7b-9466-d28c10ab3cdc',
                ],
                constraints=shared.DateAttributeConstraints(),
                default_value='fuga',
                deprecated=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='eius',
                hidden=False,
                hide_label=False,
                icon='eos',
                info_helpers=shared.DateAttributeInfoHelpers(
                    hint_custom_component='voluptas',
                    hint_text='ab',
                    hint_text_key='cupiditate',
                    hint_tooltip_placement='top',
                ),
                label='consequatur',
                layout='full_width',
                name='Henrietta Hilpert',
                order=0,
                placeholder='quo',
                preview_value_formatter='esse',
                protected=False,
                readonly=False,
                render_condition='recusandae',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                sortable=False,
                type=shared.DateAttributeType.DATE,
                value_formatter='distinctio',
            ),
        ],
        blueprint='c7178e47-96f2-4a70-8688-282aa482562f',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    '222e9817-ee17-4cbe-a1e6-b7b95bc0ab3c',
                ],
                attributes=[
                    shared.BooleanAttribute(
                        purpose=[
                            '0c4f3789-fd87-41f9-9dd2-efd121aa6f1e',
                        ],
                        constraints=shared.BooleanAttributeConstraints(),
                        default_value='vel',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='in',
                        hidden=False,
                        hide_label=False,
                        icon='eius',
                        info_helpers=shared.BooleanAttributeInfoHelpers(
                            hint_custom_component='libero',
                            hint_text='illum',
                            hint_text_key='soluta',
                            hint_tooltip_placement='top',
                        ),
                        label='accusantium',
                        layout='full_width',
                        name='Miranda Carter',
                        order=0,
                        placeholder='ullam',
                        preview_value_formatter='nisi',
                        protected=False,
                        readonly=False,
                        render_condition='aut',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        sortable=False,
                        type=shared.BooleanAttributeType.BOOLEAN,
                        value_formatter='voluptatum',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "qui": 'quibusdam',
                    },
                ],
            ),
        ],
        dialog_config={
            "ex": 'deleniti',
        },
        draft=False,
        enable_setting=[
            '360_features',
        ],
        explicit_search_mappings={
            "itaque": shared.SearchMappings(
                fields_={
                    "dolorum": 'architecto',
                },
                index=False,
                type=shared.SearchMappingsType.FLOAT,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    'f1d17051-339d-4080-86a1-840394c26071',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='f93f5f06-42da-4c7a-b515-cc413aa63aae',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='totam',
                    key='fugiat',
                ),
                label='vel',
                order=497678,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "quos": 'vel',
        },
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            create_view=shared.EntityDefaultCreate(
                search_params={
                    "possimus": 'facilis',
                },
                table_menu_options=shared.EntityDefaultCreateTableMenuOptions(
                    icon='cum',
                    label='commodi',
                ),
                view_type=shared.EntityDefaultCreateViewType.DEFAULT,
            ),
            edit_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewType.REDIRECT,
            ),
            list_item=shared.EntitySchemaUIConfigListItem(
                summary_attributes=[
                    shared.SummaryAttribute(
                        feature_flag='reiciendis',
                        label='assumenda',
                        render_condition='nemo',
                        setting_flag='recusandae',
                        show_as_tag=False,
                        tag_color='aliquid',
                        value='aperiam',
                    ),
                ],
            ),
            sharing=shared.EntitySchemaUIConfigSharing(
                show_sharing_button=True,
            ),
            single_view=shared.EntityViewDisabled(
                view_type=shared.EntityViewDisabledViewType.DISABLED,
            ),
            table_view=shared.EntityDefaultTable(
                classic_view='in',
                dropdown_items=[
                    shared.EntityDefaultTableDropdownItems1(
                        entity='contact',
                        feature_flag='FF_MY_FEATURE_FLAG',
                        legacy=False,
                        type=shared.EntityDefaultTableDropdownItems1Type.ENTITY,
                    ),
                ],
                enable_thumbnails=False,
                navbar_actions=[
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='earum',
                                params=shared.EntityDefaultTableNavbarActionsOptionsParams(),
                            ),
                        ],
                        type='facere',
                    ),
                ],
                row_actions=[
                    'numquam',
                ],
                view_type=shared.EntityDefaultTableViewType.DEFAULT,
            ),
        ),
        version=985492,
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

