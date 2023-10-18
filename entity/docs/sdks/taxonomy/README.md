# Taxonomy
(*taxonomy*)

## Overview

Entity classification with Taxonomies

### Available Operations

* [get_taxonomy](#get_taxonomy) - getTaxonomy
* [list_taxonomies](#list_taxonomies) - listTaxonomies
* [taxonomies_classifications_search](#taxonomies_classifications_search) - taxonomiesClassificationsSearch
* [taxonomy_autocomplete](#taxonomy_autocomplete) - taxonomyAutocomplete
* [update_classifications_for_taxonomy](#update_classifications_for_taxonomy) - updateClassificationsForTaxonomy

## get_taxonomy

Get taxonomy by slug

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetTaxonomyRequest(
    taxonomy_slug='purpose',
)

res = s.taxonomy.get_taxonomy(req)

if res.taxonomy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetTaxonomyRequest](../../models/operations/gettaxonomyrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetTaxonomyResponse](../../models/operations/gettaxonomyresponse.md)**


## list_taxonomies

List taxonomies in an organisation

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.taxonomy.list_taxonomies()

if res.list_taxonomies_200_application_json_object is not None:
    # handle response
    pass
```


### Response

**[operations.ListTaxonomiesResponse](../../models/operations/listtaxonomiesresponse.md)**


## taxonomies_classifications_search

List taxonomy classifications in an organisation based on taxonomy slug

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.TaxonomiesClassificationsSearchRequest(
    request_body=operations.TaxonomiesClassificationsSearchRequestBody(
        classification_ids=[
            '140d9b86-5e3a-4ede-b609-1ca17c7aaeae',
        ],
    ),
    taxonomy_slug='Bicycle',
)

res = s.taxonomy.taxonomies_classifications_search(req)

if res.taxonomies_classifications_search_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.TaxonomiesClassificationsSearchRequest](../../models/operations/taxonomiesclassificationssearchrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.TaxonomiesClassificationsSearchResponse](../../models/operations/taxonomiesclassificationssearchresponse.md)**


## taxonomy_autocomplete

Taxonomies autocomplete

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.TaxonomyAutocompleteRequest(
    taxonomy_slug='Planner',
)

res = s.taxonomy.taxonomy_autocomplete(req)

if res.taxonomy_autocomplete_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.TaxonomyAutocompleteRequest](../../models/operations/taxonomyautocompleterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.TaxonomyAutocompleteResponse](../../models/operations/taxonomyautocompleteresponse.md)**


## update_classifications_for_taxonomy

Update taxonomies in an organisation based in taxonomy slug

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

req = operations.UpdateClassificationsForTaxonomyRequest(
    classifications_update=shared.ClassificationsUpdate(
        create=[
            shared.TaxonomyClassification(
                name='Wallbox PV',
                parents=[
                    'b4e342f2-9dee-4002-bc41-5ef6fe03f06e',
                ],
            ),
        ],
        delete=[
            '9998bd32-2c31-4e2b-b318-191a2c6ad60b',
        ],
        update=[
            shared.TaxonomyClassification(
                name='Wallbox PV',
                parents=[
                    '42062aff-2df8-4b95-9241-f68f95bbd35c',
                ],
            ),
        ],
    ),
    taxonomy_slug='or',
)

res = s.taxonomy.update_classifications_for_taxonomy(req)

if res.update_classifications_for_taxonomy_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.UpdateClassificationsForTaxonomyRequest](../../models/operations/updateclassificationsfortaxonomyrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.UpdateClassificationsForTaxonomyResponse](../../models/operations/updateclassificationsfortaxonomyresponse.md)**

