# Section

A group of Steps that define the progress of the Workflow


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `order`                                                    | *float*                                                    | :heavy_check_mark:                                         | N/A                                                        |
| `steps`                                                    | List[[components.Step](../../models/components/step.md)]   | :heavy_check_mark:                                         | N/A                                                        |
| `type`                                                     | [components.ItemType](../../models/components/itemtype.md) | :heavy_check_mark:                                         | N/A                                                        |
| `id`                                                       | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |