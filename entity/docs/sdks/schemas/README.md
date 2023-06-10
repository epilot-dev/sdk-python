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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetSchemaRequest(
    id='0b375ed4-f6fb-4ee4-9f33-317fe35b60eb',
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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetSchemaVersionsRequest(
    drafts_from=1138.16,
    drafts_size=8817.21,
    slug='contact',
    versions_from=6311.26,
    versions_size=2724.37,
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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.ListTaxonomyClassificationsForSchemaRequest(
    query='aspernatur',
    size=3790.57,
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
            shared.UserRelationAttribute(
                purpose=[
                    'ba3c2874-4ed5-43b8-8f3a-8d8f5c0b2f2f',
                    'b7b194a2-76b2-4691-afe1-f08f4294e369',
                ],
                constraints=shared.UserRelationAttributeConstraints(),
                default_value='quos',
                deprecated=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='voluptatibus',
                hidden=False,
                hide_label=False,
                icon='tempora',
                info_helpers=shared.UserRelationAttributeInfoHelpers(
                    hint_custom_component='tempora',
                    hint_text='voluptate',
                    hint_text_key='reiciendis',
                    hint_tooltip_placement='top',
                ),
                label='ex',
                layout='full_width',
                multiple=False,
                name='Ethel Towne',
                order=0,
                placeholder='quaerat',
                preview_value_formatter='incidunt',
                protected=False,
                readonly=False,
                render_condition='ipsam',
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.UserRelationAttributeType.RELATION_USER,
                value_formatter='debitis',
            ),
            shared.RepeatableAttribute(
                purpose=[
                    'ca55efd2-0e45-47e1-858b-6a89fbe3a5aa',
                ],
                constraints=shared.RepeatableAttributeConstraints(),
                default_value='corrupti',
                deprecated=False,
                enable_relation_picker=False,
                entity_builder_disable_edit=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                group='accusamus',
                has_primary=False,
                hidden=False,
                hide_label=False,
                icon='tempora',
                info_helpers=shared.RepeatableAttributeInfoHelpers(
                    hint_custom_component='atque',
                    hint_text='fugit',
                    hint_text_key='ut',
                    hint_tooltip_placement='top',
                ),
                label='fugiat',
                layout='full_width',
                name='Cecilia Quitzon IV',
                order=0,
                placeholder='ipsam',
                preview_value_formatter='sit',
                protected=False,
                readonly=False,
                relation_affinity_mode=shared.RepeatableAttributeRelationAffinityMode.STRONG,
                render_condition='quas',
                repeatable=False,
                required=False,
                setting_flag='MY_SETTING',
                show_in_table=False,
                type=shared.RepeatableAttributeType.DATE,
                value_formatter='corporis',
            ),
        ],
        blueprint='1862065e-904f-43b1-994b-8abf603a79f9',
        capabilities=[
            shared.EntityCapability(
                purpose=[
                    'e0ab7da8-a50c-4e18-bf86-bc173d689eee',
                    '9526f8d9-86e8-481e-ad4f-0e1012563f94',
                    'e29e973e-922a-457a-95be-3e060807e2b6',
                    'e3ab8845-f059-47a6-8ff2-a54a31e94764',
                ],
                attributes=[
                    shared.MultiSelectAttribute(
                        purpose=[
                            '865e7956-f925-41a5-a9da-660ff57bfaad',
                            '4f9efc1b-4512-4c10-b264-8dc2f615199e',
                            'bfd0e9fe-6c63-42ca-baed-0117996312fd',
                            'e0477177-8ff6-41d0-9747-6360a15db6a6',
                        ],
                        allow_any=False,
                        allow_extra_options=False,
                        constraints=shared.MultiSelectAttributeConstraints(),
                        default_value='aliquid',
                        deprecated=False,
                        disable_case_sensitive=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='perferendis',
                        hidden=False,
                        hide_label=False,
                        icon='eum',
                        info_helpers=shared.MultiSelectAttributeInfoHelpers(
                            hint_custom_component='voluptas',
                            hint_text='iste',
                            hint_text_key='id',
                            hint_tooltip_placement='top',
                        ),
                        label='ab',
                        layout='full_width',
                        name='Woodrow Volkman',
                        options=[
                            'deleniti',
                            'vitae',
                            shared.MultiSelectAttributeOptions2(
                                title='Ms.',
                                value='quo',
                            ),
                        ],
                        order=0,
                        placeholder='ex',
                        preview_value_formatter='ut',
                        protected=False,
                        readonly=False,
                        render_condition='ad',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.MultiSelectAttributeType.CHECKBOX,
                        value_formatter='voluptatem',
                    ),
                    shared.TagsAttribute(
                        purpose=[
                            '61891baa-0fe1-4ade-808e-6f8c5f350d8c',
                            'db5a3418-1430-4104-a181-3d5208ece7e2',
                            '53b66845-1c6c-46e2-85e1-6deab3fec957',
                        ],
                        constraints=shared.TagsAttributeConstraints(),
                        default_value='blanditiis',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='officia',
                        hidden=False,
                        hide_label=False,
                        icon='voluptas',
                        info_helpers=shared.TagsAttributeInfoHelpers(
                            hint_custom_component='numquam',
                            hint_text='nemo',
                            hint_text_key='quos',
                            hint_tooltip_placement='top',
                        ),
                        label='eius',
                        layout='full_width',
                        name='Caroline Dooley',
                        options=[
                            'quasi',
                            'rem',
                        ],
                        order=0,
                        placeholder='fugiat',
                        preview_value_formatter='dicta',
                        protected=False,
                        readonly=False,
                        render_condition='nisi',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        suggestions=[
                            'consectetur',
                        ],
                        type=shared.TagsAttributeType.TAGS,
                        value_formatter='aperiam',
                    ),
                    shared.TagsAttribute(
                        purpose=[
                            'b0929921-aefb-49f5-8c4d-86e68e4be056',
                            '013f59da-757a-459e-8fef-66ef1caa3383',
                            'c2beb477-373c-48d7-af64-d1db1f2c4310',
                            '661e9634-9e1c-4f9e-86e3-a437000ae6b6',
                        ],
                        constraints=shared.TagsAttributeConstraints(),
                        default_value='facilis',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='placeat',
                        hidden=False,
                        hide_label=False,
                        icon='perspiciatis',
                        info_helpers=shared.TagsAttributeInfoHelpers(
                            hint_custom_component='expedita',
                            hint_text='deleniti',
                            hint_text_key='a',
                            hint_tooltip_placement='top',
                        ),
                        label='voluptate',
                        layout='full_width',
                        name='Lindsey Treutel',
                        options=[
                            'corporis',
                            'est',
                        ],
                        order=0,
                        placeholder='error',
                        preview_value_formatter='esse',
                        protected=False,
                        readonly=False,
                        render_condition='labore',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        suggestions=[
                            'vero',
                        ],
                        type=shared.TagsAttributeType.TAGS,
                        value_formatter='consectetur',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "dolorem": 'ad',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '965bb8a7-2026-4114-b5e1-39dbc2259b1a',
                ],
                attributes=[
                    shared.InvitationEmailAttribute(
                        purpose=[
                            '8c070e10-84cb-4067-ad1a-d879eeb9665b',
                            '85efbd02-bae0-4be2-9782-259e3ea4b519',
                            '7f92443d-a7ce-452b-895c-537c6454efb0',
                        ],
                        constraints=shared.InvitationEmailAttributeConstraints(),
                        default_value='libero',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='ratione',
                        hidden=False,
                        hide_label=False,
                        icon='labore',
                        info_helpers=shared.InvitationEmailAttributeInfoHelpers(
                            hint_custom_component='totam',
                            hint_text='occaecati',
                            hint_text_key='voluptas',
                            hint_tooltip_placement='top',
                        ),
                        label='quo',
                        layout='full_width',
                        name='Bethany Paucek',
                        order=0,
                        placeholder='impedit',
                        preview_value_formatter='delectus',
                        protected=False,
                        readonly=False,
                        render_condition='tempore',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.InvitationEmailAttributeType.INVITATION_EMAIL,
                        value_formatter='vero',
                    ),
                    shared.CountryAttribute(
                        purpose=[
                            'd5707577-9291-477d-aac6-46ecb573409e',
                            '3eb1e5a2-b12e-4b07-b116-db99545fc95f',
                            'a88970e1-89db-4b30-bcb3-3ea055b197cd',
                            '44e2f52d-82d3-4513-bb6f-48b656bcdb35',
                        ],
                        constraints=shared.CountryAttributeConstraints(),
                        default_value='voluptatibus',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='voluptatibus',
                        hidden=False,
                        hide_label=False,
                        icon='consequuntur',
                        info_helpers=shared.CountryAttributeInfoHelpers(
                            hint_custom_component='debitis',
                            hint_text='labore',
                            hint_text_key='rerum',
                            hint_tooltip_placement='top',
                        ),
                        label='eos',
                        layout='full_width',
                        name='Audrey Durgan',
                        order=0,
                        placeholder='rem',
                        preview_value_formatter='eligendi',
                        protected=False,
                        readonly=False,
                        render_condition='fugiat',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.CountryAttributeType.COUNTRY,
                        value_formatter='unde',
                    ),
                    shared.AutomationAttribute(
                        purpose=[
                            '319c177d-525f-477b-914e-eb52ff785fc3',
                            '7814d4c9-8e0c-42bb-89eb-75dad636c600',
                        ],
                        constraints=shared.AutomationAttributeConstraints(),
                        default_value='ad',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='quae',
                        hidden=False,
                        hide_label=False,
                        icon='amet',
                        info_helpers=shared.AutomationAttributeInfoHelpers(
                            hint_custom_component='illum',
                            hint_text='praesentium',
                            hint_text_key='quidem',
                            hint_tooltip_placement='top',
                        ),
                        label='cum',
                        layout='full_width',
                        name='Joyce Carroll DVM',
                        order=0,
                        placeholder='iusto',
                        preview_value_formatter='amet',
                        protected=False,
                        readonly=False,
                        render_condition='provident',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.AutomationAttributeType.AUTOMATION,
                        value_formatter='dolorum',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "repudiandae": 'consequatur',
                        "nemo": 'molestiae',
                        "itaque": 'facilis',
                    },
                    {
                        "aperiam": 'sint',
                        "accusamus": 'eos',
                        "totam": 'dicta',
                    },
                    {
                        "velit": 'dolor',
                    },
                    {
                        "a": 'dolor',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '81d4c700-b607-4f3c-93c7-3b9da3f2ceda',
                    '7e23f225-7411-4faf-8b75-44e472e80285',
                    '7a5b4046-3a7d-4575-b140-0e764ad7334e',
                ],
                attributes=[
                    shared.CountryAttribute(
                        purpose=[
                            '781b36a0-8088-4d10-8efa-da200ef0422e',
                            'b2164cf9-ab83-466c-b23f-fda9e06bee48',
                            '25c1fc0e-115c-480b-bf91-8544ec42defc',
                        ],
                        constraints=shared.CountryAttributeConstraints(),
                        default_value='porro',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='accusamus',
                        hidden=False,
                        hide_label=False,
                        icon='totam',
                        info_helpers=shared.CountryAttributeInfoHelpers(
                            hint_custom_component='reiciendis',
                            hint_text='ab',
                            hint_text_key='sint',
                            hint_tooltip_placement='top',
                        ),
                        label='nihil',
                        layout='full_width',
                        name='Charlene Kuhic',
                        order=0,
                        placeholder='vel',
                        preview_value_formatter='neque',
                        protected=False,
                        readonly=False,
                        render_condition='corporis',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.CountryAttributeType.COUNTRY,
                        value_formatter='voluptas',
                    ),
                    shared.BooleanAttribute(
                        purpose=[
                            '7b408f05-e3d4-48fd-af31-3a1f5fd94259',
                            'c0b36f25-ea94-44f3-b756-c11f6c37a512',
                            '6243835b-bc05-4a23-a45c-efc5fde10a0c',
                        ],
                        constraints=shared.BooleanAttributeConstraints(),
                        default_value='necessitatibus',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='quia',
                        hidden=False,
                        hide_label=False,
                        icon='dicta',
                        info_helpers=shared.BooleanAttributeInfoHelpers(
                            hint_custom_component='vel',
                            hint_text='perspiciatis',
                            hint_text_key='debitis',
                            hint_tooltip_placement='top',
                        ),
                        label='ullam',
                        layout='full_width',
                        name='Ms. Donna Auer',
                        order=0,
                        placeholder='iure',
                        preview_value_formatter='quibusdam',
                        protected=False,
                        readonly=False,
                        render_condition='quod',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.BooleanAttributeType.BOOLEAN,
                        value_formatter='nemo',
                    ),
                    shared.AutomationAttribute(
                        purpose=[
                            '4762799b-fbbe-4694-9fb2-bb4ecae6c3d5',
                        ],
                        constraints=shared.AutomationAttributeConstraints(),
                        default_value='illum',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='facilis',
                        hidden=False,
                        hide_label=False,
                        icon='non',
                        info_helpers=shared.AutomationAttributeInfoHelpers(
                            hint_custom_component='mollitia',
                            hint_text='assumenda',
                            hint_text_key='recusandae',
                            hint_tooltip_placement='top',
                        ),
                        label='distinctio',
                        layout='full_width',
                        name='Leon Schumm',
                        order=0,
                        placeholder='laborum',
                        preview_value_formatter='incidunt',
                        protected=False,
                        readonly=False,
                        render_condition='maxime',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.AutomationAttributeType.AUTOMATION,
                        value_formatter='ipsam',
                    ),
                    shared.TextAttribute(
                        purpose=[
                            'a8aa94c0-2644-4cf5-a9d9-a4578adc1ac6',
                            '00dec001-ac80-42e2-ac09-ff8f0f816ff3',
                        ],
                        constraints=shared.TextAttributeConstraints(),
                        default_value='eius',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='esse',
                        hidden=False,
                        hide_label=False,
                        icon='in',
                        info_helpers=shared.TextAttributeInfoHelpers(
                            hint_custom_component='eligendi',
                            hint_text='quasi',
                            hint_text_key='neque',
                            hint_tooltip_placement='top',
                        ),
                        label='vero',
                        layout='full_width',
                        multiline=False,
                        name='Edward Denesik II',
                        order=0,
                        placeholder='dicta',
                        preview_value_formatter='odit',
                        protected=False,
                        readonly=False,
                        render_condition='corporis',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.TextAttributeType.STRING,
                        value_formatter='rerum',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "vel": 'accusantium',
                        "id": 'laboriosam',
                        "ex": 'quas',
                    },
                ],
            ),
            shared.EntityCapability(
                purpose=[
                    '51a472af-923c-4594-9f83-f350cf876ffb',
                ],
                attributes=[
                    shared.TextAttribute(
                        purpose=[
                            'c6ecbb4e-243c-4f78-9ffa-feda53e5ae6e',
                        ],
                        constraints=shared.TextAttributeConstraints(),
                        default_value='accusantium',
                        deprecated=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='officia',
                        hidden=False,
                        hide_label=False,
                        icon='impedit',
                        info_helpers=shared.TextAttributeInfoHelpers(
                            hint_custom_component='quasi',
                            hint_text='blanditiis',
                            hint_text_key='eius',
                            hint_tooltip_placement='top',
                        ),
                        label='quisquam',
                        layout='full_width',
                        multiline=False,
                        name='Gayle Mraz',
                        order=0,
                        placeholder='magnam',
                        preview_value_formatter='reprehenderit',
                        protected=False,
                        readonly=False,
                        render_condition='quod',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.TextAttributeType.STRING,
                        value_formatter='quos',
                    ),
                    shared.RepeatableAttribute(
                        purpose=[
                            '73a40e19-42f3-42e5-9055-756f5d56d0bd',
                        ],
                        constraints=shared.RepeatableAttributeConstraints(),
                        default_value='perferendis',
                        deprecated=False,
                        enable_relation_picker=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='id',
                        has_primary=False,
                        hidden=False,
                        hide_label=False,
                        icon='sapiente',
                        info_helpers=shared.RepeatableAttributeInfoHelpers(
                            hint_custom_component='sed',
                            hint_text='possimus',
                            hint_text_key='repellat',
                            hint_tooltip_placement='top',
                        ),
                        label='repudiandae',
                        layout='full_width',
                        name='Josephine Stroman',
                        order=0,
                        placeholder='voluptatibus',
                        preview_value_formatter='iure',
                        protected=False,
                        readonly=False,
                        relation_affinity_mode=shared.RepeatableAttributeRelationAffinityMode.WEAK,
                        render_condition='minus',
                        repeatable=False,
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.RepeatableAttributeType.PAYMENT,
                        value_formatter='dolorum',
                    ),
                    shared.MultiSelectAttribute(
                        purpose=[
                            '8941aebc-0b80-4a69-a4d3-b2ecfcc8f895',
                            '010f5dd3-d6fa-4180-8e54-c82f168a363c',
                            '8873e484-380b-41f6-b8ca-275a60a04c49',
                            '5cc69917-1b51-4c1b-9b1c-f4b888ebdfc4',
                        ],
                        allow_any=False,
                        allow_extra_options=False,
                        constraints=shared.MultiSelectAttributeConstraints(),
                        default_value='quod',
                        deprecated=False,
                        disable_case_sensitive=False,
                        entity_builder_disable_edit=False,
                        feature_flag='FF_MY_FEATURE_FLAG',
                        group='minus',
                        hidden=False,
                        hide_label=False,
                        icon='porro',
                        info_helpers=shared.MultiSelectAttributeInfoHelpers(
                            hint_custom_component='id',
                            hint_text='excepturi',
                            hint_text_key='occaecati',
                            hint_tooltip_placement='top',
                        ),
                        label='libero',
                        layout='full_width',
                        name='Cory Welch DDS',
                        options=[
                            shared.MultiSelectAttributeOptions2(
                                title='Miss',
                                value='recusandae',
                            ),
                        ],
                        order=0,
                        placeholder='veritatis',
                        preview_value_formatter='aut',
                        protected=False,
                        readonly=False,
                        render_condition='laudantium',
                        required=False,
                        setting_flag='MY_SETTING',
                        show_in_table=False,
                        type=shared.MultiSelectAttributeType.MULTISELECT,
                        value_formatter='dolor',
                    ),
                ],
                feature_flag='FF_MY_FEATURE_FLAG',
                legacy=False,
                name='customer_messaging',
                setting_flag='MY_SETTING',
                title='Messaging',
                ui_hooks=[
                    {
                        "magni": 'rerum',
                        "doloremque": 'voluptatem',
                    },
                    {
                        "at": 'eum',
                        "reprehenderit": 'voluptatum',
                    },
                    {
                        "nihil": 'atque',
                        "rerum": 'deserunt',
                        "atque": 'nostrum',
                    },
                    {
                        "architecto": 'est',
                        "enim": 'rem',
                        "magni": 'quae',
                    },
                ],
            ),
        ],
        dialog_config={
            "placeat": 'enim',
            "labore": 'sapiente',
            "saepe": 'delectus',
        },
        draft=False,
        enable_setting=[
            '360_features',
            '360_features',
            '360_features',
        ],
        explicit_search_mappings={
            "cumque": shared.SearchMappings(
                fields_={
                    "quaerat": 'doloribus',
                    "quia": 'officiis',
                    "mollitia": 'cumque',
                },
                index=False,
                type=shared.SearchMappingsType.INTEGER,
            ),
            "enim": shared.SearchMappings(
                fields_={
                    "nemo": 'illum',
                    "nesciunt": 'sit',
                },
                index=False,
                type=shared.SearchMappingsType.LONG,
            ),
            "minus": shared.SearchMappings(
                fields_={
                    "recusandae": 'voluptates',
                    "praesentium": 'dicta',
                    "fugit": 'sit',
                    "aliquid": 'necessitatibus',
                },
                index=False,
                type=shared.SearchMappingsType.TEXT,
            ),
        },
        feature_flag='FF_MY_FEATURE_FLAG',
        group_settings=[
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '3fa4a41c-480d-43f2-932a-f03102d514f4',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='cc6f18bf-9621-4a6a-8f77-a87ee3e4be75',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='explicabo',
                    key='impedit',
                ),
                label='aliquid',
                order=339843,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    '34418e3b-b91c-48d9-b5e0-e8419d8f84f1',
                    '44f3e07e-dcc4-4aa5-b3ca-bd905a972e05',
                    '6728227b-2d30-4947-8bf7-a4fa87cf535a',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='6fae54eb-f60c-4321-b023-b75d2367fe1a',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='accusantium',
                    key='quod',
                ),
                label='minus',
                order=550994,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
            shared.EntitySchemaGroupSettings(
                purpose=[
                    'f79f0a39-6d90-4c36-8b7c-15dfbace188b',
                    '1c4ee2c8-c6ce-4611-beeb-1c7cbdb6eec7',
                    '4378ba25-3177-447d-8915-ad2caf5dd672',
                    '3dc0f5ae-2f3a-46b7-8087-8756143f5a6c',
                ],
                expanded=False,
                feature_flag='FF_MY_FEATURE_FLAG',
                id='98b55554-080d-440b-8acc-6cbd6b5f3ec9',
                info_tooltip_title=shared.EntitySchemaGroupSettingsInfoTooltipTitle(
                    default='voluptatem',
                    key='provident',
                ),
                label='adipisci',
                order=34267,
                render_condition='_is_composite_price = "false"',
                setting_flag='MY_SETTING',
            ),
        ],
        icon='person',
        layout_settings={
            "repellat": 'omnis',
            "explicabo": 'vel',
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
                    shared.SummaryAttribute(
                        feature_flag='ipsam',
                        label='nostrum',
                        render_condition='sequi',
                        setting_flag='voluptatum',
                        show_as_tag=False,
                        tag_color='quasi',
                        value='error',
                    ),
                    'email',
                    shared.SummaryAttribute(
                        feature_flag='voluptate',
                        label='eius',
                        render_condition='expedita',
                        setting_flag='aperiam',
                        show_as_tag=False,
                        tag_color='voluptates',
                        value='possimus',
                    ),
                    shared.SummaryAttribute(
                        feature_flag='voluptatem',
                        label='repudiandae',
                        render_condition='corporis',
                        setting_flag='ea',
                        show_as_tag=False,
                        tag_color='eos',
                        value='aliquam',
                    ),
                ],
            ),
            sharing=shared.EntitySchemaUIConfigSharing(
                show_sharing_button=True,
            ),
            single_view=shared.RedirectEntityView(
                route='/app/pricing-hub/product/:entityId',
                view_type=shared.RedirectEntityViewViewType.REDIRECT,
            ),
            table_view=shared.EntityViewDisabled(
                view_type=shared.EntityViewDisabledViewType.DISABLED,
            ),
        ),
        version=980649,
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

