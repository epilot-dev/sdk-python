# epilot-pricing

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=pricing
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DollarAvailabilityCheckRequest(
    availability_check_params=shared.AvailabilityCheckParams(
        filters=shared.AvailabilityFilters(
            available_date=dateutil.parser.parse('2017-07-21').date(),
            location=shared.AvailabilityLocation(),
        ),
        products=[
            'string',
        ],
    ),
    x_ivy_org_id='string',
)

res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [availability_api](docs/sdks/availabilityapi/README.md)

* [dollar_availability_check](docs/sdks/availabilityapi/README.md#dollar_availability_check) - availabilityCheck

### [cart_api](docs/sdks/cartapi/README.md)

* [dollar_checkout_cart](docs/sdks/cartapi/README.md#dollar_checkout_cart) - checkoutCart

### [catalog_api](docs/sdks/catalogapi/README.md)

* [dollar_search_catalog](docs/sdks/catalogapi/README.md#dollar_search_catalog) - searchCatalog

### [deprecated](docs/sdks/deprecated/README.md)

* [~~dollar_create_opportunity~~](docs/sdks/deprecated/README.md#dollar_create_opportunity) - createOpportunity :warning: **Deprecated**

### [order_api](docs/sdks/orderapi/README.md)

* [create_order](docs/sdks/orderapi/README.md#create_order) - createOrder
* [put_order](docs/sdks/orderapi/README.md#put_order) - putOrder
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://pricing-api.sls.epilot.io` | None |
| 1 | `https://pricing-api.sls.epilot.io` | None |

For example:


```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
    server_idx=1
)

req = operations.DollarAvailabilityCheckRequest(
    availability_check_params=shared.AvailabilityCheckParams(
        filters=shared.AvailabilityFilters(
            available_date=dateutil.parser.parse('2017-07-21').date(),
            location=shared.AvailabilityLocation(),
        ),
        products=[
            'string',
        ],
    ),
    x_ivy_org_id='string',
)

res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import epilot
import dateutil.parser
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
    server_url="https://pricing-api.sls.epilot.io"
)

req = operations.DollarAvailabilityCheckRequest(
    availability_check_params=shared.AvailabilityCheckParams(
        filters=shared.AvailabilityFilters(
            available_date=dateutil.parser.parse('2017-07-21').date(),
            location=shared.AvailabilityLocation(),
        ),
        products=[
            'string',
        ],
    ),
    x_ivy_org_id='string',
)

res = s.availability_api.dollar_availability_check(req)

if res.availability_result is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
