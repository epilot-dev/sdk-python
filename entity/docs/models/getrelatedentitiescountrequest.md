# GetRelatedEntitiesCountRequest


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `id`                              | *str*                             | :heavy_check_mark:                | Entity id                         |                                   |
| `slug`                            | *str*                             | :heavy_check_mark:                | Entity Type                       | contact                           |
| `exclude_schemas`                 | List[*str*]                       | :heavy_minus_sign:                | Filter results to exclude schemas | file,message                      |