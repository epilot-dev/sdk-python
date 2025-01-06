# ExtensionAuthBlock


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `url`                                                                 | *str*                                                                 | :heavy_check_mark:                                                    | URL to use for authentication. Supports variable interpolation.       |
| `body`                                                                | Dict[str, *str*]                                                      | :heavy_minus_sign:                                                    | JSON body to use for authentication. Supports variable interpolation. |
| `cache`                                                               | [Optional[models.Cache]](../models/cache.md)                          | :heavy_minus_sign:                                                    | N/A                                                                   |
| `headers`                                                             | Dict[str, *str*]                                                      | :heavy_minus_sign:                                                    | Headers to use for authentication. Supports variable interpolation.   |
| `method`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | HTTP method to use for authentication                                 |
| `params`                                                              | Dict[str, *str*]                                                      | :heavy_minus_sign:                                                    | Parameters to append to the URL. Supports variable interpolation.     |