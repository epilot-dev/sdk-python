# journeys

### Available Operations

* [create_journey](#create_journey) - createJourney
* [get_journey](#get_journey) - getJourney
* [get_journey_products](#get_journey_products) - getJourneyProducts
* [get_journeys_by_org_id](#get_journeys_by_org_id) - getJourneysByOrgId
* [patch_update_journey](#patch_update_journey) - patchUpdateJourney
* [remove_journey](#remove_journey) - removeJourney
* [search_journeys](#search_journeys) - searchJourneys
* [update_journey](#update_journey) - updateJourney

## create_journey

Create a Journey

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = {
    "vel": 'error',
    "deserunt": 'suscipit',
    "iure": 'magnam',
    "debitis": 'ipsa',
}

res = s.journeys.create_journey(req)

if res.journey_response is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateJourneyResponse](../../models/operations/createjourneyresponse.md)**


## get_journey

Get journey by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetJourneyRequest(
    id='509cdffe-424f-457a-95c2-9708c304ce77',
    org_id='delectus',
    source='tempora',
)

res = s.journeys.get_journey(req)

if res.journey_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetJourneyRequest](../../models/operations/getjourneyrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetJourneyResponse](../../models/operations/getjourneyresponse.md)**


## get_journey_products

Get products available in the journey by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetJourneyProductsRequest(
    city='South Paxton',
    id='509cdffe-424f-457a-95c2-9708c304ce77',
    org_id='placeat',
    postal_code='45398-0306',
    source='perferendis',
    street='8971 Strosin Wall',
    street_number='molestiae',
)

res = s.journeys.get_journey_products(req)

if res.journey_products_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetJourneyProductsRequest](../../models/operations/getjourneyproductsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetJourneyProductsResponse](../../models/operations/getjourneyproductsresponse.md)**


## get_journeys_by_org_id

Get all journeys by organization id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetJourneysByOrgIDRequest(
    id='123',
)

res = s.journeys.get_journeys_by_org_id(req)

if res.get_journeys_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetJourneysByOrgIDRequest](../../models/operations/getjourneysbyorgidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetJourneysByOrgIDResponse](../../models/operations/getjourneysbyorgidresponse.md)**


## patch_update_journey

Update a Journey (partially / patch). Support for nested properties updates (e.g. "property[0].name").

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = {
    "quod": 'esse',
    "totam": 'porro',
    "dolorum": 'dicta',
    "nam": 'officia',
}

res = s.journeys.patch_update_journey(req)

if res.journey_response is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PatchUpdateJourneyResponse](../../models/operations/patchupdatejourneyresponse.md)**


## remove_journey

Remove journey by id

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.RemoveJourneyRequest(
    id='509cdffe-424f-457a-95c2-9708c304ce77',
)

res = s.journeys.remove_journey(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveJourneyRequest](../../models/operations/removejourneyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveJourneyResponse](../../models/operations/removejourneyresponse.md)**


## search_journeys

Search Journeys

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.SearchJourneysQueryRequest(
    from_=0,
    q='_tags:*Flex*',
    size=25,
    sort='_created_at:desc',
)

res = s.journeys.search_journeys(req)

if res.search_journeys_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.SearchJourneysQueryRequest](../../models/shared/searchjourneysqueryrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.SearchJourneysResponse](../../models/operations/searchjourneysresponse.md)**


## update_journey

Update a Journey

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = {
    "fugit": 'deleniti',
    "hic": 'optio',
    "totam": 'beatae',
}

res = s.journeys.update_journey(req)

if res.journey_response is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdateJourneyResponse](../../models/operations/updatejourneyresponse.md)**

