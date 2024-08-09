# AccessTokenParameters


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `name`                                               | *str*                                                | :heavy_check_mark:                                   | Human readable name for access token                 | Postman Access Token                                 |
| `assignments`                                        | List[*str*]                                          | :heavy_minus_sign:                                   | List of role ids attached to an user                 |                                                      |
| `token_type`                                         | [Optional[models.TokenType]](../models/tokentype.md) | :heavy_minus_sign:                                   | N/A                                                  |                                                      |