<!-- Start SDK Example Usage [usage] -->
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