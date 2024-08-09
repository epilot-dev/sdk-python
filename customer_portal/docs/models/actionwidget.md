# ActionWidget


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `list_index`                                                       | *int*                                                              | :heavy_check_mark:                                                 | Index of the widget in the list, used for ordering (left or right) |
| `type`                                                             | [models.ActionWidgetType](../models/actionwidgettype.md)           | :heavy_check_mark:                                                 | N/A                                                                |
| `actions`                                                          | List[[models.WidgetAction](../models/widgetaction.md)]             | :heavy_minus_sign:                                                 | N/A                                                                |
| `headline`                                                         | [Optional[models.Headline]](../models/headline.md)                 | :heavy_minus_sign:                                                 | N/A                                                                |
| `sub_headline`                                                     | [Optional[models.SubHeadline]](../models/subheadline.md)           | :heavy_minus_sign:                                                 | N/A                                                                |