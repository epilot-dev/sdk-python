# CatalogAPI

## Overview

Provides a way to query the entire catalog of products and prices.


### Available Operations

* [dollar_search_catalog](#dollar_search_catalog) - searchCatalog

## dollar_search_catalog

Provides a querying functionalities over products and prices of the Catalog for a given organization.

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

req = operations.DollarSearchCatalogRequest(
    catalog_search=shared.CatalogSearch(
        availability=shared.AvailabilityFilters(
            available_date=dateutil.parser.parse('2017-07-21').date(),
            location=shared.AvailabilityLocation(
                city='West Liaville',
                country='Namibia',
                postal_code='63996',
                street='3649 Boyle Cape',
                street_number='reiciendis',
            ),
        ),
        from_=6667.67,
        hydrate=False,
        q='mollitia',
        size=6706.38,
        sort='dolores',
    ),
    x_ivy_org_id='dolorem',
)

res = s.catalog_api.dollar_search_catalog(req)

if res.catalog_search_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DollarSearchCatalogRequest](../../models/operations/dollarsearchcatalogrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.DollarSearchCatalogResponse](../../models/operations/dollarsearchcatalogresponse.md)**

