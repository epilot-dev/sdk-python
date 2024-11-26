# CustomVariables
(*custom_variables*)

## Overview

### Available Operations

* [create_custom_variable](#create_custom_variable) - Create custom variable
* [delete_custom_variable](#delete_custom_variable) - Delete custom variable
* [get_blue_print_table_config](#get_blue_print_table_config) - Get default table config
* [get_custom_variable](#get_custom_variable) - Get custom variable
* [get_custom_variables](#get_custom_variables) - Get custom variables
* [search_custom_variables](#search_custom_variables) - searchCustomVariables
* [update_custom_variable](#update_custom_variable) - Update custom variable

## create_custom_variable

Create custom variable

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    res = s.custom_variables.create_custom_variable(request={
        "created_at": "2022-04-19T12:41:43.662Z",
        "created_by": "100042",
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "key": "my_custom_table",
        "name": "My Custom table",
        "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">\n" +
        "  <thead>\n" +
        "    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">\n" +
        "      {{#each table_config.header.columns as |column|}}\n" +
        "        {{#if column.enable}}\n" +
        "          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>\n" +
        "        {{/if}}\n" +
        "      {{/each}}\n" +
        "    </tr>\n" +
        "  </thead>\n" +
        "  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">\n" +
        "    <!-- Start rendering products -->\n" +
        "    {{#each order.products as |product|}}\n" +
        "      {{#if @last}}\n" +
        "        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">\n" +
        "      {{else}}\n" +
        "        <tr style=\"height: 48px;;font-size:14px;\">\n" +
        "      {{/if}}\n" +
        "        {{#each @root.table_config.header.columns as |column|}}\n" +
        "          {{#if column.enable}}\n" +
        "            {{#if (eq column.id 'item')}}\n" +
        "              <!-- Item -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">\n" +
        "                {{#if @root.table_config.body.product_name.enable}}\n" +
        "                  {{product.name}}\n" +
        "                {{/if}}\n" +
        "                {{#if @root.table_config.body.price_description.enable}}\n" +
        "                  <br>\n" +
        "                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>\n" +
        "                {{/if}}\n" +
        "                {{#if @root.table_config.body.product_description.enable}}\n" +
        "                  <br>\n" +
        "                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>\n" +
        "                {{/if}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'quantity')}}\n" +
        "              <!-- Quantity -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'tax')}}\n" +
        "              <!-- Tax -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">\n" +
        "                {{product.price.tax_rate}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'unit_amount')}}\n" +
        "              <!-- Unit amount -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">\n" +
        "                {{product.price.unit_amount_net}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'net_total')}}\n" +
        "              <!-- Amount Subtotal -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">\n" +
        "                {{product.price.amount_subtotal}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'amount_tax')}}\n" +
        "              <!-- Tax amount-->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">\n" +
        "                {{product.price.amount_tax}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'gross_total')}}\n" +
        "              <!-- Gross total -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">\n" +
        "                {{product.price.amount_total}}\n" +
        "                {{#if @root.table_config.body.payment_type.enable}}\n" +
        "                  {{#if (eq product.price.type 'recurring')}}\n" +
        "                    <br>\n" +
        "                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>\n" +
        "                  {{/if}}\n" +
        "                {{/if}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "          {{/if}}\n" +
        "        {{/each}}\n" +
        "        </tr>\n" +
        "    {{/each}}\n" +
        "    <!-- Finish rendering products -->\n" +
        "    {{#if table_config.footer.gross_total.enable}}\n" +
        "      {{#each order.total_details.recurrences as |item|}}\n" +
        "        <tr style=\"height: 48px;font-size: 14px;\">\n" +
        "          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>\n" +
        "          {{#if @root.table_config.footer.payment_type.enable}}\n" +
        "            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>\n" +
        "          {{/if}}\n" +
        "          {{#if (isColumnEnabled @root.table_config 'net_total')}}\n" +
        "            {{#if @root.table_config.footer.net_total.enable}}\n" +
        "              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>\n" +
        "            {{/if}}\n" +
        "          {{/if}}\n" +
        "          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}\n" +
        "            {{#if @root.table_config.footer.amount_tax.enable}}\n" +
        "              <br>\n" +
        "              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>\n" +
        "            {{/if}}\n" +
        "          </td>\n" +
        "        </tr>\n" +
        "      {{/each}}\n" +
        "    {{/if}}\n" +
        "    <tr style=\"height:16px !important;\"></tr>\n" +
        "  </tbody>\n" +
        "</table>\n" +
        "",
        "type": epilot_template_variables.Type.CUSTOM,
        "updated_at": "2022-04-20T12:41:43.662Z",
        "updated_by": "100042",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CustomVariable](../../models/customvariable.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomVariable](../../models/customvariable.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_custom_variable

Immediately and permanently deletes a custom variable

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    s.custom_variables.delete_custom_variable(id="rbse777b-3cf8-4bff-bb0c-253fd1123250")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Custom vairable ID                                                  | rbse777b-3cf8-4bff-bb0c-253fd1123250                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_blue_print_table_config

Get default table config

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    res = s.custom_variables.get_blue_print_table_config()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomVariable](../../models/customvariable.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_custom_variable

Get custom variable

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    res = s.custom_variables.get_custom_variable(id="rbse777b-3cf8-4bff-bb0c-253fd1123250")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Custom vairable ID                                                  | rbse777b-3cf8-4bff-bb0c-253fd1123250                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomVariable](../../models/customvariable.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_custom_variables

Get all custom variables of organization

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    res = s.custom_variables.get_custom_variables()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.CustomVariable]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## search_custom_variables

Search custom variables

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    res = s.custom_variables.search_custom_variables(request={
        "query": "logo",
        "sort_by": "[\"created_at\",\"created_at:desc\",\"name\",\"name:desc\",\"key\"]",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CustomVariablesSearchParams](../../models/customvariablessearchparams.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.SearchCustomVariablesResponseBody](../../models/searchcustomvariablesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_custom_variable

Update custom variable

### Example Usage

```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as s:
    res = s.custom_variables.update_custom_variable(id="rbse777b-3cf8-4bff-bb0c-253fd1123250", custom_variable={
        "created_at": "2022-04-19T12:41:43.662Z",
        "created_by": "100042",
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "key": "my_custom_table",
        "name": "My Custom table",
        "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">\n" +
        "  <thead>\n" +
        "    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">\n" +
        "      {{#each table_config.header.columns as |column|}}\n" +
        "        {{#if column.enable}}\n" +
        "          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>\n" +
        "        {{/if}}\n" +
        "      {{/each}}\n" +
        "    </tr>\n" +
        "  </thead>\n" +
        "  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">\n" +
        "    <!-- Start rendering products -->\n" +
        "    {{#each order.products as |product|}}\n" +
        "      {{#if @last}}\n" +
        "        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">\n" +
        "      {{else}}\n" +
        "        <tr style=\"height: 48px;;font-size:14px;\">\n" +
        "      {{/if}}\n" +
        "        {{#each @root.table_config.header.columns as |column|}}\n" +
        "          {{#if column.enable}}\n" +
        "            {{#if (eq column.id 'item')}}\n" +
        "              <!-- Item -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">\n" +
        "                {{#if @root.table_config.body.product_name.enable}}\n" +
        "                  {{product.name}}\n" +
        "                {{/if}}\n" +
        "                {{#if @root.table_config.body.price_description.enable}}\n" +
        "                  <br>\n" +
        "                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>\n" +
        "                {{/if}}\n" +
        "                {{#if @root.table_config.body.product_description.enable}}\n" +
        "                  <br>\n" +
        "                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>\n" +
        "                {{/if}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'quantity')}}\n" +
        "              <!-- Quantity -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'tax')}}\n" +
        "              <!-- Tax -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">\n" +
        "                {{product.price.tax_rate}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'unit_amount')}}\n" +
        "              <!-- Unit amount -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">\n" +
        "                {{product.price.unit_amount_net}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'net_total')}}\n" +
        "              <!-- Amount Subtotal -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">\n" +
        "                {{product.price.amount_subtotal}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'amount_tax')}}\n" +
        "              <!-- Tax amount-->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">\n" +
        "                {{product.price.amount_tax}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "            {{#if (eq column.id 'gross_total')}}\n" +
        "              <!-- Gross total -->\n" +
        "              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">\n" +
        "                {{product.price.amount_total}}\n" +
        "                {{#if @root.table_config.body.payment_type.enable}}\n" +
        "                  {{#if (eq product.price.type 'recurring')}}\n" +
        "                    <br>\n" +
        "                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>\n" +
        "                  {{/if}}\n" +
        "                {{/if}}\n" +
        "              </td>\n" +
        "            {{/if}}\n" +
        "          {{/if}}\n" +
        "        {{/each}}\n" +
        "        </tr>\n" +
        "    {{/each}}\n" +
        "    <!-- Finish rendering products -->\n" +
        "    {{#if table_config.footer.gross_total.enable}}\n" +
        "      {{#each order.total_details.recurrences as |item|}}\n" +
        "        <tr style=\"height: 48px;font-size: 14px;\">\n" +
        "          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>\n" +
        "          {{#if @root.table_config.footer.payment_type.enable}}\n" +
        "            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>\n" +
        "          {{/if}}\n" +
        "          {{#if (isColumnEnabled @root.table_config 'net_total')}}\n" +
        "            {{#if @root.table_config.footer.net_total.enable}}\n" +
        "              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>\n" +
        "            {{/if}}\n" +
        "          {{/if}}\n" +
        "          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}\n" +
        "            {{#if @root.table_config.footer.amount_tax.enable}}\n" +
        "              <br>\n" +
        "              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>\n" +
        "            {{/if}}\n" +
        "          </td>\n" +
        "        </tr>\n" +
        "      {{/each}}\n" +
        "    {{/if}}\n" +
        "    <tr style=\"height:16px !important;\"></tr>\n" +
        "  </tbody>\n" +
        "</table>\n" +
        "",
        "type": epilot_template_variables.Type.CUSTOM,
        "updated_at": "2022-04-20T12:41:43.662Z",
        "updated_by": "100042",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Custom variable ID                                                  | rbse777b-3cf8-4bff-bb0c-253fd1123250                                |
| `custom_variable`                                                   | [Optional[models.CustomVariable]](../../models/customvariable.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomVariable](../../models/customvariable.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |