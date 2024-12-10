# TaxonomySDK
(*taxonomy*)

## Overview

Taxonomies and Classifications

### Available Operations

* [bulk_delete_classifications](#bulk_delete_classifications) - bulkDeleteClassifications
* [bulk_move_classifications](#bulk_move_classifications) - bulkMoveClassifications
* [create_taxonomy](#create_taxonomy) - createTaxonomy
* [delete_taxonomy](#delete_taxonomy) - deleteTaxonomy
* [delete_taxonomy_classification](#delete_taxonomy_classification) - deleteTaxonomyClassification
* [get_taxonomy](#get_taxonomy) - getTaxonomy
* [get_taxonomy_bulk_action_job_by_id](#get_taxonomy_bulk_action_job_by_id) - getTaxonomyBulkActionJobById
* [get_taxonomy_bulk_action_jobs](#get_taxonomy_bulk_action_jobs) - getTaxonomyBulkActionJobs
* [get_taxonomy_classification](#get_taxonomy_classification) - getTaxonomyClassification
* [list_taxonomies](#list_taxonomies) - listTaxonomies
* [taxonomies_classifications_search](#taxonomies_classifications_search) - taxonomiesClassificationsSearch
* [taxonomy_autocomplete](#taxonomy_autocomplete) - taxonomyAutocomplete
* [update_classifications_for_taxonomy](#update_classifications_for_taxonomy) - updateClassificationsForTaxonomy
* [update_taxonomy](#update_taxonomy) - updateTaxonomy
* [update_taxonomy_classification](#update_taxonomy_classification) - updateTaxonomyClassification

## bulk_delete_classifications

Permanently deletes taxonomy classifications. The classifications are deleted through a bulk
async operation which also deletes all references of the deleted classifications from the entities
referencing them.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.bulk_delete_classifications(request={
        "classification_ids": [
            "taxonomy-slug:classification-slug",
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.BulkDeleteClassificationsRequestBody](../../models/bulkdeleteclassificationsrequestbody.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.TaxonomyBulkJobTriggerResponse](../../models/taxonomybulkjobtriggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## bulk_move_classifications

Moves classifications from one taxonomy to another, through a bulk async operation which
also updates all references from the old classification to the new one under the target taxonomy.


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.bulk_move_classifications(request={
        "classification_ids": [
            "taxonomy-slug:classification-slug",
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.BulkMoveClassificationsRequestBody](../../models/bulkmoveclassificationsrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.TaxonomyBulkJobTriggerResponse](../../models/taxonomybulkjobtriggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_taxonomy

Create a new taxonomy

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.create_taxonomy(request={
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    epilot.taxonomy.delete_taxonomy(request={
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.delete_taxonomy_classification(request={
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.get_taxonomy(request={
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

## get_taxonomy_bulk_action_job_by_id

Gets a bulk action job by job id

### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.get_taxonomy_bulk_action_job_by_id(request={
        "job_id": "<id>",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.GetTaxonomyBulkActionJobByIDRequest](../../models/gettaxonomybulkactionjobbyidrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[List[models.TaxonomyBulkJob]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_taxonomy_bulk_action_jobs

Gets bulk actions jobs by job status:
- <undefined> = all active jobs
- PENDING = all active jobs
- FAILED = all failed jobs
- COMPLETED = all completed jobs


### Example Usage

```python
import epilot_entity
from epilot_entity import Epilot

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.get_taxonomy_bulk_action_jobs()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.GetTaxonomyBulkActionJobsRequest](../../models/gettaxonomybulkactionjobsrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[List[models.TaxonomyBulkJob]](../../models/.md)**

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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.get_taxonomy_classification(request={
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.list_taxonomies()

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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.taxonomies_classifications_search(request={
        "request_body": {
            "classification_ids": [
                "taxonomy-slug:classification-slug",
            ],
        },
        "archived": False,
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.taxonomy_autocomplete(request={
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.update_classifications_for_taxonomy(request={
        "taxonomy_slug": "<value>",
        "classifications_update": {
            "create": [
                {
                    "name": "Wallbox PV",
                    "manifest": [
                        "123e4567-e89b-12d3-a456-426614174000",
                    ],
                    "color": "#FF5733",
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
                    "color": "#FF5733",
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
                    "color": "#FF5733",
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
                    "color": "#FF5733",
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
                    "color": "#FF5733",
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.update_taxonomy(request={
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

with Epilot(
    security=epilot_entity.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = epilot.taxonomy.update_taxonomy_classification(request={
        "classification_slug": "purpose:<name>",
        "taxonomy_classification": {
            "name": "Wallbox PV",
            "manifest": [
                "123e4567-e89b-12d3-a456-426614174000",
            ],
            "color": "#FF5733",
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