# DynamicDueDate

set a Duedate for a step then a specific


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `number_of_units`                                                        | *float*                                                                  | :heavy_check_mark:                                                       | N/A                                                                      |
| `time_period`                                                            | [models.TimePeriod](../models/timeperiod.md)                             | :heavy_check_mark:                                                       | N/A                                                                      |
| `action_type_condition`                                                  | [Optional[models.ActionTypeCondition]](../models/actiontypecondition.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `step_id`                                                                | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |