# LayoutSettings

Custom grid definitions for the layout. These settings are composed by managed and un-managed properties:
- Managed Properties: are interpreted and transformed into layout styles
- Un-managed Properties: are appended as styles into the attribute mounting node



## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `additional_properties`                                                  | Dict[str, *Any*]                                                         | :heavy_minus_sign:                                                       | N/A                                                                      |
| `grid_gap`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Defines the grid gap for the mounting node of the attribute.             |
| `grid_template_columns`                                                  | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Defines the grid column template for the mounting node of the attribute. |