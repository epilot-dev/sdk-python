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
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.create_order(request=components.OrderPayload(
    billing_address=[
        components.Address(
            tags=[
                '<value>',
            ],
            additional_info='',
            city='Cologne',
            country='DE',
            postal_code='52000',
            street='Im Media Park',
            street_number='8a',
            additional_properties={

            },
        ),
    ],
    billing_company_name='epilot cloud',
    billing_email='j.pinho@epilot.cloud',
    billing_first_name='Joao',
    billing_last_name='Pinho',
    currency='EUR',
    delivery_address=[
        components.Address(
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=[
                    components.Price(
                        tax=components.Price1(),
                        unit_amount_currency='EUR',
                        additional_properties={
                            '$ref': '#/components/examples/price',
                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=16,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=5472.14,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=4,
        ),
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=components.Two(),
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=6182.37,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
    ],
    payment_method=[
        components.PaymentMethod(
            details={

            },
            type='IBAN',
        ),
    ],
    source_type='manual',
    status=components.OrderStatus.QUOTE,
    additional_properties={
        'expires_at': '2022-06-30T16:17:00.000Z',
        'billing_contact': {
            '$relation': [
                {
                    'entity_id': '1834a54e-b68f-4f7f-a98a-fe16f11bc2a5',
                    '_tags': [
                        '<value>',
                    ],
                },
            ],
        },
        'dates': [
            {
                '_tags': [
                    'Instalation Date',
                ],
                'dates': '',
                'value': '2022-06-30T16:29:00.000Z',
            },
        ],
    },
))

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
| errors.SDKError  | 4xx-5xx          | */*              |

### Example

```python
import dateutil.parser
import epilot
from epilot.models import components, errors

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.order_api.create_order(request=components.OrderPayload(
    billing_address=[
        components.Address(
            tags=[
                '<value>',
            ],
            additional_info='',
            city='Cologne',
            country='DE',
            postal_code='52000',
            street='Im Media Park',
            street_number='8a',
            additional_properties={

            },
        ),
    ],
    billing_company_name='epilot cloud',
    billing_email='j.pinho@epilot.cloud',
    billing_first_name='Joao',
    billing_last_name='Pinho',
    currency='EUR',
    delivery_address=[
        components.Address(
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=[
                    components.Price(
                        tax=components.Price1(),
                        unit_amount_currency='EUR',
                        additional_properties={
                            '$ref': '#/components/examples/price',
                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=16,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=5472.14,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=4,
        ),
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=components.Two(),
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=6182.37,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
    ],
    payment_method=[
        components.PaymentMethod(
            details={

            },
            type='IBAN',
        ),
    ],
    source_type='manual',
    status=components.OrderStatus.QUOTE,
    additional_properties={
        'expires_at': '2022-06-30T16:17:00.000Z',
        'billing_contact': {
            '$relation': [
                {
                    'entity_id': '1834a54e-b68f-4f7f-a98a-fe16f11bc2a5',
                    '_tags': [
                        '<value>',
                    ],
                },
            ],
        },
        'dates': [
            {
                '_tags': [
                    'Instalation Date',
                ],
                'dates': '',
                'value': '2022-06-30T16:29:00.000Z',
            },
        ],
    },
))

except errors.Error as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
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
from epilot.models import components

s = epilot.Epilot(
    server_idx=1,
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.create_order(request=components.OrderPayload(
    billing_address=[
        components.Address(
            tags=[
                '<value>',
            ],
            additional_info='',
            city='Cologne',
            country='DE',
            postal_code='52000',
            street='Im Media Park',
            street_number='8a',
            additional_properties={

            },
        ),
    ],
    billing_company_name='epilot cloud',
    billing_email='j.pinho@epilot.cloud',
    billing_first_name='Joao',
    billing_last_name='Pinho',
    currency='EUR',
    delivery_address=[
        components.Address(
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=[
                    components.Price(
                        tax=components.Price1(),
                        unit_amount_currency='EUR',
                        additional_properties={
                            '$ref': '#/components/examples/price',
                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=16,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=5472.14,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=4,
        ),
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=components.Two(),
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=6182.37,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
    ],
    payment_method=[
        components.PaymentMethod(
            details={

            },
            type='IBAN',
        ),
    ],
    source_type='manual',
    status=components.OrderStatus.QUOTE,
    additional_properties={
        'expires_at': '2022-06-30T16:17:00.000Z',
        'billing_contact': {
            '$relation': [
                {
                    'entity_id': '1834a54e-b68f-4f7f-a98a-fe16f11bc2a5',
                    '_tags': [
                        '<value>',
                    ],
                },
            ],
        },
        'dates': [
            {
                '_tags': [
                    'Instalation Date',
                ],
                'dates': '',
                'value': '2022-06-30T16:29:00.000Z',
            },
        ],
    },
))

if res.order is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import dateutil.parser
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_url="https://pricing-api.sls.epilot.io",
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.create_order(request=components.OrderPayload(
    billing_address=[
        components.Address(
            tags=[
                '<value>',
            ],
            additional_info='',
            city='Cologne',
            country='DE',
            postal_code='52000',
            street='Im Media Park',
            street_number='8a',
            additional_properties={

            },
        ),
    ],
    billing_company_name='epilot cloud',
    billing_email='j.pinho@epilot.cloud',
    billing_first_name='Joao',
    billing_last_name='Pinho',
    currency='EUR',
    delivery_address=[
        components.Address(
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=[
                    components.Price(
                        tax=components.Price1(),
                        unit_amount_currency='EUR',
                        additional_properties={
                            '$ref': '#/components/examples/price',
                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=16,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=5472.14,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=4,
        ),
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=components.Two(),
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=6182.37,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
    ],
    payment_method=[
        components.PaymentMethod(
            details={

            },
            type='IBAN',
        ),
    ],
    source_type='manual',
    status=components.OrderStatus.QUOTE,
    additional_properties={
        'expires_at': '2022-06-30T16:17:00.000Z',
        'billing_contact': {
            '$relation': [
                {
                    'entity_id': '1834a54e-b68f-4f7f-a98a-fe16f11bc2a5',
                    '_tags': [
                        '<value>',
                    ],
                },
            ],
        },
        'dates': [
            {
                '_tags': [
                    'Instalation Date',
                ],
                'dates': '',
                'value': '2022-06-30T16:29:00.000Z',
            },
        ],
    },
))

if res.order is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client=http_client)
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
from epilot.models import components

s = epilot.Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.create_order(request=components.OrderPayload(
    billing_address=[
        components.Address(
            tags=[
                '<value>',
            ],
            additional_info='',
            city='Cologne',
            country='DE',
            postal_code='52000',
            street='Im Media Park',
            street_number='8a',
            additional_properties={

            },
        ),
    ],
    billing_company_name='epilot cloud',
    billing_email='j.pinho@epilot.cloud',
    billing_first_name='Joao',
    billing_last_name='Pinho',
    currency='EUR',
    delivery_address=[
        components.Address(
            tags=[
                'billing',
            ],
        ),
    ],
    line_items=[
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=[
                    components.Price(
                        tax=components.Price1(),
                        unit_amount_currency='EUR',
                        additional_properties={
                            '$ref': '#/components/examples/price',
                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=16,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=5472.14,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=4,
        ),
        components.PriceItemInput(
            price=components.CompositePrice(
                price_components=components.Two(),
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/composite-price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
        components.PriceItemInput(
            price=components.Price(
                tax=[
                    components.Tax(
                        created_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                        org='123',
                        schema='tax',
                        title='<value>',
                        updated_at=dateutil.parser.isoparse('2021-02-09T12:41:43.662Z'),
                        behavior=components.Behavior.EXCLUSIVE_MIXED,
                        rate=6182.37,
                        type=components.TaxType.VAT,
                        tags=[
                            'example',
                            'mock',
                        ],
                        active=True,
                        description='Tax description',
                        region='DE',
                        region_label='Germany',
                        additional_properties={

                        },
                    ),
                ],
                unit_amount_currency='EUR',
                additional_properties={
                    '$ref': '#/components/examples/price',
                },
            ),
            currency='EUR',
            price_id='7e24ff5d-d580-4136-a32f-19191eed039a',
            product_id='6241487f-b7fd-428b-ab92-24ee0b37fd84',
            quantity=1,
        ),
    ],
    payment_method=[
        components.PaymentMethod(
            details={

            },
            type='IBAN',
        ),
    ],
    source_type='manual',
    status=components.OrderStatus.QUOTE,
    additional_properties={
        'expires_at': '2022-06-30T16:17:00.000Z',
        'billing_contact': {
            '$relation': [
                {
                    'entity_id': '1834a54e-b68f-4f7f-a98a-fe16f11bc2a5',
                    '_tags': [
                        '<value>',
                    ],
                },
            ],
        },
        'dates': [
            {
                '_tags': [
                    'Instalation Date',
                ],
                'dates': '',
                'value': '2022-06-30T16:29:00.000Z',
            },
        ],
    },
))

if res.order is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
