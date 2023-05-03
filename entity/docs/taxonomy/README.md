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
            '0960a668-151a-4472-af92-3c5949f83f35',
            '0cf876ff-b901-4c6e-8bb4-e243cf789ffa',
            'feda53e5-ae6e-40ac-984c-2b9c247c8837',
        ],
    ),
    taxonomy_slug='amet',
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
    query='laborum',
    size=2669.46,
    taxonomy_slug='perferendis',
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
                created_at=dateutil.parser.isoparse('2022-06-08T21:51:55.851Z'),
                id='42f32e55-0557-456f-9d56-d0bd0af2dfe1',
                name='Wallbox PV',
                parents=[
                    'db4f62cb-a3f8-4941-aebc-0b80a6924d3b',
                ],
                updated_at=dateutil.parser.isoparse('2022-02-12T16:14:24.791Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2020-02-07T14:24:22.214Z'),
                id='cc8f8950-10f5-4dd3-96fa-1804e54c82f1',
                name='Wallbox PV',
                parents=[
                    '8a363c88-73e4-4843-80b1-f6b8ca275a60',
                    'a04c495c-c699-4171-b51c-1bdb1cf4b888',
                ],
                updated_at=dateutil.parser.isoparse('2020-10-13T02:27:28.104Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2020-02-18T05:26:29.481Z'),
                id='c4ccca99-bc7f-4c0b-adce-10873e42b006',
                name='Wallbox PV',
                parents=[
                    '678878ba-8581-4a58-a08c-54fefa9c95f2',
                    'eac5565d-307c-4fee-8120-6e2813fa4a41',
                    'c480d3f2-132a-4f03-902d-514f4cc6f18b',
                    'f9621a6a-4f77-4a87-ae3e-4be752c65b34',
                ],
                updated_at=dateutil.parser.isoparse('2022-11-24T01:03:51.181Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2021-03-09T05:37:08.074Z'),
                id='3bb91c8d-975e-40e8-819d-8f84f144f3e0',
                name='Wallbox PV',
                parents=[
                    'edcc4aa5-f3ca-4bd9-85a9-72e056728227',
                    'b2d30947-0bf7-4a4f-a87c-f535a6fae54e',
                ],
                updated_at=dateutil.parser.isoparse('2021-01-13T05:01:27.465Z'),
            ),
        ],
        delete=[
            '0c321f02-3b75-4d23-a7fe-1a0cc8df79f0',
            'a396d90c-364b-47c1-9dfb-ace188b1c4ee',
        ],
        update=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2021-04-29T16:18:41.909Z'),
                id='c6ce611f-eeb1-4c7c-bdb6-eec74378ba25',
                name='Wallbox PV',
                parents=[
                    '17747dc9-15ad-42ca-b5dd-6723dc0f5ae2',
                ],
                updated_at=dateutil.parser.isoparse('2022-05-22T05:03:27.540Z'),
            ),
        ],
    ),
    taxonomy_slug='officia',
)

res = s.taxonomy.update_classifications_for_taxonomy(req)

if res.update_classifications_for_taxonomy_200_application_json_object is not None:
    # handle response
```
