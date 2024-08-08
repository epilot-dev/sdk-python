# SearchProvidersParams

A search providers payload


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `postal_code`                                                              | *str*                                                                      | :heavy_check_mark:                                                         | The postal code to search for providers                                    |
| `type`                                                                     | [models.SearchProvidersParamsType](../models/searchprovidersparamstype.md) | :heavy_check_mark:                                                         | The provider type (power or gas)                                           |
| `city`                                                                     | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | The city to search for providers                                           |
| `street`                                                                   | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | The street to search for providers                                         |
| `street_number`                                                            | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | The street number to search for providers                                  |