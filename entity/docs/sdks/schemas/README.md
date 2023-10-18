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
    pass
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
    slug='contact',
)

res = s.schemas.get_schema(req)

if res.entity_schema_item is not None:
    # handle response
    pass
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

req = operations.ListSchemasRequest()

res = s.schemas.list_schemas(req)

if res.list_schemas_200_application_json_object is not None:
    # handle response
    pass
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
    slug='contact',
    taxonomy_slug='purpose',
)

res = s.schemas.list_taxonomy_classifications_for_schema(req)

if res.list_taxonomy_classifications_for_schema_200_application_json_object is not None:
    # handle response
    pass
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
            shared.TextAttribute(
                purpose=[
                    'a93c7b74-037c-43b9-94a9-6166aa0e2336',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='channels',
                layout='full_width',
                name='exploit',
                order=0,
                setting_flag='MY_SETTING',
            ),
            shared.TextAttribute(
                purpose=[
                    '6bf8fcc1-de0f-432d-a571-5210cf504680',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='till',
                layout='full_width',
                name='grill',
                order=0,
                setting_flag='MY_SETTING',
            ),
            shared.TextAttribute(
                purpose=[
                    'fd6bef20-dd28-47b6-95b3-e0e28c6d1668',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='discrete',
                layout='full_width',
                name='Unbranded',
                order=0,
                setting_flag='MY_SETTING',
            ),
            shared.TextAttribute(
                purpose=[
                    '4eb242b7-20a7-4fd0-81cb-030766bc3807',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='radical',
                layout='full_width',
                name='compressing',
                order=0,
                setting_flag='MY_SETTING',
            ),
            shared.TextAttribute(
                purpose=[
                    '37b1710c-2601-4905-a25f-bb37949e5c67',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='firmware',
                layout='full_width',
                name='IP',
                order=0,
                setting_flag='MY_SETTING',
            ),
            shared.TextAttribute(
                purpose=[
                    '47c7479d-9c56-40ea-b969-366d774fa49a',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='voluptatem',
                layout='full_width',
                name='withdrawal',
                order=0,
                setting_flag='MY_SETTING',
            ),
            shared.TextAttribute(
                purpose=[
                    '19da9b26-82a9-4ba9-8c09-53674af53c32',
                ],
                constraints=shared.TextAttributeConstraints(),
                feature_flag='FF_MY_FEATURE_FLAG',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_tooltip_placement='top',
                ),
                label='Corporate',
                layout='full_width',
                name='synthesize',
                order=0,
                setting_flag='MY_SETTING',
            ),
        ],
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    '3faa88fa-b246-43c7-80e7-5fefd4fb709f',
                ],
                attributes=[
                    shared.StatusAttribute(
                        purpose=[
                            '3acc8e6b-9335-4e75-97f7-7f7639161823',
                        ],
                        constraints=shared.StatusAttributeConstraints(),
                        feature_flag='FF_MY_FEATURE_FLAG',
                        info_helpers=shared.StatusAttributeInfoHelpers(
                            hint_tooltip_placement='top',
                        ),
                        label='analyzer',
                        layout='full_width',
                        name='Classical',
                        options=[
                            'Lamborghini',
                        ],
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
                            "newton": 'hacking',
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
            "North": 'Kia',
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
                fields_={
                    "HDD": 'engage',
                },
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    'e87e0545-1ea9-476b-baa4-556cbb2f4955',
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                id='<ID>',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(),
                label='Orchestrator',
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    'f0c06824-2f55-46b2-8c16-cff63699539a',
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                id='<ID>',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(),
                label='Folk',
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings=shared.EntitySchemaLayoutSettings(
            additional_properties={
                "male": 'Health',
            },
        ),
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            shared.EntityDefaultCreate(
                search_params={
                    "Avon": 'marvelous',
                },
                table_menu_options=shared.EntityDefaultCreateTableMenuOptions(),
            ),
            shared.EntityViewDisabled(),
            list_item=shared.EntitySchemaUIConfigListItem(
                summary_attributes=[
                    'email',
                ],
            ),
            sharing=shared.EntitySchemaUIConfigSharing(
                show_sharing_button=True,
            ),
            shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
            ),
            shared.EntityDefaultTable(
                dropdown_items=[
                    shared.EntityDefaultTableDropdownItems1(
                        entity='contact',
                        feature_flag='FF_MY_FEATURE_FLAG',
                    ),
                ],
                navbar_actions=[
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='invoice',
                                params=shared.EntityDefaultTableNavbarActionsOptionsParams(),
                            ),
                        ],
                        type='XML',
                    ),
                ],
                row_actions=[
                    'Mouse',
                ],
            ),
        ),
    ),
    slug='contact',
)

res = s.schemas.put_schema(req)

if res.entity_schema_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PutSchemaRequest](../../models/operations/putschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PutSchemaResponse](../../models/operations/putschemaresponse.md)**

