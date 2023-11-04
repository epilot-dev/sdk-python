# ~~AppendValueMapper~~

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`                                                                                                                                                                                                                                                                                                                              | [MappingAttributeMode](../../models/shared/mappingattributemode.md)                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                  | - copy_if_exists - it replaces the target attribute with the source value - append_if_exists - it currently replaces target attribute with array like values. Useful when you have multiple values to be added into one attribute. - set_value - it sets a value to a predefined value. Must be used together with value property.<br/> |
| `source`                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                  | JSON source path for the value to be extracted from the main entity. Eg: steps[1].['Product Info'].price<br/>                                                                                                                                                                                                                       |
| `target`                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                  | JSON like target path for the attribute. Eg. last_name                                                                                                                                                                                                                                                                              |
| `target_unique`                                                                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                  | Array of keys which should be used when checking for uniqueness. Eg: [country, city, postal_code]<br/>                                                                                                                                                                                                                              |
| `value_json`                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                  | To be provided only when mapping json objects into a target attribute. Eg array of addresses.<br/>                                                                                                                                                                                                                                  |