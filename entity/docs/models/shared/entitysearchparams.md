# EntitySearchParams


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `aggs`                                                                                                     | [Optional[EntitySearchParamsAggs]](../../models/shared/entitysearchparamsaggs.md)                          | :heavy_minus_sign:                                                                                         | Aggregation supported by ElasticSearch allows summarizing data as metrics, statistics, or other analytics. |                                                                                                            |
| `fields_`                                                                                                  | list[*str*]                                                                                                | :heavy_minus_sign:                                                                                         | List of entity fields to include in search results                                                         |                                                                                                            |
| `from_`                                                                                                    | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `hydrate`                                                                                                  | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | When true, enables entity hydration to resolve nested $relation & $relation_ref references in-place.       |                                                                                                            |
| `include_scores`                                                                                           | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | Adds a `_score` number field to results that can be used to rank by match score                            |                                                                                                            |
| `q`                                                                                                        | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Lucene queries supported with ElasticSearch                                                                | _schema:contact AND status:active                                                                          |
| `size`                                                                                                     | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | Max search size is 1000 with higher values defaulting to 1000                                              |                                                                                                            |
| `sort`                                                                                                     | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        | _created_at:desc                                                                                           |