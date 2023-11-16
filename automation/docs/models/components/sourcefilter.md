# SourceFilter

A filter to identify which source entities to pick as relations from main entity


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `attribute`                                                        | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Filter by a specific relation attribute on the main entity         |
| `limit`                                                            | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Limit relations to maximum number (default, all matched relations) |
| `relation_tag`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Filter by relation tag (label) on the main entity                  |
| `schema`                                                           | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Filter by specific schema                                          |
| `self_`                                                            | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Picks main entity as relation (overrides other filters)            |
| `tag`                                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Filter by a specific tag on the related entity                     |