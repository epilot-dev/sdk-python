# AccessTokenParameters


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `assignments`                                                  | List[*str*]                                                    | :heavy_minus_sign:                                             | List of role ids attached to an user                           |                                                                |
| `name`                                                         | *str*                                                          | :heavy_check_mark:                                             | Human readable name for access token                           | Postman Access Token                                           |
| `token_type`                                                   | [Optional[shared.TokenType]](../../models/shared/tokentype.md) | :heavy_minus_sign:                                             | N/A                                                            |                                                                |