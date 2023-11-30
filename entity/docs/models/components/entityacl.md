# EntityACL

Access control list (ACL) for an entity. Defines sharing access to external orgs or users.


## Fields

| Field                   | Type                    | Required                | Description             | Example                 |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `additional_properties` | Dict[str, *Any*]        | :heavy_minus_sign:      | N/A                     |                         |
| `delete`                | List[*str*]             | :heavy_minus_sign:      | N/A                     | org:456                 |
| `edit`                  | List[*str*]             | :heavy_minus_sign:      | N/A                     | org:456                 |
| `view`                  | List[*str*]             | :heavy_minus_sign:      | N/A                     | org:456                 |