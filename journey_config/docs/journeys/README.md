# journeys

### Available Operations

* [create_journey](#create_journey) - createJourney
* [get_journey](#get_journey) - getJourney
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


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "vel": "error",
    "deserunt": "suscipit",
    "iure": "magnam",
    "debitis": "ipsa",
}

res = s.journeys.create_journey(req)

if res.journey_response is not None:
    # handle response
```

## get_journey

Get journey by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetJourneyRequest(
    id="509cdffe-424f-457a-95c2-9708c304ce77",
    org_id="delectus",
    source="tempora",
)

res = s.journeys.get_journey(req)

if res.journey_response is not None:
    # handle response
```

## get_journeys_by_org_id

Get all journeys by organization id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetJourneysByOrgIDRequest(
    id="123",
)

res = s.journeys.get_journeys_by_org_id(req)

if res.get_journeys_response is not None:
    # handle response
```

## patch_update_journey

Update a Journey (partially / patch). Support for nested properties updates (e.g. "property[0].name").

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "molestiae": "minus",
    "placeat": "voluptatum",
}

res = s.journeys.patch_update_journey(req)

if res.journey_response is not None:
    # handle response
```

## remove_journey

Remove journey by id

### Example Usage

```python
import epilot
from epilot.models import operations

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.RemoveJourneyRequest(
    id="509cdffe-424f-457a-95c2-9708c304ce77",
)

res = s.journeys.remove_journey(req)

if res.status_code == 200:
    # handle response
```

## search_journeys

Search Journeys

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.SearchJourneysQueryRequest(
    from_=479977,
    q="_tags:*Flex*",
    size=25,
    sort="_created_at:desc",
)

res = s.journeys.search_journeys(req)

if res.search_journeys_response is not None:
    # handle response
```

## update_journey

Update a Journey

### Example Usage

```python
import epilot


s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = {
    "nisi": "recusandae",
    "temporibus": "ab",
    "quis": "veritatis",
}

res = s.journeys.update_journey(req)

if res.journey_response is not None:
    # handle response
```
