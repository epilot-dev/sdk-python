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
import dateutil.parser
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.order_api.dollar_calculate_pricing_details(request={
    "line_items": [
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_VOLUME,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.EXTERNAL_GETAG,
                tax=[
                    epilot_pricing.Tax(
                        created_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        org="123",
                        schema_="tax",
                        title="<value>",
                        updated_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        rate=384.55,
                        type=epilot_pricing.TaxType.VAT,
                        tags=[
                            "example",
                            "mock",
                        ],
                        active=True,
                        description="Tax description",
                        region="DE",
                        region_label="Germany",
                        **{

                        },
                    ),
                ],
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 1311.93,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.MONTHLY,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "396cb5f3-ea0b-4629-99ca-303661de5a9b",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "c5695fb5-f02d-4e46-9fb2-a36dc4e9876f",
            "quantity": 2,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_GRADUATED,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.TIERED_FLATFEE,
                tax={},
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 6753.96,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.YEARLY,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "2abe0c6f-63ef-417b-8c85-5546359382d9",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.ONE_TIME,
                    "metadata": {
                        "journey_title": "P&G",
                        "step_name": "Number Inputs",
                    },
                    "name": "Estimated consumption",
                    "price_id": "2abe0c6f-63ef-417b-8c85-5546359382d9",
                    "value": 2,
                },
            ],
            "product_id": "c5695fb5-f02d-4e46-9fb2-a36dc4e9876f",
            "quantity": 1,
            "unit_amount_currency": "EUR",
        },
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
import dateutil.parser
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
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_FLATFEE,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.PER_UNIT,
                tax={},
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 2823.45,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_6_MONTHS,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 16,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_VOLUME,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.EXTERNAL_GETAG,
                tax=[
                    epilot_pricing.Tax(
                        created_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        org="123",
                        schema_="tax",
                        title="<value>",
                        updated_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        rate=4578.94,
                        type=epilot_pricing.TaxType.VAT,
                        tags=[
                            "example",
                            "mock",
                        ],
                        active=True,
                        description="Tax description",
                        region="DE",
                        region_label="Germany",
                        **{

                        },
                    ),
                ],
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 7146.52,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_6_MONTHS,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 4,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.EXTERNAL_GETAG,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.TIERED_VOLUME,
                tax=[
                    epilot_pricing.Tax(
                        created_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        org="123",
                        schema_="tax",
                        title="<value>",
                        updated_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        rate=8686.64,
                        type=epilot_pricing.TaxType.VAT,
                        tags=[
                            "example",
                            "mock",
                        ],
                        active=True,
                        description="Tax description",
                        region="DE",
                        region_label="Germany",
                        **{

                        },
                    ),
                ],
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 1604.53,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.WEEKLY,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 1,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_FLATFEE,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.TIERED_GRADUATED,
                tax=[
                    epilot_pricing.Tax(
                        created_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        org="123",
                        schema_="tax",
                        title="<value>",
                        updated_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        rate=1372.59,
                        type=epilot_pricing.TaxType.VAT,
                        tags=[
                            "example",
                            "mock",
                        ],
                        active=True,
                        description="Tax description",
                        region="DE",
                        region_label="Germany",
                        **{

                        },
                    ),
                ],
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 8728,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_QUARTER,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 1,
            "unit_amount_currency": "EUR",
        },
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
import dateutil.parser
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
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.EXTERNAL_GETAG,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.PER_UNIT,
                tax={},
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 7225.71,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.MONTHLY,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 16,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.PER_UNIT,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.PER_UNIT,
                tax={},
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 2948.39,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_6_MONTHS,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 4,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.TIERED_VOLUME,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.TIERED_GRADUATED,
                tax={},
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 9498.85,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_6_MONTHS,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 1,
            "unit_amount_currency": "EUR",
        },
        {
            "pricing_model": epilot_pricing.PriceItemDtoPricingModel.EXTERNAL_GETAG,
            "price": epilot_pricing.Price(
                pricing_model=epilot_pricing.PricePricingModel.TIERED_FLATFEE,
                tax=[
                    epilot_pricing.Tax(
                        created_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        org="123",
                        schema_="tax",
                        title="<value>",
                        updated_at=dateutil.parser.isoparse("2021-02-09T12:41:43.662Z"),
                        rate=3350.72,
                        type=epilot_pricing.TaxType.VAT,
                        tags=[
                            "example",
                            "mock",
                        ],
                        active=True,
                        description="Tax description",
                        region="DE",
                        region_label="Germany",
                        **{

                        },
                    ),
                ],
                unit_amount_currency="EUR",
                **{
                    "$ref": "#/components/examples/price",
                },
            ),
            "product": epilot_pricing.ProductInput(
                **{
                    "$ref": "#/components/examples/product",
                },
            ),
            "external_fees_mappings": [
                {
                    "amount_total": 1000,
                    "amount_total_decimal": "10.00",
                    "frequency_unit": epilot_pricing.FrequencyUnit.WEEKLY,
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                },
            ],
            "external_fees_metadata": {
                "amount_total": 8995.58,
                "amount_total_decimal": "<value>",
                "billing_period": epilot_pricing.ExternalFeeMetadataBillingPeriod.EVERY_QUARTER,
                "breakdown": {},
                "currency": "EUR",
            },
            "price_id": "7e24ff5d-d580-4136-a32f-19191eed039a",
            "price_mappings": [
                {
                    "frequency_unit": epilot_pricing.PriceInputMappingFrequencyUnit.WEEKLY,
                    "metadata": {
                        "journey_title": "energy journey",
                        "step_name": "avg consumption picker",
                    },
                    "name": "avg consumption",
                    "price_id": "589B011B-F8D9-4F8E-AD71-BACE4B543C0F",
                    "value": 1000.245,
                },
            ],
            "product_id": "6241487f-b7fd-428b-ab92-24ee0b37fd84",
            "quantity": 1,
            "unit_amount_currency": "EUR",
        },
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
