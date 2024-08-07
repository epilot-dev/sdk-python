# CreateStepReq


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `name`                                                             | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `automation_config`                                                | [Optional[models.AutomationConfig]](../models/automationconfig.md) | :heavy_minus_sign:                                                 | Configuration for automation execution to run                      |
| `execution_type`                                                   | [Optional[models.StepType]](../models/steptype.md)                 | :heavy_minus_sign:                                                 | N/A                                                                |
| `insertion_index`                                                  | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | N/A                                                                |
| `section_id`                                                       | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `status`                                                           | [Optional[models.StepStatus]](../models/stepstatus.md)             | :heavy_minus_sign:                                                 | N/A                                                                |