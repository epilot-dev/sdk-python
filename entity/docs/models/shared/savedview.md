# SavedView

A saved entity view


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `created_by`                                               | *Any*                                                      | :heavy_check_mark:                                         | N/A                                                        |                                                            |
| `is_favorited_by`                                          | list[*str*]                                                | :heavy_minus_sign:                                         | List of users (IDs) that have favorited the view           |                                                            |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | User-friendly identifier for the saved view                | View listing German                                        |
| `org`                                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Organisation ID a view belongs to                          | 66                                                         |
| `shared`                                                   | *Optional[bool]*                                           | :heavy_minus_sign:                                         | boolean property for if a view is shared with organisation | true                                                       |
| `slug`                                                     | list[*str*]                                                | :heavy_check_mark:                                         | list of schemas a view can belong to                       |                                                            |
| `ui_config`                                                | dict[str, *Any*]                                           | :heavy_check_mark:                                         | N/A                                                        |                                                            |