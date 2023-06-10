# Section

A group of Steps that define the progress of the Workflow


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `id`                                        | *Optional[str]*                             | :heavy_minus_sign:                          | N/A                                         |
| `name`                                      | *str*                                       | :heavy_check_mark:                          | N/A                                         |
| `order`                                     | *float*                                     | :heavy_check_mark:                          | N/A                                         |
| `steps`                                     | list[[Step](../../models/shared/step.md)]   | :heavy_check_mark:                          | N/A                                         |
| `type`                                      | [ItemType](../../models/shared/itemtype.md) | :heavy_check_mark:                          | N/A                                         |