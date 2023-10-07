# Activity


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `message`                                                   | *Optional[str]*                                             | :heavy_check_mark:                                          | Message for activity. Supports handlebars syntax.           | {{caller}} did something with {{entity payload.entity.id}}. |
| `payload`                                                   | dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         | [object Object]                                             |
| `title`                                                     | *Optional[str]*                                             | :heavy_check_mark:                                          | Title for activity. Supports handlebars syntax.             | My custom activity                                          |
| `type`                                                      | *Optional[str]*                                             | :heavy_check_mark:                                          | N/A                                                         | MyCustomActivity                                            |