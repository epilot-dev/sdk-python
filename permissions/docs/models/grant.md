# Grant


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `action`                                                   | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        | entity-read                                                |
| `conditions`                                               | List[[models.GrantCondition](../models/grantcondition.md)] | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `effect`                                                   | [Optional[models.Effect]](../models/effect.md)             | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `resource`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | entity:123:contact:f7c22299-ca72-4bca-8538-0a88eeefc947    |