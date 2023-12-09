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
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_schema

By default gets the latest version of the Schema and to get the specific version of schema pass the id.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_schema_versions

Get all versions of this schema ordered by the latest versions including drafts.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)

req = operations.GetSchemaVersionsRequest(
    slug='contact',
)

res = s.schemas.get_schema_versions(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetSchemaVersionsRequest](../../models/operations/getschemaversionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetSchemaVersionsResponse](../../models/operations/getschemaversionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_schema_blueprints

List canonical versions of all available schemas

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.schemas.list_schema_blueprints()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.ListSchemaBlueprintsResponse](../../models/operations/listschemablueprintsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_schemas

Get the latest versions of all schemas

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.schemas.list_schemas(unpublished=False)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `unpublished`                    | *Optional[bool]*                 | :heavy_minus_sign:               | Return unpublished draft schemas |


### Response

**[operations.ListSchemasResponse](../../models/operations/listschemasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_taxonomy_classifications_for_schema

List taxonomy classifications for a given schema

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.schemas.list_taxonomy_classifications_for_schema(slug='contact', taxonomy_slug='string', query='string', size=8152.22)

if res.object is not None:
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_schema

Create or update a schema with a new version

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="",
    ),
)


res = s.schemas.put_schema(slug='contact', entity_schema=components.EntitySchema(
    attributes=[
        components.TextAttribute(
            purpose=[
                'a93c7b74-037c-43b9-94a9-6166aa0e2336',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        components.TextAttribute(
            purpose=[
                '535d6bf8-fcc1-4de0-b32d-65715210cf50',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        components.TextAttribute(
            purpose=[
                '4680eaf6-fd6b-4ef2-8dd2-87b615b3e0e2',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        components.TextAttribute(
            purpose=[
                '8c6d1668-543e-44eb-a42b-720a7fd081cb',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        components.TextAttribute(
            purpose=[
                '030766bc-3807-45c8-837b-1710c2601905',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        components.TextAttribute(
            purpose=[
                'e25fbb37-949e-45c6-b657-647c7479d9c5',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
                hint_tooltip_placement='top',
            ),
            label='string',
            layout='full_width',
            name='string',
            order=0,
            setting_flag='MY_SETTING',
        ),
        components.TextAttribute(
            purpose=[
                '60ea7969-366d-4774-ba49-a55907519da9',
            ],
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            info_helpers=components.TextAttributeInfoHelpers(
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
        components.EntityCapability(
            purpose=[
                'b2682a9b-a9cc-4095-b674-af53c32a28a3',
            ],
            attributes=[
                components.PartnerOrganisationAttribute(
                    purpose=[
                        'aa88fab2-463c-4780-a75f-efd4fb709f43',
                    ],
                    constraints=components.PartnerOrganisationAttributeConstraints(),
                    feature_flag='FF_MY_FEATURE_FLAG',
                    info_helpers=components.PartnerOrganisationAttributeInfoHelpers(
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
                components.UIHooks(
                    additional_properties={
                        'key': 'string',
                    },
                    component='PricingItems',
                    hook='EntityDetailsV2:Tab',
                    icon='email',
                    import_='@epilot360/notes',
                    order=10,
                    render_condition='_is_composite_price = "false"',
                    required_permission=components.RequiredPermission(
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
        'key': 'string',
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
        'image': components.SearchMappings(
            fields={
                'key': 'string',
            },
        ),
    },
    feature_flag='FF_MY_FEATURE_FLAG',
    group_settings=[
        components.GroupSettings(
            purpose=[
                'acc8e6b9-335e-475d-bf77-f76391618236',
            ],
            feature_flag='FF_MY_FEATURE_FLAG',
            id='<ID>',
            info_tooltip_title=components.InfoTooltipTitle(),
            label='string',
            render_condition='_is_composite_price = "false"',
            setting_flag='MY_SETTING',
        ),
        components.GroupSettings(
            purpose=[
                '09a0d8c5-8211-4d87-949e-87e05451ea97',
            ],
            feature_flag='FF_MY_FEATURE_FLAG',
            id='<ID>',
            info_tooltip_title=components.InfoTooltipTitle(),
            label='string',
            render_condition='_is_composite_price = "false"',
            setting_flag='MY_SETTING',
        ),
    ],
    icon='person',
    layout_settings=components.LayoutSettings(
        additional_properties={
            'key': 'string',
        },
    ),
    name='Contact',
    plural='Contacts',
    published=False,
    slug='contact',
    title_template='{{first_name}} {{last_name}}',
    ui_config=components.UIConfig(
        create_view=components.RedirectEntityView(
        route='/app/pricing-hub/product/:entityId',
    ),
        edit_view=components.EntityViewDisabled(),
        list_item=components.ListItem(
            quick_actions=[
                components.EntityAction(
                    action='preview_file',
                    icon='visibility',
                    label='Preview File',
                    permission='entity:edit',
                ),
            ],
            summary_attributes=[
                components.SummaryAttribute(
                    label='string',
                    value='string',
                ),
            ],
        ),
        sharing=components.Sharing(
            show_sharing_button=True,
        ),
        single_view=components.RedirectEntityView(
        route='/app/pricing-hub/product/:entityId',
    ),
        table_view=components.RedirectEntityView(
        route='/app/pricing-hub/product/:entityId',
    ),
    ),
), draft=False)

if res.entity_schema_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `slug`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Entity Type                                                                  | contact                                                                      |
| `entity_schema`                                                              | [Optional[components.EntitySchema]](../../models/components/entityschema.md) | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |
| `draft`                                                                      | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |                                                                              |


### Response

**[operations.PutSchemaResponse](../../models/operations/putschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
