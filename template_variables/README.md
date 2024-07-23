# epilot-template-variables

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=template_variables
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_variables.create_custom_variable(request=components.CustomVariable(
    config=components.Config(),
    created_at='2022-04-19T12:41:43.662Z',
    created_by='100042',
    helper_logic='return param1 * param2;',
    helper_params=[
        'param1',
        'param2',
    ],
    id='rbse777b-3cf8-4bff-bb0c-253fd1123250',
    key='my_custom_table',
    name='My Custom table',
    template='<table style="table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;">
  <thead>
    <tr style="height: 48px;border-bottom: 1px solid #D5E1ED;">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style="{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style="vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style="height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;">
      {{else}}
        <tr style="height: 48px;;font-size:14px;">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id \'item\')}}
              <!-- Item -->
              <td style="{{makeStyle @root.table_config.body.product_name.style}}">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.price_description.style}}">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.product_description.style}}">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id \'quantity\')}}
              <!-- Quantity -->
              <td style="{{makeStyle @root.table_config.body.quantity.style}}">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id \'tax\')}}
              <!-- Tax -->
              <td style="{{makeStyle @root.table_config.body.tax.style}}">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id \'unit_amount\')}}
              <!-- Unit amount -->
              <td style="{{makeStyle @root.table_config.body.unit_amount.style}}">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id \'net_total\')}}
              <!-- Amount Subtotal -->
              <td style="{{makeStyle @root.table_config.body.net_total.style}}">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id \'amount_tax\')}}
              <!-- Tax amount-->
              <td style="{{makeStyle @root.table_config.body.amount_tax.style}}">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id \'gross_total\')}}
              <!-- Gross total -->
              <td style="{{makeStyle @root.table_config.body.gross_total.style}}">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type \'recurring\')}}
                    <br>
                    <span style="{{makeStyle @root.table_config.body.payment_type.style}}">{{product.price.billing_period}}</span>
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
        <tr style="height: 48px;font-size: 14px;">
          <td style="padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;" colspan="{{calculate_colspan @root.table_config}}"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style="{{makeStyle @root.table_config.footer.payment_type.style}}" colspan="2">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config \'net_total\')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style="{{makeStyle @root.table_config.footer.net_total.style}}">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style="{{makeStyle @root.table_config.footer.gross_total.style}}">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style="{{makeStyle @root.table_config.footer.amount_tax.style}}">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style="height:16px !important;"></tr>
  </tbody>
</table>
',
    type=components.Type.CUSTOM,
    updated_at='2022-04-20T12:41:43.662Z',
    updated_by='100042',
))

if res is not None:
    # handle response
    pass

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

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import epilot
from epilot.models import components, errors

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

res = None
try:
    res = s.custom_variables.create_custom_variable(request=components.CustomVariable(
    config=components.Config(),
    created_at='2022-04-19T12:41:43.662Z',
    created_by='100042',
    helper_logic='return param1 * param2;',
    helper_params=[
        'param1',
        'param2',
    ],
    id='rbse777b-3cf8-4bff-bb0c-253fd1123250',
    key='my_custom_table',
    name='My Custom table',
    template='<table style="table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;">
  <thead>
    <tr style="height: 48px;border-bottom: 1px solid #D5E1ED;">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style="{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style="vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style="height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;">
      {{else}}
        <tr style="height: 48px;;font-size:14px;">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id \'item\')}}
              <!-- Item -->
              <td style="{{makeStyle @root.table_config.body.product_name.style}}">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.price_description.style}}">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.product_description.style}}">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id \'quantity\')}}
              <!-- Quantity -->
              <td style="{{makeStyle @root.table_config.body.quantity.style}}">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id \'tax\')}}
              <!-- Tax -->
              <td style="{{makeStyle @root.table_config.body.tax.style}}">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id \'unit_amount\')}}
              <!-- Unit amount -->
              <td style="{{makeStyle @root.table_config.body.unit_amount.style}}">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id \'net_total\')}}
              <!-- Amount Subtotal -->
              <td style="{{makeStyle @root.table_config.body.net_total.style}}">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id \'amount_tax\')}}
              <!-- Tax amount-->
              <td style="{{makeStyle @root.table_config.body.amount_tax.style}}">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id \'gross_total\')}}
              <!-- Gross total -->
              <td style="{{makeStyle @root.table_config.body.gross_total.style}}">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type \'recurring\')}}
                    <br>
                    <span style="{{makeStyle @root.table_config.body.payment_type.style}}">{{product.price.billing_period}}</span>
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
        <tr style="height: 48px;font-size: 14px;">
          <td style="padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;" colspan="{{calculate_colspan @root.table_config}}"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style="{{makeStyle @root.table_config.footer.payment_type.style}}" colspan="2">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config \'net_total\')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style="{{makeStyle @root.table_config.footer.net_total.style}}">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style="{{makeStyle @root.table_config.footer.gross_total.style}}">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style="{{makeStyle @root.table_config.footer.amount_tax.style}}">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style="height:16px !important;"></tr>
  </tbody>
</table>
',
    type=components.Type.CUSTOM,
    updated_at='2022-04-20T12:41:43.662Z',
    updated_by='100042',
))

except errors.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

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
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_idx=0,
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_variables.create_custom_variable(request=components.CustomVariable(
    config=components.Config(),
    created_at='2022-04-19T12:41:43.662Z',
    created_by='100042',
    helper_logic='return param1 * param2;',
    helper_params=[
        'param1',
        'param2',
    ],
    id='rbse777b-3cf8-4bff-bb0c-253fd1123250',
    key='my_custom_table',
    name='My Custom table',
    template='<table style="table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;">
  <thead>
    <tr style="height: 48px;border-bottom: 1px solid #D5E1ED;">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style="{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style="vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style="height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;">
      {{else}}
        <tr style="height: 48px;;font-size:14px;">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id \'item\')}}
              <!-- Item -->
              <td style="{{makeStyle @root.table_config.body.product_name.style}}">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.price_description.style}}">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.product_description.style}}">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id \'quantity\')}}
              <!-- Quantity -->
              <td style="{{makeStyle @root.table_config.body.quantity.style}}">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id \'tax\')}}
              <!-- Tax -->
              <td style="{{makeStyle @root.table_config.body.tax.style}}">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id \'unit_amount\')}}
              <!-- Unit amount -->
              <td style="{{makeStyle @root.table_config.body.unit_amount.style}}">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id \'net_total\')}}
              <!-- Amount Subtotal -->
              <td style="{{makeStyle @root.table_config.body.net_total.style}}">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id \'amount_tax\')}}
              <!-- Tax amount-->
              <td style="{{makeStyle @root.table_config.body.amount_tax.style}}">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id \'gross_total\')}}
              <!-- Gross total -->
              <td style="{{makeStyle @root.table_config.body.gross_total.style}}">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type \'recurring\')}}
                    <br>
                    <span style="{{makeStyle @root.table_config.body.payment_type.style}}">{{product.price.billing_period}}</span>
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
        <tr style="height: 48px;font-size: 14px;">
          <td style="padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;" colspan="{{calculate_colspan @root.table_config}}"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style="{{makeStyle @root.table_config.footer.payment_type.style}}" colspan="2">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config \'net_total\')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style="{{makeStyle @root.table_config.footer.net_total.style}}">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style="{{makeStyle @root.table_config.footer.gross_total.style}}">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style="{{makeStyle @root.table_config.footer.amount_tax.style}}">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style="height:16px !important;"></tr>
  </tbody>
</table>
',
    type=components.Type.CUSTOM,
    updated_at='2022-04-20T12:41:43.662Z',
    updated_by='100042',
))

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import epilot
from epilot.models import components

s = epilot.Epilot(
    server_url="https://template-variables-api.sls.epilot.io",
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_variables.create_custom_variable(request=components.CustomVariable(
    config=components.Config(),
    created_at='2022-04-19T12:41:43.662Z',
    created_by='100042',
    helper_logic='return param1 * param2;',
    helper_params=[
        'param1',
        'param2',
    ],
    id='rbse777b-3cf8-4bff-bb0c-253fd1123250',
    key='my_custom_table',
    name='My Custom table',
    template='<table style="table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;">
  <thead>
    <tr style="height: 48px;border-bottom: 1px solid #D5E1ED;">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style="{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style="vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style="height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;">
      {{else}}
        <tr style="height: 48px;;font-size:14px;">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id \'item\')}}
              <!-- Item -->
              <td style="{{makeStyle @root.table_config.body.product_name.style}}">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.price_description.style}}">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.product_description.style}}">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id \'quantity\')}}
              <!-- Quantity -->
              <td style="{{makeStyle @root.table_config.body.quantity.style}}">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id \'tax\')}}
              <!-- Tax -->
              <td style="{{makeStyle @root.table_config.body.tax.style}}">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id \'unit_amount\')}}
              <!-- Unit amount -->
              <td style="{{makeStyle @root.table_config.body.unit_amount.style}}">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id \'net_total\')}}
              <!-- Amount Subtotal -->
              <td style="{{makeStyle @root.table_config.body.net_total.style}}">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id \'amount_tax\')}}
              <!-- Tax amount-->
              <td style="{{makeStyle @root.table_config.body.amount_tax.style}}">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id \'gross_total\')}}
              <!-- Gross total -->
              <td style="{{makeStyle @root.table_config.body.gross_total.style}}">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type \'recurring\')}}
                    <br>
                    <span style="{{makeStyle @root.table_config.body.payment_type.style}}">{{product.price.billing_period}}</span>
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
        <tr style="height: 48px;font-size: 14px;">
          <td style="padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;" colspan="{{calculate_colspan @root.table_config}}"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style="{{makeStyle @root.table_config.footer.payment_type.style}}" colspan="2">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config \'net_total\')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style="{{makeStyle @root.table_config.footer.net_total.style}}">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style="{{makeStyle @root.table_config.footer.gross_total.style}}">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style="{{makeStyle @root.table_config.footer.amount_tax.style}}">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style="height:16px !important;"></tr>
  </tbody>
</table>
',
    type=components.Type.CUSTOM,
    updated_at='2022-04-20T12:41:43.662Z',
    updated_by='100042',
))

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import epilot
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = epilot.Epilot(client=http_client)
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
import epilot
from epilot.models import components

s = epilot.Epilot(
    security=components.Security(
        epilot_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_variables.create_custom_variable(request=components.CustomVariable(
    config=components.Config(),
    created_at='2022-04-19T12:41:43.662Z',
    created_by='100042',
    helper_logic='return param1 * param2;',
    helper_params=[
        'param1',
        'param2',
    ],
    id='rbse777b-3cf8-4bff-bb0c-253fd1123250',
    key='my_custom_table',
    name='My Custom table',
    template='<table style="table-layout: fixed;width: 100%;max-width: 1000px;border-collapse: collapse;">
  <thead>
    <tr style="height: 48px;border-bottom: 1px solid #D5E1ED;">
      {{#each table_config.header.columns as |column|}}
        {{#if column.enable}}
          <th style="{{makeStyle @root.table_config.header.style}};{{makeStyle column.style}};">{{column._label}}</th>
        {{/if}}
      {{/each}}
    </tr>
  </thead>
  <tbody style="vertical-align: baseline  !important;font-weight: 400;font-size: 12px;position: relative;">
    <!-- Start rendering products -->
    {{#each order.products as |product|}}
      {{#if @last}}
        <tr style="height: 48px;;font-size:14px;border-bottom: 1px solid #D5E1ED;">
      {{else}}
        <tr style="height: 48px;;font-size:14px;">
      {{/if}}
        {{#each @root.table_config.header.columns as |column|}}
          {{#if column.enable}}
            {{#if (eq column.id \'item\')}}
              <!-- Item -->
              <td style="{{makeStyle @root.table_config.body.product_name.style}}">
                {{#if @root.table_config.body.product_name.enable}}
                  {{product.name}}
                {{/if}}
                {{#if @root.table_config.body.price_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.price_description.style}}">{{product.price.description}}</span>
                {{/if}}
                {{#if @root.table_config.body.product_description.enable}}
                  <br>
                  <span style="{{makeStyle @root.table_config.body.product_description.style}}">{{product.description}}</span>
                {{/if}}
              </td>
            {{/if}}
            {{#if (eq column.id \'quantity\')}}
              <!-- Quantity -->
              <td style="{{makeStyle @root.table_config.body.quantity.style}}">{{product.price.quantity}}
              </td>
            {{/if}}
            {{#if (eq column.id \'tax\')}}
              <!-- Tax -->
              <td style="{{makeStyle @root.table_config.body.tax.style}}">
                {{product.price.tax_rate}}
              </td>
            {{/if}}
            {{#if (eq column.id \'unit_amount\')}}
              <!-- Unit amount -->
              <td style="{{makeStyle @root.table_config.body.unit_amount.style}}">
                {{product.price.unit_amount_net}}
              </td>
            {{/if}}
            {{#if (eq column.id \'net_total\')}}
              <!-- Amount Subtotal -->
              <td style="{{makeStyle @root.table_config.body.net_total.style}}">
                {{product.price.amount_subtotal}}
              </td>
            {{/if}}
            {{#if (eq column.id \'amount_tax\')}}
              <!-- Tax amount-->
              <td style="{{makeStyle @root.table_config.body.amount_tax.style}}">
                {{product.price.amount_tax}}
              </td>
            {{/if}}
            {{#if (eq column.id \'gross_total\')}}
              <!-- Gross total -->
              <td style="{{makeStyle @root.table_config.body.gross_total.style}}">
                {{product.price.amount_total}}
                {{#if @root.table_config.body.payment_type.enable}}
                  {{#if (eq product.price.type \'recurring\')}}
                    <br>
                    <span style="{{makeStyle @root.table_config.body.payment_type.style}}">{{product.price.billing_period}}</span>
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
        <tr style="height: 48px;font-size: 14px;">
          <td style="padding-top: 16px; padding-bottom: 8px; border: none !important; vertical-align: top;" colspan="{{calculate_colspan @root.table_config}}"></td>
          {{#if @root.table_config.footer.payment_type.enable}}
            <td style="{{makeStyle @root.table_config.footer.payment_type.style}}" colspan="2">{{item.billing_period}}</td>
          {{/if}}
          {{#if (isColumnEnabled @root.table_config \'net_total\')}}
            {{#if @root.table_config.footer.net_total.enable}}
              <td style="{{makeStyle @root.table_config.footer.net_total.style}}">{{item.amount_subtotal}}</td>
            {{/if}}
          {{/if}}
          <td style="{{makeStyle @root.table_config.footer.gross_total.style}}">{{item.amount_total}}
            {{#if @root.table_config.footer.amount_tax.enable}}
              <br>
              <span style="{{makeStyle @root.table_config.footer.amount_tax.style}}">{{item.full_amount_tax}}</span>
            {{/if}}
          </td>
        </tr>
      {{/each}}
    {{/if}}
    <tr style="height:16px !important;"></tr>
  </tbody>
</table>
',
    type=components.Type.CUSTOM,
    updated_at='2022-04-20T12:41:43.662Z',
    updated_by='100042',
))

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
