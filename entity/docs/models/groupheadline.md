# GroupHeadline


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `group`                                                     | *str*                                                       | :heavy_check_mark:                                          | The group of headline attribute                             |
| `label`                                                     | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `name`                                                      | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `type`                                                      | [models.GroupHeadlineType](../models/groupheadlinetype.md)  | :heavy_check_mark:                                          | N/A                                                         |
| `manifest`                                                  | List[*str*]                                                 | :heavy_minus_sign:                                          | Manifest ID used to create/update the schema group headline |
| `divider`                                                   | [Optional[models.Divider]](../models/divider.md)            | :heavy_minus_sign:                                          | N/A                                                         |
| `enable_divider`                                            | *Optional[bool]*                                            | :heavy_minus_sign:                                          | N/A                                                         |
| `id`                                                        | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `layout`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `order`                                                     | *Optional[int]*                                             | :heavy_minus_sign:                                          | The order of headline attribute                             |