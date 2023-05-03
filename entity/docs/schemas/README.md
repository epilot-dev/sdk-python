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
    slug='contact',
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
    query='aut',
    size=5130.75,
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
            shared.ConsentAttribute(
                purpose=[
                    '840394c2-6071-4f93-b5f0-642dac7af515',
                ],
                constraints={
                    "quod": 'labore',
                    "ab": 'adipisci',
                    "fuga": 'id',
                    "suscipit": 'velit',
                },
                default_value='culpa',
                deprecated=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='est',
                hidden=False,
                hide_label=False,
                icon='recusandae',
                identifiers=[
                    'fugiat',
                    'vel',
                    'ducimus',
                ],
                info_helpers=shared.ConsentAttributeInfoHelpers(
                    hint_custom_component='quos',
                    hint_text='vel',
                    hint_text_key='labore',
                    hint_tooltip_placement='top',
                ),
                label='possimus',
                layout='full_width',
                name='Felipe Johns',
                order=968904,
                placeholder='assumenda',
                preview_value_formatter='nemo',
                protected=False,
                readonly=False,
                render_condition='recusandae',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                topic='aliquid',
                type=shared.ConsentAttributeTypeEnum.CONSENT,
                value_formatter='aperiam',
            ),
            shared.OrderedListAttribute(
                purpose=[
                    '75ed4f6f-bee4-41f3-b317-fe35b60eb1ea',
                ],
                constraints={
                    "aspernatur": 'voluptas',
                    "voluptas": 'voluptas',
                },
                default_value='minima',
                deprecated=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='nobis',
                hidden=False,
                hide_label=False,
                icon='dolorum',
                info_helpers=shared.OrderedListAttributeInfoHelpers(
                    hint_custom_component='adipisci',
                    hint_text='minus',
                    hint_text_key='dolores',
                    hint_tooltip_placement='top',
                ),
                label='blanditiis',
                layout='full_width',
                name='Valerie Haag',
                order=351870,
                placeholder='adipisci',
                preview_value_formatter='cum',
                protected=False,
                readonly=False,
                render_condition='blanditiis',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.OrderedListAttributeTypeEnum.ORDERED_LIST,
                value_formatter='quas',
            ),
        ],
        blueprint='f3a8d8f5-c0b2-4f2f-b7b1-94a276b26916',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    '1f08f429-4e36-498f-847f-603e8b445e80',
                    'ca55efd2-0e45-47e1-858b-6a89fbe3a5aa',
                    '8e4824d0-ab40-4750-88e5-1862065e904f',
                    '3b1194b8-abf6-403a-b9f9-dfe0ab7da8a5',
                ],
                attributes=[
                    shared.ComputedAttribute(
                        purpose=[
                            '187f86bc-173d-4689-aee9-526f8d986e88',
                            '1ead4f0e-1012-4563-b94e-29e973e922a5',
                            '7a15be3e-0608-407e-ab6e-3ab8845f0597',
                            'a60ff2a5-4a31-4e94-b64a-3e865e7956f9',
                        ],
                        constraints={
                            "ullam": 'quasi',
                        },
                        default_value='animi',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='nostrum',
                        hidden=False,
                        hide_label=False,
                        icon='mollitia',
                        info_helpers=shared.ComputedAttributeInfoHelpers(
                            hint_custom_component='provident',
                            hint_text='possimus',
                            hint_text_key='animi',
                            hint_tooltip_placement='top',
                        ),
                        label='ex',
                        layout='full_width',
                        name='Ruth Zulauf',
                        order=448143,
                        placeholder='nam',
                        preview_value_formatter='earum',
                        protected=False,
                        readonly=False,
                        render_condition='officia',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.ComputedAttributeTypeEnum.COMPUTED,
                        value_formatter='laborum',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "voluptatibus": 'molestias',
                        "officiis": 'sapiente',
                    },
                    {
                        "vitae": 'rerum',
                        "tempora": 'quis',
                        "inventore": 'fugit',
                        "cumque": 'quae',
                    },
                    {
                        "velit": 'aspernatur',
                    },
                    {
                        "eius": 'rem',
                        "at": 'impedit',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    'f615199e-bfd0-4e9f-a6c6-32ca3aed0117',
                ],
                attributes=[
                    shared.TagsAttribute(
                        purpose=[
                            '312fde04-7717-478f-b61d-017476360a15',
                            'db6a6606-59a1-4ade-aab5-851d6c645b08',
                        ],
                        constraints={
                            "aliquid": 'beatae',
                            "voluptatum": 'omnis',
                            "veritatis": 'rerum',
                        },
                        default_value='est',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='culpa',
                        hidden=False,
                        hide_label=False,
                        icon='voluptatem',
                        info_helpers=shared.TagsAttributeInfoHelpers(
                            hint_custom_component='sapiente',
                            hint_text='officiis',
                            hint_text_key='architecto',
                            hint_tooltip_placement='top',
                        ),
                        label='fuga',
                        layout='full_width',
                        name='Ms. Doyle Barrows',
                        options=[
                            'sapiente',
                            'rem',
                        ],
                        order=796320,
                        placeholder='nemo',
                        preview_value_formatter='asperiores',
                        protected=False,
                        readonly=False,
                        render_condition='ratione',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        suggestions=[
                            'perferendis',
                            'illum',
                        ],
                        type=shared.TagsAttributeTypeEnum.TAGS,
                        value_formatter='totam',
                    ),
                    shared.FileAttribute(
                        purpose=[
                            'b5a34181-4301-4042-9813-d5208ece7e25',
                            '3b668451-c6c6-4e20-9e16-deab3fec9578',
                            'a6458427-3a84-418d-9623-09fb0929921a',
                            'efb9f58c-4d86-4e68-a4be-056013f59da7',
                        ],
                        allowed_extensions=[
                            'csv',
                            'csv',
                        ],
                        constraints={
                            "est": 'quis',
                            "sint": 'accusamus',
                        },
                        default_access_control=shared.FileAttributeDefaultAccessControlEnum.PRIVATE,
                        default_value='hic',
                        deprecated=False,
                        display_images_landscaped=False,
                        enable_description=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='necessitatibus',
                        hidden=False,
                        hide_label=False,
                        icon='asperiores',
                        info_helpers=shared.FileAttributeInfoHelpers(
                            hint_custom_component='ex',
                            hint_text='voluptas',
                            hint_text_key='debitis',
                            hint_tooltip_placement='top',
                        ),
                        label='delectus',
                        layout='full_width',
                        multiple=False,
                        name='Alexandra Pfannerstill',
                        order=244889,
                        placeholder='atque',
                        preview_value_formatter='ipsum',
                        protected=False,
                        readonly=False,
                        render_condition='impedit',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.FileAttributeTypeEnum.IMAGE,
                        value_formatter='soluta',
                    ),
                    shared.AutomationAttribute(
                        purpose=[
                            '477373c8-d72f-464d-9db1-f2c4310661e9',
                            '6349e1cf-9e06-4e3a-8370-00ae6b6bc9b8',
                            'f759eac5-5a97-441d-b113-52965bb8a720',
                        ],
                        constraints={
                            "vel": 'quae',
                        },
                        default_value='quae',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='modi',
                        hidden=False,
                        hide_label=False,
                        icon='neque',
                        info_helpers=shared.AutomationAttributeInfoHelpers(
                            hint_custom_component='exercitationem',
                            hint_text='itaque',
                            hint_text_key='et',
                            hint_tooltip_placement='top',
                        ),
                        label='ipsum',
                        layout='full_width',
                        name='Orville Ratke',
                        order=159146,
                        placeholder='nostrum',
                        preview_value_formatter='omnis',
                        protected=False,
                        readonly=False,
                        render_condition='libero',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.AutomationAttributeTypeEnum.AUTOMATION,
                        value_formatter='dicta',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "fugiat": 'officia',
                        "quos": 'placeat',
                        "sit": 'iusto',
                    },
                    {
                        "voluptates": 'inventore',
                    },
                    {
                        "totam": 'dolore',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    'b0672d1a-d879-4eeb-9665-b85efbd02bae',
                    '0be2d782-259e-43ea-8b51-97f92443da7c',
                    'e52b895c-537c-4645-8efb-0b34896c3ca5',
                    'acfbe2fd-5707-4577-9291-77deac646ecb',
                ],
                attributes=[
                    shared.PaymentMethodRelationAttribute(
                        purpose=[
                            '409e3eb1-e5a2-4b12-ab07-f116db99545f',
                        ],
                        constraints={
                            "sint": 'enim',
                            "hic": 'animi',
                            "quas": 'totam',
                            "molestias": 'odio',
                        },
                        default_value='eaque',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='saepe',
                        has_primary=False,
                        hidden=False,
                        hide_label=False,
                        icon='architecto',
                        info_helpers=shared.PaymentMethodRelationAttributeInfoHelpers(
                            hint_custom_component='quos',
                            hint_text='iste',
                            hint_text_key='assumenda',
                            hint_tooltip_placement='top',
                        ),
                        label='tempore',
                        layout='full_width',
                        name='Lee Batz',
                        order=741238,
                        placeholder='ipsum',
                        preview_value_formatter='adipisci',
                        protected=False,
                        readonly=False,
                        render_condition='saepe',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.PaymentMethodRelationAttributeTypeEnum.RELATION_PAYMENT_METHOD,
                        value_formatter='deserunt',
                    ),
                    shared.LinkAttribute(
                        purpose=[
                            '5b197cd4-4e2f-452d-82d3-513bb6f48b65',
                            '6bcdb35f-f2e4-4b27-937a-8cd9e7319c17',
                        ],
                        constraints={
                            "fugiat": 'ad',
                            "aspernatur": 'enim',
                        },
                        default_value='delectus',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='iusto',
                        hidden=False,
                        hide_label=False,
                        icon='dignissimos',
                        info_helpers=shared.LinkAttributeInfoHelpers(
                            hint_custom_component='libero',
                            hint_text='illo',
                            hint_text_key='ab',
                            hint_tooltip_placement='top',
                        ),
                        label='incidunt',
                        layout='full_width',
                        name='Elias Rice',
                        order=970079,
                        placeholder='earum',
                        preview_value_formatter='reprehenderit',
                        protected=False,
                        readonly=False,
                        render_condition='praesentium',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.LinkAttributeTypeEnum.LINK,
                        value_formatter='nemo',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "sequi": 'nihil',
                        "deleniti": 'illo',
                        "labore": 'assumenda',
                        "aliquam": 'quisquam',
                    },
                    {
                        "laudantium": 'repudiandae',
                        "consequatur": 'maxime',
                        "aspernatur": 'nam',
                    },
                    {
                        "quas": 'provident',
                        "repudiandae": 'rerum',
                        "dignissimos": 'corporis',
                    },
                    {
                        "similique": 'repellendus',
                        "iure": 'dolorem',
                        "commodi": 'impedit',
                        "commodi": 'aut',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '503d8bb3-1180-4f73-9ae9-e057eb809e28',
                ],
                attributes=[
                    shared.TextAttribute(
                        purpose=[
                            '31f3981d-4c70-40b6-87f3-c93c73b9da3f',
                        ],
                        constraints={
                            "quo": 'itaque',
                        },
                        default_value='illum',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='laborum',
                        hidden=False,
                        hide_label=False,
                        icon='dignissimos',
                        info_helpers=shared.TextAttributeInfoHelpers(
                            hint_custom_component='vero',
                            hint_text='qui',
                            hint_text_key='consectetur',
                            hint_tooltip_placement='top',
                        ),
                        label='repellat',
                        layout='full_width',
                        multiline=False,
                        name='Rose Heller',
                        order=68093,
                        placeholder='illo',
                        preview_value_formatter='hic',
                        protected=False,
                        readonly=False,
                        render_condition='deserunt',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.TextAttributeTypeEnum.STRING,
                        value_formatter='delectus',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "in": 'exercitationem',
                        "labore": 'numquam',
                        "repudiandae": 'modi',
                    },
                    {
                        "explicabo": 'accusamus',
                        "rem": 'aperiam',
                    },
                ],
            ),
        ],
        dialog_config={
            "deleniti": 'enim',
        },
        draft=False,
        enable_setting=[
            '360_features',
            '360_features',
        ],
        explicit_search_mappings={
            "minima": shared.SearchMappings(
                fields_={
                    "magnam": 'sit',
                    "modi": 'eum',
                    "nesciunt": 'mollitia',
                },
                index=False,
                type=shared.SearchMappingsTypeEnum.LONG,
            ),
            "fugiat": shared.SearchMappings(
                fields_={
                    "molestiae": 'veniam',
                    "reiciendis": 'ab',
                },
                index=False,
                type=shared.SearchMappingsTypeEnum.BOOLEAN,
            ),
            "aut": shared.SearchMappings(
                fields_={
                    "eveniet": 'odio',
                },
                index=False,
                type=shared.SearchMappingsTypeEnum.INTEGER,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    'd7334ec1-b781-4b36-a080-88d100efada2',
                    '00ef0422-eb21-464c-b9ab-8366c723ffda',
                    '9e06bee4-825c-41fc-8e11-5c80bff91854',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='4ec42def-cce8-4f19-b777-3e63562a7b40',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='rem',
                    key='maiores',
                ),
                label='accusantium',
                order=331452,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '3d48fdaf-313a-41f5-bd94-259c0b36f25e',
                    'a944f3b7-56c1-41f6-837a-5126243835bb',
                    'c05a23a4-5cef-4c5f-9e10-a0ce2169e510',
                    '019c6dc5-e347-4627-99bf-bbe6949fb2bb',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='4ecae6c3-d5db-43ad-abd5-daea4c506a8a',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='est',
                    key='occaecati',
                ),
                label='labore',
                order=777378,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "fugit": 'aliquid',
        },
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            create_view=shared.EntityDefaultCreate(
                search_params={
                    "eligendi": 'hic',
                    "nostrum": 'officiis',
                },
                table_menu_options=shared.EntityDefaultCreateTableMenuOptions(
                    icon='unde',
                    label='nulla',
                ),
                view_type=shared.EntityDefaultCreateViewTypeEnum.DEFAULT,
            ),
            edit_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewTypeEnum.REDIRECT,
            ),
            list_item=shared.EntitySchemaUIConfigListItem(
                summary_attributes=[
                    shared.SummaryAttribute(
                        feature_flag='nostrum',
                        label='esse',
                        render_condition='corrupti',
                        setting_flag='fuga',
                        show_as_tag=False,
                        tag_color='facere',
                        value='impedit',
                    ),
                    shared.SummaryAttribute(
                        feature_flag='deserunt',
                        label='quod',
                        render_condition='laboriosam',
                        setting_flag='doloremque',
                        show_as_tag=False,
                        tag_color='voluptatem',
                        value='facere',
                    ),
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
                classic_view='eaque',
                dropdown_items=[
                    shared.EntityDefaultTableDropdownItems2(
                        feature_flag='FF_MY_FEATURE_FLAG',
                        legacy=False,
                        title='Opportunities',
                        type=shared.EntityDefaultTableDropdownItems2TypeEnum.LINK,
                        uri='porro',
                    ),
                ],
                enable_thumbnails=False,
                navbar_actions=[
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='magni',
                                params={
                                    "sed": 'necessitatibus',
                                    "impedit": 'ipsa',
                                    "excepturi": 'a',
                                    "maiores": 'laudantium',
                                },
                            ),
                        ],
                        type='maiores',
                    ),
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='asperiores',
                                params={
                                    "dicta": 'suscipit',
                                    "earum": 'doloribus',
                                    "velit": 'eius',
                                },
                            ),
                        ],
                        type='esse',
                    ),
                    shared.EntityDefaultTableNavbarActions(
                        options=[
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='eligendi',
                                params={
                                    "neque": 'vero',
                                },
                            ),
                            shared.EntityDefaultTableNavbarActionsOptions(
                                label='excepturi',
                                params={
                                    "qui": 'impedit',
                                },
                            ),
                        ],
                        type='beatae',
                    ),
                ],
                row_actions=[
                    'dicta',
                    'odit',
                ],
                view_type=shared.EntityDefaultTableViewTypeEnum.DEFAULT,
            ),
        ),
        version=357639,
    ),
    draft=False,
    slug='contact',
)

res = s.schemas.put_schema(req)

if res.entity_schema_item is not None:
    # handle response
```
