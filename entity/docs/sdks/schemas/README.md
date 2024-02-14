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
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## get_schema

By default gets the latest version of the Schema and to get the specific version of schema pass the id.

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## get_schema_versions

Get all versions of this schema ordered by the latest versions including drafts.

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetSchemaVersionsRequest(
    slug='contact',
    fields=[
        'id',
        'attributes',
        'capabilites',
    ],
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
| errors.SDKError | 4x-5xx          | */*             |

## list_schema_blueprints

List canonical versions of all available schemas

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## list_schemas

Get the latest versions of all schemas

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## list_taxonomy_classifications_for_schema

List taxonomy classifications for a given schema

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## put_schema

Create or update a schema with a new version

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.put_schema(slug='contact', entity_schema=components.EntitySchema(
    attributes=[
        components.TextAttribute(
            label='Email',
            name='email',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            required=True,
            type=components.TextAttributeType.STRING,
        ),
        components.TextAttribute(
            label='First Name',
            name='first_name',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            type=components.TextAttributeType.STRING,
        ),
        components.TextAttribute(
            label='Last Name',
            name='last_name',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            type=components.TextAttributeType.STRING,
        ),
        components.TextAttribute(
            label='Birthdate',
            name='birthdate',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            type=components.TextAttributeType.STRING,
        ),
        components.TextAttribute(
            label='Salutation',
            name='salutation',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            type=components.TextAttributeType.STRING,
        ),
        components.TextAttribute(
            label='Marketing permission',
            name='marketing_permission',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            type=components.TextAttributeType.STRING,
        ),
        components.TextAttribute(
            label='Image',
            name='image',
            constraints=components.TextAttributeConstraints(),
            feature_flag='FF_MY_FEATURE_FLAG',
            layout='full_width',
            order=0,
            type=components.TextAttributeType.STRING,
        ),
    ],
    capabilities=[
        components.EntityCapability(
            name='customer_messaging',
            feature_flag='FF_MY_FEATURE_FLAG',
            title='Messaging',
        ),
    ],
    name='Contact',
    plural='Contacts',
    slug='contact',
    draft=False,
    explicit_search_mappings={
        'image': components.SearchMappings(
            index=False,
            type=components.SearchMappingsType.KEYWORD,
        ),
    },
    feature_flag='FF_MY_FEATURE_FLAG',
    group_settings=[
        components.GroupSettings(
            id='Contact Details',
            label='Contact Details',
            expanded=True,
            feature_flag='FF_MY_FEATURE_FLAG',
            order=1,
            render_condition='_is_composite_price = "false"',
        ),
        components.GroupSettings(
            id='Address Details',
            label='Address Details',
            expanded=False,
            feature_flag='FF_MY_FEATURE_FLAG',
            info_tooltip_title=components.InfoTooltipTitle(
                default='These informations are provided by the partner company and cannot be edited.',
                key='partner.partner_information_group_tooltip',
            ),
            order=2,
            render_condition='_is_composite_price = "false"',
        ),
    ],
    icon='person',
    published=False,
    title_template='{{first_name}} {{last_name}}',
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
| errors.SDKError | 4x-5xx          | */*             |
