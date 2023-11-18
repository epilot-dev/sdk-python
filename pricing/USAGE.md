<!-- Start SDK Example Usage -->
```python
import dateutil.parser
import epilot
from epilot.models import shared

s = epilot.Epilot(
    epilot_auth="",
)

req = shared.OrderPayload(
    additional_properties={
        "key": 'string',
    },
    tags=[
        'string',
    ],
    billing_address=[
        shared.Address(
            additional_properties={
                "key": 'string',
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
                "key": 'string',
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
                "$ref": 'string',
            },
            tags=[
                'string',
            ],
            billing_period=shared.BillingPeriod.WEEKLY,
            sales_tax=shared.SalesTax.NONTAXABLE,
            tax=[
            shared.Tax(
                additional_properties={
                    "_created_at": 'string',
                    "description": 'string',
                    "region_label": 'string',
                    "_schema": 'string',
                    "active": 'string',
                    "region": 'string',
                    "_org": 'string',
                    "_tags": 'string',
                    "_updated_at": 'string',
                    "_id": 'string',
                    "type": 'string',
                    "behavior": 'string',
                },
                created_at=dateutil.parser.isoparse('2022-08-23T04:46:44.470Z'),
                id='db7b9f9b-d21b-44f2-9723-407318b6c79c',
                org='string',
                schema='string',
                tags=[
                    'string',
                ],
                title='string',
                updated_at=dateutil.parser.isoparse('2022-08-04T04:36:14.538Z'),
                behavior=shared.Behavior.INCLUSIVE_LOWER,
                rate=5305.72,
                type=shared.TaxType.GST,
            ),
        ],
            unit='string',
            unit_amount_currency='EUR',
        ),
            currency='EUR',
            item_components=[
                shared.PriceItemInput(
                    price=shared.Price(
                    additional_properties={
                        "$ref": 'string',
                    },
                    tags=[
                        'string',
                    ],
                    billing_period=shared.BillingPeriod.MONTHLY,
                    sales_tax=shared.SalesTax.STANDARD,
                    tax=shared.Price1(
                    dollar_relation=[
                        shared.EntityRelation(
                            additional_properties={
                                "key": 'string',
                            },
                            tags=[
                                'string',
                            ],
                        ),
                    ],
                ),
                    unit=shared.PriceSchemas1.L,
                    unit_amount_currency='EUR',
                ),
                    currency='EUR',
                    metadata=[
                        shared.MetaData1(),
                    ],
                ),
            ],
            metadata=[
                shared.MetaData1(),
            ],
        ),
    ],
    payment_method=[
        shared.PaymentMethod(
            details={
                "key": 'string',
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
<!-- End SDK Example Usage -->