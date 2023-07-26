# catalog_api

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
                city='New Tyrelfort',
                country='Macedonia',
                postal_code='44217',
                street='425 Aiden Glen',
                street_number='natus',
            ),
        ),
        from_=1496.75,
        hydrate=False,
        q='iste',
        size=2223.21,
        sort='natus',
    ),
    x_ivy_org_id='laboriosam',
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

