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
from epilot.models import components

s = epilot.Epilot()


res = s.catalog_api.dollar_search_catalog(catalog_search=components.CatalogSearch(
    q='_id:1233432 OR _id:123432454 OR _id:23445433',
    availability=components.AvailabilityFilters(
        location=components.AvailabilityLocation(
            city='Cologne,',
            postal_code='57008,',
            street='Media Park,',
            street_number='8a',
        ),
        available_date=dateutil.parser.parse('[object Object]').date(),
    ),
    from_=0,
    size=200,
    sort='description ASC',
), x_ivy_org_id='<value>')

if res.catalog_search_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `catalog_search`                                                                                                                                                                                                                                                                         | [components.CatalogSearch](../../models/components/catalogsearch.md)                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                      | {<br/>"q": "_id:1233432 OR _id:123432454 OR _id:23445433",<br/>"sort": "description ASC",<br/>"from": 0,<br/>"size": 200,<br/>"availability": {<br/>"location": {<br/>"postal_code": "57008,",<br/>"city": "Cologne,",<br/>"street": "Media Park,",<br/>"street_number": "8a"<br/>},<br/>"available_date": {<br/>"value": "2022-05-01"<br/>}<br/>}<br/>} |
| `x_ivy_org_id`                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                       | The target Organization Id represented by the caller                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                          |


### Response

**[operations.DollarSearchCatalogResponse](../../models/operations/dollarsearchcatalogresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
