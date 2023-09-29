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
    taxonomy_slug='Oklahoma azure illum',
)

res = s.taxonomy.taxonomies_classifications_search(req)

if res.taxonomies_classifications_search_200_application_json_object is not None:
    # handle response
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
    query='Polarised optio Hybrid',
    size=7186.02,
    taxonomy_slug='Ball',
)

res = s.taxonomy.taxonomy_autocomplete(req)

if res.taxonomy_autocomplete_200_application_json_object is not None:
    # handle response
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
                created_at=dateutil.parser.isoparse('2023-01-29T09:39:45.161Z'),
                id='4e342f29-dee0-402b-8415-ef6fe03f06e9',
                name='Wallbox PV',
                parents=[
                    '998bd322-c31e-42b7-b181-91a2c6ad60b4',
                ],
                updated_at=dateutil.parser.isoparse('2021-07-20T21:22:16.417Z'),
            ),
        ],
        delete=[
            '062aff2d-f8b9-4512-81f6-8f95bbd35ce8',
        ],
        update=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2023-06-17T13:37:21.887Z'),
                id='b159c7e2-9866-4889-9ce5-7236fb33115f',
                name='Wallbox PV',
                parents=[
                    'c5f1737e-932d-42ff-8b5b-7733cd73fa8c',
                ],
                updated_at=dateutil.parser.isoparse('2021-03-21T21:08:25.425Z'),
            ),
        ],
    ),
    taxonomy_slug='flexibility Cadillac North',
)

res = s.taxonomy.update_classifications_for_taxonomy(req)

if res.update_classifications_for_taxonomy_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.UpdateClassificationsForTaxonomyRequest](../../models/operations/updateclassificationsfortaxonomyrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.UpdateClassificationsForTaxonomyResponse](../../models/operations/updateclassificationsfortaxonomyresponse.md)**

