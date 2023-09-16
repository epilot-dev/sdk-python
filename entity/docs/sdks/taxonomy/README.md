# Taxonomy

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
            'a63aae8d-6786-44db-b675-fd5e60b375ed',
        ],
    ),
    taxonomy_slug='numquam',
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
    query='doloribus',
    size=3817.6,
    taxonomy_slug='reiciendis',
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
                created_at=dateutil.parser.isoparse('2021-03-11T09:18:18.070Z'),
                id='e41f3331-7fe3-45b6-8eb1-ea426555ba3c',
                name='Wallbox PV',
                parents=[
                    '28744ed5-3b88-4f3a-8d8f-5c0b2f2fb7b1',
                ],
                updated_at=dateutil.parser.isoparse('2022-06-01T06:14:54.164Z'),
            ),
        ],
        delete=[
            'a276b269-16fe-41f0-8f42-94e3698f447f',
        ],
        update=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-12-22T16:38:34.482Z'),
                id='3e8b445e-80ca-455e-bd20-e457e1858b6a',
                name='Wallbox PV',
                parents=[
                    '89fbe3a5-aa8e-4482-8d0a-b4075088e518',
                ],
                updated_at=dateutil.parser.isoparse('2022-11-05T22:13:21.002Z'),
            ),
        ],
    ),
    taxonomy_slug='sit',
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

