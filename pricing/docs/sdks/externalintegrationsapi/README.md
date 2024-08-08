# ExternalIntegrationsAPI
(*external_integrations_api*)

## Overview

Provides endpoints for external integrations (e.g. Enet / GetAG).


### Available Operations

* [dollar_compute_price](#dollar_compute_price) - calculatePricingDetails
* [dollar_delete_credentials](#dollar_delete_credentials) - deleteCredentials
* [dollar_get_credentials](#dollar_get_credentials) - getCredentials
* [dollar_save_credentials](#dollar_save_credentials) - saveCredentials
* [dollar_search_providers](#dollar_search_providers) - searchProviders
* [dollar_search_streets](#dollar_search_streets) - searchStreets

## dollar_compute_price

Returns the price for a given product type based on location and consumption

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot()


res = s.external_integrations_api.dollar_compute_price(x_epilot_org_id="739224", integration_id=epilot_pricing.IntegrationID.GETAG, compute_price_params={
    "postal_code": "04109",
    "type": epilot_pricing.ComputePriceParamsPowerType.POWER,
    "association_id": "123456789",
    "billing_period": epilot_pricing.ComputePriceParamsPowerBillingPeriod.MONTHLY,
    "consumption": 3500,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `x_epilot_org_id`                                                                         | *str*                                                                                     | :heavy_check_mark:                                                                        | The target Organization Id represented by the caller                                      | 739224                                                                                    |
| `integration_id`                                                                          | [models.IntegrationID](../../models/integrationid.md)                                     | :heavy_check_mark:                                                                        | The integration identifier                                                                | getag                                                                                     |
| `compute_price_params`                                                                    | [Optional[models.ComputePriceParams]](../../models/computepriceparams.md)                 | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `security`                                                                                | [Optional[models.DollarComputePriceSecurity]](../../models/dollarcomputepricesecurity.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |


### Response

**[models.ComputePriceResult](../../models/computepriceresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400,403          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_delete_credentials

Delete the credentials for a given integration / organization

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.external_integrations_api.dollar_delete_credentials(integration_id=epilot_pricing.IntegrationID.GETAG)

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `integration_id`                                                    | [models.IntegrationID](../../models/integrationid.md)               | :heavy_check_mark:                                                  | The integration identifier                                          | getag                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_get_credentials

Gets the credentials for a given integration / organization

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.external_integrations_api.dollar_get_credentials(integration_id=epilot_pricing.IntegrationID.GETAG)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `integration_id`                                                    | [models.IntegrationID](../../models/integrationid.md)               | :heavy_check_mark:                                                  | The integration identifier                                          | getag                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.IntegrationCredentialsResult](../../models/integrationcredentialsresult.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400,404          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_save_credentials

Saves the credentials for a given integration / organization

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot(
    epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.external_integrations_api.dollar_save_credentials(integration_id=epilot_pricing.IntegrationID.GETAG, save_integration_credentials_params={
    "password": "password",
    "username": "username",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                      | [models.IntegrationID](../../models/integrationid.md)                                                 | :heavy_check_mark:                                                                                    | The integration identifier                                                                            | getag                                                                                                 |
| `save_integration_credentials_params`                                                                 | [Optional[models.SaveIntegrationCredentialsParams]](../../models/saveintegrationcredentialsparams.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400              | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_search_providers

Returns the list of providers available based on a given location

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot()


res = s.external_integrations_api.dollar_search_providers(x_epilot_org_id="739224", integration_id=epilot_pricing.IntegrationID.GETAG, search_providers_params={
    "postal_code": "04109",
    "type": epilot_pricing.SearchProvidersParamsType.POWER,
    "city": "Leipzig",
    "street": "Willy-Brandt-Platz",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `x_epilot_org_id`                                                                               | *str*                                                                                           | :heavy_check_mark:                                                                              | The target Organization Id represented by the caller                                            | 739224                                                                                          |
| `integration_id`                                                                                | [models.IntegrationID](../../models/integrationid.md)                                           | :heavy_check_mark:                                                                              | The integration identifier                                                                      | getag                                                                                           |
| `search_providers_params`                                                                       | [models.SearchProvidersParams](../../models/searchprovidersparams.md)                           | :heavy_check_mark:                                                                              | N/A                                                                                             |                                                                                                 |
| `security`                                                                                      | [Optional[models.DollarSearchProvidersSecurity]](../../models/dollarsearchproviderssecurity.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |                                                                                                 |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |


### Response

**[List[models.Provider]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400,403          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |

## dollar_search_streets

Returns the list of streets available for a given postal code and city

### Example Usage

```python
import epilot_pricing
from epilot_pricing import Epilot

s = Epilot()


res = s.external_integrations_api.dollar_search_streets(x_epilot_org_id="739224", integration_id=epilot_pricing.IntegrationID.GETAG, search_streets_params={
    "city": "Leipzig",
    "postal_code": "04109",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `x_epilot_org_id`                                                                           | *str*                                                                                       | :heavy_check_mark:                                                                          | The target Organization Id represented by the caller                                        | 739224                                                                                      |
| `integration_id`                                                                            | [models.IntegrationID](../../models/integrationid.md)                                       | :heavy_check_mark:                                                                          | The integration identifier                                                                  | getag                                                                                       |
| `search_streets_params`                                                                     | [models.SearchStreetsParams](../../models/searchstreetsparams.md)                           | :heavy_check_mark:                                                                          | N/A                                                                                         |                                                                                             |
| `security`                                                                                  | [Optional[models.DollarSearchStreetsSecurity]](../../models/dollarsearchstreetssecurity.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |


### Response

**[List[models.Street]](../../models/.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400,403          | application/json |
| models.SDKError  | 4xx-5xx          | */*              |
