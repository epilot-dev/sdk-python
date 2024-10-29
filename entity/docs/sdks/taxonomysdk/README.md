# TaxonomySDK
(*taxonomy*)

## Overview

Taxonomies and Classifications

### Available Operations

* [create_taxonomy](#create_taxonomy) - createTaxonomy
* [delete_taxonomy](#delete_taxonomy) - deleteTaxonomy
* [delete_taxonomy_classification](#delete_taxonomy_classification) - deleteTaxonomyClassification
* [get_taxonomy](#get_taxonomy) - getTaxonomy
* [get_taxonomy_classification](#get_taxonomy_classification) - getTaxonomyClassification
* [list_taxonomies](#list_taxonomies) - listTaxonomies
* [taxonomies_classifications_search](#taxonomies_classifications_search) - taxonomiesClassificationsSearch
* [taxonomy_autocomplete](#taxonomy_autocomplete) - taxonomyAutocomplete
* [update_classifications_for_taxonomy](#update_classifications_for_taxonomy) - updateClassificationsForTaxonomy
* [update_taxonomy](#update_taxonomy) - updateTaxonomy
* [update_taxonomy_classification](#update_taxonomy_classification) - updateTaxonomyClassification

## create_taxonomy

Create a new taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.create_taxonomy(request={
    "color": "#FF5733",
    "enabled": True,
    "icon": "purpose",
    "name": "Purpose",
    "order": 10,
    "plural": "Purposes",
    "slug": "purpose",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TaxonomyInput](../../models/taxonomyinput.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Taxonomy](../../models/taxonomy.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_taxonomy

Delete a taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

s.taxonomy.delete_taxonomy(request={
    "taxonomy_slug": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.DeleteTaxonomyRequest](../../models/deletetaxonomyrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_taxonomy_classification

Delete a classification for a taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.delete_taxonomy_classification(request={
    "classification_slug": "purpose:<name>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.DeleteTaxonomyClassificationRequest](../../models/deletetaxonomyclassificationrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.TaxonomyClassification](../../models/taxonomyclassification.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_taxonomy

Get taxonomy by slug

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.get_taxonomy(request={
    "taxonomy_slug": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetTaxonomyRequest](../../models/gettaxonomyrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Taxonomy](../../models/taxonomy.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_taxonomy_classification

Get a classification for a taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.get_taxonomy_classification(request={
    "classification_slug": "purpose:<name>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.GetTaxonomyClassificationRequest](../../models/gettaxonomyclassificationrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.TaxonomyClassification](../../models/taxonomyclassification.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_taxonomies

List taxonomies in an organization

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.list_taxonomies()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ListTaxonomiesRequest](../../models/listtaxonomiesrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ListTaxonomiesResponseBody](../../models/listtaxonomiesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## taxonomies_classifications_search

List taxonomy classifications in an organization based on taxonomy slug

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.taxonomies_classifications_search(request={
    "request_body": {
        "classification_ids": [
            "taxonomy-slug:classification-slug",
        ],
    },
    "query": "sales",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.TaxonomiesClassificationsSearchRequest](../../models/taxonomiesclassificationssearchrequest.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.TaxonomiesClassificationsSearchResponseBody](../../models/taxonomiesclassificationssearchresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## taxonomy_autocomplete

Taxonomies autocomplete

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.taxonomy_autocomplete(request={
    "taxonomy_slug": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.TaxonomyAutocompleteRequest](../../models/taxonomyautocompleterequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.TaxonomyAutocompleteResponseBody](../../models/taxonomyautocompleteresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_classifications_for_taxonomy

Update the classifications for a taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.update_classifications_for_taxonomy(request={
    "taxonomy_slug": "<value>",
    "classifications_update": {
        "create": [
            {
                "name": "Wallbox PV",
                "manifest": [
                    "123e4567-e89b-12d3-a456-426614174000",
                ],
                "id": "taxonomy-slug:classification-slug",
                "parents": [
                    "taxonomy-slug:classification-slug",
                ],
                "slug": "wallbox-pv",
            },
            {
                "name": "Wallbox PV",
                "manifest": [
                    "123e4567-e89b-12d3-a456-426614174000",
                ],
                "id": "taxonomy-slug:classification-slug",
                "parents": [
                    "taxonomy-slug:classification-slug",
                ],
                "slug": "wallbox-pv",
            },
        ],
        "delete": [
            "taxonomy-slug:classification-slug",
        ],
        "update": [
            {
                "name": "Wallbox PV",
                "manifest": [
                    "123e4567-e89b-12d3-a456-426614174000",
                ],
                "id": "taxonomy-slug:classification-slug",
                "parents": [
                    "taxonomy-slug:classification-slug",
                ],
                "slug": "wallbox-pv",
            },
            {
                "name": "Wallbox PV",
                "manifest": [
                    "123e4567-e89b-12d3-a456-426614174000",
                ],
                "id": "taxonomy-slug:classification-slug",
                "parents": [
                    "taxonomy-slug:classification-slug",
                ],
                "slug": "wallbox-pv",
            },
            {
                "name": "Wallbox PV",
                "manifest": [
                    "123e4567-e89b-12d3-a456-426614174000",
                ],
                "id": "taxonomy-slug:classification-slug",
                "parents": [
                    "taxonomy-slug:classification-slug",
                ],
                "slug": "wallbox-pv",
            },
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                 | [models.UpdateClassificationsForTaxonomyRequest](../../models/updateclassificationsfortaxonomyrequest.md) | :heavy_check_mark:                                                                                        | The request object to use for the request.                                                                |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.UpdateClassificationsForTaxonomyResponseBody](../../models/updateclassificationsfortaxonomyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_taxonomy

Update a taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.update_taxonomy(request={
    "taxonomy_slug": "<value>",
    "taxonomy": {
        "color": "#FF5733",
        "enabled": True,
        "icon": "purpose",
        "name": "Purpose",
        "order": 10,
        "plural": "Purposes",
        "slug": "purpose",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.UpdateTaxonomyRequest](../../models/updatetaxonomyrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.Taxonomy](../../models/taxonomy.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_taxonomy_classification

Update a classification for a taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

s = Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = s.taxonomy.update_taxonomy_classification(request={
    "classification_slug": "purpose:<name>",
    "taxonomy_classification": {
        "name": "Wallbox PV",
        "manifest": [
            "123e4567-e89b-12d3-a456-426614174000",
        ],
        "id": "taxonomy-slug:classification-slug",
        "parents": [
            "taxonomy-slug:classification-slug",
        ],
        "slug": "wallbox-pv",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.UpdateTaxonomyClassificationRequest](../../models/updatetaxonomyclassificationrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.TaxonomyClassification](../../models/taxonomyclassification.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |