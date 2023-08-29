# GetRelationsRequest


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `hydrate`                                                                                  | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | When true, expand relation items with full blown entities.                                 |                                                                                            |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | Entity id                                                                                  |                                                                                            |
| `include_reverse`                                                                          | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | When true, includes reverse relations in response (other entities pointing to this entity) |                                                                                            |
| `slug`                                                                                     | *str*                                                                                      | :heavy_check_mark:                                                                         | Entity Type                                                                                | contact                                                                                    |