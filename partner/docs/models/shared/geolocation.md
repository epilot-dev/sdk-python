# Geolocation

Geo-location converted from text


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `address_label`                                                                    | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Full address label as returned by the location service                             |                                                                                    |
| `lat`                                                                              | *float*                                                                            | :heavy_check_mark:                                                                 | Latitude                                                                           | 49.013                                                                             |
| `lng`                                                                              | *float*                                                                            | :heavy_check_mark:                                                                 | Longitude                                                                          | 12.101                                                                             |
| `relevance`                                                                        | *Optional[float]*                                                                  | :heavy_minus_sign:                                                                 | Relevance of the result. A number between 0 and 1. Closer to 1 means more relevant |                                                                                    |