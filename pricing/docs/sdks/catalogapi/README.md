# CatalogAPI
(*catalog_api*)

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
            location=shared.AvailabilityLocation(),
        ),
        q='firewall trusty outvote',
    ),
    x_ivy_org_id='Account woman',
)

res = s.catalog_api.dollar_search_catalog(req)

if res.catalog_search_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DollarSearchCatalogRequest](../../models/operations/dollarsearchcatalogrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.DollarSearchCatalogResponse](../../models/operations/dollarsearchcatalogresponse.md)**

