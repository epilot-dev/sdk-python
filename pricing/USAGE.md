<!-- Start SDK Example Usage [usage] -->
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