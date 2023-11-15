# Activity


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `message`                                                   | *str*                                                       | :heavy_check_mark:                                          | Message for activity. Supports handlebars syntax.           | {{caller}} did something with {{entity payload.entity.id}}. |
| `payload`                                                   | Dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         | [object Object]                                             |
| `title`                                                     | *str*                                                       | :heavy_check_mark:                                          | Title for activity. Supports handlebars syntax.             | My custom activity                                          |
| `type`                                                      | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         | MyCustomActivity                                            |