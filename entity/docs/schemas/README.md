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

## get_schema

By default gets the latest version of the Schema and to get the specific version of schema pass the id.

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
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
        epilot_auth="",
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
        epilot_auth="",
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

## list_taxonomy_classifications_for_schema

List taxonomy classifications for a given schema

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
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
        epilot_auth="",
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
                order=0,
                placeholder='possimus',
                preview_value_formatter='facilis',
                protected=False,
                readonly=False,
                render_condition='cum',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.TextAttributeType.STRING,
                value_formatter='commodi',
            ),
            shared.PaymentMethodRelationAttribute(
                purpose=[
                    'fd5e60b3-75ed-44f6-bbee-41f33317fe35',
                    'b60eb1ea-4265-455b-a3c2-8744ed53b88f',
                ],
                constraints={
                    "culpa": 'corrupti',
                },
                default_value='pariatur',
                deprecated=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='totam',
                has_primary=False,
                hidden=False,
                hide_label=False,
                icon='hic',
                info_helpers=shared.PaymentMethodRelationAttributeInfoHelpers(
                    hint_custom_component='exercitationem',
                    hint_text='nobis',
                    hint_text_key='sit',
                    hint_tooltip_placement='top',
                ),
                label='rerum',
                layout='full_width',
                name='Faith Cole',
                order=0,
                placeholder='voluptate',
                preview_value_formatter='expedita',
                protected=False,
                readonly=False,
                render_condition='ab',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.PaymentMethodRelationAttributeType.RELATION_PAYMENT_METHOD,
                value_formatter='iste',
            ),
        ],
        blueprint='4a276b26-916f-4e1f-88f4-294e3698f447',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    '03e8b445-e80c-4a55-afd2-0e457e1858b6',
                    'a89fbe3a-5aa8-4e48-a4d0-ab4075088e51',
                ],
                attributes=[
                    shared.UserRelationAttribute(
                        purpose=[
                            '065e904f-3b11-494b-8abf-603a79f9dfe0',
                        ],
                        constraints={
                            "quidem": 'reprehenderit',
                            "facere": 'fuga',
                            "praesentium": 'mollitia',
                        },
                        default_value='veniam',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='voluptatem',
                        hidden=False,
                        hide_label=False,
                        icon='quisquam',
                        info_helpers=shared.UserRelationAttributeInfoHelpers(
                            hint_custom_component='repudiandae',
                            hint_text='quasi',
                            hint_text_key='atque',
                            hint_tooltip_placement='top',
                        ),
                        label='reprehenderit',
                        layout='full_width',
                        multiple=False,
                        name='Jimmie Hoppe',
                        order=0,
                        placeholder='et',
                        preview_value_formatter='esse',
                        protected=False,
                        readonly=False,
                        render_condition='amet',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.UserRelationAttributeType.RELATION_USER,
                        value_formatter='assumenda',
                    ),
                    shared.AddressRelationAttribute(
                        purpose=[
                            '9eee9526-f8d9-486e-881e-ad4f0e101256',
                            '3f94e29e-973e-4922-a57a-15be3e060807',
                            'e2b6e3ab-8845-4f05-97a6-0ff2a54a31e9',
                        ],
                        constraints={
                            "molestiae": 'ex',
                            "ut": 'culpa',
                        },
                        default_value='adipisci',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='debitis',
                        has_primary=False,
                        hidden=False,
                        hide_label=False,
                        icon='laudantium',
                        info_helpers=shared.AddressRelationAttributeInfoHelpers(
                            hint_custom_component='eum',
                            hint_text='nemo',
                            hint_text_key='recusandae',
                            hint_tooltip_placement='top',
                        ),
                        label='esse',
                        layout='full_width',
                        name='Alvin Kemmer',
                        order=0,
                        placeholder='aspernatur',
                        preview_value_formatter='ullam',
                        protected=False,
                        readonly=False,
                        render_condition='quasi',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.AddressRelationAttributeType.RELATION_ADDRESS,
                        value_formatter='animi',
                    ),
                    shared.RelationAttribute(
                        purpose=[
                            '9da660ff-57bf-4aad-8f9e-fc1b4512c103',
                            '2648dc2f-6151-499e-bfd0-e9fe6c632ca3',
                            'aed01179-9631-42fd-a047-71778ff61d01',
                        ],
                        actions=[
                            shared.RelationAttributeActions(
                                action_type=shared.RelationAttributeActionsActionType.ADD_EXISTING,
                                default=False,
                                feature_flag='esse',
                                label='ex',
                                new_entity_item={
                                    "aliquid": 'ipsa',
                                },
                                setting_flag='laborum',
                            ),
                            shared.RelationAttributeActions(
                                action_type=shared.RelationAttributeActionsActionType.ADD_EXISTING,
                                default=False,
                                feature_flag='nostrum',
                                label='fugiat',
                                new_entity_item={
                                    "aliquid": 'officia',
                                    "suscipit": 'aliquid',
                                    "perferendis": 'eum',
                                },
                                setting_flag='voluptas',
                            ),
                        ],
                        add_button_label='iste',
                        allowed_schemas=[
                            'contact',
                            'contact',
                            'contact',
                        ],
                        constraints={
                            "error": 'possimus',
                        },
                        default_value='voluptates',
                        deprecated=False,
                        details_view_mode_enabled=False,
                        drawer_size=shared.RelationAttributeDrawerSize.MEDIUM,
                        edit_mode=shared.RelationAttributeEditMode.LIST_VIEW,
                        enable_relation_picker=False,
                        enable_relation_tags=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='laborum',
                        has_primary=False,
                        hidden=False,
                        hide_label=False,
                        icon='libero',
                        info_helpers=shared.RelationAttributeInfoHelpers(
                            hint_custom_component='ad',
                            hint_text='deleniti',
                            hint_text_key='enim',
                            hint_tooltip_placement='top',
                        ),
                        label='vitae',
                        layout='full_width',
                        name='Ruben Ryan',
                        order=0,
                        placeholder='ad',
                        preview_value_formatter='expedita',
                        protected=False,
                        readonly=False,
                        relation_affinity_mode=shared.RelationAttributeRelationAffinityMode.WEAK,
                        relation_type=shared.RelationAttributeRelationType.HAS_ONE,
                        render_condition='cum',
                        required=False,
                        reverse_attributes={
                            "beatae": 'contact.account',
                            "voluptatum": 'contact.account',
                        },
                        search_placeholder='omnis',
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        summary_fields=[
                            shared.SummaryField(
                                display_as='est',
                                field='culpa',
                            ),
                        ],
                        type=shared.RelationAttributeType.RELATION,
                        value_formatter='voluptatem',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "architecto": 'fuga',
                        "pariatur": 'debitis',
                        "voluptatem": 'alias',
                        "deleniti": 'earum',
                    },
                    {
                        "sapiente": 'rem',
                        "minus": 'nemo',
                    },
                    {
                        "ratione": 'ullam',
                        "perferendis": 'illum',
                        "totam": 'impedit',
                        "quibusdam": 'nam',
                    },
                    {
                        "culpa": 'dolor',
                        "aliquam": 'inventore',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '14301042-1813-4d52-88ec-e7e253b66845',
                    '1c6c6e20-5e16-4dea-b3fe-c9578a645842',
                    '73a8418d-1623-409f-b092-9921aefb9f58',
                ],
                attributes=[
                    shared.SequenceAttribute(
                        purpose=[
                            '86e68e4b-e056-4013-b59d-a757a59ecfef',
                            '66ef1caa-3383-4c2b-ab47-7373c8d72f64',
                            'd1db1f2c-4310-4661-a963-49e1cf9e06e3',
                            'a437000a-e6b6-4bc9-b8f7-59eac55a9741',
                        ],
                        constraints={
                            "consectetur": 'vitae',
                            "inventore": 'dolorem',
                            "ad": 'qui',
                            "iste": 'ex',
                        },
                        default_value='nemo',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='soluta',
                        hidden=False,
                        hide_label=False,
                        icon='libero',
                        info_helpers=shared.SequenceAttributeInfoHelpers(
                            hint_custom_component='rem',
                            hint_text='dolorum',
                            hint_text_key='odio',
                            hint_tooltip_placement='top',
                        ),
                        label='fugit',
                        layout='full_width',
                        name='Mr. Anne Kautzer',
                        order=0,
                        placeholder='neque',
                        prefix='OR-',
                        preview_value_formatter='exercitationem',
                        protected=False,
                        readonly=False,
                        render_condition='itaque',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        start_number=88248,
                        type=shared.SequenceAttributeType.SEQUENCE,
                        value_formatter='ipsum',
                    ),
                    shared.NumberAttribute(
                        purpose=[
                            'bc2259b1-abda-48c0-b0e1-084cb0672d1a',
                            'd879eeb9-665b-485e-bbd0-2bae0be2d782',
                            '259e3ea4-b519-47f9-a443-da7ce52b895c',
                            '537c6454-efb0-4b34-896c-3ca5acfbe2fd',
                        ],
                        constraints={
                            "reprehenderit": 'aperiam',
                            "odio": 'minima',
                        },
                        default_value='in',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        format='ducimus',
                        group='excepturi',
                        hidden=False,
                        hide_label=False,
                        icon='dolores',
                        info_helpers=shared.NumberAttributeInfoHelpers(
                            hint_custom_component='error',
                            hint_text='veritatis',
                            hint_text_key='ducimus',
                            hint_tooltip_placement='top',
                        ),
                        label='voluptate',
                        layout='full_width',
                        name='Bradford Murazik',
                        order=0,
                        placeholder='quaerat',
                        preview_value_formatter='commodi',
                        protected=False,
                        readonly=False,
                        render_condition='officiis',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.NumberAttributeType.NUMBER,
                        value_formatter='placeat',
                    ),
                    shared.InternalAttribute(
                        purpose=[
                            '73409e3e-b1e5-4a2b-92eb-07f116db9954',
                            '5fc95fa8-8970-4e18-9dbb-30fcb33ea055',
                        ],
                        constraints={
                            "architecto": 'cupiditate',
                            "molestiae": 'eligendi',
                            "possimus": 'non',
                        },
                        default_value='magnam',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='itaque',
                        hidden=False,
                        hide_label=False,
                        icon='sed',
                        info_helpers=shared.InternalAttributeInfoHelpers(
                            hint_custom_component='asperiores',
                            hint_text='veniam',
                            hint_text_key='consequuntur',
                            hint_tooltip_placement='top',
                        ),
                        label='facere',
                        layout='full_width',
                        name='Fred Stracke',
                        order=0,
                        placeholder='ab',
                        preview_value_formatter='velit',
                        protected=False,
                        readonly=False,
                        render_condition='facilis',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.InternalAttributeType.INTERNAL,
                        value_formatter='tempore',
                    ),
                    shared.UserRelationAttribute(
                        purpose=[
                            '48b656bc-db35-4ff2-a4b2-7537a8cd9e73',
                            '19c177d5-25f7-47b1-94ee-b52ff785fc37',
                            '814d4c98-e0c2-4bb8-9eb7-5dad636c6005',
                            '03d8bb31-180f-4739-ae9e-057eb809e281',
                        ],
                        constraints={
                            "velit": 'dolor',
                        },
                        default_value='sunt',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='a',
                        hidden=False,
                        hide_label=False,
                        icon='dolor',
                        info_helpers=shared.UserRelationAttributeInfoHelpers(
                            hint_custom_component='occaecati',
                            hint_text='atque',
                            hint_text_key='beatae',
                            hint_tooltip_placement='top',
                        ),
                        label='at',
                        layout='full_width',
                        multiple=False,
                        name='Mr. Bethany Koch',
                        order=0,
                        placeholder='ea',
                        preview_value_formatter='aperiam',
                        protected=False,
                        readonly=False,
                        render_condition='dignissimos',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.UserRelationAttributeType.RELATION_USER,
                        value_formatter='repellat',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "provident": 'consectetur',
                        "eligendi": 'dignissimos',
                        "consectetur": 'soluta',
                        "natus": 'temporibus',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '3f2ceda7-e23f-4225-b411-faf4b7544e47',
                    '2e802857-a5b4-4046-ba7d-575f1400e764',
                    'ad7334ec-1b78-41b3-aa08-088d100efada',
                ],
                attributes=[
                    shared.TextAttribute(
                        purpose=[
                            'ef0422eb-2164-4cf9-ab83-66c723ffda9e',
                        ],
                        constraints={
                            "nisi": 'rerum',
                        },
                        default_value='recusandae',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='voluptates',
                        hidden=False,
                        hide_label=False,
                        icon='non',
                        info_helpers=shared.TextAttributeInfoHelpers(
                            hint_custom_component='rem',
                            hint_text='quia',
                            hint_text_key='ullam',
                            hint_tooltip_placement='top',
                        ),
                        label='quisquam',
                        layout='full_width',
                        multiline=False,
                        name='Dr. Shari Roob Sr.',
                        order=0,
                        placeholder='enim',
                        preview_value_formatter='optio',
                        protected=False,
                        readonly=False,
                        render_condition='rem',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.TextAttributeType.STRING,
                        value_formatter='perferendis',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "a": 'iste',
                        "dicta": 'quos',
                        "ullam": 'dolore',
                        "modi": 'itaque',
                    },
                    {
                        "modi": 'consequuntur',
                        "assumenda": 'vero',
                        "doloribus": 'impedit',
                        "porro": 'accusamus',
                    },
                    {
                        "reiciendis": 'ab',
                        "sint": 'nihil',
                        "esse": 'iure',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '3e63562a-7b40-48f0-9e3d-48fdaf313a1f',
                    '5fd94259-c0b3-46f2-9ea9-44f3b756c11f',
                ],
                attributes=[
                    shared.ComputedAttribute(
                        purpose=[
                            '7a512624-3835-4bbc-85a2-3a45cefc5fde',
                        ],
                        constraints={
                            "alias": 'culpa',
                        },
                        default_value='ipsa',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='nobis',
                        hidden=False,
                        hide_label=False,
                        icon='necessitatibus',
                        info_helpers=shared.ComputedAttributeInfoHelpers(
                            hint_custom_component='quia',
                            hint_text='dicta',
                            hint_text_key='vel',
                            hint_tooltip_placement='top',
                        ),
                        label='perspiciatis',
                        layout='full_width',
                        name='Mr. Derrick Brakus V',
                        order=0,
                        placeholder='cumque',
                        preview_value_formatter='iure',
                        protected=False,
                        readonly=False,
                        render_condition='quibusdam',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.ComputedAttributeType.COMPUTED,
                        value_formatter='quod',
                    ),
                    shared.RelationAttribute(
                        purpose=[
                            '34762799-bfbb-4e69-89fb-2bb4ecae6c3d',
                            '5db3adeb-d5da-4ea4-8506-a8aa94c02644',
                            'cf5e9d9a-4578-4adc-9ac6-00dec001ac80',
                            '2e2ec09f-f8f0-4f81-aff3-477c13e902c1',
                        ],
                        actions=[
                            shared.RelationAttributeActions(
                                action_type=shared.RelationAttributeActionsActionType.ADD_EXISTING,
                                default=False,
                                feature_flag='odit',
                                label='corporis',
                                new_entity_item={
                                    "alias": 'error',
                                    "vel": 'accusantium',
                                    "id": 'laboriosam',
                                },
                                setting_flag='ex',
                            ),
                            shared.RelationAttributeActions(
                                action_type=shared.RelationAttributeActionsActionType.CREATE_NEW,
                                default=False,
                                feature_flag='veritatis',
                                label='ullam',
                                new_entity_item={
                                    "similique": 'incidunt',
                                },
                                setting_flag='quam',
                            ),
                        ],
                        add_button_label='magni',
                        allowed_schemas=[
                            'contact',
                            'contact',
                            'contact',
                        ],
                        constraints={
                            "omnis": 'sed',
                            "nesciunt": 'maxime',
                            "quis": 'cupiditate',
                            "aliquam": 'excepturi',
                        },
                        default_value='maiores',
                        deprecated=False,
                        details_view_mode_enabled=False,
                        drawer_size=shared.RelationAttributeDrawerSize.MEDIUM,
                        edit_mode=shared.RelationAttributeEditMode.LIST_VIEW,
                        enable_relation_picker=False,
                        enable_relation_tags=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='velit',
                        has_primary=False,
                        hidden=False,
                        hide_label=False,
                        icon='reiciendis',
                        info_helpers=shared.RelationAttributeInfoHelpers(
                            hint_custom_component='amet',
                            hint_text='nemo',
                            hint_text_key='ipsa',
                            hint_tooltip_placement='top',
                        ),
                        label='quisquam',
                        layout='full_width',
                        name='Morris Kreiger',
                        order=0,
                        placeholder='a',
                        preview_value_formatter='nobis',
                        protected=False,
                        readonly=False,
                        relation_affinity_mode=shared.RelationAttributeRelationAffinityMode.STRONG,
                        relation_type=shared.RelationAttributeRelationType.HAS_MANY,
                        render_condition='dicta',
                        required=False,
                        reverse_attributes={
                            "commodi": 'contact.account',
                            "eveniet": 'contact.account',
                            "porro": 'contact.account',
                            "tempore": 'contact.account',
                        },
                        search_placeholder='quidem',
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        summary_fields=[
                            shared.SummaryField(
                                display_as='fugit',
                                field='eius',
                            ),
                            'eligendi',
                        ],
                        type=shared.RelationAttributeType.RELATION,
                        value_formatter='asperiores',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "sint": 'repellat',
                        "a": 'animi',
                        "maiores": 'itaque',
                    },
                    {
                        "deserunt": 'corporis',
                        "velit": 'officiis',
                        "enim": 'officia',
                        "saepe": 'eum',
                    },
                ],
            ),
        ],
        dialog_config={
            "accusantium": 'officia',
            "impedit": 'quasi',
            "blanditiis": 'eius',
            "quisquam": 'eos',
        },
        draft=False,
        enable_setting=[
            '360_features',
            '360_features',
            '360_features',
        ],
        explicit_search_mappings={
            "minus": shared.SearchMappings(
                fields_={
                    "magnam": 'reprehenderit',
                },
                index=False,
                type=shared.SearchMappingsType.FLATTENED,
            ),
            "quos": shared.SearchMappings(
                fields_={
                    "amet": 'molestiae',
                    "amet": 'laborum',
                    "modi": 'perferendis',
                },
                index=False,
                type=shared.SearchMappingsType.NESTED,
            ),
            "architecto": shared.SearchMappings(
                fields_={
                    "dolore": 'sunt',
                    "maiores": 'neque',
                    "odit": 'earum',
                },
                index=False,
                type=shared.SearchMappingsType.BOOLEAN,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '55756f5d-56d0-4bd0-af2d-fe13db4f62cb',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='a3f8941a-ebc0-4b80-a692-4d3b2ecfcc8f',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='voluptatum',
                    key='iste',
                ),
                label='corporis',
                order=37129,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '0f5dd3d6-fa18-404e-94c8-2f168a363c88',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='73e48438-0b1f-46b8-8a27-5a60a04c495c',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='placeat',
                    key='voluptas',
                ),
                label='occaecati',
                order=600934,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "nihil": 'inventore',
        },
        name='Contact',
        plural='Contacts',
        published=False,
        slug='contact',
        title_template='{{first_name}} {{last_name}}',
        ui_config=shared.EntitySchemaUIConfig(
            create_view=shared.EntityViewDisabled(
                view_type=shared.EntityViewDisabledViewType.DISABLED,
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
            single_view=shared.EntityDefaultEdit(
                search_params={
                    "facere": 'facilis',
                    "beatae": 'cumque',
                    "delectus": 'labore',
                },
                table_menu_options=shared.EntityDefaultEditTableMenuOptions(
                    icon='expedita',
                    label='corrupti',
                ),
                view_type=shared.EntityDefaultEditViewType.DEFAULT,
            ),
            table_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewType.REDIRECT,
            ),
        ),
        version=543353,
    ),
    draft=False,
    slug='contact',
)

res = s.schemas.put_schema(req)

if res.entity_schema_item is not None:
    # handle response
```
