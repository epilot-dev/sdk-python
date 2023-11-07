# Message


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `de`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Message for notification. Supports handlebars syntax.                      | {{caller}} habe etwas damit gemacht {{contact.entity.id}} {{branch.name}}. |
| `en`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Message for notification. Supports handlebars syntax.                      | {{caller}} did something with {{contact.entity.id}} {{branch.name}}.       |