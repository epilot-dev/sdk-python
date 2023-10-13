# CreateUserRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `contact_id`                               | *Optional[str]*                            | :heavy_minus_sign:                         | ID of the contact                          | 123456                                     |
| `contact_identifiers`                      | dict[str, *str*]                           | :heavy_minus_sign:                         | Identifiers to identify a contact          |                                            |
| `email`                                    | *str*                                      | :heavy_check_mark:                         | User's email address                       | testemail921@yopmail.com                   |
| `first_name`                               | *Optional[str]*                            | :heavy_minus_sign:                         | First Name of the portal user              | John                                       |
| `last_name`                                | *Optional[str]*                            | :heavy_minus_sign:                         | Last Name of the portal user               | Doe                                        |
| `org_id`                                   | *str*                                      | :heavy_check_mark:                         | ID of the organization                     | 728                                        |
| `password`                                 | *str*                                      | :heavy_check_mark:                         | User's password                            | 124n$aAJs*d41h4                            |
| `secondary_identifier`                     | *Optional[str]*                            | :heavy_minus_sign:                         | Secondary identifier to identify a contact | 123456                                     |