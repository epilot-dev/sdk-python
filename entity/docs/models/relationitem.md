# RelationItem


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `attribute`                           | *str*                                 | :heavy_check_mark:                    | N/A                                   |
| `entity_id`                           | *str*                                 | :heavy_check_mark:                    | N/A                                   |
| `tags`                                | List[*str*]                           | :heavy_minus_sign:                    | N/A                                   |
| `org_id`                              | *Optional[str]*                       | :heavy_minus_sign:                    | Organization Id the entity belongs to |
| `reverse`                             | *Optional[bool]*                      | :heavy_minus_sign:                    | Whether this is a reverse relation    |