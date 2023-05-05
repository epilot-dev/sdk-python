# taxonomy

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
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetTaxonomyRequest(
    taxonomy_slug='purpose',
)

res = s.taxonomy.get_taxonomy(req)

if res.taxonomy is not None:
    # handle response
```

## list_taxonomies

List taxonomies in an organisation

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.taxonomy.list_taxonomies()

if res.list_taxonomies_200_application_json_object is not None:
    # handle response
```

## taxonomies_classifications_search

List taxonomy classifications in an organisation based on taxonomy slug

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TaxonomiesClassificationsSearchRequest(
    request_body=operations.TaxonomiesClassificationsSearchRequestBody(
        classification_ids=[
            '3b9da3f2-ceda-47e2-bf22-57411faf4b75',
            '44e472e8-0285-47a5-b404-63a7d575f140',
        ],
    ),
    taxonomy_slug='aut',
)

res = s.taxonomy.taxonomies_classifications_search(req)

if res.taxonomies_classifications_search_200_application_json_object is not None:
    # handle response
```

## taxonomy_autocomplete

Taxonomies autocomplete

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.TaxonomyAutocompleteRequest(
    query='eveniet',
    size=4837.53,
    taxonomy_slug='commodi',
)

res = s.taxonomy.taxonomy_autocomplete(req)

if res.taxonomy_autocomplete_200_application_json_object is not None:
    # handle response
```

## update_classifications_for_taxonomy

Update taxonomies in an organisation based in taxonomy slug

### Example Usage

```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateClassificationsForTaxonomyRequest(
    classifications_update=shared.ClassificationsUpdate(
        create=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2021-05-09T16:27:58.630Z'),
                id='7334ec1b-781b-436a-8808-8d100efada20',
                name='Wallbox PV',
                parents=[
                    'ef0422eb-2164-4cf9-ab83-66c723ffda9e',
                ],
                updated_at=dateutil.parser.isoparse('2022-08-10T13:36:39.170Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2021-02-24T20:48:23.002Z'),
                id='e4825c1f-c0e1-415c-80bf-f918544ec42d',
                name='Wallbox PV',
                parents=[
                    'fcce8f19-7777-43e6-b562-a7b408f05e3d',
                    '48fdaf31-3a1f-45fd-9425-9c0b36f25ea9',
                    '44f3b756-c11f-46c3-ba51-26243835bbc0',
                    '5a23a45c-efc5-4fde-90a0-ce2169e51001',
                ],
                updated_at=dateutil.parser.isoparse('2021-06-20T22:36:53.570Z'),
            ),
        ],
        delete=[
            'dc5e3476-2799-4bfb-be69-49fb2bb4ecae',
            '6c3d5db3-adeb-4d5d-aea4-c506a8aa94c0',
        ],
        update=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-09-13T00:32:01.100Z'),
                id='4cf5e9d9-a457-48ad-81ac-600dec001ac8',
                name='Wallbox PV',
                parents=[
                    '2e2ec09f-f8f0-4f81-aff3-477c13e902c1',
                ],
                updated_at=dateutil.parser.isoparse('2022-11-19T10:56:46.631Z'),
            ),
        ],
    ),
    taxonomy_slug='odit',
)

res = s.taxonomy.update_classifications_for_taxonomy(req)

if res.update_classifications_for_taxonomy_200_application_json_object is not None:
    # handle response
```
