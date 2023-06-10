# StepSimplified


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `definition_id`                                                 | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `ecp`                                                           | [Optional[ECPDetails]](../../models/shared/ecpdetails.md)       | :heavy_minus_sign:                                              | Details regarding ECP for the workflow step                     |
| `enabled`                                                       | *Optional[bool]*                                                | :heavy_minus_sign:                                              | N/A                                                             |
| `entity_ref_id`                                                 | *str*                                                           | :heavy_check_mark:                                              | N/A                                                             |
| `execution_type`                                                | [Optional[StepType]](../../models/shared/steptype.md)           | :heavy_minus_sign:                                              | N/A                                                             |
| `id`                                                            | *str*                                                           | :heavy_check_mark:                                              | N/A                                                             |
| `name`                                                          | *str*                                                           | :heavy_check_mark:                                              | N/A                                                             |
| `requirements`                                                  | list[[StepRequirement](../../models/shared/steprequirement.md)] | :heavy_minus_sign:                                              | N/A                                                             |
| `type`                                                          | [ItemType](../../models/shared/itemtype.md)                     | :heavy_check_mark:                                              | N/A                                                             |