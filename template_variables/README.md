# epilot-template-variables

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=template_variables
```

Poetry
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

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
})

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_template_variables
from epilot_template_variables import Epilot

async def main():
    s = Epilot(
        security=epilot_template_variables.Security(
            epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
        ),
    )
    await s.custom_variables.create_custom_variable_async(request={
        "config": {},
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
        "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
      <thead>
        <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
          {{#each table_config.header.columns as |column|}}
            {{#if column.enable}}
              <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
            {{/if}}
          {{/each}}
        </tr>
      </thead>
      <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
        <!-- Start rendering products -->
        {{#each order.products as |product|}}
          {{#if @last}}
            <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
          {{else}}
            <tr style=\"height: 48px;;font-size:14px;\">
          {{/if}}
            {{#each @root.table_config.header.columns as |column|}}
              {{#if column.enable}}
                {{#if (eq column.id 'item')}}
                  <!-- Item -->
                  <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                    {{#if @root.table_config.body.product_name.enable}}
                      {{product.name}}
                    {{/if}}
                    {{#if @root.table_config.body.price_description.enable}}
                      <br>
                      <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                    {{/if}}
                    {{#if @root.table_config.body.product_description.enable}}
                      <br>
                      <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                    {{/if}}
                  </td>
                {{/if}}
                {{#if (eq column.id 'quantity')}}
                  <!-- Quantity -->
                  <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
                  </td>
                {{/if}}
                {{#if (eq column.id 'tax')}}
                  <!-- Tax -->
                  <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                    {{product.price.tax_rate}}
                  </td>
                {{/if}}
                {{#if (eq column.id 'unit_amount')}}
                  <!-- Unit amount -->
                  <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                    {{product.price.unit_amount_net}}
                  </td>
                {{/if}}
                {{#if (eq column.id 'net_total')}}
                  <!-- Amount Subtotal -->
                  <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                    {{product.price.amount_subtotal}}
                  </td>
                {{/if}}
                {{#if (eq column.id 'amount_tax')}}
                  <!-- Tax amount-->
                  <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                    {{product.price.amount_tax}}
                  </td>
                {{/if}}
                {{#if (eq column.id 'gross_total')}}
                  <!-- Gross total -->
                  <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                    {{product.price.amount_total}}
                    {{#if @root.table_config.body.payment_type.enable}}
                      {{#if (eq product.price.type 'recurring')}}
                        <br>
                        <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                      {{/if}}
                    {{/if}}
                  </td>
                {{/if}}
              {{/if}}
            {{/each}}
            </tr>
        {{/each}}
        <!-- Finish rendering products -->
        {{#if table_config.footer.gross_total.enable}}
          {{#each order.total_details.recurrences as |item|}}
            <tr style=\"height: 48px;font-size: 14px;\">
              <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
              {{#if @root.table_config.footer.payment_type.enable}}
                <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
              {{/if}}
              {{#if (isColumnEnabled @root.table_config 'net_total')}}
                {{#if @root.table_config.footer.net_total.enable}}
                  <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
                {{/if}}
              {{/if}}
              <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
                {{#if @root.table_config.footer.amount_tax.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
                {{/if}}
              </td>
            </tr>
          {{/each}}
        {{/if}}
        <tr style=\"height:16px !important;\"></tr>
      </tbody>
    </table>
    ",
        "type": epilot_template_variables.Type.CUSTOM,
        "updated_at": "2022-04-20T12:41:43.662Z",
        "updated_by": "100042",
    })
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [custom_variables](docs/sdks/customvariables/README.md)

* [create_custom_variable](docs/sdks/customvariables/README.md#create_custom_variable) - Create custom variable
* [delete_custom_variable](docs/sdks/customvariables/README.md#delete_custom_variable) - Delete custom variable
* [get_blue_print_table_config](docs/sdks/customvariables/README.md#get_blue_print_table_config) - Get default table config
* [get_custom_variable](docs/sdks/customvariables/README.md#get_custom_variable) - Get custom variable
* [get_custom_variables](docs/sdks/customvariables/README.md#get_custom_variables) - Get custom variables
* [update_custom_variable](docs/sdks/customvariables/README.md#update_custom_variable) - Update custom variable

### [variables](docs/sdks/variables/README.md)

* [get_categories](docs/sdks/variables/README.md#get_categories) - getCategories
* [get_variable_context](docs/sdks/variables/README.md#get_variable_context) - getVariableContext
* [replace_templates](docs/sdks/variables/README.md#replace_templates) - replaceTemplates
* [search_variables](docs/sdks/variables/README.md#search_variables) - searchVariables
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

# Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from epilot.utils import BackoffStrategy, RetryConfig
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
})

# Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

### Example

```python
import epilot_template_variables
from epilot_template_variables import Epilot, models

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


try:
    s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
})

except models.SDKError as e:
    # handle exception
    raise(e)

# Use the SDK ...

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://template-variables-api.sls.epilot.io` | None |

#### Example

```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    server_idx=0,
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
})

# Use the SDK ...

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    server_url="https://template-variables-api.sls.epilot.io",
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
})

# Use the SDK ...

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

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `epilot_auth` | http          | HTTP Bearer   |
| `epilot_org`  | apiKey        | API key       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import epilot_template_variables
from epilot_template_variables import Epilot

s = Epilot(
    security=epilot_template_variables.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


s.custom_variables.create_custom_variable(request={
    "config": {},
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
    "template": "<table style=\"table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;\">
  <thead>
    <tr style=\"height: 48px;border-bottom: 1px solid #D5E1ED;\">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style=\"{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};\">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style=\"vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;\">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style=\"height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;\">
      {{else}}
        <tr style=\"height: 48px;;font-size:14px;\">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id 'item')}}
              <!-- Item -->
              <td style=\"{{makeStyle @root.table_config.body.product_name.style}}\">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.price_description.style}}\">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style=\"{{makeStyle @root.table_config.body.product_description.style}}\">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id 'quantity')}}
              <!-- Quantity -->
              <td style=\"{{makeStyle @root.table_config.body.quantity.style}}\">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id 'tax')}}
              <!-- Tax -->
              <td style=\"{{makeStyle @root.table_config.body.tax.style}}\">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id 'unit_amount')}}
              <!-- Unit amount -->
              <td style=\"{{makeStyle @root.table_config.body.unit_amount.style}}\">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id 'net_total')}}
              <!-- Amount Subtotal -->
              <td style=\"{{makeStyle @root.table_config.body.net_total.style}}\">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id 'amount_tax')}}
              <!-- Tax amount-->
              <td style=\"{{makeStyle @root.table_config.body.amount_tax.style}}\">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id 'gross_total')}}
              <!-- Gross total -->
              <td style=\"{{makeStyle @root.table_config.body.gross_total.style}}\">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type 'recurring')}}
                    <br>
                    <span style=\"{{makeStyle @root.table_config.body.payment_type.style}}\">{{product.price.billing_period}}</span>
                  {{/if}}
                {{/if}}
              </td>
            {{/if}}
          {{/if}}
        {{/each}}
        </tr>
    {{/each}}
    <!-- Finish rendering products -->
    {{#if table_config.footer.gross_total.enable}}
      {{#each order.total_details.recurrences as |item|}}
        <tr style=\"height: 48px;font-size: 14px;\">
          <td style=\"padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;\" colspan=\"{{calculate_colspan @root.table_config}}\"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style=\"{{makeStyle @root.table_config.footer.payment_type.style}}\" colspan=\"2\">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config 'net_total')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style=\"{{makeStyle @root.table_config.footer.net_total.style}}\">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style=\"{{makeStyle @root.table_config.footer.gross_total.style}}\">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style=\"{{makeStyle @root.table_config.footer.amount_tax.style}}\">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style=\"height:16px !important;\"></tr>
  </tbody>
</table>
",
    "type": epilot_template_variables.Type.CUSTOM,
    "updated_at": "2022-04-20T12:41:43.662Z",
    "updated_by": "100042",
})

# Use the SDK ...

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from epilot_template_variables import Epilot
import logging

logging.basicConfig(level=logging.DEBUG)
s = Epilot(debug_logger=logging.getLogger("epilot_template_variables"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
