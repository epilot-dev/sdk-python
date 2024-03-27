# CheckResults


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `product_id`                                        | *str*                                               | :heavy_check_mark:                                  | N/A                                                 |
| `matching_error`                                    | Dict[str, *Any*]                                    | :heavy_minus_sign:                                  | A set of matching errors when checking availability |
| `matching_hits`                                     | *Optional[float]*                                   | :heavy_minus_sign:                                  | The number of rules matched                         |