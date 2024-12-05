# SchemasExtensionHookMeterReadingPlausibilityCheckCall


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `body`                                                                | Dict[str, *str*]                                                      | :heavy_check_mark:                                                    | JSON body to use for authentication. Supports variable interpolation. |
| `headers`                                                             | Dict[str, *str*]                                                      | :heavy_check_mark:                                                    | Headers to use. Supports variable interpolation.                      |
| `url`                                                                 | *str*                                                                 | :heavy_check_mark:                                                    | URL to call. Supports variable interpolation.                         |