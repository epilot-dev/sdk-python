# ActionWidget


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `actions`                                                              | List[[components.WidgetAction](../../models/shared/widgetaction.md)]   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `headline`                                                             | [Optional[components.Headline]](../../models/shared/headline.md)       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `list_index`                                                           | *int*                                                                  | :heavy_check_mark:                                                     | Index of the widget in the list, used for ordering (left or right)     |
| `sub_headline`                                                         | [Optional[components.SubHeadline]](../../models/shared/subheadline.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `type`                                                                 | [components.ActionWidgetType](../../models/shared/actionwidgettype.md) | :heavy_check_mark:                                                     | N/A                                                                    |