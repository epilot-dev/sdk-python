# Schemas
(*schemas*)

## Overview

Model Entities

### Available Operations

* [delete_schema](#delete_schema) - deleteSchema
* [delete_schema_attribute](#delete_schema_attribute) - deleteSchemaAttribute
* [delete_schema_capability](#delete_schema_capability) - deleteSchemaCapability
* [delete_schema_group](#delete_schema_group) - deleteSchemaGroup
* [get_json_schema](#get_json_schema) - getJsonSchema
* [get_schema](#get_schema) - getSchema
* [get_schema_attribute](#get_schema_attribute) - getSchemaAttribute
* [get_schema_capability](#get_schema_capability) - getSchemaCapability
* [get_schema_example](#get_schema_example) - getSchemaExample
* [get_schema_group](#get_schema_group) - getSchemaGroup
* [get_schema_versions](#get_schema_versions) - getSchemaVersions
* [list_schema_blueprints](#list_schema_blueprints) - listSchemaBlueprints
* [list_schemas](#list_schemas) - listSchemas
* [list_taxonomy_classifications_for_schema](#list_taxonomy_classifications_for_schema) - listTaxonomyClassificationsForSchema
* [put_schema](#put_schema) - putSchema
* [put_schema_attribute](#put_schema_attribute) - putSchemaAttribute
* [put_schema_capability](#put_schema_capability) - putSchemaCapability
* [put_schema_group](#put_schema_group) - putSchemaGroup

## delete_schema

Delete a schema, or a specific version of a schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.schemas.delete_schema(request={
    "slug": "contact",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeleteSchemaRequest](../../models/deleteschemarequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_schema_attribute

Deletes an attribute from a schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.delete_schema_attribute(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.DeleteSchemaAttributeRequest](../../models/deleteschemaattributerequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |


### Response

**[models.AttributeWithCompositeID](../../models/attributewithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_schema_capability

Deletes a Capability from a schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.delete_schema_capability(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.DeleteSchemaCapabilityRequest](../../models/deleteschemacapabilityrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |


### Response

**[models.EntityCapabilityWithCompositeID](../../models/entitycapabilitywithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_schema_group

Deletes a Capability from a schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.delete_schema_group(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.DeleteSchemaGroupRequest](../../models/deleteschemagrouprequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |


### Response

**[models.EntitySchemaGroupWithCompositeID](../../models/entityschemagroupwithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_json_schema

Get formal JSON schema definition draft 2020-12 for the given epilot schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_json_schema(request={
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetJSONSchemaRequest](../../models/getjsonschemarequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.GetJSONSchemaResponseBody](../../models/getjsonschemaresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_schema

By default gets the latest version of the Schema and to get the specific version of schema pass the id.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_schema(request={
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetSchemaRequest](../../models/getschemarequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntitySchemaItem](../../models/entityschemaitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_schema_attribute

Get a schema attribute from given attribute ID

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_schema_attribute(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.GetSchemaAttributeRequest](../../models/getschemaattributerequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |


### Response

**[models.AttributeWithCompositeID](../../models/attributewithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_schema_capability

Get a schema capability from given capability ID

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_schema_capability(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.GetSchemaCapabilityRequest](../../models/getschemacapabilityrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |


### Response

**[models.EntityCapabilityWithCompositeID](../../models/entitycapabilitywithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_schema_example

Get a full example entity for the given schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_schema_example(request={
    "slug": "contact",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetSchemaExampleRequest](../../models/getschemaexamplerequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |


### Response

**[models.GetSchemaExampleResponseBody](../../models/getschemaexampleresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_schema_group

Get a schema group from given group composite ID

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_schema_group(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetSchemaGroupRequest](../../models/getschemagrouprequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.EntitySchemaGroupWithCompositeID](../../models/entityschemagroupwithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_schema_versions

Get all versions of this schema ordered by the latest versions including drafts.

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.get_schema_versions(request={
    "slug": "contact",
    "fields": [
        "id",
        "attributes",
        "capabilites",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.GetSchemaVersionsRequest](../../models/getschemaversionsrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |


### Response

**[models.GetSchemaVersionsResponseBody](../../models/getschemaversionsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_schema_blueprints

List canonical versions of all available schemas

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.list_schema_blueprints()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListSchemaBlueprintsResponseBody](../../models/listschemablueprintsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_schemas

Get the latest versions of all schemas

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.list_schemas()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListSchemasRequest](../../models/listschemasrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListSchemasResponseBody](../../models/listschemasresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_taxonomy_classifications_for_schema

List taxonomy classifications for a given schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.list_taxonomy_classifications_for_schema(request={
    "slug": "contact",
    "taxonomy_slug": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [models.ListTaxonomyClassificationsForSchemaRequest](../../models/listtaxonomyclassificationsforschemarequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |


### Response

**[models.ListTaxonomyClassificationsForSchemaResponseBody](../../models/listtaxonomyclassificationsforschemaresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_schema

Create or update a schema with a new version

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.put_schema(request={
    "slug": "contact",
    "entity_schema": {
        "attributes": [

        ],
        "capabilities": [

        ],
        "name": "Contact",
        "plural": "Contacts",
        "slug": "contact",
        "draft": False,
        "enable_setting": [
            "360_features",
        ],
        "explicit_search_mappings": {
            "image": {
                "index": False,
                "type": epilot_entity.SearchMappingsType.KEYWORD,
            },
        },
        "feature_flag": "FF_MY_FEATURE_FLAG",
        "group_settings": [
            {
                "id": "e18a532b-ae79-4d86-a6a5-e5dbfb579d14",
                "label": "Contact Details",
                "purpose": [
                    "taxonomy-slug:classification-slug",
                ],
                "expanded": True,
                "feature_flag": "FF_MY_FEATURE_FLAG",
                "order": 1,
                "render_condition": "_is_composite_price = \"false\"",
            },
            {
                "id": "e9a1ae28-27ba-4fa0-a79c-e279cc5c4a6e",
                "label": "Address Details",
                "purpose": [
                    "taxonomy-slug:classification-slug",
                ],
                "expanded": False,
                "feature_flag": "FF_MY_FEATURE_FLAG",
                "info_tooltip_title": {
                    "default": "These informations are provided by the partner company and cannot be edited.",
                    "key": "partner.partner_information_group_tooltip",
                },
                "order": 2,
                "render_condition": "_is_composite_price = \"false\"",
            },
        ],
        "icon": "person",
        "published": False,
        "title_template": "{{first_name}} {{last_name}}",
        "ui_config": {
            "create_view": {
                "route": "/app/pricing-hub/product/:entityId",
            },
            "edit_view": {
                "route": "/app/pricing-hub/product/:entityId",
            },
            "list_item": {
                "quick_actions": [
                    {
                        "action": "preview_file",
                        "label": "Preview File",
                        "icon": "visibility",
                        "permission": "entity:edit",
                    },
                ],
                "summary_attributes": [
                    {
                        "label": "<value>",
                        "value": "<value>",
                    },
                ],
            },
            "sharing": {
                "show_sharing_button": True,
            },
            "single_view": {},
            "table_view": {
                "route": "/app/pricing-hub/product/:entityId",
            },
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PutSchemaRequest](../../models/putschemarequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.EntitySchemaItem](../../models/entityschemaitem.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_schema_attribute

Updates an attribute in the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.put_schema_attribute(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
    "attribute_with_composite_id": {
        "label": "<value>",
        "name": "<value>",
        "purpose": [
            "taxonomy-slug:classification-slug",
        ],
        "constraints": {},
        "feature_flag": "FF_MY_FEATURE_FLAG",
        "id": "d5839b94-ba20-4225-a78e-76951d352bd6",
        "info_helpers": {
            "hint_tooltip_placement": "top",
        },
        "layout": "full_width",
        "order": 0,
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.PutSchemaAttributeRequest](../../models/putschemaattributerequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |


### Response

**[models.AttributeWithCompositeID](../../models/attributewithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_schema_capability

Adds or updates an capability in the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.put_schema_capability(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
    "entity_capability_with_composite_id": {
        "name": "customer_messaging",
        "purpose": [
            "taxonomy-slug:classification-slug",
        ],
        "attributes": [

        ],
        "feature_flag": "FF_MY_FEATURE_FLAG",
        "id": "d5839b94-ba20-4225-a78e-76951d352bd6",
        "title": "Messaging",
        "ui_hooks": [
            epilot_entity.EntityCapabilityWithCompositeIDUIHooks(
                hook="EntityDetailsV2:Tab",
                component="PricingItems",
                icon="email",
                import_="@epilot360/notes",
                order=10,
                render_condition="_is_composite_price = \"false\"",
                required_permission={
                    "action": "note:view",
                    "resource": "123",
                },
                route="notes",
                title="Notes",
            ),
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.PutSchemaCapabilityRequest](../../models/putschemacapabilityrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |


### Response

**[models.EntityCapabilityWithCompositeID](../../models/entitycapabilitywithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_schema_group

Adds or updates an capability in the schema

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.schemas.put_schema_group(request={
    "composite_id": "contact:97644baa-083f-4e49-9188-fcff2ecaad7d",
    "entity_schema_group_with_composite_id": {
        "id": "e18a532b-ae79-4d86-a6a5-e5dbfb579d14",
        "label": "Contact Details",
        "purpose": [
            "taxonomy-slug:classification-slug",
        ],
        "feature_flag": "FF_MY_FEATURE_FLAG",
        "render_condition": "_is_composite_price = \"false\"",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.PutSchemaGroupRequest](../../models/putschemagrouprequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.EntitySchemaGroupWithCompositeID](../../models/entityschemagroupwithcompositeid.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
