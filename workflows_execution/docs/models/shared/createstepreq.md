# CreateStepReq


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `automation_config`                                                   | [Optional[AutomationConfig]](../../models/shared/automationconfig.md) | :heavy_minus_sign:                                                    | Configuration for automation execution to run                         |
| `execution_type`                                                      | [Optional[StepType]](../../models/shared/steptype.md)                 | :heavy_minus_sign:                                                    | N/A                                                                   |
| `insertion_index`                                                     | *float*                                                               | :heavy_check_mark:                                                    | N/A                                                                   |
| `name`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `section_id`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `status`                                                              | [Optional[StepStatus]](../../models/shared/stepstatus.md)             | :heavy_minus_sign:                                                    | N/A                                                                   |