# epilot-pricing

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=pricing
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    currency='EUR',
    delivery_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            price=shared.Price(
            additional_properties={
                '$ref': 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.WEEKLY,
            tax=shared.Price1(
            dollar_relation=[
                shared.EntityRelation(
                    additional_properties={
                        'key': 'string',
                    },
                    tags=[
                        'string',
                    ],
                ),
            ],
        ),
            unit='string',
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
            },
        ),
    ],
    source_type='journey',
)

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [order_api](docs/sdks/orderapi/README.md)

* [create_order](docs/sdks/orderapi/README.md#create_order) - createOrder
* [put_order](docs/sdks/orderapi/README.md#put_order) - putOrder

### [availability_api](docs/sdks/availabilityapi/README.md)

* [dollar_availability_check](docs/sdks/availabilityapi/README.md#dollar_availability_check) - availabilityCheck

### [cart_api](docs/sdks/cartapi/README.md)

* [dollar_checkout_cart](docs/sdks/cartapi/README.md#dollar_checkout_cart) - checkoutCart

### [catalog_api](docs/sdks/catalogapi/README.md)

* [dollar_search_catalog](docs/sdks/catalogapi/README.md#dollar_search_catalog) - searchCatalog

### [deprecated](docs/sdks/deprecated/README.md)

* [~~dollar_create_opportunity~~](docs/sdks/deprecated/README.md#dollar_create_opportunity) - createOpportunity :warning: **Deprecated**
<!-- End Available Resources and Operations [operations] -->





<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

### Example

```python
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    currency='EUR',
    delivery_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            price=shared.Price(
            additional_properties={
                '$ref': 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.WEEKLY,
            tax=shared.Price1(
            dollar_relation=[
                shared.EntityRelation(
                    additional_properties={
                        'key': 'string',
                    },
                    tags=[
                        'string',
                    ],
                ),
            ],
        ),
            unit='string',
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
            },
        ),
    ],
    source_type='journey',
)

res = None
try:
    res = s.order_api.create_order(req)
except errors.Error as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.order is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://pricing-api.sls.epilot.io` | None |
| 1 | `https://pricing-api.sls.epilot.io` | None |

#### Example

```python
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_idx=1,
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    currency='EUR',
    delivery_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            price=shared.Price(
            additional_properties={
                '$ref': 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.WEEKLY,
            tax=shared.Price1(
            dollar_relation=[
                shared.EntityRelation(
                    additional_properties={
                        'key': 'string',
                    },
                    tags=[
                        'string',
                    ],
                ),
            ],
        ),
            unit='string',
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
            },
        ),
    ],
    source_type='journey',
)

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    server_url="https://pricing-api.sls.epilot.io",
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    currency='EUR',
    delivery_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            price=shared.Price(
            additional_properties={
                '$ref': 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.WEEKLY,
            tax=shared.Price1(
            dollar_relation=[
                shared.EntityRelation(
                    additional_properties={
                        'key': 'string',
                    },
                    tags=[
                        'string',
                    ],
                ),
            ],
        ),
            unit='string',
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
            },
        ),
    ],
    source_type='journey',
)

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |

To authenticate with the API the `epilot_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.OrderPayload(
    additional_properties={
        'key': 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    currency='EUR',
    delivery_address=[
        shared.Address(
            additional_properties={
                'key': 'string',
            },
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        shared.CompositePriceItemInput(
            price=shared.Price(
            additional_properties={
                '$ref': 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.WEEKLY,
            tax=shared.Price1(
            dollar_relation=[
                shared.EntityRelation(
                    additional_properties={
                        'key': 'string',
                    },
                    tags=[
                        'string',
                    ],
                ),
            ],
        ),
            unit='string',
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.CompositePrice(
                    additional_properties={
                        '$ref': 'string',
                    },
                    tags=[
                        'string',
                    ],
                    price_components=shared.Two(
                    dollar_relation=[
                        shared.PriceComponentRelation(
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.One(),
                    ],
                ),
            ],
            metadata=[
                shared.One(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                'key': 'string',
            },
        ),
    ],
    source_type='journey',
)

res = s.order_api.create_order(req)

if res.order is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
