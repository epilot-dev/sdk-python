# GetSchemaVersionsRequest


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `slug`                            | *str*                             | :heavy_check_mark:                | Entity Type                       | contact                           |
| `drafts_from`                     | *Optional[float]*                 | :heavy_minus_sign:                | N/A                               |                                   |
| `drafts_size`                     | *Optional[float]*                 | :heavy_minus_sign:                | N/A                               |                                   |
| `fields`                          | List[*str*]                       | :heavy_minus_sign:                | N/A                               | ["id","attributes","capabilites"] |
| `versions_from`                   | *Optional[float]*                 | :heavy_minus_sign:                | N/A                               |                                   |
| `versions_size`                   | *Optional[float]*                 | :heavy_minus_sign:                | N/A                               |                                   |