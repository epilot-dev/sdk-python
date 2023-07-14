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
            '639a910a-bdca-4b62-a766-96e1ec00221b',
            '335d89ac-b3ec-4fda-8d0c-549ef0300497',
            '8a61fa1c-f206-488f-b7c1-ffc71dca163f',
            '2a3c80a9-7ff3-434c-9df8-57a9e61876c6',
        ],
    ),
    taxonomy_slug='mollitia',
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
    query='quidem',
    size=1265.12,
    taxonomy_slug='et',
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
                created_at=dateutil.parser.isoparse('2022-05-20T09:40:46.168Z'),
                id='dfc94d6f-ecd7-4993-9006-6a6d2d000355',
                name='Wallbox PV',
                parents=[
                    '38cec086-fa21-4e91-92cb-3119167b8e3c',
                ],
                updated_at=dateutil.parser.isoparse('2021-04-20T17:26:00.007Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-12-07T22:47:43.718Z'),
                id='3408d6d3-64ff-4d45-9906-d1263d48e935',
                name='Wallbox PV',
                parents=[
                    '2c9e81f3-0be3-4e43-a02d-721657650664',
                    '1870d9d2-1f9a-4d03-8c4e-cc11a0836429',
                    '068b8502-a55e-47f7-bbc8-45e320a319f4',
                    'badf947c-9a86-47bc-8242-6665816ddca8',
                ],
                updated_at=dateutil.parser.isoparse('2020-01-24T15:21:03.821Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-12-05T12:01:23.554Z'),
                id='fcb4c593-ec12-4cda-ad0e-c7afedbd80df',
                name='Wallbox PV',
                parents=[
                    '48a47f93-90c5-4888-8983-dabf9ef3ffdd',
                    '9f7f079a-f4d3-4572-8cdb-0f4d281187d5',
                ],
                updated_at=dateutil.parser.isoparse('2022-06-27T23:18:05.509Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-09-12T21:05:38.468Z'),
                id='eded85a9-065e-4628-bdfc-2032b6c87992',
                name='Wallbox PV',
                parents=[
                    'b7e13584-f7ae-412c-a891-f82ce1157172',
                ],
                updated_at=dateutil.parser.isoparse('2022-12-12T20:07:27.803Z'),
            ),
        ],
        delete=[
            '377dcfa8-9df9-475e-b566-86092e9c3ddc',
            '5f111dea-1026-4d54-9a4d-190feb21780b',
        ],
        update=[
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2020-09-25T02:22:59.870Z'),
                id='0dbbddb4-8470-48fb-8e39-1e6bc158c4c4',
                name='Wallbox PV',
                parents=[
                    '54599ea3-4226-40e9-b200-ce78a1bd8fb7',
                    'a0a116ce-723d-4409-bfa3-0e9af725b291',
                    '22030d83-f5ae-4b77-99d2-2e8c1f849382',
                    '5fdc42c8-76c2-4c2d-bb4c-fc1c76230f84',
                ],
                updated_at=dateutil.parser.isoparse('2022-01-08T03:54:51.622Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-10-18T09:43:56.655Z'),
                id='bd23fdb1-4db6-4be5-a685-998e22ae20da',
                name='Wallbox PV',
                parents=[
                    '6fc2b271-a289-4c57-a854-e90439d22246',
                ],
                updated_at=dateutil.parser.isoparse('2022-07-29T05:03:39.225Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-06-19T06:43:31.808Z'),
                id='62407084-f7ab-437c-af02-225194db5541',
                name='Wallbox PV',
                parents=[
                    'adc669af-90a2-46c7-8dc9-81f068981d6b',
                ],
                updated_at=dateutil.parser.isoparse('2022-07-20T11:17:27.497Z'),
            ),
            shared.TaxonomyClassification(
                created_at=dateutil.parser.isoparse('2022-03-17T08:05:23.562Z'),
                id='faa348c3-1bf4-407e-a4fc-f0c42b78f156',
                name='Wallbox PV',
                parents=[
                    '6398a0dc-7663-424c-8b06-c8ca12d02529',
                ],
                updated_at=dateutil.parser.isoparse('2022-07-07T09:19:49.741Z'),
            ),
        ],
    ),
    taxonomy_slug='alias',
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

