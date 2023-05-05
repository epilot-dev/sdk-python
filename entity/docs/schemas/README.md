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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteSchemaRequest(
    slug='contact',
)

res = s.schemas.delete_schema(req)

if res.status_code == 200:
    # handle response
```

## get_schema

By default gets the latest version of the Schema and to get the specific version of schema pass the id.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetSchemaRequest(
    id='4f157560-82d6-48ea-99f1-d17051339d08',
    slug='contact',
)

res = s.schemas.get_schema(req)

if res.entity_schema_item is not None:
    # handle response
```

## get_schema_versions

Get all versions of this schema ordered by the latest versions including drafts.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetSchemaVersionsRequest(
    drafts_from=156.06,
    drafts_size=5130.75,
    slug='contact',
    versions_from=4287.96,
    versions_size=6498.32,
)

res = s.schemas.get_schema_versions(req)

if res.get_schema_versions_200_application_json_object is not None:
    # handle response
```

## list_schema_blueprints

List canonical versions of all available schemas

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.schemas.list_schema_blueprints()

if res.list_schema_blueprints_200_application_json_object is not None:
    # handle response
```

## list_schemas

Get the latest versions of all schemas

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListSchemasRequest(
    unpublished=False,
)

res = s.schemas.list_schemas(req)

if res.list_schemas_200_application_json_object is not None:
    # handle response
```

## list_taxonomy_classifications_for_schema

List taxonomy classifications for a given schema

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListTaxonomyClassificationsForSchemaRequest(
    query='ab',
    size=5445.91,
    slug='contact',
    taxonomy_slug='purpose',
)

res = s.schemas.list_taxonomy_classifications_for_schema(req)

if res.list_taxonomy_classifications_for_schema_200_application_json_object is not None:
    # handle response
```

## put_schema

Create or update a schema with a new version

### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.PutSchemaRequest(
    entity_schema=shared.EntitySchema(
        attributes=[
            shared.TextAttribute(
                purpose=[
                    '94c26071-f93f-45f0-a42d-ac7af515cc41',
                ],
                constraints={
                    "fuga": 'id',
                },
                default_value='suscipit',
                deprecated=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='velit',
                hidden=False,
                hide_label=False,
                icon='culpa',
                info_helpers=shared.TextAttributeInfoHelpers(
                    hint_custom_component='est',
                    hint_text='recusandae',
                    hint_text_key='totam',
                    hint_tooltip_placement='top',
                ),
                label='fugiat',
                layout='full_width',
                multiline=False,
                name='Dora Luettgen',
                order=822560,
                placeholder='facilis',
                preview_value_formatter='cum',
                protected=False,
                readonly=False,
                render_condition='commodi',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.TextAttributeTypeEnum.STRING,
                value_formatter='in',
            ),
            shared.RelationAttribute(
                purpose=[
                    'd5e60b37-5ed4-4f6f-bee4-1f33317fe35b',
                    '60eb1ea4-2655-45ba-bc28-744ed53b88f3',
                    'a8d8f5c0-b2f2-4fb7-b194-a276b26916fe',
                    '1f08f429-4e36-498f-847f-603e8b445e80',
                ],
                actions=[
                    shared.RelationAttributeActions(
                        action_type=shared.RelationAttributeActionsActionTypeEnum.CREATE_NEW,
                        default=False,
                        feature_flag='veniam',
                        label='minima',
                        new_entity_item={
                            "reiciendis": 'nulla',
                            "magni": 'aperiam',
                            "saepe": 'numquam',
                            "veniam": 'in',
                        },
                        setting_flag='officiis',
                    ),
                    shared.RelationAttributeActions(
                        action_type=shared.RelationAttributeActionsActionTypeEnum.ADD_EXISTING,
                        default=False,
                        feature_flag='laudantium',
                        label='exercitationem',
                        new_entity_item={
                            "cum": 'laboriosam',
                            "dolorum": 'voluptatum',
                            "error": 'hic',
                        },
                        setting_flag='expedita',
                    ),
                    shared.RelationAttributeActions(
                        action_type=shared.RelationAttributeActionsActionTypeEnum.CREATE_FROM_EXISTING,
                        default=False,
                        feature_flag='neque',
                        label='dolorum',
                        new_entity_item={
                            "officia": 'dolorum',
                            "corrupti": 'accusamus',
                        },
                        setting_flag='tempora',
                    ),
                    shared.RelationAttributeActions(
                        action_type=shared.RelationAttributeActionsActionTypeEnum.CREATE_NEW,
                        default=False,
                        feature_flag='fugit',
                        label='ut',
                        new_entity_item={
                            "voluptatem": 'culpa',
                            "expedita": 'magnam',
                            "consequatur": 'esse',
                            "ipsam": 'sit',
                        },
                        setting_flag='voluptatum',
                    ),
                ],
                add_button_label='quas',
                allowed_schemas=[
                    'contact',
                    'contact',
                    'contact',
                    'contact',
                ],
                constraints={
                    "et": 'blanditiis',
                    "ex": 'sed',
                },
                default_value='sit',
                deprecated=False,
                details_view_mode_enabled=False,
                drawer_size=shared.RelationAttributeDrawerSizeEnum.MEDIUM,
                edit_mode=shared.RelationAttributeEditModeEnum.LIST_VIEW,
                enable_relation_picker=False,
                enable_relation_tags=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='nostrum',
                has_primary=False,
                hidden=False,
                hide_label=False,
                icon='saepe',
                info_helpers=shared.RelationAttributeInfoHelpers(
                    hint_custom_component='error',
                    hint_text='consequatur',
                    hint_text_key='incidunt',
                    hint_tooltip_placement='top',
                ),
                label='reiciendis',
                layout='full_width',
                name='Ms. Opal Buckridge',
                order=695270,
                placeholder='atque',
                preview_value_formatter='laborum',
                protected=False,
                readonly=False,
                relation_affinity_mode=shared.RelationAttributeRelationAffinityModeEnum.STRONG,
                relation_type=shared.RelationAttributeRelationTypeEnum.HAS_ONE,
                render_condition='laboriosam',
                required=False,
                reverse_attributes={
                    "amet": 'contact.account',
                },
                search_placeholder='deserunt',
                setting_flag='MY_SETTING',
                show_in_table=False,
                summary_fields=[
                    shared.SummaryField(
                        display_as='reiciendis',
                        field='provident',
                    ),
                    shared.SummaryField(
                        display_as='delectus',
                        field='voluptates',
                    ),
                ],
                type=shared.RelationAttributeTypeEnum.RELATION,
                value_formatter='perferendis',
            ),
        ],
        blueprint='ab7da8a5-0ce1-487f-86bc-173d689eee95',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    'f8d986e8-81ea-4d4f-8e10-12563f94e29e',
                    '973e922a-57a1-45be-be06-0807e2b6e3ab',
                ],
                attributes=[
                    shared.RepeatableAttribute(
                        purpose=[
                            '5f0597a6-0ff2-4a54-a31e-94764a3e865e',
                            '7956f925-1a5a-49da-a60f-f57bfaad4f9e',
                        ],
                        constraints={
                            "cumque": 'vitae',
                            "rerum": 'tempora',
                            "quis": 'inventore',
                            "fugit": 'cumque',
                        },
                        default_value='quae',
                        deprecated=False,
                        enable_relation_picker=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='perferendis',
                        has_primary=False,
                        hidden=False,
                        hide_label=False,
                        icon='velit',
                        info_helpers=shared.RepeatableAttributeInfoHelpers(
                            hint_custom_component='aspernatur',
                            hint_text='eum',
                            hint_text_key='eius',
                            hint_tooltip_placement='top',
                        ),
                        label='rem',
                        layout='full_width',
                        name='Edmund Daugherty',
                        order=117320,
                        placeholder='minima',
                        preview_value_formatter='beatae',
                        protected=False,
                        readonly=False,
                        relation_affinity_mode=shared.RepeatableAttributeRelationAffinityModeEnum.STRONG,
                        render_condition='provident',
                        repeatable=False,
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.RepeatableAttributeTypeEnum.DATE,
                        value_formatter='soluta',
                    ),
                    shared.InternalUserAttribute(
                        purpose=[
                            '0e9fe6c6-32ca-43ae-9011-7996312fde04',
                            '771778ff-61d0-4174-b636-0a15db6a6606',
                            '59a1adea-ab58-451d-ac64-5b08b61891ba',
                            'a0fe1ade-008e-46f8-85f3-50d8cdb5a341',
                        ],
                        constraints={
                            "veritatis": 'tempora',
                            "dolor": 'consequatur',
                            "architecto": 'sit',
                        },
                        default_value='modi',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='fugit',
                        hidden=False,
                        hide_label=False,
                        icon='ab',
                        info_helpers=shared.InternalUserAttributeInfoHelpers(
                            hint_custom_component='laudantium',
                            hint_text='quae',
                            hint_text_key='dolor',
                            hint_tooltip_placement='top',
                        ),
                        label='fugiat',
                        layout='full_width',
                        name='Kathryn Bednar',
                        order=773456,
                        placeholder='officiis',
                        preview_value_formatter='esse',
                        protected=False,
                        readonly=False,
                        render_condition='necessitatibus',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.InternalUserAttributeTypeEnum.INTERNAL_USER,
                        value_formatter='sed',
                    ),
                    shared.SequenceAttribute(
                        purpose=[
                            'b668451c-6c6e-4205-a16d-eab3fec9578a',
                        ],
                        constraints={
                            "numquam": 'nemo',
                            "quos": 'eius',
                        },
                        default_value='aspernatur',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='ducimus',
                        hidden=False,
                        hide_label=False,
                        icon='nesciunt',
                        info_helpers=shared.SequenceAttributeInfoHelpers(
                            hint_custom_component='fuga',
                            hint_text='laudantium',
                            hint_text_key='incidunt',
                            hint_tooltip_placement='top',
                        ),
                        label='quasi',
                        layout='full_width',
                        name='Clint Carroll',
                        order=233078,
                        placeholder='aperiam',
                        prefix='OR-',
                        preview_value_formatter='cupiditate',
                        protected=False,
                        readonly=False,
                        render_condition='reiciendis',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        start_number=746837,
                        type=shared.SequenceAttributeTypeEnum.SEQUENCE,
                        value_formatter='alias',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "occaecati": 'iste',
                    },
                    {
                        "inventore": 'fuga',
                    },
                    {
                        "voluptatibus": 'distinctio',
                        "omnis": 'delectus',
                        "minima": 'praesentium',
                        "maxime": 'magnam',
                    },
                ],
            ),
        ],
        dialog_config={
            "quos": 'commodi',
            "itaque": 'commodi',
            "totam": 'earum',
            "modi": 'nam',
        },
        draft=False,
        enable_setting=[
            '360_features',
            '360_features',
            '360_features',
            '360_features',
        ],
        explicit_search_mappings={
            "ipsam": shared.SearchMappings(
                fields_={
                    "alias": 'quasi',
                    "non": 'maiores',
                },
                index=False,
                type=shared.SearchMappingsTypeEnum.BOOLEAN,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    'a757a59e-cfef-466e-b1ca-a3383c2beb47',
                    '7373c8d7-2f64-4d1d-b1f2-c4310661e963',
                    '49e1cf9e-06e3-4a43-b000-ae6b6bc9b8f7',
                    '59eac55a-9741-4d31-9352-965bb8a72026',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='11435e13-9dbc-4225-9b1a-bda8c070e108',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='dolore',
                    key='eligendi',
                ),
                label='distinctio',
                order=32273,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '72d1ad87-9eeb-4966-9b85-efbd02bae0be',
                    '2d782259-e3ea-44b5-997f-92443da7ce52',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='b895c537-c645-44ef-b0b3-4896c3ca5acf',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='tempore',
                    key='vero',
                ),
                label='odit',
                order=997437,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '57075779-2917-47de-ac64-6ecb573409e3',
                    'eb1e5a2b-12eb-407f-916d-b99545fc95fa',
                    '88970e18-9dbb-430f-8b33-ea055b197cd4',
                    '4e2f52d8-2d35-413b-b6f4-8b656bcdb35f',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='f2e4b275-37a8-4cd9-a731-9c177d525f77',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='libero',
                    key='illo',
                ),
                label='ab',
                order=280114,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "saepe": 'tempore',
            "veniam": 'eos',
            "reiciendis": 'earum',
            "reprehenderit": 'praesentium',
        },
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            create_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewTypeEnum.REDIRECT,
            ),
            edit_view=shared.EntityViewDisabled(
                view_type=shared.EntityViewDisabledViewTypeEnum.DISABLED,
            ),
            list_item=shared.EntitySchemaUIConfigListItem(
                summary_attributes=[
                    shared.SummaryAttribute(
                        feature_flag='nihil',
                        label='deleniti',
                        render_condition='illo',
                        setting_flag='labore',
                        show_as_tag=False,
                        tag_color='assumenda',
                        value='aliquam',
                    ),
                    'email',
                    'email',
                    'email',
                ],
            ),
            sharing=shared.EntitySchemaUIConfigSharing(
                show_sharing_button=True,
            ),
            single_view=shared.EntityViewDisabled(
                view_type=shared.EntityViewDisabledViewTypeEnum.DISABLED,
            ),
            table_view=shared.EntityDefaultTable(
                classic_view='maxime',
                dropdown_items=[
                    shared.EntityDefaultTableDropdownItems2(
                        feature_flag='FF_MY_FEATURE_FLAG',
                        legacy=False,
                        title='Opportunities',
                        type=shared.EntityDefaultTableDropdownItems2TypeEnum.LINK,
                        uri='expedita',
                    ),
                ],
                enable_thumbnails=False,
                navbar_actions=[
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='repudiandae',
                                params={
                                    "dignissimos": 'corporis',
                                    "vero": 'similique',
                                    "repellendus": 'iure',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='dolorem',
                                params={
                                    "impedit": 'commodi',
                                    "aut": 'voluptatem',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='ad',
                                params={
                                    "amet": 'illum',
                                },
                            ),
                        ],
                        type='praesentium',
                    ),
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='cum',
                                params={
                                    "quasi": 'dicta',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='laudantium',
                                params={
                                    "earum": 'iusto',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='amet',
                                params={
                                    "dolorum": 'necessitatibus',
                                    "provident": 'repudiandae',
                                    "consequatur": 'nemo',
                                },
                            ),
                        ],
                        type='molestiae',
                    ),
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='facilis',
                                params={
                                    "aperiam": 'sint',
                                    "accusamus": 'eos',
                                    "totam": 'dicta',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='voluptatem',
                                params={
                                    "dolor": 'sunt',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='a',
                                params={
                                    "occaecati": 'atque',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='beatae',
                                params={
                                    "labore": 'minus',
                                    "esse": 'voluptatem',
                                    "perferendis": 'rerum',
                                    "ea": 'aperiam',
                                },
                            ),
                        ],
                        type='dignissimos',
                    ),
                ],
                row_actions=[
                    'velit',
                    'porro',
                    'provident',
                    'consectetur',
                ],
                view_type=shared.EntityDefaultTableViewTypeEnum.DEFAULT,
            ),
        ),
        version=753240,
    ),
    draft=False,
    slug='contact',
)

res = s.schemas.put_schema(req)

if res.entity_schema_item is not None:
    # handle response
```
