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


res = s.schemas.delete_schema(slug='contact')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `slug`             | *str*              | :heavy_check_mark: | Entity Type        | contact            |


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


res = s.schemas.get_schema(slug='contact', id='3bcef047-7721-42cd-8bca-92e24545d526')

if res.entity_schema_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `slug`             | *str*              | :heavy_check_mark: | Entity Type        | contact            |
| `id`               | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |


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
    slug='contact',
)

res = s.schemas.get_schema_versions(req)

if res.get_schema_versions_200_application_json_object is not None:
    # handle response
    pass
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
    pass
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


res = s.schemas.list_schemas(unpublished=False)

if res.list_schemas_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `unpublished`                    | *Optional[bool]*                 | :heavy_minus_sign:               | Return unpublished draft schemas |


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


res = s.schemas.list_taxonomy_classifications_for_schema(slug='contact', taxonomy_slug='string', query='string', size=8152.22)

if res.list_taxonomy_classifications_for_schema_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `slug`             | *str*              | :heavy_check_mark: | Entity Type        | contact            |
| `taxonomy_slug`    | *str*              | :heavy_check_mark: | Taxonomy slug      |                    |
| `query`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |                    |
| `size`             | *Optional[float]*  | :heavy_minus_sign: | N/A                |                    |


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


res = s.schemas.put_schema(slug='contact', entity_schema=shared.EntitySchema(
    attributes=[
        shared.TextAttribute(
            purpose=[
                'a93c7b74-037c-43b9-94a9-6166aa0e2336',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        shared.TextAttribute(
            purpose=[
                '535d6bf8-fcc1-4de0-b32d-65715210cf50',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        shared.TextAttribute(
            purpose=[
                '4680eaf6-fd6b-4ef2-8dd2-87b615b3e0e2',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        shared.TextAttribute(
            purpose=[
                '8c6d1668-543e-44eb-a42b-720a7fd081cb',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        shared.TextAttribute(
            purpose=[
                '030766bc-3807-45c8-837b-1710c2601905',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        shared.TextAttribute(
            purpose=[
                'e25fbb37-949e-45c6-b657-647c7479d9c5',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        shared.TextAttribute(
            purpose=[
                '60ea7969-366d-4774-ba49-a55907519da9',
            ],
            constraints=shared.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=shared.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
    ],
    capabilities=[
        shared.EntityCapability(
            purpose=[
                'b2682a9b-a9cc-4095-b674-af53c32a28a3',
            ],
            attributes=[
                shared.PartnerOrganisationAttribute(
                    purpose=[
                        'aa88fab2-463c-4780-a75f-efd4fb709f43',
                    ],
                    constraints=shared.PartnerOrganisationAttributeConstraints(),
                    feature_flag='FF_MY_FEATURE_FLAG',
                    info_helpers=shared.PartnerOrganisationAttributeInfoHelpers(
                        hint_tooltip_placement='top',
                    ),
                    label='string',
                    layout='full_width',
                    name='string',
                    order=0,
                    setting_flag='MY_SETTING',
                ),
            ],
            feature_flag='FF_MY_FEATURE_FLAG',
            name='customer_messaging',
            setting_flag='MY_SETTING',
            title='Messaging',
            ui_hooks=[
                shared.EntityCapabilityUIHooks(
                    additional_properties={
                        "key": 'string',
                    },
                    component='PricingItems',
                    hook='EntityDetailsV2:Tab',
                    icon='email',
                    import_='@epilot360/notes',
                    order=10,
                    render_condition='_is_composite_price = "false"',
                    required_permission=shared.EntityCapabilityUIHooksRequiredPermission(
                        action='note:view',
                        resource='123',
                    ),
                    route='notes',
                    title='Notes',
                ),
            ],
        ),
    ],
    dialog_config={
        "key": 'string',
    },
    draft=False,
    enable_setting=[
        '3',
        '6',
        '0',
        '_',
        'f',
        'e',
        'a',
        't',
        'u',
        'r',
        'e',
        's',
    ],
    explicit_search_mappings={
        "image": shared.SearchMappings(
            fields={
                "key": 'string',
            },
        ),
    },
    feature_flag='FF_MY_FEATURE_FLAG',
    group_settings=[
        shared.EntitySchemaGroupSettings(
            purpose=[
                'acc8e6b9-335e-475d-bf77-f76391618236',
            ],
            feature_flag='FF_MY_FEATURE_FLAG',
            id='<ID>',
            info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(),
            label='string',
            render_condition='_is_composite_price = "false"',
            setting_flag='MY_SETTING',
        ),
        shared.EntitySchemaGroupSettings(
            purpose=[
                '09a0d8c5-8211-4d87-949e-87e05451ea97',
            ],
            feature_flag='FF_MY_FEATURE_FLAG',
            id='<ID>',
            info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(),
            label='string',
            render_condition='_is_composite_price = "false"',
            setting_flag='MY_SETTING',
        ),
    ],
    icon='person',
    layout_settings=shared.EntitySchemaLayoutSettings(
        additional_properties={
            "key": 'string',
        },
    ),
    name='Contact',
    plural='Contacts',
    published=False,
    slug='contact',
    title_template='{{first_name}} {{last_name}}',
    ui_config=shared.EntitySchemaUIConfig(
        shared.RedirectEntityView(
            route='/app/pricing-hub/product/:entityId',
        ),
        shared.EntityViewDisabled(),
        list_item=shared.EntitySchemaUIConfigListItem(
            quick_actions=[
                shared.EntityAction(
                    action='preview_file',
                    icon='visibility',
                    label='Preview File',
                    permission='entity:edit',
                ),
            ],
            summary_attributes=[
                shared.SummaryAttribute(
                    label='string',
                    value='string',
                ),
            ],
        ),
        sharing=shared.EntitySchemaUIConfigSharing(
            show_sharing_button=True,
        ),
        shared.RedirectEntityView(
            route='/app/pricing-hub/product/:entityId',
        ),
        shared.RedirectEntityView(
            route='/app/pricing-hub/product/:entityId',
        ),
    ),
), draft=False)

if res.entity_schema_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `slug`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Entity Type                                                          | contact                                                              |
| `entity_schema`                                                      | [Optional[shared.EntitySchema]](../../models/shared/entityschema.md) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `draft`                                                              | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |


### Response

**[operations.PutSchemaResponse](../../models/operations/putschemaresponse.md)**

