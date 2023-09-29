# Section

A group of Steps that define the progress of the Workflow


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `name`                                                           | *Optional[str]*                                                  | :heavy_check_mark:                                               | N/A                                                              |
| `order`                                                          | *Optional[float]*                                                | :heavy_check_mark:                                               | N/A                                                              |
| `steps`                                                          | list[[shared.Step](undefined/models/shared/step.md)]             | :heavy_check_mark:                                               | N/A                                                              |
| `type`                                                           | [Optional[shared.ItemType]](undefined/models/shared/itemtype.md) | :heavy_check_mark:                                               | N/A                                                              |