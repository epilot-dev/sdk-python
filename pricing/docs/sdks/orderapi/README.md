# OrderAPI
(*order_api*)

## Overview

This api enables the management of orders in epilot 360, providing features such as:
 - Automatic calculation of totals and price breakdowns for taxes on the Order entity
 - Product and pricing data validation


### Available Operations

* [dollar_calculate_pricing_details](#dollar_calculate_pricing_details) - calculatePricingDetails
* [create_order](#create_order) - createOrder
* [put_order](#put_order) - putOrder

## dollar_calculate_pricing_details

Computes a set of pricing details that can be persisted on an entity with the pricing capability enabled, e.g: Orders or Contracts.

### Example Usage

```python
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.dollar_calculate_pricing_details(request={
    "line_items": [

    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.DollarCalculatePricingDetailsRequestBody](../../models/dollarcalculatepricingdetailsrequestbody.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |


### Response

**[models.PricingDetailsResponse](../../models/pricingdetailsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## create_order

Create an order

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.create_order(request=epilot_pricing.OrderPayload(
    billing_address=[
        epilot_pricing.Address(
            tags=[
                "<value>",
            ],
            additional_info="",
            city="Cologne",
            country="DE",
            postal_code="52000",
            street="Im Media Park",
            street_number="8a",
            **{

            },
        ),
    ],
    billing_company_name="epilot cloud",
    billing_email="j.pinho@epilot.cloud",
    billing_first_name="Joao",
    billing_last_name="Pinho",
    currency="EUR",
    delivery_address=[
        epilot_pricing.Address(
            tags=[
                "billing",
            ],
        ),
    ],
    line_items=[

    ],
    payment_method=[
        {
            "details": {

            },
            "type": "IBAN",
        },
    ],
    source_type="manual",
    status=epilot_pricing.OrderStatus.QUOTE,
    **{
        "expires_at": "2022-06-30T16:17:00.000Z",
        "billing_contact": {
            "$relation": [
                {
                    "entity_id": "1834a54e-b68f-4f7f-a98a-fe16f11bc2a5",
                    "_tags": [
                        "<value>",
                    ],
                },
            ],
        },
        "dates": [
            {
                "_tags": [
                    "Instalation Date",
                ],
                "dates": "",
                "value": "2022-06-30T16:29:00.000Z",
            },
        ],
    },
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.OrderPayload](../../models/orderpayload.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.Order](../../models/order.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## put_order

Update an existing Order

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.put_order(id="9d4602d3-03be-4d85-86b2-f3c6555fc606", order_payload=epilot_pricing.OrderPayload(
    billing_address=[
        epilot_pricing.Address(
            tags=[
                "<value>",
            ],
            additional_info="",
            city="Cologne",
            country="DE",
            postal_code="52000",
            street="Im Media Park",
            street_number="8a",
            **{

            },
        ),
    ],
    billing_company_name="epilot cloud",
    billing_email="j.pinho@epilot.cloud",
    billing_first_name="Joao",
    billing_last_name="Pinho",
    currency="EUR",
    delivery_address=[
        epilot_pricing.Address(
            tags=[
                "billing",
            ],
        ),
    ],
    line_items=[

    ],
    payment_method=[
        {
            "details": {

            },
            "type": "IBAN",
        },
    ],
    source_type="manual",
    status=epilot_pricing.OrderStatus.QUOTE,
    **{
        "expires_at": "2022-06-30T16:17:00.000Z",
        "billing_contact": {
            "$relation": [
                {
                    "entity_id": "1834a54e-b68f-4f7f-a98a-fe16f11bc2a5",
                    "_tags": [
                        "<value>",
                    ],
                },
            ],
        },
        "dates": [
            {
                "_tags": [
                    "Instalation Date",
                ],
                "dates": "",
                "value": "2022-06-30T16:29:00.000Z",
            },
        ],
    },
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Order entity ID                                                     | 9d4602d3-03be-4d85-86b2-f3c6555fc606                                |
| `order_payload`                                                     | [models.OrderPayload](../../models/orderpayload.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Order](../../models/order.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
