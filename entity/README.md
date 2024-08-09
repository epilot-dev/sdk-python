# epilot-entity

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=entity
```

Poetry
```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=entity
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(request={
    "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_entity
from epilot_entity import Epilot

async def main():
    s = Epilot(
        security=epilot_entity.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    res = await s.activity.attach_activity_async(request={
        "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [activity](docs/sdks/activitysdk/README.md)

* [attach_activity](docs/sdks/activitysdk/README.md#attach_activity) - attachActivity
* [create_activity](docs/sdks/activitysdk/README.md#create_activity) - createActivity
* [get_activity](docs/sdks/activitysdk/README.md#get_activity) - getActivity
* [get_entity_activity_feed](docs/sdks/activitysdk/README.md#get_entity_activity_feed) - getEntityActivityFeed

### [schemas](docs/sdks/schemas/README.md)

* [delete_schema](docs/sdks/schemas/README.md#delete_schema) - deleteSchema
* [delete_schema_attribute](docs/sdks/schemas/README.md#delete_schema_attribute) - deleteSchemaAttribute
* [delete_schema_capability](docs/sdks/schemas/README.md#delete_schema_capability) - deleteSchemaCapability
* [delete_schema_group](docs/sdks/schemas/README.md#delete_schema_group) - deleteSchemaGroup
* [get_json_schema](docs/sdks/schemas/README.md#get_json_schema) - getJsonSchema
* [get_schema](docs/sdks/schemas/README.md#get_schema) - getSchema
* [get_schema_attribute](docs/sdks/schemas/README.md#get_schema_attribute) - getSchemaAttribute
* [get_schema_capability](docs/sdks/schemas/README.md#get_schema_capability) - getSchemaCapability
* [get_schema_example](docs/sdks/schemas/README.md#get_schema_example) - getSchemaExample
* [get_schema_group](docs/sdks/schemas/README.md#get_schema_group) - getSchemaGroup
* [get_schema_versions](docs/sdks/schemas/README.md#get_schema_versions) - getSchemaVersions
* [list_schema_blueprints](docs/sdks/schemas/README.md#list_schema_blueprints) - listSchemaBlueprints
* [list_schemas](docs/sdks/schemas/README.md#list_schemas) - listSchemas
* [list_taxonomy_classifications_for_schema](docs/sdks/schemas/README.md#list_taxonomy_classifications_for_schema) - listTaxonomyClassificationsForSchema
* [put_schema](docs/sdks/schemas/README.md#put_schema) - putSchema
* [put_schema_attribute](docs/sdks/schemas/README.md#put_schema_attribute) - putSchemaAttribute
* [put_schema_capability](docs/sdks/schemas/README.md#put_schema_capability) - putSchemaCapability
* [put_schema_group](docs/sdks/schemas/README.md#put_schema_group) - putSchemaGroup

### [taxonomy](docs/sdks/taxonomysdk/README.md)

* [create_taxonomy](docs/sdks/taxonomysdk/README.md#create_taxonomy) - createTaxonomy
* [create_taxonomy_classification](docs/sdks/taxonomysdk/README.md#create_taxonomy_classification) - createTaxonomyClassification
* [delete_taxonomy](docs/sdks/taxonomysdk/README.md#delete_taxonomy) - deleteTaxonomy
* [delete_taxonomy_classification](docs/sdks/taxonomysdk/README.md#delete_taxonomy_classification) - deleteTaxonomyClassification
* [get_taxonomy](docs/sdks/taxonomysdk/README.md#get_taxonomy) - getTaxonomy
* [list_taxonomies](docs/sdks/taxonomysdk/README.md#list_taxonomies) - listTaxonomies
* [taxonomies_classifications_search](docs/sdks/taxonomysdk/README.md#taxonomies_classifications_search) - taxonomiesClassificationsSearch
* [taxonomy_autocomplete](docs/sdks/taxonomysdk/README.md#taxonomy_autocomplete) - taxonomyAutocomplete
* [update_classifications_for_taxonomy](docs/sdks/taxonomysdk/README.md#update_classifications_for_taxonomy) - updateClassificationsForTaxonomy
* [update_taxonomy](docs/sdks/taxonomysdk/README.md#update_taxonomy) - updateTaxonomy
* [update_taxonomy_classification](docs/sdks/taxonomysdk/README.md#update_taxonomy_classification) - updateTaxonomyClassification

### [saved_views](docs/sdks/savedviews/README.md)

* [create_saved_view](docs/sdks/savedviews/README.md#create_saved_view) - createSavedView
* [delete_saved_view](docs/sdks/savedviews/README.md#delete_saved_view) - deleteSavedView
* [get_saved_view](docs/sdks/savedviews/README.md#get_saved_view) - getSavedView
* [list_favorite_views_for_user](docs/sdks/savedviews/README.md#list_favorite_views_for_user) - listFavoriteViewsForUser
* [list_saved_views](docs/sdks/savedviews/README.md#list_saved_views) - listSavedViews
* [update_saved_view](docs/sdks/savedviews/README.md#update_saved_view) - updateSavedView

### [entities](docs/sdks/entities/README.md)

* [autocomplete](docs/sdks/entities/README.md#autocomplete) - autocomplete
* [create_entity](docs/sdks/entities/README.md#create_entity) - createEntity
* [delete_entity](docs/sdks/entities/README.md#delete_entity) - deleteEntity
* [get_entity](docs/sdks/entities/README.md#get_entity) - getEntity
* [get_entity_v2](docs/sdks/entities/README.md#get_entity_v2) - getEntityV2
* [list_entities](docs/sdks/entities/README.md#list_entities) - listEntities
* [patch_entity](docs/sdks/entities/README.md#patch_entity) - patchEntity
* [search_entities](docs/sdks/entities/README.md#search_entities) - searchEntities
* [update_entity](docs/sdks/entities/README.md#update_entity) - updateEntity
* [upsert_entity](docs/sdks/entities/README.md#upsert_entity) - upsertEntity
* [validate_entity](docs/sdks/entities/README.md#validate_entity) - validateEntity

### [relations](docs/sdks/relations/README.md)

* [add_relations](docs/sdks/relations/README.md#add_relations) - addRelations
* [delete_relation](docs/sdks/relations/README.md#delete_relation) - deleteRelation
* [get_related_entities_count](docs/sdks/relations/README.md#get_related_entities_count) - getRelatedEntitiesCount
* [get_relations](docs/sdks/relations/README.md#get_relations) - getRelations
* [get_relations_v2](docs/sdks/relations/README.md#get_relations_v2) - getRelationsV2
* [get_relations_v3](docs/sdks/relations/README.md#get_relations_v3) - getRelationsV3
* [remove_relations](docs/sdks/relations/README.md#remove_relations) - removeRelations
* [update_relation](docs/sdks/relations/README.md#update_relation) - updateRelation

### [export](docs/sdks/export/README.md)

* [export_entities](docs/sdks/export/README.md#export_entities) - exportEntities

### [entity_import](docs/sdks/entityimport/README.md)

* [import_entities](docs/sdks/entityimport/README.md#import_entities) - Import Entities
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.EntityValidationResultError | 422                                | application/json                   |
| models.SDKError                    | 4xx-5xx                            | */*                                |

### Example

```python
import epilot_entity
from epilot_entity import Epilot, models

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = None
try:
    res = s.entities.validate_entity(request={
    "slug": "contact",
    "entity": epilot_entity.EntityInput(
        acl=epilot_entity.EntityACL(
            delete=[
                "org:456",
            ],
            edit=[
                "org:456",
            ],
            view=[
                "org:456",
                "org:789",
            ],
            **{

            },
        ),
        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        schema_="contact",
        tags=[
            "example",
            "mock",
        ],
        **{
            "_org": "123",
            "_owners": [
                {
                    "org_id": "123",
                    "user_id": "123",
                },
            ],
            "_created_at": "2021-02-09T12:41:43.662Z",
            "_updated_at": "2021-02-09T12:41:43.662Z",
        },
    ),
})

except models.EntityValidationResultError as e:
    # handle exception
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://entity.sls.epilot.io` | None |

#### Example

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    server_idx=0,
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(request={
    "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    server_url="https://entity.sls.epilot.io",
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(request={
    "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from epilot_entity import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_entity import Epilot
from epilot_entity.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Epilot(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(request={
    "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(request={
    "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |
| `epilot_org`  | apiKey        | API key       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.activity.attach_activity(request={
    "id": "01F130Q52Q6MWSNS8N2AVXV4JN",
})

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from epilot_entity import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_entity"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
