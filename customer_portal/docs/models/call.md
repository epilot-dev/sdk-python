# Call


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `url`                                                             | *str*                                                             | :heavy_check_mark:                                                | URL to call. Supports variable interpolation.                     |
| `headers`                                                         | Dict[str, *str*]                                                  | :heavy_minus_sign:                                                | Headers to use. Supports variable interpolation.                  |
| `method`                                                          | *Optional[str]*                                                   | :heavy_minus_sign:                                                | HTTP method to use for the call                                   |
| `params`                                                          | Dict[str, *str*]                                                  | :heavy_minus_sign:                                                | Parameters to append to the URL. Supports variable interpolation. |