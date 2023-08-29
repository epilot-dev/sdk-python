# GetRelationsV2Request


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `fields_`                                                                                  | list[*str*]                                                                                | :heavy_minus_sign:                                                                         | List of entity fields to include in results                                                |                                                                                            |
| `from_`                                                                                    | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Starting page number                                                                       |                                                                                            |
| `hydrate`                                                                                  | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | When true, expand relation items with full blown entities.                                 |                                                                                            |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | Entity id                                                                                  |                                                                                            |
| `include_reverse`                                                                          | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | When true, includes reverse relations in response (other entities pointing to this entity) |                                                                                            |
| `query`                                                                                    | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Input to filter search results                                                             |                                                                                            |
| `size`                                                                                     | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Number of results to return per page                                                       |                                                                                            |
| `slug`                                                                                     | *str*                                                                                      | :heavy_check_mark:                                                                         | Entity Type                                                                                | contact                                                                                    |