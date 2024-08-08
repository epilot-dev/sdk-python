# CatalogAPI
(*catalog_api*)

## Overview

Provides a way to query the entire catalog of products and prices.


### Available Operations

* [dollar_private_search_catalog](#dollar_private_search_catalog) - privateSearchCatalog
* [dollar_search_catalog](#dollar_search_catalog) - searchCatalog

## dollar_private_search_catalog

Provides a querying functionalities over products and prices of the Catalog for a given organization.

### Example Usage

```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.catalog_api.dollar_private_search_catalog(request={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CatalogSearch](../../models/catalogsearch.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CatalogSearchResult](../../models/catalogsearchresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_search_catalog

Provides a querying functionalities over products and prices of the Catalog for a given organization.

### Example Usage

```python
import dateutil.parser
from epilot_pricing import Epilot

s = Epilot()


res = s.catalog_api.dollar_search_catalog(catalog_search={
    "q": "_id:1233432 OR _id:123432454 OR _id:23445433",
    "availability": {
        "location": {},
        "available_date": dateutil.parser.parse("2017-07-21").date(),
    },
    "from_": 0,
    "size": 200,
    "sort": "description ASC",
}, x_ivy_org_id="739224")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `catalog_search`                                                                                           | [models.CatalogSearch](../../models/catalogsearch.md)                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        | {<br/>"q": "_id:1233432 OR _id:123432454 OR _id:23445433",<br/>"sort": "description ASC",<br/>"from": 0,<br/>"size": 200<br/>} |
| `x_ivy_org_id`                                                                                             | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | The target Organization Id represented by the caller                                                       | 739224                                                                                                     |
| `security`                                                                                                 | [Optional[models.DollarSearchCatalogSecurity]](../../models/dollarsearchcatalogsecurity.md)                | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |


### Response

**[models.CatalogSearchResult](../../models/catalogsearchresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
