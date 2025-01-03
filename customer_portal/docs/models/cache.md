# Cache


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `key`                                                             | *str*                                                             | :heavy_check_mark:                                                | Key to use to identify the auth response. Supports interpolation. | {{Options.api_key}}                                               |
| `ttl`                                                             | *str*                                                             | :heavy_check_mark:                                                | Time to live in seconds for the cache. Supports interpolation.    | {{AuthResponse.data.expires_in}}                                  |