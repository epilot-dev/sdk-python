# DeleteTaxonomyClassificationRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `classification_slug`                                   | *str*                                                   | :heavy_check_mark:                                      | Taxonomy Classification slug                            |
| `taxonomy_slug`                                         | *str*                                                   | :heavy_check_mark:                                      | Taxonomy slug                                           |
| `permanent`                                             | *Optional[bool]*                                        | :heavy_minus_sign:                                      | If true, the classification will be permanently deleted |