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

## list_taxonomies

List taxonomies in an organisation

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
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
        epilot_auth="",
    ),
)

req = operations.TaxonomiesClassificationsSearchRequest(
    request_body=operations.TaxonomiesClassificationsSearchRequestBody(
        classification_ids=[
            'bdfc4ccc-a99b-4c7f-80b2-dce10873e42b',
            '006d6788-78ba-4858-9a58-208c54fefa9c',
            '95f2eac5-565d-4307-8fee-81206e2813fa',
            '4a41c480-d3f2-4132-af03-102d514f4cc6',
        ],
    ),
    taxonomy_slug='repellat',
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
        epilot_auth="",
    ),
)

req = operations.TaxonomyAutocompleteRequest(
    query='quae',
    size=5339.78,
    taxonomy_slug='expedita',
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
        epilot_auth="",
    ),
)

req = operations.UpdateClassificationsForTaxonomyRequest(
    classifications_update=shared.ClassificationsUpdate(
        create=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-03-17T11:23:26.153Z'),
                id='21a6a4f7-7a87-4ee3-a4be-752c65b34418',
                name='Wallbox PV',
                parents=[
                    '3bb91c8d-975e-40e8-819d-8f84f144f3e0',
                    '7edcc4aa-5f3c-4abd-905a-972e05672822',
                    '7b2d3094-70bf-47a4-ba87-cf535a6fae54',
                    'ebf60c32-1f02-43b7-9d23-67fe1a0cc8df',
                ],
                updated_at=dateutil.parser.isoparse('2022-05-31T03:19:09.957Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-11-12T03:58:41.553Z'),
                id='a396d90c-364b-47c1-9dfb-ace188b1c4ee',
                name='Wallbox PV',
                parents=[
                    'c8c6ce61-1fee-4b1c-bcbd-b6eec74378ba',
                ],
                updated_at=dateutil.parser.isoparse('2022-09-06T09:53:00.602Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-11-23T00:22:34.246Z'),
                id='7747dc91-5ad2-4caf-9dd6-723dc0f5ae2f',
                name='Wallbox PV',
                parents=[
                    'a6b70087-8756-4143-b5a6-c98b55554080',
                ],
                updated_at=dateutil.parser.isoparse('2022-03-24T16:26:44.342Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-04-05T19:27:13.618Z'),
                id='cacc6cbd-6b5f-43ec-9093-04f926bad255',
                name='Wallbox PV',
                parents=[
                    '819b474b-0ed2-40e5-a248-fff639a910ab',
                ],
                updated_at=dateutil.parser.isoparse('2020-09-02T19:39:17.071Z'),
            ),
        ],
        delete=[
            'b6267669-6e1e-4c00-a21b-335d89acb3ec',
            'fda8d0c5-49ef-4030-8497-8a61fa1cf206',
            '88f77c1f-fc71-4dca-963f-2a3c80a97ff3',
        ],
        update=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-03-28T10:53:29.573Z'),
                id='ddf857a9-e618-476c-aab2-1d29dfc94d6f',
                name='Wallbox PV',
                parents=[
                    'cd799390-066a-46d2-9000-355338cec086',
                    'fa21e915-2cb3-4119-967b-8e3c8db03408',
                    'd6d364ff-d455-4906-9126-3d48e935c2c9',
                    'e81f30be-3e43-4202-9721-657650664187',
                ],
                updated_at=dateutil.parser.isoparse('2022-03-05T14:32:00.362Z'),
            ),
        ],
    ),
    taxonomy_slug='provident',
)

res = s.taxonomy.update_classifications_for_taxonomy(req)

if res.update_classifications_for_taxonomy_200_application_json_object is not None:
    # handle response
```
