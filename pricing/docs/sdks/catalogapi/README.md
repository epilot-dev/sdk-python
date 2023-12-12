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
import dateutil.parser
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_search_catalog(catalog_search=shared.CatalogSearch(
    availability=shared.AvailabilityFilters(
        available_date=dateutil.parser.parse('2017-07-21').date(),
        location=shared.AvailabilityLocation(),
    ),
    q='string',
), x_ivy_org_id='string')

if res.catalog_search_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `catalog_search`                                             | [shared.CatalogSearch](../../models/shared/catalogsearch.md) | :heavy_check_mark:                                           | N/A                                                          |
| `x_ivy_org_id`                                               | *str*                                                        | :heavy_check_mark:                                           | The target Organization Id represented by the caller         |


### Response

**[operations.DollarSearchCatalogResponse](../../models/operations/dollarsearchcatalogresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 400-600          | */*              |
