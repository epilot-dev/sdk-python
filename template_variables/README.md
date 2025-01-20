# epilot-template-variables

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=template_variables
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/epilot-dev/sdk-python.git#subdirectory=template_variables
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.custom_variables.create_custom_variable(request={
        "key": "my_custom_table",
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
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "name": "My Custom table",
    })

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_template_variables
from epilot_template_variables import Epilot

async def main():
    async with Epilot(
        security=epilot_template_variables.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    ) as epilot:

        res = await epilot.custom_variables.create_custom_variable_async(request={
            "key": "my_custom_table",
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
            "helper_logic": "return param1 * param2;",
            "helper_params": [
                "param1",
                "param2",
            ],
            "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
            "name": "My Custom table",
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [custom_variables](docs/sdks/customvariables/README.md)

* [create_custom_variable](docs/sdks/customvariables/README.md#create_custom_variable) - Create custom variable
* [delete_custom_variable](docs/sdks/customvariables/README.md#delete_custom_variable) - Delete custom variable
* [get_blue_print_table_config](docs/sdks/customvariables/README.md#get_blue_print_table_config) - Get default table config
* [get_custom_variable](docs/sdks/customvariables/README.md#get_custom_variable) - Get custom variable
* [get_custom_variables](docs/sdks/customvariables/README.md#get_custom_variables) - Get custom variables
* [search_custom_variables](docs/sdks/customvariables/README.md#search_custom_variables) - searchCustomVariables
* [update_custom_variable](docs/sdks/customvariables/README.md#update_custom_variable) - Update custom variable


### [variables](docs/sdks/variables/README.md)

* [get_categories](docs/sdks/variables/README.md#get_categories) - getCategories
* [get_variable_context](docs/sdks/variables/README.md#get_variable_context) - getVariableContext
* [replace_templates](docs/sdks/variables/README.md#replace_templates) - replaceTemplates
* [search_variables](docs/sdks/variables/README.md#search_variables) - searchVariables

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import epilot_template_variables
from epilot_template_variables import Epilot
from epilot_template_variables.utils import BackoffStrategy, RetryConfig

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.custom_variables.create_custom_variable(request={
        "key": "my_custom_table",
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
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "name": "My Custom table",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import epilot_template_variables
from epilot_template_variables import Epilot
from epilot_template_variables.utils import BackoffStrategy, RetryConfig

with Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.custom_variables.create_custom_variable(request={
        "key": "my_custom_table",
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
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "name": "My Custom table",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_custom_variable_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| models.SDKError | 4XX, 5XX    | \*/\*        |

### Example

```python
import epilot_template_variables
from epilot_template_variables import Epilot, models

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:
    res = None
    try:

        res = epilot.custom_variables.create_custom_variable(request={
            "key": "my_custom_table",
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
            "helper_logic": "return param1 * param2;",
            "helper_params": [
                "param1",
                "param2",
            ],
            "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
            "name": "My Custom table",
        })

        assert res is not None

        # Handle response
        print(res)

    except models.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    server_url="https://template-variables-api.sls.epilot.io",
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.custom_variables.create_custom_variable(request={
        "key": "my_custom_table",
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
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "name": "My Custom table",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from epilot_template_variables import Epilot
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Epilot(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from epilot_template_variables import Epilot
from epilot_template_variables.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Epilot(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type   | Scheme      |
| ------------- | ------ | ----------- |
| `epilot_auth` | http   | HTTP Bearer |
| `epilot_org`  | apiKey | API key     |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot_template_variables
from epilot_template_variables import Epilot

with Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as epilot:

    res = epilot.custom_variables.create_custom_variable(request={
        "key": "my_custom_table",
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
        "helper_logic": "return param1 * param2;",
        "helper_params": [
            "param1",
            "param2",
        ],
        "id": "rbse777b-3cf8-4bff-bb0c-253fd1123250",
        "name": "My Custom table",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from epilot_template_variables import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_template_variables"))
```
<!-- End Debugging [debug] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Summary [summary] -->
## Summary

Template Variables API: API to provide variables for email and document templates.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [epilot-template-variables](#epilot-template-variables)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Debugging](#debugging)
  * [IDE Support](#ide-support)

<!-- End Table of Contents [toc] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
