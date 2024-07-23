# CartAPI
(*cart_api*)

## Overview

Used to interact with a cart during a customer's checkout session, providing:
 - An unified data model to model a Shopping Cart
 - Product and pricing data validation
 - Checkout a cart into an order or quote


### Available Operations

* [dollar_checkout_cart](#dollar_checkout_cart) - checkoutCart

## dollar_checkout_cart

Checkouts a cart and executes the specified checkout `mode` process.

A Checkout implicitly finalizes the provided cart (if not transient from a fast-checkout) and behaves in one of the following modes:
- `create_order` (**default**): the payment happens at a later date or managed by 3rd-party CRM (SAP)
- `create_invoice`: the payment happens on the online checkout (paypal, stripe, adyen)
- `create_quote`: the checkout represents a price quote request

Fast checkout is also supported, by passing the Cart contents directly.
When a fast checkout is performed the cart is considered transient and there is no cart persistance.

If the checkout `mode` is omitted, the `mode` will default to `create_order`.


### Example Usage

```python
import dateutil.parser
import epilot
from epilot.models import components

s = epilot.Epilot()


res = s.cart_api.dollar_checkout_cart(checkout_cart=components.CheckoutCart(
    cart=components.CartDto(
        line_items=[
            components.PriceItemDto(
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
                            rate=1382.48,
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
                product=components.ProductInput(
                    additional_properties={
                        '$ref': '#/components/examples/product',
                    },
                ),
                price_id='df240bab-9f71-4a9a-a9e1-59f18827dbf9',
                product_id='b7185fb7-b10f-4875-bda7-288631446555',
                quantity=3,
            ),
            components.PriceItemDto(
                price=components.Price(
                    tax=components.Price1(),
                    unit_amount_currency='EUR',
                    additional_properties={
                        '$ref': '#/components/examples/price',
                    },
                ),
                product=components.ProductInput(
                    additional_properties={
                        '$ref': '#/components/examples/product',
                    },
                ),
                price_id='7b028fdf-0b0a-4077-a8f1-d0cbbd14b7cf',
                product_id='607d2952-8f3e-484f-a82b-4880528b7f55',
                quantity=2,
            ),
        ],
        additional_addresses=[
            components.Address(
                tags=[
                    'billing',
                ],
            ),
        ],
        billing_address=components.Address(
            tags=[
                'billing',
            ],
            additional_info='headquarters office',
            city='new york city',
            country='united states',
            additional_properties={
                'street1': 'wallstreet',
                'street2': 1,
                'country_code': 'US',
            },
        ),
        customer=components.Customer(
            company_name='company limited',
            email='johndoe@company.com',
            first_name='john',
            last_name='doe',
            phone='+44233242423',
            vat_id='123892321',
        ),
        delivery_address=components.Address(
            tags=[
                'billing',
            ],
            additional_info='remote cowork place',
            city='berverly hills',
            country='california',
            additional_properties={
                'street1': 'berverly hills avenue',
                'street2': 'block 1',
                'country_code': 'CA',
            },
        ),
        source=components.OrderSource(
            http='/app/v2/journey-builder/editor/db7f6940-994b-11ec-a46d-9f1824ff2939',
            title='Journey: PH Journey',
        ),
        source_id='ce99875f-fba9-4fe2-a8f9-afaf52059051',
        source_type='journey',
    ),
    mode=components.CheckoutMode.CREATE_ORDER,
), x_ivy_org_id='<value>')

if res.checkout_cart_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `checkout_cart`                                                    | [components.CheckoutCart](../../models/components/checkoutcart.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `x_ivy_org_id`                                                     | *str*                                                              | :heavy_check_mark:                                                 | The target Organization Id represented by the caller               |


### Response

**[operations.DollarCheckoutCartResponse](../../models/operations/dollarcheckoutcartresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
