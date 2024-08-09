# GetRelationsV3Request


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `exclude_schemas`                                                                                    | List[*str*]                                                                                          | :heavy_minus_sign:                                                                                   | Filter results to exclude schemas                                                                    |                                                                                                      |
| `from_`                                                                                              | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | Starting page number                                                                                 |                                                                                                      |
| `hydrate`                                                                                            | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | When true, enables entity hydration to resolve nested $relation & $relation_ref references in-place. |                                                                                                      |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Entity id                                                                                            |                                                                                                      |
| `include_reverse`                                                                                    | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | When true, includes reverse relations in response (other entities pointing to this entity)           |                                                                                                      |
| `include_schemas`                                                                                    | List[*str*]                                                                                          | :heavy_minus_sign:                                                                                   | Filter results to only include schemas                                                               |                                                                                                      |
| `size`                                                                                               | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | Number of results to return per page                                                                 |                                                                                                      |
| `slug`                                                                                               | *str*                                                                                                | :heavy_check_mark:                                                                                   | Entity Type                                                                                          | contact                                                                                              |