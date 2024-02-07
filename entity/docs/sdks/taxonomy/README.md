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
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.taxonomy.get_taxonomy(taxonomy_slug='string')

if res.taxonomy is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `taxonomy_slug`    | *str*              | :heavy_check_mark: | Taxonomy slug      |


### Response

**[operations.GetTaxonomyResponse](../../models/operations/gettaxonomyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_taxonomies

List taxonomies in an organisation

### Example Usage

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.taxonomy.list_taxonomies()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.ListTaxonomiesResponse](../../models/operations/listtaxonomiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## taxonomies_classifications_search

List taxonomy classifications in an organisation based on taxonomy slug

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.taxonomy.taxonomies_classifications_search(taxonomy_slug='string', request_body=operations.TaxonomiesClassificationsSearchRequestBody(
    classification_ids=[
        '140d9b86-5e3a-4ede-b609-1ca17c7aaeae',
    ],
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy_slug`                                                                                                                          | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | Taxonomy slug                                                                                                                            |
| `request_body`                                                                                                                           | [Optional[operations.TaxonomiesClassificationsSearchRequestBody]](../../models/operations/taxonomiesclassificationssearchrequestbody.md) | :heavy_minus_sign:                                                                                                                       | N/A                                                                                                                                      |


### Response

**[operations.TaxonomiesClassificationsSearchResponse](../../models/operations/taxonomiesclassificationssearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## taxonomy_autocomplete

Taxonomies autocomplete

### Example Usage

```python
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.taxonomy.taxonomy_autocomplete(taxonomy_slug='string', query='string', size=6737.99)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `taxonomy_slug`                     | *str*                               | :heavy_check_mark:                  | Taxonomy slug                       |
| `query`                             | *Optional[str]*                     | :heavy_minus_sign:                  | Input to autocomplete               |
| `size`                              | *Optional[float]*                   | :heavy_minus_sign:                  | Minimum number of results to return |


### Response

**[operations.TaxonomyAutocompleteResponse](../../models/operations/taxonomyautocompleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_classifications_for_taxonomy

Update taxonomies in an organisation based in taxonomy slug

### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components, operations

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.taxonomy.update_classifications_for_taxonomy(taxonomy_slug='string', classifications_update=components.ClassificationsUpdate(
    create=[
        components.TaxonomyClassification(
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
        components.TaxonomyClassification(
            name='Wallbox PV',
            parents=[
                '42062aff-2df8-4b95-9241-f68f95bbd35c',
            ],
        ),
    ],
))

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `taxonomy_slug`                                                                                | *str*                                                                                          | :heavy_check_mark:                                                                             | Taxonomy slug                                                                                  |
| `classifications_update`                                                                       | [Optional[components.ClassificationsUpdate]](../../models/components/classificationsupdate.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |


### Response

**[operations.UpdateClassificationsForTaxonomyResponse](../../models/operations/updateclassificationsfortaxonomyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
