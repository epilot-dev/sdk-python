# CustomVariables
(*custom_variables*)

### Available Operations

* [create_custom_variable](#create_custom_variable) - Create custom variable
* [delete_custom_variable](#delete_custom_variable) - Delete custom variable
* [get_blue_print_table_config](#get_blue_print_table_config) - Get default table config
* [get_custom_variable](#get_custom_variable) - Get custom variable
* [get_custom_variables](#get_custom_variables) - Get custom variables
* [update_custom_variable](#update_custom_variable) - Update custom variable

## create_custom_variable

Create custom variable

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = shared.CustomVariable(
    config=shared.CustomVariableConfig(),
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
    type=shared.CustomVariableType.CUSTOM,
    updated_at='2022-04-20T12:41:43.662Z',
    updated_by='100042',
)

res = s.custom_variables.create_custom_variable(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.CustomVariable](../../models/shared/customvariable.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateCustomVariableResponse](../../models/operations/createcustomvariableresponse.md)**


## delete_custom_variable

Immediately and permanently deletes a custom variable

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.DeleteCustomVariableRequest(
    id='<ID>',
)

res = s.custom_variables.delete_custom_variable(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeleteCustomVariableRequest](../../models/operations/deletecustomvariablerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.DeleteCustomVariableResponse](../../models/operations/deletecustomvariableresponse.md)**


## get_blue_print_table_config

Get default table config

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.custom_variables.get_blue_print_table_config()

if res.custom_variable is not None:
    # handle response
```


### Response

**[operations.GetBluePrintTableConfigResponse](../../models/operations/getblueprinttableconfigresponse.md)**


## get_custom_variable

Get custom variable

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.GetCustomVariableRequest(
    id='<ID>',
)

res = s.custom_variables.get_custom_variable(req)

if res.custom_variable is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetCustomVariableRequest](../../models/operations/getcustomvariablerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetCustomVariableResponse](../../models/operations/getcustomvariableresponse.md)**


## get_custom_variables

Get all custom variables of organization

### Example Usage

```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)


res = s.custom_variables.get_custom_variables()

if res.custom_variables is not None:
    # handle response
```


### Response

**[operations.GetCustomVariablesResponse](../../models/operations/getcustomvariablesresponse.md)**


## update_custom_variable

Update custom variable

### Example Usage

```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        epilot_auth="",
    ),
)

req = operations.UpdateCustomVariableRequest(
    custom_variable=shared.CustomVariable(
        config=shared.CustomVariableConfig(),
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
        type=shared.CustomVariableType.CUSTOM,
        updated_at='2022-04-20T12:41:43.662Z',
        updated_by='100042',
    ),
    id='<ID>',
)

res = s.custom_variables.update_custom_variable(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateCustomVariableRequest](../../models/operations/updatecustomvariablerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateCustomVariableResponse](../../models/operations/updatecustomvariableresponse.md)**

